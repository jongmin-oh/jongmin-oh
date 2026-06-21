# 오종민 — Zero to One 위키

> 원본 소스: 사용자가 직접 작성한 커리어 정리 문서
> 수집일: 2026-06-21

---

AI 챗봇 '레플리'를 코파운더로 4년간 0→1로 키운 개발자
일의 경계를 가리지 않고, 페인포인트가 보이면 곧장 자동화하며, 회사에 필요한 일을 스스로 찾아서 하는 인재
MAU 3만 · 일 최고 70만 대화 규모까지 직접 만들고 운영 (TIPS · 예비창업패키지 · 구글 창구 선정)

---

## 경력

| 회사 | 기간 | 역할 |
|------|------|------|
| 레플리 (Reppley) | 2022.10 – 재직중 (3년 8개월) | AI Co-founder / 백엔드·AI 개발 |
| 아토머스 | 2021.09 – 2021.12 (4개월) | AI 엔지니어 |
| 인디제이 | 2021.04 – 2021.07 (4개월) | AI 엔지니어 |

---

## 핵심 역량

Python · FastAPI · AWS · AWS Lambda / SAM · React · RDBMS · Redis
Stable Diffusion · Prompt Engineering · SBERT / 임베딩 검색 · Faiss / ONNX 최적화

### 기술 성향 — 서버리스 우선

개인적으로 서버리스를 굉장히 선호하며, 가능하면 서버리스로 설계한다. 운영 부담과 고정 비용을 줄이고, 트래픽에 따라 자연스럽게 확장되는 구조를 좋아한다.

특히 AWS Lambda에 아주 익숙하고, SAM으로 빠르게 구현·배포한다.

- 선톡 시스템 — 메인 서버에 붙일 수도 있었지만 복잡성을 우려해 별도 Lambda(SAM) + SQS로 분리
- 이미지 자동 검열·이벤트 보상 등 자동화 — 상시 서버 대신 이벤트 기반으로 처리
- 정적 프론트 — 맛보기 웹·널스체크를 S3 + CloudFront로 서버리스 호스팅
- 단, GPU 추론처럼 서버리스가 비용·지연 면에서 불리한 워크로드는 직접 GPU 계약(시간당 단가)으로 전환하는 등 워크로드 특성에 맞게 선택한다

### 일하는 방식

- 업무의 경계를 가리지 않는다 — 개발에 그치지 않고 제품이 굴러가는 데 필요한 일이면 직접 메운다. QA 테스트 전담, 앱 내 공지사항 관리, 이벤트 웹뷰 페이지 관리, 이메일 CS 대응, 콘텐츠 검열까지 운영 전반을 직접 담당했다. 그렇게 직접 부딪힌 페인포인트를 다시 도구·자동화로 해결한 것이 운영 도구 내재화다.
- 오버엔지니어링 경계 — 간결함을 최우선으로 둔다. 컴포넌트를 더하기 전에 "정말 필요한가"를 먼저 묻고, 가장 단순한 가설부터 검증한다. (예: 장기기억에서 업계 표준 RAG를 검토 후 폐기하고 LLM+Redis로 단순화)
- 비용·복잡성 우선 고려 — 기능을 넣기 전에 운영 비용이 선형으로 늘지 않는지, 운영 부담이 커지지 않는지부터 본다.
- 검증된 패턴 빠른 흡수 — 시장에서 통한 기능·UX를 빠르게 흡수해 자사 제품에 맞게 구현하고, 자사 사용자에게 다시 검증한다.
- 트레이드오프 직접 진단 — 기존 도구의 한계가 명확하면 직접 만들어 해결한다. (예: ComfyUI 속도 + SD WebUI API를 합친 서빙 엔진 자체 구현)
- 명세 주도 개발 (SDD) — AI가 코드를 써주는 시대에 병목은 "어떻게 짜지"가 아니라 "무엇을 원하는지 정의하고 결과를 판별하기"로 옮겨갔다고 본다.
- 학습 태도 — 읽고 넘기지 않고 바로 적용. 새로운 방식이 보이면 지금 하는 프로젝트에 직접 적용해 내 스킬로 굳힌다.
- 남은 과제 — 리텐션·전환 같은 정량 지표를 끝까지 추적·검증하는 사이클은 부족했음을 인지하고 보완하려 한다.

---

## 레플리 (Reppley) — AI Co-founder

2022.10 – 재직중 · 정규직 · 백엔드·AI 개발

캐릭터 페르소나 챗봇 서비스를 0→1로 만들고 운영. MAU 3만 · 일 70만 건 규모까지 성장.

### 메인 — 캐릭터 페르소나 챗봇 서비스 API (2024.01 – 2026.05)

