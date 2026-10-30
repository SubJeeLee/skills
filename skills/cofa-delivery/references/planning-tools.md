# Spec Kit, BMAD, Superpowers의 역할

2026-10-30 공개 공식 자료를 확인한 비교다. 명령명·기능·Codex 통합 방식은 버전에 따라 달라지므로 실제 설치본의 안내를 확인한다. 이 문서를 읽는 것만으로 도구를 설치하거나 호출할 수 있게 되지는 않는다.

| 도구 | 중심 용도 | 겹치는 부분 |
| --- | --- | --- |
| [Spec Kit](https://github.com/github/spec-kit) | 명세를 계획·작업·구현·검증에 연결 | 요구사항 확인, 기술 계획, 작업 분해 |
| [BMAD](https://github.com/bmad-code-org/BMAD-METHOD) | 업무·제품·UX·아키텍처 관점의 요구 정리 | 문제 정의, 설계, 검토, 구현 지원 |
| [Superpowers](https://github.com/obra/superpowers) | 설계 확인부터 구현·테스트·검토까지 개발 절차 | 질문, 접근법 비교, 설계·작업 계획 |

## 추천 협업 패턴

1. 과제와 기존 코드를 먼저 읽는다.
2. Spec Kit을 사용하기로 했다면 기준 명세와 기술 계획을 작성한다.
3. 업무 조건이 복잡한 경우 BMAD에 기존 명세의 누락·모순만 검토하도록 맡긴다.
4. 발견 사항을 같은 기준 명세에 반영한다. 새 요구사항 문서를 경쟁시키지 않는다.
5. 구현 이후 필요하면 Superpowers의 검증·디버깅 지침을 사용한다.

전체 플러그인의 자동 호출이 이 역할 분담과 충돌하면 설치본의 적용 범위를 조정하거나 한 도구로 줄인다. 세 프레임워크의 전체 절차를 연속 실행하지 않는다.

## 검토의 출력

문제 / 원문 근거 / 구현에 미치는 영향 / 수정 제안 / 중요도.

미확인 조건은 '구현 전 확인', '가정 명시 후 진행 가능', '범위 밖'으로 분류한다. 도구의 이름이나 여러 페르소나를 사용했다는 사실을 독립 검증·성과로 표현하지 않는다.

## 참고

- [Spec Kit SDD](https://github.com/github/spec-kit#spec-driven-development)
- [BMAD 계획 경로 선택](https://docs.bmad-method.org/plan/choose-a-planning-path/)
- [Superpowers brainstorming](https://github.com/obra/superpowers/blob/main/skills/brainstorming/SKILL.md)
