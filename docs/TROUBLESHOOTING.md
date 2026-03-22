# Troubleshooting

## Scope

This page is for diagnosing common failure patterns when using `openpencil-design-orchestrator`.

It is not a generic MCP debugging manual. It focuses on failures that break the skill's intended staged, bounded workflow.

## Fast triage

When a result looks wrong, classify the failure first:

1. **Environment failure**
   - Pencil / OpenPencil is not running
   - MCP is unavailable or unstable
   - the wrong transport mode is assumed

2. **Workflow failure**
   - the task skipped planning
   - the task jumped directly into broad edits
   - the task did not re-read structure before editing

3. **Scope failure**
   - the request was too broad
   - the edit crossed multiple sections without control
   - the output drifted beyond the approved skeleton

4. **Fallback failure**
   - MCP was unavailable, but the flow behaved as if live editing still worked
   - fallback mode was needed but not acknowledged explicitly

## Common symptoms and likely causes

### Symptom: it tries to redesign the whole page immediately
Likely causes:
- the request was framed as unconstrained generation
- skeleton phase was skipped
- section scope was never established

Check:
1. Did the prompt ask for a full product/page redesign?
2. Was the task narrowed to one page or one section?
3. Did planning happen before mutation?

### Symptom: it edits multiple sections even though only one was intended
Likely causes:
- task scope was ambiguous
- the section boundary was not restated before editing
- refinement drifted into restructuring

Check:
1. Did the prompt explicitly say “only this section”?
2. Was the section named clearly?
3. Did the workflow report nodes touched before continuing?

### Symptom: it acts as if MCP is available, but nothing is actually connected
Likely causes:
- preflight was skipped
- the environment was assumed rather than checked
- fallback mode was required but not declared

Check:
1. Run `scripts/preflight-check.sh`
2. Verify whether Pencil/OpenPencil is actually running
3. Verify whether the task should proceed in fallback mode instead

### Symptom: it gives polished prose but not a controlled execution plan
Likely causes:
- prompt wording biased toward idea generation instead of orchestration
- planning output format was not constrained
- the task was treated as generic design ideation

Check:
1. Did the prompt ask for plan / skeleton / section / refine explicitly?
2. Did the output identify current mode and current phase?
3. Did it state exact scope before proposing changes?

### Symptom: refinement changes information architecture
Likely causes:
- refinement phase was used too early
- skeleton was not treated as approved baseline
- visual polish and restructuring got mixed together

Check:
1. Was skeleton approved first?
2. Is refinement touching structure instead of spacing / hierarchy / consistency?
3. Should the task be sent back to planning instead?

## Minimum recovery sequence

When things drift, use this reset sequence:

1. stop broad edits
2. restate current mode: MCP-first / fallback
3. restate current phase
4. narrow scope to one page or one section
5. re-read the current structure
6. continue with the next bounded step only

## When to switch to fallback mode

Switch to fallback mode when:
- MCP connectivity is absent
- Pencil/OpenPencil is unavailable
- the environment cannot confirm live-edit readiness
- the workflow can still produce useful planning, structure, or audit output without pretending to mutate live state

## When to stop instead of improvising

Stop and report instead of continuing when:
- the current structure is unknown
- the intended section cannot be identified reliably
- the request conflicts with previously approved structure
- a “small refinement” would actually become a structural rewrite

## Related files

- `INSTALL.md`
- `../references/risk-matrix.md`
- `../references/fallback-mode.md`
- `../references/workflow-sequence.md`