주요 기능: 캐릭터 챗 / 속마음 엿보기 / 사진 보내기 / 페르소나 만들기·다듬기 / 상황 이미지
한 일: 시장 패턴 흡수 / 비용 최적화 (대화 요약 + 프롬프트 캐싱, 건당 비용 30% 절감) / 5개 기능 직접 설계·구현
스택: AWS ECS · AWS ElastiCache · Python · FastAPI
결과: MAU 3만, 일 최고 70만 건 / 구글플레이 소셜 6위, 앱스토어 전체 107위 / TIPS · 예비창업패키지 · 구글 창구 선정

### 선톡 전송 시스템

목표: 캐릭터가 먼저 말 걸어오는 경험으로 리텐션 향상
기능: Continue (이전 대화 이어가기) / WakeUp (새 대화 시작)
한 일: 별도 Lambda(SAM) + SQS로 분리 / LLM 호출 메시지 생성 / 기존 채팅 발송 시스템 재사용 / SQS 비동기 처리 / 7일간 5만 건 직접 검토하며 프롬프트 반복 개선
스택: AWS Lambda (SAM) · AWS SQS · Python
결과: 일평균 8,000건 발송 안정 운영 / 리텐션 지표 추적 못함 [추적 못함]

### 캐릭터 이미지 생성 서비스 0→1 구축

문제: 외부 서비스 이탈 / SaaS API 단가 부담 → "앱 내 무료 + 빠른 생성" 차별점 직접 구축
한 일:
- 인프라: GPU 직접 계약 (가비아 RTX A 시리즈), 호출당→시간당 단가 전환
- 속도: ComfyUI 속도 + SD WebUI API 호환 헤드리스 서버 직접 구현 (ComfyUI API Server)
- 비용: 한→영 번역 키워드 캐싱 시스템 구축
- 운영 리스크: NSFW 감지 모델 자체 개발
스택: Python · FastAPI · ComfyUI · Stable Diffusion · 가비아 GPU (RTX A)
결과: 일평균 3,000건 / 생성 속도 5초 이내 (경쟁사 대비 최대 12배) / 인프라 비용 월 24만원 (SaaS 대비 최소 5배 절감)
정리 글: https://buly.kr/FhPsQw

### 장기기억 시스템

문제: 오래 대화할수록 캐릭터가 이전 대화를 기억 못함
의사결정: RAG 검토 후 4가지 이유로 폐기 (운영 비용 / 운영 복잡성 / 아키텍처 락인 / 도메인 가설)
한 일: LLM + Redis 조합으로 구현 / LLM-as-judge 평가 파이프라인 / 자체 벤치마크 반복 튜닝
스택: AWS ElastiCache (Redis) · 경량 LLM
결과: 자체 벤치마크 기준 품질 향상 / RAG 대비 비용·복잡성 절감 / 안정 운영

### 맛보기 채팅 웹페이지

문제: 휴대폰 번호 가입 거부감 + 앱 설치 마찰 → 비오가닉 유저 전환율 낮음
기능: 회원가입·앱 설치 없이 즉시 채팅 체험 / 틱톡 홍보 연동 / 공유 링크 바이럴 루프
한 일: React 미경험 → AI 코딩 도구로 직접 구현·배포 / 틱톡 유입 연결 / 바이럴 루프 설계
스택: React · AWS S3 + CloudFront + Route 53
결과: 진입점 신규 출시 / 틱톡 채널 연동 / 전환 지표 추적 못함 [추적 못함]
URL: https://chat-preview.reppley.com

### 운영 도구 내재화

맥락: QA·공지사항·이벤트·이메일 CS·콘텐츠 검열 등 운영 전반 직접 담당 → 페인포인트를 도구화
관리자 페이지 (셀프서비스 전환):
- 큐레이션 관리자: SQL → 드래그앤드롭
- 공지사항 관리자: S3 업로드 + SQL → 담당자 직접 작성·발행
- 테스트 어드민: QA 반복 요청 → 셀프 처리
- 운영 어드민: 하트 지급·문의 답변·커스텀 푸시·유저 조회 → UI 통합
자동화:
- SNS 이벤트 보상: 구글폼→스프레드시트→Postman 수동 → 자동 지급
- 앱 테스트: 수작업 → Appium + Small TC 자동화
- 캐릭터 이미지 자동 검열: 부적절 사진 노출 사건 이후 자동화
- 채팅 데이터 로그 수집·분석: 슬랙 정기 리포트
- 유저 문의 이메일 → 슬랙 라우팅
스택: FastAPI · JavaScript · HTML · CSS · AI 코딩 도구
결과: 9개 반복 작업 셀프서비스 전환 / 이미지 노출 사고 재발 방지

