---
title: 정밀의료 AI 문진 솔루션
type: project
tags: [external, medical, LLM, QLoRA, fine-tuning, data-augmentation, failure]
created: 2026-06-21
updated: 2026-06-21
sources: [career-wiki-seed.md]
---

# 정밀의료 AI 문진 솔루션

**성격**: 외부 사업 과제  
**발주**: 강원정보문화산업진흥원 — 2023년 데이터 활용 의료·건강 생태계 조성사업  
**주제**: 소화기 질환 진단·예측 정밀의료 AI 문진 솔루션 개발

## 개요

소화기 질환 대상으로 환자와 멀티턴 문진 대화를 진행하는 AI. 의료 도메인은 신뢰성 최우선 → 신뢰된 국내 자료 정제 → 학습 데이터 구축 → sLLM 파인튜닝까지 전 과정 직접 수행.

## 한 일

### 지식 DB 구축

질병관리청 국가건강정보포털 + 대한소화기학회 진료지침 정제.  
구조화 자료를 줄글로 변환 → 최종 **47개 소화기 질환** 데이터셋.

### 데이터 문제 진단

기존 공개 데이터(`ko_medical_chat`)의 한계 분석:
- 넓은 진료과목 (소화기 특화 없음)
- 어색한 한국어
- 신뢰성·설득력 부족

→ 소화기내과 전용 데이터 필요성 도출.

### 데이터 증강 파이프라인

```
신뢰 정보 (47개 질환)
  → GPT로 가상 환자 페르소나 생성
  → AI 전문의 ↔ 가상 환자 문진 대화 생성
  → 47 × 50건 = 1,947건 추가
  → 최종 5,018건 (j5ng/ko_medical_chat_v2 공개)
```

**비용 최적화**: OpenAI Batch API로 데이터 생성 비용 약 **50% 절감** (총 $11).

### 모델 파인튜닝

- 베이스 모델: EleutherAI/polyglot-ko-12.8b
- 방법: QLoRA 파인튜닝
- 학습 전략: 의사 발화 마스킹·예측 학습
- 결과 모델: `polyglot-ko-medical-chat-12.8B`

## 스택

`Python` · `polyglot-ko-12.8b` · `QLoRA` · `HuggingFace` · `OpenAI API (GPT-4o / Batch API)`

## 회고 — 실패 경험

> EEVE 등 더 좋은 베이스 모델에 증강 데이터를 추가 학습해도 기대만큼 성능이 오르지 않았고, 의료 도메인 지식을 효과적으로 주입하는 **domain adaptation 방법**을 끝까지 찾지 못한 점이 아쉬움.

**배움**: 데이터 품질·양 개선과 모델 크기 업그레이드만으로는 도메인 특화 성능을 담보하기 어렵다. 의료처럼 전문 지식이 깊은 도메인은 domain adaptation 전략(pre-training, instruction tuning 설계, 평가 파이프라인)이 별도로 필요하다.

## 공개 데이터

`j5ng/ko_medical_chat_v2` — Hugging Face 공개
