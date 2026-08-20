# Phase 1 Checklist — First Agent (SOUL, Memory, Vault)

**Reference:** [`docs/01-phase-1-first-agent.md`](../docs/01-phase-1-first-agent.md)

An agent verifying this phase must check every box against real state — not assume it.

- [ ] `hermes doctor` completes cleanly (no missing required dependencies)
- [ ] `hermes chat -q "..."` returns a response
- [ ] `~/.hermes/SOUL.md` (or profile SOUL) exists, is not a verbatim template copy,
      and contains: name, role, values, behavioral directives, lanes
- [ ] `memories/USER.md` exists with ≥3 declarative facts about the operator
- [ ] `memories/MEMORY.md` exists with ≥1 environment fact or tool quirk
- [ ] Memory round-trips: tell the agent a new fact, start a new session, confirm it
      recalls the fact
- [ ] Vault tree exists (`Research/{papers,market,alignment}`, `Writing/...`, `Team`,
      `Archive`) — verify with `find` or `ls`
- [ ] The agent knows the vault path and files one test note there on request

**Verification output to capture:** `hermes doctor` result, `ls` of SOUL/memory paths,
`find` of vault tree, and the recalled-fact session exchange.

**Done when:** all boxes checked against real state.
