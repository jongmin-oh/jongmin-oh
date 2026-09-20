#!/usr/bin/env python3
import sys
import re
import os
import argparse
import tempfile
from pathlib import Path

# Add local bundled tools to sys.path if present
WORKSPACE_ROOT = Path(__file__).resolve().parent.parent
TOOLS_LIB = WORKSPACE_ROOT / "tools" / "lib"
if TOOLS_LIB.exists():
    sys.path.insert(0, str(TOOLS_LIB))

try:
    import typst
except ImportError:
    print("Error: typst module not found. Run: pip install typst", file=sys.stderr)
    sys.exit(1)

FONTS_DIR = WORKSPACE_ROOT / "tools" / "fonts"
USER_FONTS = Path.home() / ".local" / "share" / "fonts"
WINDOWS_FONTS = Path("/mnt/c/Windows/Fonts")
FONT_PATHS = []
if FONTS_DIR.exists():
    FONT_PATHS.append(str(FONTS_DIR))
if USER_FONTS.exists():
    FONT_PATHS.append(str(USER_FONTS))
if WINDOWS_FONTS.exists():
    FONT_PATHS.append(str(WINDOWS_FONTS))


def parse_numbered_items(text):
    items = []
    # Pattern: **1. Title**\nBody or **1. Title** Body
    pattern = r'\*\*(\d+)\.\s*(.*?)\*\*\s*\n*(.*?)(?=\n\*\*\d+\.|\Z)'
    matches = re.findall(pattern, text, re.DOTALL)
    for num, title, body in matches:
        items.append({
            "num": num.strip(),
            "title": title.strip(),
            "body": body.strip()
        })
    return items


def parse_markdown(md_text):
    has_headers = bool(re.search(r'^##\s+', md_text, re.MULTILINE))

    if has_headers:
        # Standard 4-block structured layout
        sections = re.split(r'\n(?=##\s+)', md_text.strip())
        data = {
            "type": "4block",
            "intro": sections[0].strip() if not sections[0].startswith("##") else "",
            "sec1_title": "제가 회사에서 할 수 있는 일 세 가지",
            "sec1_items": [],
            "sec2_title": "제가 회사에 더할 수 있는 것 세 가지",
            "sec2_items": [],
            "sec3_title": "솔직하게 부족한 부분",
            "sec3_body": "",
            "sec4_title": "마지막으로",
            "sec4_body": ""
        }
        rest_sections = sections[1:] if not sections[0].startswith("##") else sections
        for sec in rest_sections:
            lines = sec.strip().split("\n", 1)
            header = lines[0].replace("##", "").strip()
            body = lines[1].strip() if len(lines) > 1 else ""

            if "할 수 있는 일" in header:
                data["sec1_title"] = header
                data["sec1_items"] = parse_numbered_items(body)
            elif "더할 수 있는 것" in header or "줄 수 있는 것" in header:
                data["sec2_title"] = header
                data["sec2_items"] = parse_numbered_items(body)
            elif "부족한" in header:
                data["sec3_title"] = header
                data["sec3_body"] = body
            elif "마지막" in header:
                data["sec4_title"] = header
                data["sec4_body"] = body

        return data
    else:
        # Narrative / Paragraph format (e.g. Day1)
        paragraphs = [p.strip() for p in md_text.strip().split('\n\n') if p.strip()]
        data = {
            "type": "narrative",
            "headline": "",
            "intro": "",
            "lead_quote": "",
            "lead_story": "",
            "items_title": "제가 합류하면 세 가지를 기대하실 수 있습니다.",
            "items": [],
            "vision_title": "제가 회사에서 만들고 싶은 변화",
            "vision_body": "",
            "closing_title": "솔직하게 말씀드릴 부분",
            "closing_body": ""
        }
        idx = 0
        if idx < len(paragraphs) and paragraphs[idx].startswith("**") and paragraphs[idx].endswith("**"):
            data["headline"] = paragraphs[idx].strip("*")
            idx += 1
        if idx < len(paragraphs) and not paragraphs[idx].startswith("**"):
            data["intro"] = paragraphs[idx]
            idx += 1
        if idx < len(paragraphs) and paragraphs[idx].startswith("**"):
            data["lead_quote"] = paragraphs[idx]
            idx += 1
        if idx < len(paragraphs) and not paragraphs[idx].startswith("**"):
            data["lead_story"] = paragraphs[idx]
            idx += 1

        while idx < len(paragraphs):
            p = paragraphs[idx]
            if "세 가지를 기대" in p or "할 수 있는 일" in p:
                data["items_title"] = p.strip("*")
            elif any(p.startswith(f"**{k}") for k in ["첫째", "둘째", "셋째", "넷째", "1", "2", "3"]):
                m = re.match(r'\*\*(첫째|둘째|셋째|넷째|\d+)[,.]?\s*(.*?)\*\*\s*(.*)', p, re.DOTALL)
                if m:
                    num_text, title, body = m.groups()
                    data["items"].append({"num": num_text, "title": title, "body": body})
                else:
                    data["items"].append({"num": f"{len(data['items'])+1}", "title": "", "body": p})
            elif "만들고 싶은" in p or "변화" in p or "기여" in p:
                if p.startswith("**"):
                    m = re.match(r'\*\*(.*?)\*\*\s*(.*)', p, re.DOTALL)
                    if m:
                        data["vision_title"] = m.group(1)
                        data["vision_body"] = m.group(2)
                    else:
                        data["vision_body"] = p
                else:
                    data["vision_body"] = p
            elif "마지막" in p or "솔직하게" in p or "부족한" in p:
                if p.startswith("**"):
                    m = re.match(r'\*\*(.*?)\*\*\s*(.*)', p, re.DOTALL)
                    if m:
                        data["closing_title"] = m.group(1)
                        data["closing_body"] = m.group(2)
                    else:
                        data["closing_body"] = p
                else:
                    data["closing_body"] = p
            else:
                if not data["vision_body"]:
                    data["vision_body"] = p
                else:
                    data["closing_body"] += "\n\n" + p
            idx += 1

        return data


