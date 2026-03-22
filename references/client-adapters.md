# Client Adapters

Use this file when the user mentions a specific MCP client or coding agent.

## Shared Baseline

Public docs indicate a common MCP config pattern:

```json
{
  "mcpServers": {
    "open-pencil": {
      "command": "openpencil-mcp"
    }
  }
}
```

Use `stdio` for local interactive clients. Use `HTTP` for controlled automation or remote flows.

## Claude Code

Typical pattern:

- ensure Pencil/OpenPencil is already running if the MCP server depends on the desktop app
- add the MCP entry using `openpencil-mcp`
- verify the server is visible in the Claude MCP tool list
- start with read-only inspection before mutation

Use when:

- iterating live with a local design file
- doing multi-step section edits
- refining an already-structured design

## Codex

Public docs mention a verification flow:

1. run Pencil first
2. open Codex
3. run `/mcp`
4. confirm Pencil appears

Recommended usage:

- start with planning or structure inspection
- avoid giant monolithic prompts
- keep phases explicit inside the prompt

## Cursor

Typical pattern:

- configure MCP in Cursor’s MCP/tool settings
- verify Pencil appears in the tools panel
- test read access first

Watch for:

- tools panel not showing the server
- plan/tool restrictions
- prompt box or extension visibility issues

## Windsurf

Treat Windsurf similarly to other MCP-aware IDE clients:

- add the `openpencil-mcp` server
- verify the tool is visible before issuing mutations
- prefer the same staged workflow used in Claude Code / Cursor

## HTTP Transport Clients / Automation

Use HTTP only when the environment benefits from remote or scripted access.

Recommended defaults:

- bind to localhost unless explicitly needed otherwise
- keep `eval` disabled
- constrain root path
- use auth token if supported
- treat HTTP as lower-trust than local `stdio`

## Client-Specific Failure Signals

Common public failure signals include:

- server not appearing in the tool list
- extension connected but prompt editor absent
- login/auth mismatch messages
- permission or plan restrictions in the client UI

When these appear:

1. verify Pencil/OpenPencil is running
2. verify `openpencil-mcp` exists in PATH
3. verify the MCP config path and JSON syntax
4. retry read-only access before write actions
