---
title: 실업급여 RAG QA — 근거를 보여주고 모르면 답하지 않는 문서 QA
type: project
tags: [personal, assignment, rag, hybrid-search, evaluation, llm-as-judge, gold-set, serverless, lambda, fastapi, human-feedback]
created: 2026-09-27
updated: 2026-09-27
sources: [document-rag-qa-system/ 저장소 README·decision/·evaluation/reports 직접 리딩 2026-09-27, 본인 설명 2026-09-27]
---

# 실업급여 RAG QA — 근거를 보여주고 모르면 답하지 않는 문서 QA

**성격**: 1인 개발 · 취업 과제전형 · 배포 완료 (AWS Lambda Function URL)  
**기간**: 2026.09.24 – 09.27 (커밋 111개)  
**저장소**: `document-rag-qa-system/`

> 과제전형이지만 **RAG의 문제 정의 → 구축 → 평가 → 배포 → 피드백 루프**를 한 사이클 전부 혼자 돈 경험. 회사에서 RAG를 *보류*했던 경험([[projects/company/장기기억시스템]])과 짝을 이룬다 — **RAG가 맞는 문제에서만 RAG를 쓴다.**

## 문제 정의 — 왜 실업급여인가

본인이 **직접 실업급여를 받으며 겪은 문제**에서 출발.

- 주변 수급자들도 "나도 받을 수 있나?", "받는 동안 뭘 해야 안 끊기나?"를 몰라 헤맴. 정보는 법령·기관 안내·블로그에 흩어져 있고 금액·기준이 매년 바뀌어 오래된 정보가 흔함.
- 고용센터 방문 시 **고령자**가 특히 많았음 — 법령이 어렵고 스스로 찾을 방법을 몰라 전화하거나 직접 찾아옴.
- 잘못 알면 수급을 놓치거나 **부정수급**이 됨 → **근거(citation)를 보여주고, 모르면 답하지 않는 RAG**가 실제 가치를 갖는 도메인. 출처·쪽 번호를 고용센터(1350) 문의 때 그대로 보여줄 수도 있음.
- LLM이 사전 지식으로 그럴듯한 오답(예전 상한액, 폐지된 절차)을 만들기 쉬워 hallucination 관찰에도 적합.

**Corpus**: 법제처 생활법령 「실업급여」(59쪽, 2026-08-31 기준) + 고용노동부 취업드림수첩(35장 ≈ 책자 68쪽, 2026-02). 전자는 "받을 수 있나·얼마나", 후자는 "받는 동안 무엇을 해야 하나". 기준일 차이를 알려진 이슈로 명시하고 답변에 출처별 기준일 표시.

## 무엇을 만들었나

```
PDF ─(1회성, 사람 검수)→ Markdown ─→ 문서 구조 기반 청크 120개 ─→ pplx-embed-v1-4b 벡터
질문 → ① LLM 질의 재작성 → ② 하이브리드 검색(임베딩 + 글자 2-gram BM25, RRF, top-5)
     → ③ 구조화 출력 {answerable, answer} → ④ 서버가 [n] 파싱해 citation 생성
피드백 → DynamoDB(90일 TTL) → 사람 검토 → Gold Set 추가 → 회귀 평가 → 배포
```

- **API**: FastAPI `POST /ask`, `POST /feedback` · 웹 UI 포함
- **배포**: AWS SAM → Lambda(Python 3.13) + Function URL + DynamoDB. API 키는 SSM Parameter Store
- **LLM**: Gemini 3.7 Flash(재작성·답변) · Judge: OpenRouter GPT(다른 개발사 → 자기 선호 편향 감소)

### 의도적으로 안 쓴 것

| 안 쓴 것 | 이유 |
|---|---|
| 벡터 DB | 청크 120개 → 순수 Python 전수 비교 ~10ms. 수만 청크가 되면 교체 |
| LangChain·LlamaIndex | 파이프라인이 3단계라 직접 구현이 더 짧고, 각 단계를 평가 trace로 그대로 노출 가능 |
| 형태소 분석기 | 글자 2-gram BM25가 kiwipiepy보다 Recall@5 높음(0.691 vs 0.605) + 의존성 0 |
| Streaming | `answerable` 판정·인용 번호 파싱을 완성된 응답에서 한 번에 처리. 대기 대부분이 재작성·thinking이라 체감 차이 작다고 판단 |

→ [[skills/working-style]]의 오버엔지니어링 경계·서버리스 우선이 그대로 적용된 사례.

## 평가 — 이 프로젝트의 핵심