def escape_typst(text):
    if not text:
        return ""
    # In Typst content blocks: escape \, #, [, ]
    return text.replace("\\", "\\\\").replace("#", "\\#").replace("[", "\\[").replace("]", "\\]")


def generate_typst_4block(data, company, role, name, blog, github):
    intro_esc = escape_typst(data["intro"])
    sec3_esc = escape_typst(data["sec3_body"])
    sec4_esc = escape_typst(data["sec4_body"])

    typ = f"""
#set page(
  paper: "a4",
  margin: (top: 15mm, bottom: 14mm, left: 18mm, right: 18mm),
  footer: context align(center)[
    #set text(font: ("Pretendard", "Malgun Gothic"), size: 7.5pt, fill: rgb("#94a3b8"))
    {name} — {company} {role} 지원서
  ]
)

#set text(
  font: ("Pretendard", "Malgun Gothic"),
  size: 8.5pt,
  weight: 400,
  fill: rgb("#1e293b"),
  lang: "ko"
)

#set par(
  leading: 0.60em,
  justify: true
)

// Header
#grid(
  columns: (1fr, auto),
  gutter: 10pt,
  align: (left + horizon, right + horizon),
  [
    #text(size: 16pt, weight: 800, fill: rgb("#0f172a"))[{name}]
    #h(6pt)
    #box(
      fill: rgb("#eff6ff"),
      radius: 3pt,
      inset: (x: 6pt, y: 3pt)
    )[#text(size: 9pt, weight: 700, fill: rgb("#2563eb"))[{role}]]
    #v(2pt)
    #text(size: 8.3pt, weight: 500, fill: rgb("#64748b"))[{company} 지원]
  ],
  [
    #set text(size: 7.8pt, fill: rgb("#64748b"))
    #align(right)[
      #text(weight: 600, fill: rgb("#475569"))[Blog] #link("https://{blog}")[{blog.replace('@', '\\@')}] \\
      #v(1pt)
      #text(weight: 600, fill: rgb("#475569"))[GitHub] #link("https://{github}")[{github}]
    ]
  ]
)
#v(2pt)
#line(length: 100%, stroke: 1.2pt + rgb("#0f172a"))
#v(3pt)

// Opening Statement Box
#rect(
  width: 100%,
  fill: rgb("#f8fafc"),
  stroke: (left: 3.5pt + rgb("#2563eb"), rest: 0.5pt + rgb("#e2e8f0")),
  inset: (x: 10pt, y: 7.5pt),
  radius: (right: 3pt)
)[
  #set text(size: 8.3pt, fill: rgb("#334155"))
  #set par(leading: 0.60em)
  {intro_esc}
]

#v(2pt)

#let section_heading(title) = {{
  v(5pt)
  text(size: 10pt, weight: 700, fill: rgb("#0f172a"))[#title]
  v(1pt)
  line(length: 100%, stroke: 0.6pt + rgb("#cbd5e1"))
  v(2pt)
}}

#let item_block(num, title, body) = {{
  block(width: 100%, inset: (bottom: 3.5pt))[
    #grid(
      columns: (auto, 1fr),
      gutter: 4.5pt,
      [#box(fill: rgb("#eff6ff"), radius: 2.5pt, inset: (x: 4.5pt, y: 1.5pt))[#text(size: 7.8pt, weight: 700, fill: rgb("#2563eb"))[#num]]],
      [#text(weight: 700, size: 8.5pt, fill: rgb("#0f172a"))[#title]]
    )
    #v(1.5pt)
    #block(inset: (left: 2pt))[
      #set text(size: 8.2pt, fill: rgb("#334155"))
      #set par(leading: 0.58em)
      #body
    ]
  ]
}}

// Section 1
#section_heading("{escape_typst(data['sec1_title'])}")
"""
    for it in data["sec1_items"]:
        typ += f'#item_block("{it["num"]}", "{escape_typst(it["title"])}", [\n{escape_typst(it["body"])}\n])\n\n'

    typ += f'// Section 2\n#section_heading("{escape_typst(data["sec2_title"])}")\n'
    for it in data["sec2_items"]:
        typ += f'#item_block("{it["num"]}", "{escape_typst(it["title"])}", [\n{escape_typst(it["body"])}\n])\n\n'

    typ += f"""// Section 3
#section_heading("{escape_typst(data['sec3_title'])}")
#block(width: 100%, inset: (left: 2pt, bottom: 2pt))[
  #set text(size: 8.2pt, fill: rgb("#334155"))
  #set par(leading: 0.58em)
  {sec3_esc}
]

// Section 4
#section_heading("{escape_typst(data['sec4_title'])}")
#rect(
  width: 100%,
  fill: rgb("#f1f5f9"),
  inset: (x: 9pt, y: 6pt),
  radius: 3pt
)[
  #set text(size: 8.5pt, weight: 600, fill: rgb("#0f172a"))
  #set par(leading: 0.58em)
  {sec4_esc}
]
"""
    return typ


