# Jongmin Oh — Personal Career Wiki Schema

This is the schema and operating manual for Jongmin Oh's personal LLM-maintained career wiki.
The LLM reads this file at the start of every session to understand the wiki's structure and conventions.

---

## Directory layout

```
/
├── CLAUDE.md          ← this file (schema + instructions)
├── raw/               ← immutable source documents (never modified by LLM)
│   └── ...
└── wiki/              ← LLM-maintained knowledge base
    ├── index.md       ← catalog of all wiki pages (update on every change)
    ├── log.md         ← append-only session log
    ├── overview.md    ← top-level career synthesis
    ├── timeline.md    ← chronological career timeline
    ├── entities/      ← companies, orgs, institutions
    ├── projects/      ← specific projects and products built
    ├── papers/        ← academic/research output
    ├── skills/        ← technical skills and domain knowledge
    └── reflections/   ← lessons learned, career insights, self-analysis
```

---

## Page conventions

Every wiki page begins with YAML frontmatter:

```yaml
---
title: <Page title>
type: overview | timeline | entity | project | paper | skill | reflection
tags: [comma, separated, tags]
created: YYYY-MM-DD
updated: YYYY-MM-DD
sources: [list of raw/ filenames that informed this page]
---
```

- Cross-link related pages with `[[Page Title]]` (Obsidian-style wikilinks).
- All pages are in Korean or English — follow the user's language in conversation.
- Keep pages factual and structured. Avoid padding.

---

## Operations

### Ingest
When the user provides a new source (journal entry, article, link, transcript):
1. Read the source carefully.
2. Discuss key takeaways with the user.
3. Save the source to `raw/` if it's a file.
4. Write or update relevant wiki pages (projects, entities, skills, reflections).
5. Update `wiki/index.md`.
6. Append an entry to `wiki/log.md`: `## [YYYY-MM-DD] ingest | <source title>`.

### Query
When the user asks a question:
1. Read `wiki/index.md` to find relevant pages.
2. Read the relevant pages.
3. Synthesize and answer with citations like `(→ [[Page]])`.
4. If the answer is valuable enough to persist, offer to file it as a new wiki page.

### Update
When the user shares new information about themselves (memory, correction, new role):
1. Find and update all affected pages.
2. Note any contradictions with previous content.
3. Update `wiki/index.md` and log the change.

### Lint
When the user asks for a wiki health check:
1. Look for orphan pages, broken cross-links, stale claims, missing pages.
2. Suggest gaps that could be filled by asking the user questions.
3. Report findings and ask for direction.

---

## Tone and style

- This is a personal wiki for Jongmin Oh to understand and articulate his own career.
- Be honest, precise, and substantive. No filler.
- Surface patterns and insights the user may not have articulated themselves.
- When building reflections or skill pages, synthesize across multiple sources — don't just summarize one entry.

---

## Current known facts (seed)

Populated from README.md on wiki initialization:

- **Name**: Jongmin Oh (오종민)
- **Current role**: AI Engineer & Co-Founder at Reppley
- **Past roles**: AI Engineer at INDJ (music recommendation), AI Engineer at atommerce (chatbot RONI)
- **Education**: LIKELION AI program, 1st batch
- **Research**: Paper on emotion analysis in song lyrics using BERT + emotional lexicon (Korean Computer Information Society, July 2022)
- **Blog**: https://velog.io/@acdongpgm
