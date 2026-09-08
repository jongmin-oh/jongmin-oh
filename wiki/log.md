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

## [2026-07-11] update | 장기기억 시스템 — Redis → DynamoDB 마이그레이션

- 채팅방 단위 누적으로 Redis 메모리 한계 → DynamoDB 마이그레이션 사실 추가 (본인 제보).
- 갱신: 장기기억시스템.md(구현·스택·결과), overview.md, working-style.md(원칙 2), index.md, interview/fulcrum-2차-준비.md(why-chain 2행 추가).

## [2026-09-02] ingest | nightly/ 저장소 → projects/personal/Nightly.md 신규 생성

별도 저장소 `nightly/`(2026.08.09 시작)의 코드를 직접 읽어 프로젝트 페이지 신설. 메신저로 특정 페르소나와 대화하는 봇 — 캐릭터 챗봇을 에이전트 프레임워크 + 지식 그래프 위에서 다시 만드는 프로젝트.

기록할 만한 판단: ①검색을 페르소나 모델에서 분리(말투 오염·캐시 붕괴·지연) ②할루시네이션을 '더 정확한 검색'이 아니라 '근거를 넉넉히'로 뒤집어 해결 ③상태 50필드를 enum 정규화 없이 문자열로 둔 것(프롬프트에서 더 낫고 매핑 로직이 안 붙음) ④서버리스에서만 생기는 문제 4종을 직접 해결 ⑤지식 그래프 빌드 시 허브 도달성까지 셀프체크(도달 못 하는 주제 = 검색이 영원히 못 닿는 섬).

[[projects/company/장기기억시스템]]과의 대비를 의의에 명시 — 거기서는 RAG를 걷어냈고 여기서는 넣되 사실 단위 + 에이전트 선별로 재설계. 같은 문제의 반대편 실험.

갱신: index.md · timeline.md · skills/technical.md · skills/working-style.md · overview.md.

※ 저장소의 인물·관계 문서는 개인 신상이라 커리어 위키로 옮기지 않았다. 페르소나 이름·구현 세부(파라미터·ID 설계 등)도 페이지에서 제외 — 서비스 성격과 일하는 방식만 남긴다(본인 지시).

## [2026-09-02] ingest | AI-novel-api/ 저장소 → projects/company/AI소설생성API.md 신규 생성

레플리 소설 콘텐츠 생성 서비스(2026.06~08, 단독)를 저장소 직접 분석해 프로젝트 페이지 신설. 사용자가 장르·분위기·시점·문체·인물을 고르면 웹소설을 연재 형태로 생성하는 기능. 백지 생성과 유저 초안 보강을 짝으로 제공.

일하는 방식으로 남긴 것: ①경쟁 서비스 기능을 옵션 단위까지 명세화한 뒤 착수(시장 검증→흡수→자사 재검증) ②"다음 화가 안 이어진다"를 요약이 마지막 장면의 위치·긴장을 소실시키는 문제로 진단해 원인에서 해결 ③모델 선택을 실험으로 결정 — LLM 심사위원 무변별(94~98%) → 직접 정독 재채점도 무승부 → 결론은 품질이 아니라 결과의 예측 가능성(분량 요동·생성 실패)에서 남 ④자주 번복되는 결정을 저장소 안에 "현재 결정 + 변경 이력(원복도 새 줄)"로 기록해 문서↔코드 drift를 잡아냄.

갱신: index.md · timeline.md · entities/companies/레플리.md · skills/technical.md · overview.md(핵심 특징 "모델 선택을 실험으로 결정" 행).

※ **구현 세부·스택·파라미터는 회사 자산이라 위키 전반에서 의도적으로 제외**(본인 지시). 서비스 성격과 일하는 방식만 기록한다. 초안에 있던 아키텍처·모델명·인프라 서술은 이 페이지들에서 제거했다.
※ 소스 `AI-novel-api/`는 자체 .git을 가진 별도 저장소라 raw/로 복사하지 않았다.

## [2026-09-02] update | Nightly — 프로젝트의 '왜'가 채워짐 (본인 설명)

코드만 읽었을 때 빠져 있던 두 가지를 본인이 보완: ①Nightly는 **레플리에서 구현하지 못했던 계획들을 실제로 만들어보는 프로젝트**다 ②**하나의 캐릭터에만 집중**하는데, 이유는 **대부분의 과금 유저가 여러 캐릭터를 옮겨 다니기보다 한 캐릭터와 오래 쌓은 애착 관계를 더 중요하게 여겼기 때문**. 하나로 좁히면 그 캐릭터의 온톨로지를 구축해 훨씬 깊이 있는 서비스를 만들 수 있다.

즉 온톨로지·GraphRAG는 기술 취향이 아니라 **과금 유저 행동 관찰 → 한 캐릭터 집중 → 깊이 확보**라는 제품 결정에서 나온 아키텍처다. LangGraph + 다중 도구 + ReAct도 흐름을 코드로 박지 않고 **모델이 판단하게 하는 모델 드리븐 구조**를 의도한 것.