def generate_typst_narrative(data, company, role, name, blog, github):
    headline_esc = escape_typst(data["headline"])
    intro_esc = escape_typst(data["intro"])
    quote_raw = data["lead_quote"]
    # Parse quote bold lead if present
    quote_esc = escape_typst(re.sub(r'^\*\*(.*?)\*\*\s*', r'\1\n', quote_raw))
    story_esc = escape_typst(data["lead_story"])
    items_title_esc = escape_typst(data["items_title"])
    vision_title_esc = escape_typst(data["vision_title"])
    vision_body_esc = escape_typst(data["vision_body"])
    closing_title_esc = escape_typst(data["closing_title"])
    closing_body_esc = escape_typst(data["closing_body"])

    typ = f"""
#set page(
  paper: "a4",
  margin: (top: 14mm, bottom: 13mm, left: 17mm, right: 17mm),
  footer: context align(center)[
    #set text(font: ("Pretendard", "Malgun Gothic"), size: 7.5pt, fill: rgb("#94a3b8"))
    {name} — {company} {role} 지원서
  ]
)

#set text(
  font: ("Pretendard", "Malgun Gothic"),
  size: 8.3pt,
  weight: 400,
  fill: rgb("#1e293b"),
  lang: "ko"
)

#set par(
  leading: 0.58em,
  justify: true
)

// Header
#grid(
  columns: (1fr, auto),
  gutter: 10pt,
  align: (left + horizon, right + horizon),
  [
    #text(size: 16pt, weight: 800, fill: rgb("#0f172a"))[{name}]
    #h(6pt)
    #box(
      fill: rgb("#eff6ff"),
      radius: 3pt,
      inset: (x: 6pt, y: 3pt)
    )[#text(size: 9pt, weight: 700, fill: rgb("#2563eb"))[{role}]]
    #v(2pt)
    #text(size: 8.3pt, weight: 500, fill: rgb("#64748b"))[{company} 지원]
  ],
  [
    #set text(size: 7.8pt, fill: rgb("#64748b"))
    #align(right)[
      #text(weight: 600, fill: rgb("#475569"))[Blog] #link("https://{blog}")[{blog.replace('@', '\\@')}] \\
      #v(1pt)
      #text(weight: 600, fill: rgb("#475569"))[GitHub] #link("https://{github}")[{github}]
    ]
  ]
)
#v(2pt)
#line(length: 100%, stroke: 1.2pt + rgb("#0f172a"))
#v(3pt)

// Headline Box
#rect(
  width: 100%,
  fill: rgb("#f8fafc"),
  stroke: (left: 3.5pt + rgb("#2563eb"), rest: 0.5pt + rgb("#e2e8f0")),
  inset: (x: 10pt, y: 7pt),
  radius: (right: 3pt)
)[
  #text(size: 8.8pt, weight: 700, fill: rgb("#0f172a"))[{headline_esc}]
  #v(2pt)
  #set text(size: 8.1pt, fill: rgb("#334155"))
  #set par(leading: 0.58em)
  {intro_esc}
]

#v(2pt)

// Section 1: JD Connection & RAG Decision
#block(width: 100%, inset: (bottom: 2pt))[
  #set text(size: 8.1pt, fill: rgb("#334155"))
  #set par(leading: 0.58em)
  {quote_esc}
  #v(2pt)
  {story_esc}
]

#v(3pt)
#text(size: 9.8pt, weight: 700, fill: rgb("#0f172a"))[{items_title_esc}]
#v(1pt)
#line(length: 100%, stroke: 0.6pt + rgb("#cbd5e1"))
#v(2pt)

#let item_block(num_text, title, body) = {{
  block(width: 100%, inset: (bottom: 3pt))[
    #grid(
      columns: (auto, 1fr),
      gutter: 4pt,
      [#box(fill: rgb("#eff6ff"), radius: 2.5pt, inset: (x: 4pt, y: 1.5pt))[#text(size: 7.8pt, weight: 700, fill: rgb("#2563eb"))[#num_text]]],
      [#text(weight: 700, size: 8.4pt, fill: rgb("#0f172a"))[#title]]
    )
    #v(1.5pt)
    #block(inset: (left: 2pt))[
      #set text(size: 8.1pt, fill: rgb("#334155"))
      #set par(leading: 0.58em)
      #body
    ]
  ]
}}
"""
    for it in data["items"]:
        typ += f'#item_block("{escape_typst(it["num"])}", "{escape_typst(it["title"])}", [\n{escape_typst(it["body"])}\n])\n\n'

    typ += f"""#v(2pt)
#text(size: 9.8pt, weight: 700, fill: rgb("#0f172a"))[{vision_title_esc}]
#v(1pt)
#line(length: 100%, stroke: 0.6pt + rgb("#cbd5e1"))
#v(2pt)

#block(width: 100%, inset: (left: 2pt, bottom: 2pt))[
  #set text(size: 8.1pt, fill: rgb("#334155"))
  #set par(leading: 0.58em)
  {vision_body_esc}
]

#v(2pt)
#text(size: 9.8pt, weight: 700, fill: rgb("#0f172a"))[{closing_title_esc}]
#v(1pt)
#line(length: 100%, stroke: 0.6pt + rgb("#cbd5e1"))
#v(2pt)

#rect(
  width: 100%,
  fill: rgb("#f1f5f9"),
  inset: (x: 8pt, y: 5pt),
  radius: 3pt
)[
  #set text(size: 8.1pt, fill: rgb("#334155"))
  #set par(leading: 0.58em)
  {closing_body_esc}
]
"""
    return typ