---

## 이전 경력

### 아토머스 — AI 감정 위로 챗봇 '로니' (2021.09 – 2021.12, 4개월)

배경: 마인드카페 내 무응답 고민 게시글 → AI 캐릭터 로니가 공감·위로 댓글 자동 작성
담당: 챗봇 응답 API 개발 (1인)
성과:
1. 데이터 바우처 Q&A 3만 건 + 마인드카페 80만 건 → 최종 60만 건 학습 데이터셋 구축
2. SentenceTransformer(klue/roberta) 기반 Retrieval 챗봇 설계·학습
3. Flask 기반 모델 서빙 API 개발
스택: Flask · SentenceTransformer (klue/roberta)

### 인디제이 — 음원 가사 감정 분석 (2021.04 – 2021.07, 4개월)

배경: 음원별 가사 감정 분석 → 추천시스템 Feature로 활용. 현재 감정에 맞는 채널 추천
담당: 한국어·영어 가사 감정 분류 모델 개발 (1인 단독)
성과:
1. 한국어 가사 15,000문장 직접 라벨링, 영어는 Kaggle 공개 데이터셋 활용
2. 한국어 — BERT 긍·부정 분류 + Lexicon 결합 하이브리드 모델
3. 영어 — BERT 다중 감정 분류(6-class)
4. 분석 결과를 추천시스템 감정 Feature로 통합
스택: Python · TensorFlow · MySQL · Pandas

---

## 개인 프로젝트

🤗 Hugging Face 공개 모델 누적 다운로드 합산 15만+ (150,436회)
- 맞춤법 교정기: 111,795회
- 존댓말/반말 분류기: 38,641회

### 위로 챗봇 '오복이'

대학교 4학년 졸업작품 · 1인 개발 · 2022.11 출시 후 사비로 운영·유지보수

개요: 고민·질문에 위로로 답하는 감성 대화 챗봇 (심리상담사 컨셉, 물범 캐릭터). Retrieval 기반 싱글턴 챗봇.
프론트엔드: 카카오톡 채널 + 오픈빌더
웹사이트: Streamlit (도메인 j5ng.com, CloudFront HTTPS)
서버: 초기 GCP 무료 크레딧 → AWS 예약 인스턴스(t3a-medium) 사비 구매

개발 로그:
| 버전/시점 | 변경 |
|-----------|------|
| v1.0 (2022.11) | Elasticsearch 키워드 검색 + nori 형태소 분석기, 답변 후보 10만 개 |
| v2.0 (2023.02) | ES → SBERT 임베딩 검색 (klue/roberta-base KorSTS/NLI 파인튜닝 → KR-SBERT) |
| 2023.04 | Faiss + PQ 양자화 → 임베딩 메모리 1/4, 검색 속도 향상 |
| 2023.04 | Torch → ONNX uint8 양자화 → 임베딩 속도 약 7배, 모델 1/4, 정확도 손실 거의 없음 |
| 2023.06~09 | 답변 데이터 재구축. ChatGPT·HyperClova 재생성 + 검수·중복 제거 → 최종 35,363건 |
| 2023.10 | 하이브리드 검색(BM25 + 임베딩) RRF 결합 |

스택: Python · FastAPI · Gunicorn · SBERT · ONNX · Faiss · ChromaDB · Elasticsearch · Streamlit · AWS EC2/CloudFront · 카카오톡 오픈빌더
링크: https://comfort.j5ng.com/ · http://pf.kakao.com/_BNZRb · https://github.com/jongmin-oh/comfort_chatbot

### 한국어 맞춤법 교정기 (et5-typos-corrector)

ETRI ET5 fine-tuning · 한국어 구어체 전용 맞춤법 교정
학습 데이터: 모두의 말뭉치 + 맞춤법 교정 데이터 → 318,882쌍
GPU 지원: AICA(인공지능산업융합사업단)
누적 다운로드: 111,795회
링크: https://huggingface.co/j5ng/et5-typos-corrector
스택: Python · PyTorch · HuggingFace Transformers · T5 (ET5) · Fine-tuning

### 존댓말/반말 분류기 (kcbert-formal-classifier)

KcBERT(beomi/kcbert-base) fine-tuning · 존댓말/반말 판별
데이터: 스마일게이트 말투 데이터셋 + AI허브 감성 대화 말뭉치
누적 다운로드: 38,641회
예: "교수님께서 자료 가져오라했는데 기억나?" → 반말(92.86%) 정확 분류
링크: https://huggingface.co/j5ng/kcbert-formal-classifier
스택: Python · PyTorch · HuggingFace Transformers · KcBERT · Fine-tuning

