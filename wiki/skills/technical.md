---
title: 기술 스킬
type: skill
tags: [skills, python, AWS, fastapi, serverless, NLP, stable-diffusion, langgraph, agent, neo4j, graphrag]
created: 2026-06-21
updated: 2026-09-07
sources: [career-wiki-seed.md]
---

# 기술 스킬

## 핵심 스택

`Python` · `FastAPI` · `AWS` · `AWS Lambda / SAM` · `React` · `RDBMS` · `Redis`  
`Stable Diffusion` · `Prompt Engineering` · `SBERT / 임베딩 검색` · `Faiss / ONNX 최적화` · `RAG / ChromaDB`  
`LangGraph / LangChain` · `Neo4j / GraphRAG` · `Langfuse` · `OpenRouter`

---

## 백엔드

| 기술 | 숙련도 | 증거 |
|------|--------|------|
| Python | 메인 언어 | 전 경력 |
| FastAPI | 주력 프레임워크 | 레플리 메인 API, 오복이, 이미지 생성 서버 등 |
| Flask | 초기 | atommerce 로니 API |
| AWS ECS | | 레플리 메인 API |
| AWS Lambda / SAM | **매우 익숙** | 선톡 시스템, 각종 자동화 |
| AWS SQS | | 선톡 시스템 |
| AWS ElastiCache (Redis) | | 레플리 장기기억, 메인 API 캐싱 |
| RDBMS | | 레플리 전반 |
| AWS S3 + CloudFront | | 맛보기 챗, 널스체크, 오복이 웹 |

## AI / ML

| 기술 | 증거 |
|------|------|
| BERT / Transformers fine-tuning | 가사 감정 분류(INDJ), 로니(atommerce), et5, kcbert |
| SBERT / 임베딩 검색 | 오복이 v2.0 이후 |
| Faiss (PQ 양자화) | 오복이 메모리 최적화 |
| ONNX 양자화 (uint8) | 오복이 속도 7배 |
| 하이브리드 검색 (BM25 + Dense, RRF) | 오복이 v4.0 |
| Stable Diffusion / ComfyUI | 레플리 이미지 생성 서비스 |
| Prompt Engineering | 레플리 선톡 (5만 건 직접 검토), 메인 챗봇 |
| 평가 지표 정의 | [[projects/company/선톡전송시스템]] — 정답 없는 생성 결과를 기능의 본질 목표(리텐션)로 환원해 '푸시 클릭률' 단일 지표로 정의, 프롬프트 지침 개정 |
| LLM-as-judge | 레플리 장기기억 평가 파이프라인, AI 소설 생성 서비스 루브릭 채점, 선톡 자동 채점(5만 건 수작업 검수 대체) |
| 장문 창작 프롬프트 설계 | [[projects/company/AI소설생성API]] — 웹소설 회차 생성 |
| 프롬프트 A/B 테스트 | [[projects/company/캐릭터챗봇API]] — 실트래픽 분할 서빙, 대화 지속 턴 수 지표로 45% 향상 |
| 모델 비교 실험 | AI 소설 생성 서비스 — 동일조건 A/B, 결과 예측 가능성으로 결론 |
| QLoRA fine-tuning | 정밀의료 AI (polyglot-ko-12.8b) |
| RAG (Retrieval-Augmented Generation) | 정밀의료 AI 문진 — ChromaDB + klue/roberta-large, 할루시네이션 방지 목적 |
| ChromaDB | 정밀의료 AI 벡터 DB |

## 에이전트 / LLM 오케스트레이션

| 기술 | 증거 |
|------|------|
| LangGraph | [[projects/personal/Nightly]] — 조건부 엣지 기반 대화 그래프 |
| ReAct 루프 (직접 구현) | Nightly — 검색 전용 서브에이전트 |
| Tool calling | Nightly — 지식 그래프 조회, 외부 API |
| GraphRAG (Neo4j) | Nightly — 사실 단위 검색, 관계 엣지 |
| LLM 관측·세션 트레이싱 (Langfuse) | Nightly |
| 프로바이더 라우팅·폴백 (OpenRouter) | Nightly |
| 프롬프트 캐시 친화 설계 | Nightly, [[projects/company/캐릭터챗봇API]](건당 30% 절감) |
| 상태 추출 파이프라인 | Nightly — 대화에서 상대 정보 추출, 전용 모델 분리 |

## 프론트엔드

| 기술 | 숙련도 | 증거 |
|------|--------|------|
| React | AI 코딩 도구로 구현 | 맛보기 채팅 웹, 관리자 페이지들 |
| React 19 + TypeScript | | 널스체크 |
| JavaScript / HTML / CSS | | 운영 도구들 |
| Streamlit | | 오복이 웹 |

## 인프라 / DevOps

| 기술 | 증거 |
|------|------|
| Docker (CUDA) | ComfyUI API Server |
| AWS SAM (arm64 Lambda) | Nightly, 선톡 시스템 |
| Mangum (ASGI → Lambda) | Nightly |
| Neo4j | Nightly 지식 그래프 |
| AWS Route 53 | 맛보기 채팅 웹 |
| Appium | 앱 테스트 자동화 |
| Elasticsearch | 오복이 v1.0 |

## 데이터

| 기술 | 증거 |
|------|------|
| 데이터 수집·정제·라벨링 | 가사 15,000문장(INDJ), 60만 건(atommerce), 의료 지식 DB |
| OpenAI Batch API | 의료 데이터 생성 (비용 50% 절감) |
| TensorFlow | INDJ |
| Pandas / MySQL | INDJ |
