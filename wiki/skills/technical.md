---
title: 기술 스킬
type: skill
tags: [skills, python, AWS, fastapi, serverless, NLP, stable-diffusion, langgraph, agent, neo4j, graphrag]
created: 2026-06-21
updated: 2026-09-02
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
| LLM-as-judge | 레플리 장기기억 평가 파이프라인 |
| QLoRA fine-tuning | 정밀의료 AI (polyglot-ko-12.8b) |
| RAG (Retrieval-Augmented Generation) | 정밀의료 AI 문진 — ChromaDB + klue/roberta-large, 할루시네이션 방지 목적 |
| ChromaDB | 정밀의료 AI 벡터 DB |

## 에이전트 / LLM 오케스트레이션

| 기술 | 증거 |
|------|------|
| LangGraph (StateGraph, ToolNode, tools_condition, add_messages) | [[projects/personal/Nightly]] — 5노드 그래프, 조건부 엣지 |
| ReAct 루프 (직접 구현) | Nightly — 검색 전용 서브에이전트, 스텝 상한 4 |
| Tool calling | Nightly — 지식 그래프 조회 2종 + 날씨 API |
| GraphRAG (Neo4j / Cypher) | Nightly — Topic←Fact 2계층, 언급·의미관계 엣지 |
| Langfuse (LLM 관측·세션 트레이싱) | Nightly — 방 단위 세션, 람다 flush 강제 |
| OpenRouter (프로바이더 라우팅·폴백) | Nightly — Novita/Friendli 순서 지정 |
| 프롬프트 캐시 친화 설계 | Nightly(고정부 prefix 배치), [[projects/company/캐릭터챗봇API]](건당 30% 절감) |
| 상태 추출 파이프라인 | Nightly — 50필드 스키마, 4턴 주기, 추출 전용 모델 분리 |

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
