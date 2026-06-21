# Wiki Log

Append-only record of all wiki operations. Each entry starts with `## [DATE] type | description`.

Quick parse: `grep "^## \[" wiki/log.md | tail -10`

---

## [2026-06-21] init | Wiki initialized from README.md

## [2026-06-21] update | 운영도구내재화.md — Slack 인터랙션 운영 채널 추가 (이벤트 하트 지급, 사용자/콘텐츠 재재, CS 알림, 불건전 챗봇 필터링), 핵심 맥락에 전담 운영자 부재 + 모바일 대응 배경 추가

Seed pages created: overview.md, timeline.md, entities/reppley.md, entities/indj.md, entities/atommerce.md, entities/likelion.md, papers/bert-emotion-lyrics.md, index.md.

## [2026-06-21] ingest | career-wiki-seed.md — 오종민 Zero to One 위키

사용자가 직접 작성한 커리어 정리 문서 ingest. 레플리 4년 커리어 전체 + 개인 프로젝트.

신규 생성 페이지 (13개):
- entities/inhapoly.md, entities/cheonggang.md
- projects/reppley-main-api.md, projects/suntok.md, projects/image-generation.md
- projects/long-term-memory.md, projects/preview-chat.md, projects/ops-tools.md
- projects/obok.md, projects/et5-typos-corrector.md, projects/kcbert-formal-classifier.md
- projects/nurscheck.md, projects/comfyui-api-server.md, projects/medical-ai.md
- skills/technical.md, skills/working-style.md

업데이트 페이지 (6개):
- overview.md, timeline.md, entities/reppley.md, entities/indj.md, entities/atommerce.md, papers/bert-emotion-lyrics.md, index.md

Raw 소스: raw/career-wiki-seed.md

## [2026-06-21] ingest | 초기 스타트업 시행착오 회고

사용자 구술 회고 5개 ingest → reflections/초기-스타트업-시행착오.md 신규 생성.
3 클러스터: A. 완벽주의가 타이밍을 죽인다(1.노출 두려움→수요 부재, 2.완벽 추구→사용자 이탈, 3.MVP 스코프 크립), B. 잘못된 채용의 진짜 비용(4.bad hire가 A급 인재를 밀어냄), C. 만들기가 만병통치약(5.지표 하락에 데이터 진단 없이 기능 추가 반복).
관통선: "개발자 본능(만들어서 해결)이 초기엔 가장 비싼 버릇".
크로스링크: skills/working-style, 그로스해킹과 제품관점의 전환, overview.
index.md 업데이트.

## [2026-06-21] update | 초기-스타트업-시행착오.md — 6번(solution-first) 메타 승격

추가 회고 "문제로부터 시작하지 않고 솔루션을 문제에 맞췄다"를 평면 항목이 아니라 1·3·5를 꿰는 근본 진단으로 승격. "근본 진단 — 문제가 아니라 솔루션에서 시작했다" 섹션 신설(증상↔루트 매핑표), 관통선 표에 루트 행 추가, 전제 문단을 solution-first로 재서술. problem-first ↔ 그로스해킹 reflection 연결. index.md 요약 갱신.

## [2026-06-21] update | 초기-스타트업-시행착오.md — 클러스터 D(effort-first) 추가, 1차 마무리

추가 회고 "중요한 건 미루고 구현하기 쉬운 것만 만들었다(이건 빨리 할 수 있잖아요)"를 클러스터 D "쉬운 것이 중요한 것을 밀어낸다"(우선순위 역전, effort-first→impact-first)로 신설. 근본 진단 섹션에 "effort-first는 solution-first의 사촌"(출발점 vs 순서) 연결 추가. 관통선 표에 D행 추가. index.md 갱신. → 사용자 "1차 마무리, 생각나면 더".

## [2026-06-21] update | 역방향 링크 — working-style·그로스해킹 → 초기-스타트업-시행착오

skills/working-style.md: 원칙2(오버엔지니어링 경계)에 "기원: 시행착오 클러스터 A/3번" 백링크, 남은 과제에 "자각의 뿌리: 시행착오 5번(클러스터 C/solution-first)" 백링크. reflections/그로스해킹: "관점의 전환" 절에 "이 세션이 충격이었던 이유=시행착오를 언어로 정리, problem-first가 solution-first의 반대편" 백링크. 양방향 연결 완성.
