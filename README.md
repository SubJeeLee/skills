# Skills

AI 코딩 에이전트와 제한된 시간 안에 문제를 정의하고, 구현·검증·설명하기 위한 한국어 작업 지침 모음입니다. 프레임워크나 모델의 성능 향상을 보장하는 패키지가 아니라, 판단 기준과 검증 증거를 유지하기 위한 준비 자료입니다.

현재 제공하는 Skill은 **cofa-delivery**입니다. 180분 구현 과제의 준비와 리허설을 위한 자료이며, 실제 시험의 허용 범위는 해당 시험의 최신 안내가 우선합니다.

## 처음 읽을 파일

| 목적 | 파일 |
| --- | --- |
| AI의 진입점과 단계별 읽기 경로 | [SKILL.md](skills/cofa-delivery/SKILL.md) |
| 180분 전체 시나리오 | [응시 시나리오](skills/cofa-delivery/references/scenario.md) |
| 확인된 규칙과 미확인 사항 | [규칙 요약](skills/cofa-delivery/references/exam-boundaries.md) |
| 첫 요청과 단계별 요청 예시 | [프롬프트](skills/cofa-delivery/references/prompts.md) |
| Spec Kit·BMAD·Superpowers 역할 비교 | [계획 도구](skills/cofa-delivery/references/planning-tools.md) |
| 하네스·Skill·MCP 후보 | [도구 목록](skills/cofa-delivery/references/tool-catalog.md) |
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

## 시험 반입 관련 미확인 사항

공개 GitHub 자료를 가져올 수 있다는 안내와 **응시자가 시험 전에 작성해 공개한 개인 템플릿의 반입 허용**은 같은 의미가 아닙니다. 후자는 확인되지 않았습니다. 이 저장소가 공개돼 있다는 사실은 시험 사용 허가를 뜻하지 않습니다.

후속 서술형 단계에서는 AI를 사용하지 않습니다. 이 저장소의 서술형 자료는 시험 전 연습 또는 허용된 과제 수행 단계의 이해도 점검용입니다. 서술형 중 기존 docs 열람 가능 여부도 확인되지 않았습니다.

## 범위

- 실제 비공개 시험 문제·해답·제공 데이터·완성 코드를 포함하지 않습니다.
- 가상 연습 과제는 예시이며 출제 예측이 아닙니다.
- 외부 프로젝트의 Skill이나 코드 원문을 복제하지 않고 링크와 용도를 정리합니다.
- 기본 동작에는 MCP, 외부 모델, API 키, 훅, 자동 설치 스크립트가 필요하지 않습니다.
- 이 저장소를 사용하는 것만으로 작업 폴더에 파일이 생성되거나 도구가 설치되지는 않습니다.

## 검증

```bash
python3 scripts/check_repository.py
```

이 검사는 로컬 Markdown 링크와 Skill의 필수 메타데이터를 확인합니다. 시험 허용 여부, Codex 자동 인식, 실제 구현 성능을 검증하지는 않습니다.

작성 기준일: 2026-10-30. 제3자 프로젝트의 기능과 설치 방식은 사용 전에 공식 자료를 다시 확인하세요.
