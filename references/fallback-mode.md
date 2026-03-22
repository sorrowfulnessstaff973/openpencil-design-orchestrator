# Fallback Mode

Use fallback mode when MCP is unavailable, unstable, or inappropriate for the task.

## When to Switch

Switch from MCP-first to fallback when:

- the MCP server is missing or cannot connect
- Pencil/OpenPencil is not available locally
- repeated read/write attempts fail
- the user only needs planning, review, or prompt design rather than live mutation

## Fallback Levels

### Level 1 - Read-Only Planning

Use when:
- the user wants architecture, prompt design, or workflow guidance

Do:
- produce the phase plan
- produce prompt scaffolds
- identify likely pages/sections/components
- stop short of claiming any live mutation happened

### Level 2 - File-Level Guidance

Use when:
- MCP is down but the file format/path is available

Do:
- inspect file layout if practical
- suggest minimal patch strategy
- keep changes bounded and explain assumptions clearly

Do not:
- pretend the result is equivalent to MCP-native editing

### Level 3 - Community/Experimental JSON Patch Workflow

Use only with caution.

A public third-party example shows a non-MCP `.pen` JSON workflow. Treat it as fallback inspiration, not a default or guaranteed-compatible path.

Rules:
- label it as non-primary
- keep changes minimal
- preserve backups/checkpoints
- avoid claiming official support unless the user provides supporting evidence

## Fallback Output Format

When in fallback mode, always say:

1. why MCP mode is unavailable
2. which fallback level is active
3. what assumptions are being made
4. what the user should verify before applying changes

## Do Not Do In Fallback

- do not claim live edits succeeded
- do not silently invent node IDs or page trees
- do not overfit to unofficial community workflows without warning
