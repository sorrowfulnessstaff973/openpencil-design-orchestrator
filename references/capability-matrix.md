# Capability Matrix

Use this file to judge whether `openpencil-mcp` matches the user’s requirements.

## Requirement Match Table

| Requirement | Match | Notes |
| --- | --- | --- |
| MCP-accessible from coding agents | Yes | Public docs explicitly mention Claude Code, Codex, Cursor, Windsurf, and other MCP clients. |
| Read existing design structure | Yes | Public tool list includes page tree, node inspection, component listing, variables, fonts, bounds, and related read tools. |
| Create new design structure | Yes | Public tool list includes create page, create shape, render JSX, create component, create instance. |
| Modify existing design nodes | Yes | Public tool list includes layout, fill, stroke, text, font, effects, visibility, constraints, move, resize, and related mutators. |
| Perform structural edits | Yes | Public tool list includes reparent, group, ungroup, clone, delete, rename, boolean ops, and page switching. |
| Export output artifacts | Yes | Public tool list includes image and SVG export. |
| Analyze design system consistency | Yes | Public tool list includes color, typography, spacing, cluster analysis, variable and collection tools, and diff snapshots. |
| Support staged prompt workflow | Yes | Public docs and release notes describe layered flows such as planning, skeleton, content, and refine. |
| Safe remote automation by default | Partial | HTTP mode is safer than stdio by default because `eval` is disabled, but remote safety still depends on deployment choices and auth/config hygiene. |
| Zero local setup / zero app dependency | Partial | Some public workflows depend on the local app or local MCP installation/config. Not guaranteed to be fully remote-only or zero-setup. |
| Stable one-shot full-product generation | Partial | The tool surface is rich, but public evidence suggests staged workflows are safer than monolithic prompts. |
| Low-risk unrestricted escape hatch | No | `eval` exists in stdio mode and should be treated as high risk, not as a default workflow. |

## Capability Groups

### 1. Read / Inspect

High confidence capabilities:

- open files or create documents
- inspect page tree and nodes
- list pages, components, fonts, variables, collections
- compute bounds and ancestry/children
- analyze color, typography, spacing, clusters
- diff snapshots

Use for:
- design audits
- structure reviews
- token audits
- preflight before mutation

### 2. Create / Generate

High confidence capabilities:

- create pages
- create shapes and vectors
- render JSX into design nodes
- create components and instances

Use for:
- scaffold generation
- section skeletons
- reusable component setup

### 3. Modify / Refine

High confidence capabilities:

- update position, size, text, font, opacity, radius, rotation
- set fill, stroke, effects, layout, constraints
- move, resize, replace, align, distribute

Use for:
- section-level edits
- consistency passes
- responsive/layout refinement

### 4. Structure / Organize

High confidence capabilities:

- group and ungroup
- rename and clone
- reparent nodes
- switch pages
- boolean operations
- flatten nodes

Use for:
- hierarchy cleanup
- component extraction
- page-by-page reorganization

### 5. Export / Review

High confidence capabilities:

- export images
- export SVG
- compare against snapshot states

Use for:
- change review
- artifact generation
- before/after proof

## Best-Fit Use Cases

`openpencil-mcp` is a good fit when the user wants:

- MCP-driven design editing from Claude Code, Codex, Cursor, or Windsurf
- staged page or section generation
- design system inspection or cleanup
- structured refactors of a design file
- export and audit workflows around an existing design

## Weak-Fit / Caution Cases

Use caution when the user wants:

- one-shot generation of a whole product without checkpoints
- unattended high-risk automation with `eval`
- fully remote workflows with no local app or MCP installation assumptions
- guaranteed identical behavior across every MCP client

## Recommendation Summary

### Strong Yes

- MCP-first design orchestration
- staged prompt execution
- section-scoped editing
- design analysis / audit / export workflows

### Partial Yes

- remote automation
- fully headless workflows
- broad autonomous generation without supervision

### No by Default

- unrestricted `eval`
- giant unbounded one-prompt redesigns
