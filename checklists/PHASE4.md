# Phase 4 Checklist — Team Coordination (Kanban, Chief of Staff, Dispatch)

**Reference:** [`docs/04-phase-4-team-coordination.md`](../docs/04-phase-4-team-coordination.md)

- [ ] `hermes kanban init --board <team>` succeeded (idempotent, safe to re-run)
- [ ] A real task was created, assigned to a specific profile, and shows correct
      assignee + status in `hermes kanban show <id>`
- [ ] A comment with attribution was added and persists
- [ ] Task lifecycle round-trips: ready → claimed → done (and separately: block →
      unblock, with a reason naming what's needed and from whom)
- [ ] Dispatcher enabled: `hermes config get kanban.dispatch_in_gateway` → true; no
      standalone `kanban daemon` running that would race claims
- [ ] A dispatch was observed: create a task assigned to a working profile, and confirm
      the profile actually ran and completed it (real run, not assumed)
- [ ] Chief-of-staff profile exists with a coordination-only SOUL (does not drift into
      doing the work itself)
- [ ] Chief-of-staff cron jobs exist (board review 07:00 Mon–Sat, weekly alignment Mon)
- [ ] Acceptance criteria are present in task bodies ("done" is checkable)

**Verification output to capture:** `hermes kanban list --board <team>` showing the
lifecycle states, one observed dispatch completion, `hermes cron list` for the chief-of-
staff jobs.

**Done when:** work flows through the board across agents, dispatch works for real, and
the chief of staff owns coordination.
