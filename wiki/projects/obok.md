---
title: 위로 챗봇 오복이
type: project
tags: [personal, chatbot, retrieval, SBERT, ONNX, faiss, kakao, graduation]
created: 2026-06-21
updated: 2026-06-21
sources: [career-wiki-seed.md]
---

# 위로 챗봇 '오복이'

**성격**: 대학교 4학년 졸업작품 · 1인 개발  
**출시**: 2022.11  
**운영**: 출시 후 사비로 지속 운영·유지보수 중  
**링크**: https://comfort.j5ng.com/ · http://pf.kakao.com/_BNZRb · https://github.com/jongmin-oh/comfort_chatbot

## 개요

고민·질문에 위로로 답하는 감성 대화 챗봇. 심리상담사 컨셉, 물범 캐릭터. AI 비서가 아니라 정서적 대화 파트너.

**구현**: 질문과 가장 유사한 기존 질문을 검색해 매칭 답변을 주는 **Retrieval 기반 싱글턴 챗봇**.

캐릭터 이미지는 저작권 회피를 위해 DALL·E로 직접 생성.

## 운영 인프라

| 레이어 | 선택 | 이유 |
|--------|------|------|
| 프론트 | 카카오톡 채널 + 오픈빌더 | 접근성 높은 채널, 채널 챗봇 무료화로 과금 부담 없음 |
| 웹사이트 | Streamlit (j5ng.com, CloudFront HTTPS) | 빠른 구현 |
| 서버 | GCP 무료 크레딧 → AWS 예약 인스턴스 t3a-medium (사비) | 지속 운영을 위해 1년치 사비 구매 |

## 개발 로그 — 알고리즘 진화

| 버전/시점 | 변경 | 의의 |
|-----------|------|------|
| v1.0 (2022.11) | Elasticsearch + nori 형태소 분석기, 답변 후보 10만 개 | 키워드 기반 Sparse 검색 |
| v2.0 (2023.02) | ES → SBERT 임베딩 검색 (klue/roberta-base KorSTS/NLI → KR-SBERT) | Dense 검색으로 전환, 의미 기반 매칭 |
| 2023.04 | **Faiss + PQ 양자화** → 임베딩 메모리 1/4, 검색 속도 향상 | 메모리 최적화 |
| 2023.04 | **ONNX uint8 양자화** → 임베딩 속도 약 7배, 모델 크기 1/4, 정확도 손실 거의 없음(dot ±0.02 이하) | 추론 속도 최적화 |
| 2023.06–09 | 답변 데이터 재구축: ChatGPT·HyperClova 재생성 + 직접 검수·중복 제거 → 최종 **35,363건** | 데이터 품질 혁신 |
| 2023.10 | **하이브리드 검색** (BM25 + 임베딩) RRF 결합 | Sparse+Dense 합산으로 랭킹 정확도 개선 |

## 스택

`Python` · `FastAPI` · `Gunicorn` · `SBERT` · `ONNX` · `Faiss` · `ChromaDB` · `Elasticsearch` · `Streamlit` · `AWS EC2/CloudFront` · `카카오톡 오픈빌더`

## 운영 경험 (트러블슈팅)

- 생성 AI 연동 실험 → 과금·악성 유저 문제로 중지
- 동일 질문 반복 악성 유저 대응 → 차단·요청 제한 검토

## 의의

- 졸업작품으로 시작했으나 출시 후에도 **사비로 지속 운영·고도화**한 1인 풀스택 프로젝트
- 검색 챗봇의 알고리즘·인프라·데이터 품질을 처음부터 끝까지 직접 개선: ES → SBERT → Faiss/ONNX → 하이브리드
- [[entities/atommerce\|atommerce]] Retrieval 챗봇 경험의 심화·발전판

## 연관

→ [[papers/bert-emotion-lyrics\|가사 감정 분석 논문]] (같은 시기)
→ [[skills/technical\|임베딩 검색 / SBERT / ONNX 최적화]] 스킬 기반
