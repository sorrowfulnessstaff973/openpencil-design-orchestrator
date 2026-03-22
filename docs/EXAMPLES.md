# Usage Examples

## Scope

These examples are designed to reinforce the repository's staged, bounded philosophy.

They are not one-shot “design the whole product” prompts.

## Example 1 — Start with structure only

Use when the page is new or still ambiguous.

Prompt:

> Plan the page structure first, then create only the skeleton. Do not polish visuals yet. Keep the work bounded to one landing page.

What good output should include:
- explicit planning phase
- page sections in order
- skeleton-only intent
- no premature refinement

## Example 2 — Redesign one section only

Use when the overall page should stay stable.

Prompt:

> Only redesign the hero section. Do not touch the rest of the page. Re-read the current structure before proposing changes.

What good output should include:
- one-section scope
- read-before-write behavior
- explicit section boundary
- no collateral changes

## Example 3 — Audit before editing

Use when the current design may already be close, but quality is uncertain.

Prompt:

> Audit spacing, typography hierarchy, and token consistency before editing. If structure is stable, propose refinement only.

What good output should include:
- audit-first behavior
- issue list before mutation
- distinction between refinement and restructuring

## Example 4 — Fallback-aware planning

Use when MCP is unavailable but useful work can still continue.

Prompt:

> MCP may be unavailable. If live editing is not ready, switch to fallback mode and produce a section-by-section execution plan instead of pretending to edit.

What good output should include:
- explicit fallback declaration
- no fake live-edit claims
- usable next-step plan

## Example 5 — Controlled refinement

Use when structure is already approved.

Prompt:

> The skeleton is already approved. Refine spacing, alignment, emphasis hierarchy, and consistency only. Do not change information architecture.

What good output should include:
- refinement-only scope
- preserved structure
- visual consistency focus
