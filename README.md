# openpencil-design-orchestrator

An Agent Skill for orchestrating Pencil / OpenPencil design work through a staged, MCP-first workflow.

## What it does

`openpencil-design-orchestrator` turns vague AI-assisted design requests into a controlled sequence of steps:

1. **Preflight** – verify Pencil/OpenPencil, MCP readiness, and current structure
2. **Planning** – break work into pages, sections, components, tokens, and execution order
3. **Skeleton** – build structural scaffolding only
4. **Section Content** – edit one section at a time with bounded scope
5. **Refinement** – improve spacing, hierarchy, consistency, and polish
6. **Save / Handoff** – summarize changes and remaining risks

The goal is to avoid uncontrolled one-shot design mutations and keep changes small, reviewable, and reversible.

## Best fit

Use this skill when you need to:

- work with Pencil / OpenPencil through MCP
- orchestrate AI-assisted design changes safely
- perform section-by-section design edits
- audit layout, consistency, spacing, tokens, and structure
- adapt workflows across Claude Code, Codex, Cursor, or Windsurf

## Not for

This skill is not the best primary path for:

- unconstrained whole-product one-shot generation
- blind large-scale destructive edits
- pretending live editing works when MCP is unavailable
- default-on high-risk automation via unrestricted `eval`

## Repository layout

```text
.
├── SKILL.md
├── references/
├── scripts/
├── dist/
│   └── openpencil-design-orchestrator.skill
├── source/
│   └── NOTICE.txt
└── README.md
```

## Key files

- `SKILL.md` – trigger description, workflow rules, operating constraints
- `references/` – prompt framework, workflow sequence, fallback mode, risk matrix, client adapters, capability notes
- `scripts/preflight-check.sh` – quick environment and MCP readiness check
- `scripts/scaffold-phase-prompt.py` – generate phase-specific prompt scaffolds
- `dist/openpencil-design-orchestrator.skill` – packaged distributable skill file

## Typical usage patterns

### 1. Build a new page safely
Example: “Create a SaaS landing page, but start with skeleton only.”

### 2. Revise one section without collateral damage
Example: “Only redesign the hero section; do not touch the rest.”

### 3. Audit an existing design
Example: “Review spacing, typography hierarchy, and token consistency before editing.”

## Packaging

The packaged distributable artifact is included here:

- `dist/openpencil-design-orchestrator.skill`

If you modify the source, repackage the skill from the source folder / repo root using your normal skill packaging flow.

## Notes

This repository is organized for GitHub readability:

- source files live at the repository root
- packaged artifact lives in `dist/`
- minimal repo-only files like `.gitignore` are included

## License

This repository is released under the MIT License. See [LICENSE](./LICENSE).

## GitHub setup suggestions

If you are publishing this repository on GitHub, you can reuse the prepared metadata in [GITHUB_METADATA.md](./GITHUB_METADATA.md), including:

- repository short description
- bilingual summary text
- suggested topics
- optional About text
