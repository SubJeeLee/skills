# 출처와 최신성

검토 기준일: 2026-10-30. 이 저장소는 독립적인 개인 준비 자료이며 SK하이닉스·COFA·OpenAI 등의 공식 문서나 승인·후원 자료가 아니다.

2026-11-03 보완: README 기반 질문 선별과 HTML 아키텍처·데이터·Docker 투어 Skill을 추가했다. 기존 시험 일정·운영 규칙을 재응시의 최신 공지로 갱신했다는 뜻은 아니다. 복기한 실제 시험 문제·데이터·대화는 포함하지 않는다.

같은 날 여러 Bash에서 제공 Codex를 직접 실행하는 운영안과 문제 정의 검토 Skill을 추가했다. 참가자의 환경 설명을 반영한 준비 지침이며 실제 동시 Codex 세션·공유 파일·자원 한도의 지원을 실측하거나 공식 승인한 자료는 아니다. 수동 분리 CLI 세션, 네이티브 서브에이전트, 한 세션의 역할 전환을 구분한다.

## 참가자가 제공한 안내

- 「시험 필수확인사항 브리프」 1쪽: 일정, 단계별 시간, 제한과 공개 도구 활용.
- 「Proctor 설치 및 촬영가이드」 1쪽: 장비, 신분증 가림, 설치·연결·촬영.
- 「사전 체험 및 응시환경 상세 가이드」 1~5쪽: 환경, 작업·저장·제출, 후속 서술형, 도구·감독·FAQ.

개인 배포 PDF·초대 링크·QR·실제 시험 자료는 공개하지 않는다. [요약](../skills/cofa-delivery/references/exam-boundaries.md)은 참가자가 제공한 문서에 대한 개인 검토이며 최신 공식 안내가 우선이다. 규칙의 빈틈을 허용으로 해석하지 않는다.

## 공식 제품·프로젝트 자료

| 출처 | 확인한 내용 |
| --- | --- |
| [AGENTS.md](https://learn.chatgpt.com/docs/agent-configuration/agents-md) | 프로젝트 지침 탐색과 세션 시작 시 읽기 |
| [Codex Skills](https://learn.chatgpt.com/docs/build-skills) | Skill 구성과 프로젝트 탐색 경로 |
| [Codex Subagents](https://learn.chatgpt.com/docs/agent-configuration/subagents) | 독립 작업 분리와 병렬 쓰기·토큰 비용 |
| [OpenAI Docs MCP](https://developers.openai.com/learn/docs-mcp) | 문서 검색·읽기 전용 서버 |
| [Spec Kit](https://github.com/github/spec-kit) | 명세에서 구현으로 연결하는 워크플로 |
| [BMAD 계획 경로](https://docs.bmad-method.org/plan/choose-a-planning-path/) | 의도의 명확성에 따른 계획 선택 |
| [Superpowers](https://github.com/obra/superpowers) | 설계·검증·디버깅 Skill |
| [ECC](https://github.com/affaan-m/ECC) | Codex 지원 경로 및 개별 Skill |
| [OMX](https://github.com/Yeachan-Heo/oh-my-codex) | Codex 하네스·의존성·역할 분담·실행 옵션 |
| [Playwright MCP](https://github.com/microsoft/playwright-mcp) | MCP와 CLI+Skill 접근의 차이 |
| [Context7](https://github.com/upstash/context7) | 문서 질의와 인증 방식 |
| [Dockerfile reference](https://docs.docker.com/reference/dockerfile/) | Dockerfile 지시문, 빌드·실행 구분과 EXPOSE 의미. 2026-11-03 확인 |
| [Docker 빌드 컨텍스트](https://docs.docker.com/build/concepts/context/) | COPY가 접근하는 컨텍스트와 .dockerignore. 2026-11-03 확인 |
| [Docker 다단계 빌드](https://docs.docker.com/build/building/multi-stage/) | 단계 간 빌드 산출물 복사와 실행 이미지 경계. 2026-11-03 확인 |

일반 Codex의 기능 지원은 COFA 설치본의 지원을 보장하지 않는다. 이 저장소는 외부 지침 원문을 포함하지 않는다. 원문 코드를 재사용하면 해당 라이선스·고지를 별도로 확인한다.

## 개인 후기

[크래프톤 FDE 코파톤 후기](https://brunch.co.kr/@luma/5): 이전 대회의 참가자 경험이다. 과정·결과 이해·인계의 중요성을 참고했으나, 당시 시간·모델·배점·반입 방식은 이번 시험 규칙으로 취급하지 않는다. 본문·이미지를 재배포하지 않는다.

## 권장안과 미확인 정보

- 180분 작업 배분, 역할 분담, 템플릿, 연습 질문은 이 저장소의 권장안이다.
- 가상 설비 신고 과제는 연습 예시이며 실제 출제 정보가 아니다.
- 개인 공개 템플릿 반입, 서술형 docs 열람, Playwright의 허용 범위와 COFA 기능·사용 한도는 미확인이다.
- 특정 도구를 사용한 사실만으로 평가 점수가 높아진다는 근거는 없다.

## 공개 범위

이 저장소의 공개에는 일반 작업 지침·연습 예시·출처 링크만 포함한다. 실제 시험 문제·데이터·제출물·대화 기록·개인 신상·연락처·개인 초대 링크는 포함하지 않는다.
