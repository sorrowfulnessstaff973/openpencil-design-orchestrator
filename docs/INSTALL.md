# Installation Guide

## Scope

This guide covers how to install and verify `openpencil-design-orchestrator` as a skill repository artifact.

This guide does **not** claim automatic support for every client or environment.
Use only the workflows already documented in this repository.

## What you need first

Before installation, confirm:

- you have access to an OpenClaw-compatible skill environment
- you can import or place a `.skill` artifact into that environment
- Pencil / OpenPencil and its MCP path are already handled separately if your workflow depends on live MCP editing

This repository is about **design orchestration**, not generic MCP installation.

## Option 1 — Install from the packaged `.skill`

1. Download the latest packaged artifact from the latest release
2. Import or place the `.skill` file into your target skill environment
3. Restart or reload the environment if required by that environment

## Option 2 — Use from source

1. Clone this repository
2. Copy the skill source into your local skill directory
3. Keep the repository as a source-of-truth repo for future edits

## Minimum verification

Use this repository in a small, bounded scenario first.

Recommended verification prompt:

- “Plan the page structure first, then create only the skeleton.”
- “Only redesign the hero section; do not touch the rest.”
- “Audit spacing, hierarchy, and token consistency before editing.”

A successful first verification should show:

- staged workflow behavior
- bounded scope
- no blind whole-page rewrite
- read-before-write discipline
- fallback awareness when MCP is unavailable

## What success looks like

You should see the skill encourage or enforce:

1. preflight before mutation
2. planning before structure changes
3. section-bounded edits
4. refinement after structure is stable
5. explicit fallback instead of pretending live edit works

## What failure looks like

Treat these as signs the workflow is not being applied correctly:

- it jumps directly into a whole-page redesign
- it skips reading current structure
- it edits multiple sections without scope control
- it assumes MCP is available without checking
- it claims live editing when running in fallback-only conditions

## First troubleshooting checks

If results look wrong, check in this order:

1. Did you install the correct artifact/version?
2. Are you invoking the repository for a staged design task rather than generic design generation?
3. Is MCP actually available, or should the task be treated as fallback mode?
4. Did the request specify a bounded scope such as one page or one section?
5. Are you asking for orchestration, or are you accidentally asking for unconstrained generation?

## Related files

- `../SKILL.md`
- `../references/prompt-framework.md`
- `../references/workflow-sequence.md`
- `../references/fallback-mode.md`
- `../references/risk-matrix.md`
