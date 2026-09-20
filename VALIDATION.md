# Release validation — 2.0.0

Date: 2026-09-20
Python used: 3.13.5

## Checks completed

- Package-specific validator: **Passed**. It checks 44 required files, the package's frontmatter/UI metadata conventions, local Markdown file links, template interfaces, and behavioral-fixture structure.
- Standard-library unit tests: **38 passed**. The 26 retained tests cover safe initialization and package validation; 12 added tests cover V2 metadata, model/handoff template sections, fixture counts/version/status, duplicate IDs, text expectations, tool-citation markers, and escaping links.
- Behavioral fixture definitions: **36 cases**. Their JSON structure is checked; their execution status remains `not_run`.
- Cross-file review: checked the three knowledge objects, experience-model placement, scope/approval/evidence separation, condition-to-consequence reasoning, novice collaboration, distinct acceptance/research tracks, and upgrade instructions.
- Distribution: ZIP contains one `miles-game-experience-designer` root and 44 regular files. Bytecode caches and preparation scripts are excluded. Archive extraction, content equality, validator, and all unit tests are checked on the extracted copy before delivery.

## Evidence boundaries

The automated checks execute deterministic helper scripts and inspect package files. They do not run an agent, evaluate a real game's design, or observe players. All **36 behavioral scenarios remain unexecuted against a live host/model**. The original worked examples report no implementation or player-test results.

A passing template-heading check establishes the template interface, not semantic design quality. Compatibility with the documented directory format does not certify behavior in every skill host. The initializer is tested locally on the stated Python version; Python 3.10+ compatibility is the code's intended requirement, not a multi-version certification.

## References

V2 reopened Agent Skills packaging, OpenAI's skill documentation, the Fullerton book overview, and XAG 103. It added the author overview/contents for Norman's Emotional Design and the Design Council's Double Diamond description. Other source-access notes are inherited from the supplied V1.1 registry; full books, linked recordings, and legacy PDF sources were not freshly reviewed for V2. See [Sources](references/sources.md).

## Reproduce the deterministic checks

From the extracted skill directory:

```bash
python3 scripts/validate_skill.py
python3 -m unittest discover -s tests -v
```

For actual agent testing, use [evals/README.md](evals/README.md), retain responses and file diffs, and report host/model/settings and case-level evidence separately.
