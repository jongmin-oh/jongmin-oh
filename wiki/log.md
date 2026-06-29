# Wiki Log

Append-only record of all wiki operations. Each entry starts with `## [DATE] type | description`.

Quick parse: `grep "^## \[" wiki/log.md | tail -10`

---

## [2026-06-21] init | Wiki initialized from README.md

## [2026-06-21] update | 운영도구내재화.md — Slack 인터랙션 운영 채널 추가 (이벤트 하트 지급, 사용자/콘텐츠 재재, CS 알림, 불건전 챗봇 필터링), 핵심 맥락에 전담 운영자 부재 + 모바일 대응 배경 추가

Seed pages created: overview.md, timeline.md, entities/reppley.md, entities/indj.md, entities/atommerce.md, entities/likelion.md, papers/bert-emotion-lyrics.md, index.md.

## [2026-06-21] ingest | career-wiki-seed.md — 오종민 Zero to One 위키

## [2026-06-27] update | 캐릭터챗봇API.md — 24/7 운영 & 장애 대응 섹션 추가 (gunicorn 워커 타임아웃, LLM 프로바이더 장애 폴백, 로그 클라이언트 객체 재생성 OOM, ECS 기본 타임아웃 15초). 포트폴리오 강점① "빠름+안정 운영" 근거. 출처: 본인 회고 2026-06-27

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

## [2026-06-27] update | working-style.md — 원칙 7 "24시간 실시간 B2C 운영 경험" 추가

사용자가 본인 강점으로 제시: "24시간 돌아가는 B2C 운영 경험" — 대부분의 B2B 개발자가 못 느끼는 차별점이라는 본인 프레이밍. working-style 핵심 원칙 6→7로 확장, 신규 원칙 7 신설(실시간 트래픽 감각/사용자 반응 즉시성/악용 상시성 + B2B 대비 차별점 강조, 원칙 1과의 폭 vs 깊이 구분). overview.md 핵심 특징 표에 "24시간 B2C 운영" 행 추가. index.md working-style 요약 갱신.

## [2026-06-27] update | overview.md + working-style.md — 헤드라인 강점 "초기 검증 제품 최속 구현" 명시

사용자가 본인 강점으로 제시: "기술에 매몰되지 않고 신경 덜 쓰는 서버리스로 초기 POC 검증 제품을 가장 빠르게 구현." 기존에 0→1·빠른 프로토타이핑(overview 정체성)과 서버리스 우선(working-style 원칙 3)으로 분산돼 있던 것을 하나로 꿰어 헤드라인 강점으로 승격. overview 정체성 블록에 "헤드라인 강점" 문단 추가 + 핵심 특징 표에 "초기 검증 제품 최속 구현" 행 추가. working-style 원칙 3 제목을 "서버리스 우선 — 신경 덜 쓰고 최속 검증"으로 바꾸고 목적(운영 신경 최소화 = POC 최속 검증, 헤드라인 강점) 문단 추가, overview 크로스링크.

## [2026-06-27] update | 헤드라인 강점 ↔ 초기-스타트업-시행착오 양방향 크로스링크

"초기 검증 제품 최속 구현"(강점)과 클러스터 A "완벽주의가 타이밍을 죽인다"(교훈)를 동전의 양면으로 연결. reflections/초기-스타트업-시행착오 "이 시행착오들이 낳은 것" 섹션에 강점=교훈의 실행 엔진 bullet 추가. working-style 원칙 3에 강점=교훈에서 굳은 것이라는 출처 링크 추가. 양쪽 updated 2026-06-27 갱신.

## [2026-06-27] ingest | reflections/개발을-잘한다는-것.md 신규 생성

사용자가 본인이 다시 내린 "개발을 잘한다는 것"의 정의 5가지 제시(AI 시대): 1.단순 설계 2.문서처럼 읽히는 코드 3.AI가 이해하는 구조 4.꼼꼼한 테스트 5.실수의 경험화. 전제="프로그램 잘 짜는 능력은 더 이상 기준이 아니다(commoditize)". 신규 reflection 페이지 생성 — 관통선: 1·2·3=명료성 축(단순함이 사람·AI 이해 동시 향상), 4·5=신뢰성 축(사전/사후 실수 차단). 크로스링크: working-style 원칙 2·6(실천편), 초기-스타트업-시행착오 5번↔전제(실패의 자산화), overview. working-style·시행착오 페이지에 역링크 추가, index.md에 행 추가.

## [2026-06-29] update | 맛보기채팅웹.md — 디자이너와 Figma 협업 내용 추가

"협업 — 디자이너와 Figma로 소통하며 개발" 섹션 신규 추가. 디자이너가 Figma로 UI/UX 시안을 잡으면 그 시안 기준으로 컴포넌트·레이아웃·인터랙션 구현하며 디테일 맞춰가는 협업 흐름. 의의=단순 풀스택 구현을 넘어 디자인 핸드오프를 읽고 시안대로 프론트 구현하는 협업 역량의 실례. 스택에 Figma(디자인 핸드오프) 추가, 태그 figma·design-collab 추가, updated 2026-06-29 갱신.
