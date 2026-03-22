# Workflow Sequence

Use this file to decide what to do next during Pencil/OpenPencil work.

## Default Sequence

1. Open or create the document.
2. Read structure first.
3. Produce a plan.
4. Build skeleton.
5. Fill one section at a time.
6. Refine consistency.
7. Save and summarize.

## Recommended MCP Operation Pattern

Use this order when the tool surface allows it:

1. `open_file` or `new_document`
2. `get_page_tree`, `find_nodes`, `get_node`
3. structure creation (`create_shape`, containers, layout primitives, or document-specific scaffold tools)
4. incremental updates (`set_fill`, `set_stroke`, `set_layout`, `update_node`, `set_effects`)
5. structural edits (`reparent_node`, `group_nodes`, `clone_node`, `delete_node`)
6. `save_file`

## Mutation Discipline

Apply these rules:

- Read before writing.
- Change one page or one section per batch.
- Re-read after each mutation batch if the page tree may have changed.
- Avoid mixing structural edits and broad stylistic polish in the same batch.
- Do not continue after unresolved node conflicts.

## Decision Tree

### If the request is vague

- Do planning only.
- Do not modify the design yet.

### If the structure is missing

- Do skeleton next.
- Do not polish visuals yet.

### If the structure is approved but content is thin

- Do section content next.
- Work section-by-section.

### If the content exists but consistency is weak

- Do refine next.
- Limit changes to consistency and polish.

### If the environment is unstable

- Stop mutation.
- Run preflight again.
- Switch to fallback mode if MCP is not reliable.

## Strong Recommendations

- Prefer planning -> skeleton -> section -> refine over all-in-one generation.
- Prefer local `stdio` MCP for interactive design sessions.
- Prefer `HTTP` MCP for controlled automation with a tighter safety boundary.
- Keep `eval` off in remote or semi-trusted automation paths.

## Anti-Patterns

Avoid these workflows:

- blind write without reading the current tree
- full-app redesign from a single vague prompt
- multi-page mutation in the same batch when the user asked for one area
- continuing after stale-tree or missing-node signals
