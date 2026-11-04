# Ponytail provenance

- Upstream: https://github.com/DietrichGebert/ponytail
- Revision: `96608e078b2d5ea607c5c3b8b5a54d1c1fba6846`
- Original file: `skills/ponytail/SKILL.md`
- Original SHA-256: `9badd22a32e19cb884e46dfa8d3aae82bb81dfa5484105b8b4f0262df823a509`
- License: MIT, copyright 2026 DietrichGebert; included in [LICENSE](LICENSE).
- Imported on: 2026-11-04 (Asia/Seoul).

This is the core instruction skill only. No plugin hooks, lifecycle configuration, dashboard, extra review commands, installers or model credentials are included.

Local adaptations normalize the description to one YAML line, preserve the upstream argument hint under metadata for the local validator, and add a COFA implementation profile before the unchanged upstream body. The profile preserves task completeness, file ownership, evidence and requested explanations; it does not claim improved completion time or official COFA support.

The unmodified original and MIT notice are also bundled inside cofa-delivery under `references/ponytail/` so its standalone folder can apply the same principles without locating another skill. Both copies are pinned to the revision above. Updating the source requires reviewing and updating both packages together.
