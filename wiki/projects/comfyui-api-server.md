---
title: ComfyUI API Server
type: project
tags: [personal, open-source, stable-diffusion, ComfyUI, FastAPI, Docker, GPU]
created: 2026-06-21
updated: 2026-06-21
sources: [career-wiki-seed.md]
---

# ComfyUI API Server

**성격**: 1인 개발 · GitHub 공개 (GPL-3.0)  
**실서비스 용도**: [[projects/image-generation\|레플리 이미지 생성 서비스]]의 핵심 서빙 엔진  
**링크**: https://github.com/jongmin-oh/comfyUI-api-server

## 문제 정의

| 도구 | 장점 | 한계 |
|------|------|------|
| ComfyUI | 빠른 생성 속도, 최신 샘플러·최적화 | REST API 없어 서비스에 붙이기 어려움 |
| SD WebUI | `/sdapi/v1` REST API 훌륭 | 무겁고 느리며 UI 중심이라 서버 운영 부적합 |

→ "ComfyUI의 속도"와 "SD WebUI의 익숙한 API" 동시 필요 → **직접 만들기로 결정**.

## 해결책

ComfyUI 실행 엔진 위에 SD WebUI 호환 REST API를 얹은 **헤드리스 순수 서버** 직접 구현.  
UI 코드 전부 제거. 기존 SD WebUI 도구·스크립트가 그대로 동작하는 드롭인(drop-in) 서버.

## 핵심 엔지니어링 결정

| 결정 | 내용 |
|------|------|
| 드롭인 호환 | `/sdapi/v1/txt2img`, `/sdapi/v1/img2img` 등 SD WebUI 스펙 완전 구현 |
| 디스크 I/O 제거 | 추론 중 이미지를 디스크에 쓰지 않고 base64 메모리로만 처리 → 지연·부하 감소 |
| 모델 LRU 캐싱 | 자주 쓰는 모델을 VRAM에 유지 → 재로딩 비용 절감 |
| 기능 폭 | LoRA 체이닝, 17종+ 샘플러 매핑, CLIP skip, 인페인팅 지원 |
| 배포 표준화 | NVIDIA GPU 기반 Docker 원커맨드 빌드·실행 |

## 스택

`Python` · `FastAPI` · `ComfyUI` · `Stable Diffusion` · `Docker (CUDA)` · `NVIDIA GPU`

## 결과 (실서비스 지표)

레플리 이미지 생성 서비스 기반:
- 일 3,000건 처리
- 생성 속도 5초 이내
- 인프라 비용 월 24만원

## 의의

- 기존 도구의 트레이드오프를 정확히 진단 → 직접 새 도구 제작 → 자사 실서비스 적용의 전 과정
- [[skills/working-style\|"트레이드오프 직접 진단"]] 원칙의 가장 선명한 사례
- 사이드 프로젝트가 아니라 **실서비스 핵심 엔진**으로 운영 중
