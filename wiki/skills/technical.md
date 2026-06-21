---
title: 기술 스킬
type: skill
tags: [skills, python, AWS, fastapi, serverless, NLP, stable-diffusion]
created: 2026-06-21
updated: 2026-06-21
sources: [career-wiki-seed.md]
---

# 기술 스킬

## 핵심 스택

`Python` · `FastAPI` · `AWS` · `AWS Lambda / SAM` · `React` · `RDBMS` · `Redis`  
`Stable Diffusion` · `Prompt Engineering` · `SBERT / 임베딩 검색` · `Faiss / ONNX 최적화` · `RAG / ChromaDB`

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