- **Gold Set**: 네이버 지식iN **실제 질문 41문항** (full 18 / partial 18 / none 5). 근거를 청크 ID가 아닌 **원문 문자 구간**으로 표시 → 청킹 방식을 바꿔도 같은 Gold Set으로 비교.
- **지표 3층**: 검색(Hit/Recall/Coverage/Precision@k) · 결정론(거부 정확도, citation integrity, Gold 근거 일치) · LLM Judge 1–5점(Correctness·Completeness·Faithfulness·Partial handling·Clarity).
- **재현성**: 리포트에 커밋·dirty 여부·모델 버전·seed·Judge 프롬프트 해시·인덱스 해시 기록.

### 한 번에 한 변수 실험

| 변경 | Before → After | 결정 |
|---|---|---|
| 고정 길이 → 문서 구조 청킹 | Recall@5 0.595 → 0.643 | 채택 |
| Dense → 하이브리드(BM25+RRF) | Recall@5 0.643 → 0.691, multi-hop 0.519 → 0.612 | 채택 (Hit@5 1문항 하락 명시) |
| LLM 질의 재작성 | Recall@5 0.691 → 0.788 | 채택 (지연 증가 대가) |
| Gemini Embedding 2 → pplx | Recall@5 0.769 → 0.811, 가격 약 1/7 | "품질 동등 이상 + 가격"으로 채택 (Recall@1 하락 명시) |
| 가독성 프롬프트 H5 → H6 → H6b | H5는 Clarity 하락 → **롤백**. H6: 답변 380 → 224자, 원문 복사율 0.205 → 0.029, Clarity 3.32 → 3.63. 단 Completeness 하락 → H6b로 보완 | 채택 |
| Gemma 4 31B → Gemini 3.8 → 3.7 Flash | 저가 Gemma는 Faithfulness 낮아 **되돌림**. 3.7이 3.8보다 Correctness 4.00 → 4.31 | "같은 가격에서 3.8 이상"으로 채택 |

**최종 운영 수치**: Recall@5 0.807 · Hit@5 1.000 · Answerability accuracy 0.976 · Citation integrity 1.000 · Correctness 4.17/5 · Clarity 4.47/5

**답변 재생성 플로우**: 저장된 top-5를 고정하고 답변만 다시 생성해, 검색 변동을 섞지 않고 프롬프트·LLM 효과만 분리 비교. 품질을 올리는 기능이 아니라 **실험의 인과를 명확히 하는 평가 기반**.

## 어떻게 판단했나 — 드러난 패턴

- **숫자를 과장하지 않음**: 41문항·거부 5문항의 작은 표본이라 "명확한 우위" 대신 "경향", "동등 이상"으로만 해석. 모든 비교에서 평균과 함께 **개선·악화 문항 수**를 같이 봄. 선톡 클릭률 2배를 대조군 부재로 성과 주장하지 않았던 것과 같은 태도(→ [[reflections/그로스해킹과-제품관점의-전환]]).
- **실패를 문서화**: 알려진 이슈(KIN-13 인접 주제 오답, KIN-09 검색 실패), Judge를 사람 채점과 대조하지 않았다는 한계, Gemini 직접 호출에 ZDR 미적용이라는 보안 조건까지 README에 명시.
- **운영을 전제로 설계**: 휴먼 피드백 → 사람 분류(문서/검색/생성/표현 문제) → Gold Set 추가 → 회귀 평가 → 배포 루프. 피드백 저장 실패가 답변을 실패시키지 않게 분리, 개인정보는 TTL + 사람 검토 후에만 Gold Set 반영.
- **기준부터 정의**: 무엇이 "좋은 답변"인지를 거부·인용·정확성·가독성 지표로 먼저 정의하고 그 위에서 실험 → [[projects/company/선톡전송시스템]]의 "기준부터 정의한다" 패턴의 RAG판.

## 레플리 RAG 폐기 경험과의 대비

| | [[projects/company/장기기억시스템]] | 이 프로젝트 |
|---|---|---|
| 문제 | 대화 기억 | 법령·안내문 질의응답 |
| RAG 판단 | **보류** → Episodic+State 기억(LLM+KV) 먼저 | **채택** |
| 이유 | 핵심은 정보 검색이 아니라 "관계와 경험의 지속성" | 출처 제시·모르면 거부가 제품 가치의 핵심 |

→ 같은 기술을 한 번은 미루고 한 번은 쓴 것. **기술이 아니라 문제가 결정한다**는 [[reflections/코더에서-문제해결사로]]의 증거.

## 향후 과제 (README 기준)

사람 채점 표본으로 Judge 일치도 측정 · 인접 주제 거부 강화 · doc2query 비교 · 멀티턴 질의 재작성 · CI 게이트(결정론 지표는 임계값, Judge는 추세).

## 관련

- [[projects/personal/오복이]] — 하이브리드 검색(BM25+임베딩 RRF)을 처음 쓴 곳
- [[projects/company/정밀의료AI문진]] — 이전 RAG 경험(ChromaDB, 할루시네이션 방지)
- [[skills/technical]] · [[skills/working-style]]
