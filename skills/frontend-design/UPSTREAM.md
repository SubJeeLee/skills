# Upstream and COFA adaptation

- Source: https://github.com/anthropics/skills
- Pinned commit: `ca45fc496a3436251f191354091d557da31c15b5`
- Skill directory: `skills/frontend-design`
- Imported on: 2026-11-05 (Asia/Seoul).
- License: [LICENSE.txt](LICENSE.txt), copied without changes.

`SKILL.md` retains the original frontmatter and body and adds a clearly marked COFA profile before the body. The profile keeps confirmed requirements, functional delivery, file ownership and verification ahead of design; it limits first-pass UI work or defers optional motion. It overrides readiness-only replies and mandatory visual workflows in COFA. This is a local adaptation, not an official COFA integration.

The original instruction file is also bundled in cofa-delivery's `references/ui/` so that folder can be used alone. Both packages must be updated together. No installers, hooks, remote fonts, browser drivers or runtime dependencies are installed by this copy.

## Imported byte identities

- `skills/frontend-design/SKILL.md`: SHA-256 `d91970639e9f5c37682ac7ab60094d35f1c7c1f38d731bd56396563aee10c1d3`.
