---
title: atommerce
type: entity
tags: [company, startup, past, AI, chatbot, mental-health]
created: 2026-06-21
updated: 2026-06-21
sources: [career-wiki-seed.md]
---

# atommerce (아토머스)

**타입**: 스타트업  
**웹사이트**: http://www.atommerce.com  
**역할**: AI 엔지니어  
**기간**: 2021.09 – 2021.12 (4개월)  
**상태**: 과거

## 제품 — 마인드카페 내 AI 챗봇 '로니'

마인드카페는 정신건강 커뮤니티 앱. 사용자가 고민을 게시하면 **무응답 상태로 방치되는 문제**가 있었다.  
→ AI 캐릭터 로니가 공감·위로 댓글을 자동 작성해 해결.

뉴스 기사: https://www.aitimes.kr/news/articleView.html?idxno=23722

## 종민이 한 일 (1인 개발)

1. **데이터셋 구축** — 데이터 바우처 사업 Q&A 3만 건 + 실제 마인드카페 데이터 80만 건 전처리·정제 → 최종 **60만 건** 학습 데이터셋
2. **모델 설계·학습** — SentenceTransformer(klue/roberta) 기반 **Retrieval 챗봇**. 유사 고민을 검색해 공감형 응답 생성
3. **서빙 API 개발** — Flask 기반 모델 서빙 API. 실시간 응답·확장성 고려 구조 설계

**스택**: `Flask` · `SentenceTransformer (klue/roberta)`

## 커리어 연결고리

- Retrieval 기반 챗봇 → [[projects/obok\|오복이]](졸업작품)에서 같은 패턴 발전시킴
- 감정 위로 도메인 경험 → [[entities/reppley\|레플리]] 캐릭터 챗봇의 원형
- 특허 출원 (2022.11): "AI 기반 챗봇 학습 데이터 생성 방법" — atommerce 및 오복이 Retrieval 챗봇 학습 데이터 구축 방법론과 연결 가능성 있음
