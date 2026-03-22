# openpencil-design-orchestrator

**English** | [简体中文](./README.zh-CN.md)

[![Release](https://img.shields.io/github/v/release/ziiinian/openpencil-design-orchestrator?display_name=tag)](https://github.com/ziiinian/openpencil-design-orchestrator/releases)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](./LICENSE)
[![Repo](https://img.shields.io/badge/OpenClaw-Agent%20Skill-blue)](https://github.com/ziiinian/openpencil-design-orchestrator)

Controlled AI-assisted design workflow for Pencil / OpenPencil.

An Agent Skill for orchestrating Pencil / OpenPencil design work through a staged, MCP-first workflow.

## Quick Start

### Option 1 — Download the packaged skill
Go to the latest release and download:

- [`openpencil-design-orchestrator.skill`](https://github.com/ziiinian/openpencil-design-orchestrator/releases/latest)

### Option 2 — Inspect the source
Browse the skill source directly in this repository:

- `SKILL.md`
- `references/`
- `scripts/`

## Installation / Use

This repository ships both the **source skill** and a packaged `.skill` release artifact.

Typical usage flow:

1. Download the `.skill` artifact from the latest release
2. Install/import it into your skill environment
3. Use it when working with Pencil / OpenPencil design tasks that need staged, bounded execution

Typical trigger examples:

- “Use Pencil/OpenPencil to redesign this hero section, but do it section-by-section.”
- “Audit this design for spacing, typography, and token consistency before editing.”
- “Plan the page structure first, then create only the skeleton.”

## Install and verify

For installation and first-run verification, see:

- [Installation Guide](./docs/INSTALL.md)
- [简体中文安装说明](./docs/INSTALL.zh-CN.md)

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
├── README.md
├── README.zh-CN.md
├── references/
├── scripts/
├── dist/
│   └── openpencil-design-orchestrator.skill
├── source/
│   └── NOTICE.txt
└── LICENSE
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

## Roadmap

Possible future improvements:

- richer example prompts for more design scenarios
- more client-specific adapter notes
- expanded fallback examples for non-MCP workflows
- release notes for future versions beyond the initial public release

## Release

- Latest release: <https://github.com/ziiinian/openpencil-design-orchestrator/releases/latest>
- First public release: <https://github.com/ziiinian/openpencil-design-orchestrator/releases/tag/v1.0.0>

## License

This repository is released under the MIT License. See [LICENSE](./LICENSE).
