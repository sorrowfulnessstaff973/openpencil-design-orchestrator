# Contributing

## Scope

Contributions should preserve the repository's core behavior:

- staged workflow
- MCP-first preference
- bounded edits
- read-before-write discipline
- safe fallback

## Good contribution directions

Examples of useful changes:
- clearer installation and verification guidance
- better troubleshooting for bounded workflow failures
- tighter examples that reinforce scope control
- evaluation materials that check real staged behavior
- scripts that improve verification or packaging without widening execution risk

## Avoid

Do not propose contributions that:
- turn the skill into unconstrained one-shot generation
- remove preflight or planning discipline
- assume MCP is always available
- blur fallback mode into fake live-edit claims
- widen refinement into structural rewrite by default

## Contribution rule of thumb

If a change makes the workflow:
- broader,
- more implicit,
- harder to verify,
- or less honest about fallback,

then it is probably a bad fit.