### 널스체크 (Nurse Burnout Check)

신규·저연차 간호사를 위한 소진·이직·회복 의사결정 지원 서비스
계기: 1년차 간호사인 동생의 고민 → 간호사 맥락에 특화된 번아웃 진단 도구 부재 → 직접 제작
기능:
- 간호사 특화 5차원 자가점검: 25문항·약 4분 (개인번아웃/업무번아웃/정서위험/이직압력/환경불일치)
- 점수가 아닌 결정 지원: 유형 분류(고위험 소진형/환경 불일치형/준비된 이직 필요형/직무 재설계형) + 다음 행동 추천
- 고위험 응답 시 위기 상담 자원 즉시 안내
- 결과 공유 링크
스택: React 19 · TypeScript · Vite · Plain CSS (design tokens) · Playwright (E2E) · S3 + CloudFront
배포: https://번아웃.com/

### ComfyUI API Server

1인 개발 · GitHub 공개(GPL-3.0) · 레플리 이미지 생성 서비스 실서비스 핵심 엔진

문제: ComfyUI(빠르지만 API 없음) ↔ SD WebUI(API 좋지만 느림) 트레이드오프 동시 해결
해결: ComfyUI 실행 엔진 위에 SD WebUI 호환 REST API를 얹은 헤드리스 순수 서버 직접 구현
핵심 엔지니어링:
- 드롭인 호환: /sdapi/v1/txt2img, /sdapi/v1/img2img 등 SD WebUI 스펙 구현
- 디스크 I/O 제거: 이미지를 base64 메모리로만 처리
- 모델 캐싱: LRU 캐싱으로 재로딩 비용 절감
- 기능 폭: LoRA 체이닝, 17종+ 샘플러, CLIP skip, 인페인팅
- Docker 원커맨드 빌드·실행
스택: Python · FastAPI · ComfyUI · Stable Diffusion · Docker (CUDA) · NVIDIA GPU
링크: https://github.com/jongmin-oh/comfyUI-api-server

---

## 외부 사업·과제

### 정밀의료 AI 문진 솔루션

2023년 데이터 활용 의료·건강 생태계 조성사업 (강원정보문화산업진흥원)
소화기 질환 대상 멀티턴 문진 대화 AI

한 일:
- 지식 DB 구축: 질병관리청 + 대한소화기학회 → 47개 소화기 질환 데이터셋
- 데이터 증강 파이프라인: 신뢰 정보 → GPT 가상 환자 → AI 전문의 문진 대화 생성. 1,947건 추가, 최종 5,018건 (j5ng/ko_medical_chat_v2 공개)
- 비용 최적화: OpenAI Batch API로 데이터 생성 비용 약 50% 절감 (총 $11)
- 모델 파인튜닝: polyglot-ko-12.8b QLoRA 파인튜닝, 의사 발화 마스킹·예측 학습
스택: Python · polyglot-ko-12.8b · QLoRA · HuggingFace · OpenAI API (GPT-4o / Batch API)
회고 [실패 경험]: 더 좋은 베이스 모델에 증강 데이터 추가 학습해도 기대만큼 성능이 오르지 않았고, 의료 도메인 지식을 효과적으로 주입하는 domain adaptation 방법을 끝까지 찾지 못함.

---

## 학력

| 학교 | 기간 | 전공 | 학위 |
|------|------|------|------|
| 인하공업전문대학 | 2022.03 – 2023.02 | 컴퓨터정보과 | 전공 심화 (학사학위) GPA 4.36 / 4.5 |
| 청강문화산업대학교 | 2014.03 – 2021.02 | 게임공학부 | 3년제 전문학사 |

---

## 특허

인공지능 기반 챗봇 학습 데이터 생성 방법
특허번호: 제 10-2757044 호 (등록)
출원번호: 제 10-2022-0160871 호
출원일: 2022.11.25
등록일: 2025.01.15
특허권자: 오종민

---

## 참고 링크

| 분류 | 링크 |
|------|------|
| Velog | https://velog.io/@acdongpgm |
| Github | https://github.com/jongmin-oh |
| 이미지 생성 정리글 | https://buly.kr/FhPsQw |
| 맛보기 채팅 | https://chat-preview.reppley.com |
| 오복이 웹 | https://comfort.j5ng.com/ |
| et5-typos-corrector | https://huggingface.co/j5ng/et5-typos-corrector |
| kcbert-formal-classifier | https://huggingface.co/j5ng/kcbert-formal-classifier |
| 널스체크 | https://번아웃.com/ |
| ComfyUI API Server | https://github.com/jongmin-oh/comfyUI-api-server |
