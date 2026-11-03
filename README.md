# Skills

AI 코딩 에이전트와 제한된 시간 안에 문제를 정의하고, 구현·검증·설명하기 위한 한국어 작업 지침 모음입니다. 프레임워크나 모델의 성능 향상을 보장하는 패키지가 아니라, 판단 기준과 검증 증거를 유지하기 위한 준비 자료입니다.

현재 제공하는 Skill은 **cofa-delivery**, **cofa-requirements-interview**, **cofa-requirements-review**, **cofa-architecture-tour**, **visual-explainer**입니다. 180분 구현 과제의 준비와 리허설을 위한 자료이며, 실제 시험의 허용 범위는 해당 시험의 최신 안내가 우선합니다.

| Skill | 역할 |
| --- | --- |
| [cofa-delivery](skills/cofa-delivery/SKILL.md) | 전체 진행, 위임, 검증과 인계 기준 |
| [cofa-requirements-interview](skills/cofa-requirements-interview/SKILL.md) | README 기반 담당자 질문 선별, 답변 검증과 요구사항 반영 |
| [cofa-requirements-review](skills/cofa-requirements-review/SKILL.md) | 별도 세션에서 원문·실제 담당자 답변·명세의 누락·충돌·가정을 검토 |
| [cofa-architecture-tour](skills/cofa-architecture-tour/SKILL.md) | 아키텍처·데이터·구현 순서·Docker 흐름의 독립 HTML과 코드 투어 |
| [visual-explainer](skills/visual-explainer/SKILL.md) | 공개 MIT Skill의 고정 버전과 COFA 프로필. 단계별 SVG·HTML 시각 설명 |

## 처음 읽을 파일

| 목적 | 파일 |
| --- | --- |
| AI의 진입점과 단계별 읽기 경로 | [SKILL.md](skills/cofa-delivery/SKILL.md) |
| 180분 전체 시나리오 | [응시 시나리오](skills/cofa-delivery/references/scenario.md) |
| 확인된 규칙과 미확인 사항 | [규칙 요약](skills/cofa-delivery/references/exam-boundaries.md) |
| 첫 요청과 단계별 요청 예시 | [프롬프트](skills/cofa-delivery/references/prompts.md) |
| 여러 Bash의 메인·검토 세션 시작과 인계 | [Bash 세션 운영](skills/cofa-delivery/references/bash-sessions.md) |
| 에이전트 역할·수정 경계·검증과 판단 기록 | [여러 세션·멀티 에이전트 운영](skills/cofa-delivery/references/multi-agent.md) |
| Spec Kit·BMAD·Superpowers 역할 비교 | [계획 도구](skills/cofa-delivery/references/planning-tools.md) |
| 하네스·Skill·MCP 후보 | [도구 목록](skills/cofa-delivery/references/tool-catalog.md) |
| COFA MCP 탭에 넣을 JSON 예제와 연결 확인 | [MCP JSON 안내](skills/cofa-delivery/references/mcp-json.md) |
| AI 없이 직접 답하는 연습 | [서술형 준비](skills/cofa-delivery/references/written-practice.md) |
| 자료의 근거와 최신성 | [출처](docs/SOURCES.md) |

## AI에게 읽히는 방법

이 저장소를 읽을 수 있는 환경에서 다음처럼 요청합니다.

```text
skills/cofa-delivery/SKILL.md를 읽고 현재 단계에 필요한 참조만 적용해줘.
실제 과제의 지침과 기존 프로젝트 규칙을 먼저 확인해줘.
기술 스택, 설치된 도구, 허용 범위가 확인되기 전에는 추정하지 마.
```

단순히 clone했다고 Skill이 자동 등록되지는 않습니다. 일반 Codex의 프로젝트 Skill 탐색 경로는 `.agents/skills/`이며, 클라이언트와 버전의 지원 여부를 확인해야 합니다. 등록 없이 파일을 명시적으로 읽혀 사용하는 것도 가능합니다. 기존 지침을 덮어쓰거나 플랫폼 설정을 변경하지 않습니다.

추가 Skill을 사용할 때는 필요한 폴더가 함께 있는 저장소를 읽히거나 해당 Skill도 각각 추가합니다. `cofa-delivery` 하나만 설치한 경우 다른 Skill이 자동으로 함께 설치되지는 않습니다. 별도 Skill이 없으면 기존 문제 정의·설계 참조로 진행할 수 있습니다.

`visual-explainer`는 `SKILL.md` 하나가 아닌 폴더 전체를 등록합니다. 클라이언트가 Skill을 실제로 읽고 Node.js와 작업 파일에 접근할 수 있으면 자연어 요청으로 HTML을 만들 수 있습니다. 설치가 HTML을 자동 생성하는 것은 아닙니다. [COFA용 실행 조건과 요청 예시](skills/visual-explainer/references/cofa.md)를 참고하세요.

```text
visual-explainer를 적용하고 COFA 프로필을 따라줘.
현재 코드의 대표 요청 흐름을 파일·함수 근거와 함께 단계별 HTML로 만들어줘.
제공 작업 공간에 저장하고 브라우저 자동 실행 없이 결과 경로를 알려줘.
```

## 여러 Bash에서 사용하는 기본 구성

