# Prompt Framework

Use these templates to keep Pencil/OpenPencil work staged, bounded, and verifiable.

## Global Rules

Apply these rules to every phase:

- Keep edits bounded to the approved scope.
- Re-read relevant pages/nodes before mutation.
- Stop on ambiguity that changes structure or scope.
- Prefer tool-directed instructions over aesthetic-only prose.
- Require a compact change report after each phase.

## Phase 0 - Preflight Prompt

```text
You are working with Pencil/OpenPencil.

Before making changes:
- confirm the current file/page context
- confirm whether MCP is available
- identify whether transport is stdio or HTTP
- validate that the target page/section can be read
- do not modify anything yet

Return:
1. current mode
2. readable pages/sections
3. blocking issues
4. recommended next phase
```

## Phase 1 - Planning Prompt

```text
You are designing in Pencil/OpenPencil via MCP.

Task:
Create a design execution plan for this request: {TASK}

Hard rules:
- Do not create or modify nodes yet.
- Only produce a structured plan.
- Break the work into pages, sections, and components.
- Identify reusable tokens, layout rules, and visual constraints.
- Flag any ambiguity before execution.

Return:
1. pages
2. sections per page
3. component inventory
4. token/style plan
5. execution order
6. risk points
7. verification checkpoints
```

## Phase 2 - Skeleton Prompt

```text
Build only the structural skeleton for the approved plan.

Hard rules:
- Create only pages, frames, sections, groups, and layout containers.
- Do not polish visuals.
- Do not generate final copy unless placeholder text is required.
- Use clear hierarchy and autolayout where appropriate.
- Keep naming explicit and reusable.

After execution, report:
1. created pages
2. created sections/frames
3. layout structure used
4. unresolved structure risks
```

## Phase 3 - Section Content Prompt

```text
Fill content for only this section: {SECTION_NAME}

Hard rules:
- Modify only the target section.
- Do not touch other pages or sections.
- Re-read the relevant nodes before editing.
- Keep structure stable unless a local fix is necessary.
- If a conflict appears, stop and report it.

Return:
1. nodes changed
2. nodes created
3. text/content inserted
4. tokens/styles applied
5. anything needing confirmation
```

## Phase 4 - Refine Prompt

```text
Refine the current design for consistency and polish.

Hard rules:
- Do not restructure the information architecture.
- Do not add new sections unless strictly necessary.
- Focus only on spacing, alignment, typography consistency, color/token consistency, and emphasis hierarchy.
- Keep the existing component logic intact.

Return:
1. refinements made
2. consistency fixes
3. remaining weak spots
```

## Phase 5 - Safety / Failure Prompt

```text
Before making further changes, validate the current page tree and target nodes.

If any of the following happens, stop and report instead of continuing:
- stale page tree
- missing target node
- cross-section mutation conflict
- transport/MCP instability
- permission mismatch

If MCP is unavailable, switch to fallback guidance mode instead of guessing.
```

## Bad Prompt Patterns

Avoid these patterns:

- “Design the whole product in one shot.”
- “Make it high-end / Apple-like / modern” without structural constraints.
- “Optimize everything” without naming scope.
- “Feel free to change anything if needed.”

These prompts usually increase drift, hidden scope expansion, and rollback difficulty.

## Good Prompt Patterns

Prefer these properties:

- phase-specific
- scope-bounded
- verifiable output
- explicit stop conditions
- one page or one section per batch
