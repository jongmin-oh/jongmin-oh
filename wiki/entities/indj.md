---
title: INDJ
type: entity
tags: [company, startup, past, AI, music, recommendation, NLP]
created: 2026-06-21
updated: 2026-06-21
sources: [career-wiki-seed.md]
---

# INDJ (인디제이)

**타입**: 스타트업  
**웹사이트**: https://www.indj.ai/  
**역할**: AI 엔지니어  
**기간**: 2021.04 – 2021.07 (4개월)  
**상태**: 과거

## 제품

AI 기반 음악 서비스. 현재 감정에 맞는 채널 추천, 유사 감정 기반 음원 그룹화.

## 종민이 한 일 (1인 단독)

**한국어·영어 가사 감정 분류 모델 개발** → 추천시스템의 핵심 Feature로 통합.

1. **데이터** — 한국어 가사 15,000문장 **직접 라벨링** (한국어 9개 감정). 영어는 Kaggle 공개 데이터셋 활용 (6개 감정).
2. **한국어 모델** — BERT 긍·부정 분류 + **Lexicon(감정 단어 사전)** 결합 하이브리드 모델
3. **영어 모델** — BERT 다중 감정 분류 (6-class) 설계·학습
4. **통합** — 분석 결과를 추천시스템 감정 Feature로 통합 → 맞춤형 채널 추천·감정 기반 플레이리스트 구성

**스택**: `Python` · `TensorFlow` · `MySQL` · `Pandas`

## 연구 연결

[[papers/bert-emotion-lyrics\|2022 한국컴퓨터정보학회 논문]] — "BERT + 감정 어휘 사전 결합 음원 가사 감정 분석"은 이 시기 INDJ 작업의 직접적 학술 결과물이다. 한국어 9개 감정 분류 + Lexicon 결합이라는 하이브리드 접근이 논문 주제와 일치.

## 패턴

INDJ → atommerce → Reppley 모두 "AI가 인간 감정을 이해·반응하는" 제품이다. INDJ가 이 패턴의 시작점.
