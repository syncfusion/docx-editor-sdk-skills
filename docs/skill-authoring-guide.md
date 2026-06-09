# Skill Authoring Guide

Use this guide when adding or updating a skill in this repository.

## Required structure

Each skill must live under `skills/<skill-name>/` and include:

```text
skills/<skill-name>/
├── SKILL.md
├── README.md
└── references/
```

Add a `scripts/` folder only when the skill documents an execution mode that creates temporary scripts. Track empty execution folders with `.gitkeep`.

## SKILL.md frontmatter

Every `SKILL.md` must start with YAML frontmatter:

```yaml
---
name: <skill-folder-name>
description: <clear trigger-oriented description>
metadata:
  author: Syncfusion Inc
  version: "<library-version>"
---
```

Optional metadata such as `compatibility` may be added, but keep it consistent across similar skills.

## Recommended SKILL.md sections

Use consistent sections where they apply:

1. Overview
2. Key Capabilities
3. Prerequisites
4. Quick Start Examples
5. Modes and intent-routing rules
6. Code References
7. Rules

If a skill supports only code generation, document one mode only and avoid references to CSX, Dart script execution, or temporary scripts.

## Reference files

- Put product/API snippets in `references/*.md`.
- Put script templates in `references/template.*` only for skills with execution mode.
- For `.csx` templates, include `Syncfusion.Licensing` and avoid pinned `#r "nuget: ..."` versions unless a specific feature requires a fixed package version.
- Link every referenced file from `SKILL.md` or `README.md`.
- Do not leave stale links to renamed files.
- Use placeholders intentionally and document what each placeholder means.

## Validation

Run this before opening a pull request:

```bash
python scripts/validate_skills.py
```

The validator checks required files, skill frontmatter, relative links, referenced `references/` files, stale placeholder package versions, and basic documentation consistency.
