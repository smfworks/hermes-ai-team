# Phase 3 Checklist — Second Agent (Profiles, Roles, Models)

**Reference:** [`docs/03-phase-3-second-agent.md`](../docs/03-phase-3-second-agent.md)

- [ ] `hermes profile list` shows the `default`/first agent plus ≥1 additional profile
- [ ] Each additional profile has its own SOUL.md, distinct from the template and from
      other profiles (names, roles, lanes differ)
- [ ] Lanes do not collide: for any task type, exactly one profile owns it (or ownership
      is explicit)
- [ ] Model pins are intentional: `hermes -p <name> config get model.default` returns a
      deliberate choice, not an accident
- [ ] Profiles share the token pool (no forked credentials that expire independently)
- [ ] (Desktop) Bots tab shows the new agent with a face, title, and description
- [ ] `hermes -p <second> chat -q "What are your current priorities?"` returns
      role-appropriate behavior (not identical to the first agent)
- [ ] Gateways run persistently for any profile expected to receive scheduled/kanban work
      (`systemctl --user status hermes-gateway@<name>` active)

**Verification output to capture:** `hermes profile list`, per-profile SOUL excerpts
(redacted), one role-appropriate exchange per agent.

**Done when:** two or more distinct specialists exist and answer from their roles.
