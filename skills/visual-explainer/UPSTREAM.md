# Upstream provenance

- Project: [nicobailon/visual-explainer](https://github.com/nicobailon/visual-explainer).
- Pinned commit: [3d592addcc1689ea2251ee67991f12f8a30fd2d9](https://github.com/nicobailon/visual-explainer/commit/3d592addcc1689ea2251ee67991f12f8a30fd2d9).
- Imported directory: `plugins/visual-explainer/`, version 0.14.0, 2026-11-03.
- License: [MIT](LICENSE), copyright Nico Bailon. Bundled Pele retains its [separate MIT notice](kit/vendor/PELE-LICENSE).

## Local changes

- Moved the frontmatter `compatibility` value into `metadata.compatibility` for the local Codex skill validator.
- Added a COFA routing section to `SKILL.md` and [usage profile](references/cofa.md).
- Added [render-cofa.mjs](kit/render-cofa.mjs), a thin wrapper around upstream's pure `renderPage` function. It disables executable flow-model imports, omits browser checks/opening, removes the injected Google Fonts links, applies a restrictive resource CSP, and preserves existing outputs unless `--force` is requested.
- Included the upstream root MIT license here so the copied skill remains attributable when installed alone.

The remaining imported files are retained from the pinned directory. Optional MCP, Pi, PPTX and video resources are present for provenance and completeness but are not automatically installed or enabled. Dependencies for those features are not bundled by this copy. This is a locally adapted copy, not an official COFA integration or an endorsement by the upstream author.

The wrapper's CSP restricts resource loading; it is not a sandbox for arbitrary untrusted HTML and does not prove a diagram's correctness. Review generated sources and keep actual exam code, data and diagrams in the provided task workspace.