def main():
    parser = argparse.ArgumentParser(description="Export Cover Letter Markdown to a single Pretendard PDF")
    parser.add_argument("markdown_file", help="Path to the cover letter markdown file")
    parser.add_argument("--company", help="Company name (defaults to parsed from filename)")
    parser.add_argument("--role", help="Job role/position (defaults to parsed from filename)")
    parser.add_argument("--name", default="오종민", help="Applicant name (default: 오종민)")
    parser.add_argument("--blog", default="velog.io/@acdongpgm", help="Blog URL")
    parser.add_argument("--github", default="github.com/jongmin-oh", help="GitHub URL")

    args = parser.parse_args()

    md_path = Path(args.markdown_file).resolve()
    if not md_path.exists():
        print(f"File not found: {md_path}", file=sys.stderr)
        sys.exit(1)

    stem = md_path.stem
    # Remove common suffixes like _자기소개서, -자기소개서, _자소서
    clean_stem = re.sub(r'(_|-)?(자기소개서|자소서)$', '', stem)
    parts = re.split(r'[_-]', clean_stem, maxsplit=1)

    company = args.company or (parts[0] if len(parts) > 0 else "회사")
    role = args.role or (parts[1].replace("-", " ").replace("_", " ") if len(parts) > 1 else "포지션")
    if role == "FDE":
        role = "FDE (Forward Deployed Engineer)"

    with open(md_path, "r", encoding="utf-8") as f:
        md_text = f.read()

    data = parse_markdown(md_text)

    parent_dir = md_path.parent
    pdf_file = parent_dir / f"{md_path.stem}.pdf"

    if data.get("type") == "narrative":
        typ_content = generate_typst_narrative(data, company, role, args.name, args.blog, args.github)
    else:
        typ_content = generate_typst_4block(data, company, role, args.name, args.blog, args.github)

    # Compile using a temporary file so no intermediate files are left behind
    with tempfile.NamedTemporaryFile("w", suffix=".typ", encoding="utf-8", delete=False) as tmp:
        tmp.write(typ_content)
        tmp_path = tmp.name

    try:
        typst.compile(tmp_path, output=str(pdf_file), font_paths=FONT_PATHS)
        print(f"[SUCCESS] Generated: {pdf_file}")
    finally:
        if os.path.exists(tmp_path):
            os.remove(tmp_path)


if __name__ == "__main__":
    main()