갱신: Nightly.md('왜 하나의 캐릭터인가' 절 신설, 모델 드리븐·온톨로지 서술 보강, 의의 재작성), 캐릭터챗봇API.md('이어지는 실험' 절 + 역링크), overview.md(핵심 특징 행 추가), index.md · timeline.md 요약 갱신.

## [2026-09-07] update | 캐릭터챗봇API.md 외 — 프롬프트 트래픽 분할 A/B 테스트 추가

사용자 구술 경험(커버레터 작업 중 확인) 반영:
- 레플리 캐릭터 챗봇 서비스에서 팀 내 주관적 의견 대립(설득 싸움)을 피하고 데이터로 결론을 내리기 위해 퇴사 몇 달 전 프롬프트 A/B 테스트 환경 구축.
- 실제 인입 트래픽을 분할 서빙하며, 핵심 평가 지표로 '대화 지속 턴 수' 설정.
- 4회 반복 실험으로 유료 사용자 대화 지속 턴 수 45% 향상 달성.

갱신:
- projects/company/캐릭터챗봇API.md: '프롬프트 A/B 테스트 (트래픽 분할 검증)' 섹션 신설, 결과 지표 추가, 태그 ab-test 추가.
- skills/technical.md: AI/ML 표에 '프롬프트 A/B 테스트' 행 추가.
- reflections/그로스해킹과-제품관점의-전환.md: '지금 하고 있는 것 & 실천'에 프롬프트 A/B 테스트 실행 내용 추가.
- overview.md: 핵심 특징 표 및 주요 지표에 대화 지속 턴 수 45% 향상 지표 추가.
- index.md: 캐릭터 챗봇 API 요약 갱신.

## [2026-09-08] update | 선톡 전송 시스템 — 평가 지표 정의 + 자동 채점 (본인 확인, 커버레터 작업 중)

기존 기록의 `⚠️ 리텐션 등 정량 지표는 당시 추적 못함 [추적 못함]`을 **본인 확인으로 정정**한다. 실제로는 지표를 추적 못한 게 아니라, **지표가 없는 상태에서 지표를 정의하는 일을 먼저 했다.**

- **문제**: 경량 모델(비용 제약)로 생성한 선톡 5만 건을 직접 읽어도 좋고 나쁨을 가를 기준이 없었음. "캐릭터답다"·"자연스럽다"는 사람마다 잣대가 달라 합의 불가.
- **해법**: 기능의 본질적 목표인 **리텐션 상승**으로 되돌아가 측정 가능한 단일 지표를 **푸시 메시지 클릭률**로 정의.
- **적용**: 페르소나 일관성·문장 완성도 등 부가 목표보다 클릭률을 우선하도록 **프롬프트 지침 개정**.
- **자동화**: 세운 기준을 **자동 채점 시스템**으로 옮겨 5만 건 수작업 검수 병목 제거.

이로써 선톡(2022~23) → 캐릭터 챗봇 A/B 테스트(퇴사 전) 사이에 **"기준부터 정의한다"**는 일관된 패턴 선이 생겼다. A/B 테스트의 '대화 지속 턴 수' 단일 지표 설정은 선톡에서 이미 한 번 해본 일이다.

갱신: projects/company/선톡전송시스템.md('평가 기준을 어떻게 정의했는가' 절 신설, 한 일·결과·tags·sources 갱신) · projects/company/캐릭터챗봇API.md(A/B 절에 선행 사례 역링크) · skills/technical.md('평가 지표 정의' 행 신설, LLM-as-judge에 선톡 자동 채점 추가) · overview.md(핵심 특징 행 + 주요 지표) · index.md 요약.

※ 남은 미확인: **클릭률 개선 폭의 구체 수치**는 기록에 없음 `[수치 확인 필요]`. 면접 대비상 확인 권장.

## [2026-09-08] update | 선톡 시스템 — '아쉬운 점: 배치 추론' 추가 (본인 회고)

본인 회고: 시간이 더 있었다면 **Gemini Batch API** 등 배치 추론으로 **같은 비용에 더 상위 모델**을 써서 선톡 품질을 올릴 수 있었다.

핵심은 선톡이 **예약 발송 비동기 워크로드**라 지연을 감내할 수 있었다는 점. 당시 판단은 "비용 부족 → 경량 모델"로 바로 갔는데, 실제 선택지는 모델 등급뿐 아니라 **추론 방식(실시간 vs 배치)** 에도 있었다. 워크로드의 지연 허용치를 먼저 따졌다면 트레이드오프 축이 하나 더 보였을 사례.

갱신: projects/company/선톡전송시스템.md('아쉬운 점 — 배치 추론을 못 썼다' 절 신설, tags에 batch-inference).
