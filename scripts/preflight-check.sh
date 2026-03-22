#!/usr/bin/env bash
set -euo pipefail

found=0
printf '== OpenPencil MCP Preflight ==\n'

if command -v openpencil-mcp >/dev/null 2>&1; then
  printf '[OK] openpencil-mcp found: %s\n' "$(command -v openpencil-mcp)"
  found=1
else
  printf '[WARN] openpencil-mcp not found in PATH\n'
fi

printf '\n== Common MCP config paths ==\n'
paths=(
  "$HOME/.claude/settings.json"
  "$HOME/.cursor/mcp.json"
  "$HOME/.cursor/settings.json"
  "$HOME/.config/Cursor/User/mcp.json"
  "$HOME/.config/Cursor/User/settings.json"
  "$HOME/.config/Windsurf/User/settings.json"
  "$HOME/.config/Windsurf/User/mcp.json"
)

for p in "${paths[@]}"; do
  if [[ -f "$p" ]]; then
    printf '[FOUND] %s\n' "$p"
  fi
done

printf '\n== Readiness Summary ==\n'
if [[ "$found" -eq 1 ]]; then
  printf 'Mode readiness: MCP binary present. Next: verify client config and confirm Pencil/OpenPencil is running if required.\n'
else
  printf 'Mode readiness: MCP binary missing. Next: install/configure openpencil-mcp or switch to fallback mode.\n'
fi
