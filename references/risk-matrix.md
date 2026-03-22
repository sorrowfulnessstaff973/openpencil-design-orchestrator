# Risk Matrix

Use this file to choose guardrails before or during Pencil/OpenPencil work.

## High-Risk Items

### 1. One-shot giant prompt

Signal:
- user asks for a whole app or full redesign in one pass

Risk:
- scope drift
- hidden structural changes
- hard-to-explain outputs
- poor rollbackability

Mitigation:
- split into planning -> skeleton -> section -> refine

## 2. Stale page tree or stale node references

Signal:
- writes fail after a page switch
- node references no longer behave as expected
- unexpected mutation targets

Risk:
- editing the wrong area
- silent corruption of structure

Mitigation:
- re-read page tree and target nodes before each mutation batch
- stop if the target node is missing or ambiguous

## 3. MCP transport instability

Signal:
- server disappears from the client
- intermittent read/write failures
- desktop app closes or hangs

Risk:
- partial mutations
- inconsistent state across tool/client boundaries

Mitigation:
- rerun preflight
- reduce batch size
- switch to fallback mode when instability persists

## 4. `eval` exposure

Signal:
- workflow depends on unrestricted command execution inside the MCP surface

Risk:
- elevated security exposure
- lower portability
- harder reviewability

Mitigation:
- avoid by default
- keep disabled for HTTP mode unless explicit approval and clear need exist

## 5. Cross-section drift

Signal:
- a prompt intended for one section starts modifying adjacent areas

Risk:
- collateral edits
- broken review loop

Mitigation:
- bind prompts to one section at a time
- require a changed-node summary after each batch

## Known Fixed Issues From Public Release Notes

Public release notes document fixes for:

- MCP crash from env access in CJS build
- Linux orphan process after app close
- blank page on page switch
- push-back loops after external updates
- missing page-aware operation support (`pageId`)

Treat these as historical failure classes worth guarding against even if fixed.

## Ongoing Open Risks

- desktop lifecycle dependence in local MCP flows
- configuration drift between clients
- false confidence from sparse public issue tracker signals
- over-reliance on creative prompts instead of structured prompts

## Safe Defaults

- MCP-first
- `stdio` for local interactive work
- `HTTP` for controlled automation
- `eval` off by default
- one page/section per mutation batch
- read before write
