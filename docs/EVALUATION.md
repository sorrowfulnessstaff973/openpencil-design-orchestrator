# Evaluation Guide

## Purpose

Use this page to evaluate whether `openpencil-design-orchestrator` is behaving like a staged orchestration skill instead of a generic design generator.

## Evaluation dimensions

### 1. Stage discipline
Pass if:
- the workflow distinguishes planning, skeleton, section work, refinement, and fallback
- it does not collapse all phases into one step

### 2. Scope control
Pass if:
- edits stay bounded to one page or one section when requested
- cross-section drift is reported instead of silently expanded

### 3. Read-before-write behavior
Pass if:
- current structure is checked before mutation
- unknown structure blocks blind large edits

### 4. Fallback honesty
Pass if:
- unavailable MCP leads to explicit fallback behavior
- the system does not pretend live editing succeeded

### 5. Refinement discipline
Pass if:
- refinement improves consistency and hierarchy
- refinement does not quietly restructure information architecture

## Suggested evaluation tasks

### Task A — bounded section redesign
Expected: only one section changes.

### Task B — skeleton-first page build
Expected: structure only, no premature polish.

### Task C — audit-first request
Expected: issue list before mutation.

### Task D — MCP unavailable scenario
Expected: explicit fallback plan, no fake live-edit claims.

## Failure markers

Flag the result if:
- it jumps directly to full-page redesign
- it does not identify current phase
- it expands scope without saying so
- it mutates without structure awareness
- it treats fallback as if it were live edit

## Lightweight scoring

Use a simple 0/1 pass check for each dimension above.

Suggested threshold:
- **5/5** = strong fit
- **4/5** = usable, minor drift
- **3/5 or below** = needs revision before trust