- Bash A: 제공 Codex로 문제 정의·구현·통합을 맡는 메인 세션.
- Bash B: 제공 Codex에 `cofa-requirements-review`를 읽혀 원문과 명세를 대조하는 검토 세션. 제품과 명세는 수정하지 않고 지정 보고서만 작성합니다.
- Bash C: 필요할 때 개발 서버나 검사를 실행하는 터미널입니다.

별도 Bash의 세션은 메인의 대화를 자동으로 알거나 결과를 자동 전달하지 않습니다. 실제 공유 파일 접근·동시 실행 지원을 확인한 뒤 [메인·검토 시작 프롬프트와 인계 절차](skills/cofa-delivery/references/bash-sessions.md)를 사용합니다. 네이티브 서브에이전트 기능 없이도 적용할 수 있는 운영안이며, 지원되지 않으면 한 세션에서 순차 검토합니다.

## 단계별 요청 예시

```text
cofa-delivery로 전체 진행 기준을 유지해줘.
담당자에게 질문하기 전 cofa-requirements-interview로 README의 미확인 조건을 추려줘.
설계와 첫 구현 이후에는 cofa-architecture-tour로 실제 근거가 있는 HTML 흐름도를 만들고,
계획·코드 확인·실행 검증 상태를 구분해서 내가 데이터 흐름을 설명할 수 있게 도와줘.
```

HTML은 외부 라이브러리 없이 생성합니다. 먼저 Python 3이 있는지 확인하고, 저장소 루트에서 아래 명령으로 가상 예제를 만들어 볼 수 있습니다. 기존 출력이 있으면 기본적으로 덮어쓰지 않습니다.

```bash
python3 skills/cofa-architecture-tour/scripts/render.py skills/cofa-architecture-tour/assets/example.json --output /tmp/cofa-architecture-example.html
```

예제는 공개용 합성 자료이며 앱·Docker 빌드 성공을 뜻하지 않습니다. 실제 과제의 모델 JSON·HTML과 질문 답변은 해당 작업 공간에 두고 이 공개 저장소에 올리지 않습니다.

## MCP 연결 방식

사전체험 화면의 MCP 탭은 `{"mcpServers": {}}` 형태의 JSON을 편집하고 저장하는 방식입니다. [연결 안내](skills/cofa-delivery/references/mcp-json.md)에 기존 서버를 보존해 합치는 절차와 [JSON 예제](skills/cofa-delivery/assets/mcp/)를 정리했습니다. 일반 Codex용 TOML이나 `codex mcp add` 명령을 이 화면에 붙여 넣지 않습니다.

서버별 필드와 실제 연결은 COFA에서 확인해야 합니다. 예제 저장만으로 설치·인증·도구 호출이 성공했다고 보지 않으며, 여러 Bash의 Codex 세션에서 각각 확인합니다. 이 저장소는 MCP를 자동 연결하지 않습니다.

## 시험 반입 관련 미확인 사항

공개 GitHub 자료를 가져올 수 있다는 안내와 **응시자가 시험 전에 작성해 공개한 개인 템플릿의 반입 허용**은 같은 의미가 아닙니다. 후자는 확인되지 않았습니다. 이 저장소가 공개돼 있다는 사실은 시험 사용 허가를 뜻하지 않습니다.

후속 서술형 단계에서는 AI를 사용하지 않습니다. 이 저장소의 서술형 자료는 시험 전 연습 또는 허용된 과제 수행 단계의 이해도 점검용입니다. 서술형 중 기존 docs 열람 가능 여부도 확인되지 않았습니다.

## 범위

- 실제 비공개 시험 문제·해답·제공 데이터·완성 코드를 포함하지 않습니다.
- 가상 연습 과제는 예시이며 출제 예측이 아닙니다.
- 대부분의 외부 도구는 링크와 용도만 정리합니다. 사용자가 추가 요청한 `visual-explainer`는 MIT 고지와 고정 커밋을 보존한 복사본이며 [출처·변경 내역](skills/visual-explainer/UPSTREAM.md)을 제공합니다.
- 기본 동작에는 MCP, 외부 모델, API 키, 훅, 자동 설치 스크립트가 필요하지 않습니다.
- 이 저장소를 사용하는 것만으로 작업 폴더에 파일이 생성되거나 도구가 설치되지는 않습니다.

## 검증

```bash
python3 scripts/check_repository.py
python3 scripts/test_architecture_renderer.py
node scripts/test_visual_explainer.mjs
```

첫 검사는 로컬 Markdown 링크와 Skill의 필수 메타데이터를 확인합니다. 두 번째는 HTML 생성기의 모델 무결성, 근거 필드 요구, 문자열 삽입과 기존 파일 보존을 확인합니다. 세 번째는 복사한 visual-explainer와 COFA 래퍼의 렌더링·리소스 정책·기존 파일 보존을 확인합니다. 시험 허용 여부, Codex 자동 인식, 실제 앱·Docker 실행 성공을 검증하지는 않습니다.

최초 작성: 2026-10-30. 담당자 질문·HTML 구조도 Skill 추가: 2026-11-03. 제3자 프로젝트의 기능과 설치 방식은 사용 전에 공식 자료를 다시 확인하세요.
