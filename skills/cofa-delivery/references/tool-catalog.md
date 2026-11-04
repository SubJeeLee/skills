# 도구 선택 목록

2026-10-30에 공식 저장소·문서를 확인한 후보이며, 2026-11-03 MCP JSON 연결 안내와 Serena를 보완했다. 스타 수나 모델 지원 표시는 설치 성공·성능·시험 허용을 보장하지 않는다. 설치하지 않은 도구를 이미 사용할 수 있다고 표현하지 않는다.

## 하네스와 플러그인

| 후보 | 용도 | 선택 기준과 주의점 |
| --- | --- | --- |
| [Superpowers](https://github.com/obra/superpowers) | 설계·계획·구현·검증·디버깅 | 전체 절차 또는 필요한 Skill 선택. 자동 호출·참조 의존성 확인 |
| [ECC](https://github.com/affaan-m/ECC) | 다양한 개발 Skill·검증·맥락 관리 | Codex 경로가 있어도 개별 Skill의 훅·명령 호환성 확인 |
| [OMX](https://github.com/Yeachan-Heo/oh-my-codex) | Codex 역할 분담·팀·검토·상태 유지 | CLI·설정·일부 tmux 의존성, 제공 환경 호환성 확인 |
| [Spec Kit](https://github.com/github/spec-kit) | 명세→계획→작업→구현 | 실제 설치본의 Codex 통합·명령과 기존 프로젝트 지원 확인 |

OMX README의 `--madmax`는 승인·샌드박스 우회 옵션과 연결된다. 시험에서 해당 예시를 그대로 실행하지 않는다. 전체 하네스 여러 개를 동시에 적용하기보다 하나의 기준 워크플로를 정한다.

GSD의 기존 [저장소](https://github.com/gsd-build/get-shit-done)는 보관 처리됐고 [GSD Core](https://github.com/open-gsd/gsd-core)로 이동했다. 옛 설치 예시·스타 수를 현재 실행 근거로 삼지 않는다.

## 상황별 Skill

| 후보 | 필요한 상황 |
| --- | --- |
| [Ponytail 적용 기준](ponytail.md) / [별도 Skill](../../ponytail/SKILL.md) | 코드 작성·수정 시 full 원칙을 기본 적용. 기존 코드·의존성을 재사용하며 필수 요구와 배정 범위·검사·설명 기록 유지 |
| [검증 후 완료 선언](https://github.com/obra/superpowers/blob/main/skills/verification-before-completion/SKILL.md) | 실제 검사 증거와 완료 상태 구분 |
| [체계적 디버깅](https://github.com/obra/superpowers/blob/main/skills/systematic-debugging/SKILL.md) | 반복 오류·원인 추적 |
| [OpenAI security-best-practices](https://github.com/openai/skills/tree/main/skills/.curated/security-best-practices) | 관련 언어·프레임워크의 보안 검토를 요청할 때 |
| [OpenAI Docs](https://developers.openai.com/learn/docs-mcp) | 과제 자체가 OpenAI 기능·API·Codex 사용법 확인을 요구할 때 |
| [Vercel agent-skills](https://github.com/vercel-labs/agent-skills) | 실제 스택이 React·Next.js 등 관련 기술일 때만 |
| [visual-explainer 공개 원본](https://github.com/nicobailon/visual-explainer) / [이 저장소의 복사본](../../visual-explainer/SKILL.md) | 실제 코드 근거를 단계별 HTML로 설명할 때. 기본 HTML에는 MCP가 필수가 아니며 COFA 프로필·Node·전체 리소스 폴더 확인 |

Skill 한 파일에 다른 도구·참조·스크립트 의존성이 있을 수 있다. 복사 전에 전체 필요한 구성과 라이선스를 확인한다. 지침 원문이 Code Review·TDD·보안 보고 등 더 큰 절차를 호출하는지도 확인한다.

## MCP와 검증 도구

COFA는 MCP 탭의 `mcpServers` JSON과 저장 버튼을 설정 진입점으로 사용한다. 실제 예제·필드 호환성·각 Bash 세션의 연결 확인은 [MCP JSON 안내](mcp-json.md)를 따른다. 일반 Codex의 TOML·설치 명령을 설정 화면에 그대로 붙여 넣지 않는다.

| 후보 | 역할 | 시험 판단 |
| --- | --- | --- |
| [OpenAI Docs MCP](https://developers.openai.com/learn/docs-mcp) | 공식 OpenAI 문서 검색·읽기 | 필요한 과제일 때, 일반 문서 질의만 사용 |
| [Context7](https://github.com/upstash/context7) | 라이브러리·버전별 문서 | 인증·외부 질의 전송·제공 환경 지원 확인 |
| [Serena](https://github.com/oraios/serena) | 심볼·참조 관계 기반 코드 탐색·편집 | 설치·언어 서버·프로젝트 경로와 역할별 수정 범위 확인 |
| [GitHub MCP](https://github.com/github/github-mcp-server) | 저장소·이슈·PR 도구 | 인증·쓰기·외부 전송 조건 확인. 다운로드만으로 충분할 수 있음 |
| [Playwright Test](https://github.com/microsoft/playwright) | 반복 가능한 브라우저 테스트 | 실행 허용 범위 미확인 |
| [Playwright MCP](https://github.com/microsoft/playwright-mcp) | 에이전트의 브라우저 탐색·조작 | 자동 조작 제한에 대한 운영진 확인 전 사용하지 않음 |
| [Playwright CLI+Skills](https://github.com/microsoft/playwright-cli) | CLI 기반 브라우저 작업 | CLI 방식도 자동 조작 제한의 예외가 아님 |
| [Chrome DevTools MCP](https://github.com/ChromeDevTools/chrome-devtools-mcp) | 브라우저 검사·성능·조작 | 브라우저 기능과 네트워크·텔레메트리 조건 확인 |
| [Repomix](https://github.com/yamadashy/repomix) | 코드 맥락 패키징 | 큰 저장소에 필요할 때만 로컬 사용. 외부 업로드 금지 |

읽기 전용 MCP도 검색어를 외부로 보낸다. 문제·코드·개인정보를 외부 질의에 포함하지 않는다. 공개 문서의 라이브러리명·버전·일반 사용법만 허용 범위에서 조회한다. MCP 또는 플러그인 허용이 모든 도구 행동을 허용하는 것은 아니다.

## 선택 절차

1. 지금 부족한 능력·정보가 무엇인지 확인한다.
2. 기존 Codex·셸·테스트로 해결 가능한지 확인한다.
3. 설치·인증·외부 연결·자동 실행·훅·모델 호출을 점검한다.
4. 공개 자료 접근과 시험 사용 권한을 구분한다.
5. 허용되고 실익이 있는 최소 구성으로 시험한다. 반복 실패하면 기본 환경으로 진행한다.

이 저장소는 도구를 자동 설치·연결·실행하지 않는다. 현재 모델을 교체하거나 개인 인증을 설정하지 않는다.
