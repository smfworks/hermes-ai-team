# Phase 4 — Team Coordination: Kanban, Chief of Staff, Dispatch

**Goal:** give the team a durable, shared way to assign, track, block, and complete work —
and a coordinator that keeps it all moving.

Chat is ephemeral. Kanban is durable SQLite. All profiles see the board regardless of
connection state, tasks carry status/assignee/comments/deadlines, and the dispatcher can
automatically spawn an assigned agent to do the work.

## Set up the board

```bash
hermes kanban init --board team     # idempotent

# Create / list / show / comment / assign / complete / block
hermes kanban create "Research Q3 market developments" \
  --board team --assignee atlas \
  --body "Scan 5 competitors for launches, funding, personnel changes since June.
Write findings to ~/AgentVault/Research/market/q3-landscape.md"

hermes kanban list --board team
hermes kanban show <task_id> --board team
hermes kanban comment <task_id> --board team --author liam --body "..."
hermes kanban assign <task_id> --board team --assignee atlas
hermes kanban complete <task_id> --board team
hermes kanban block <task_id> --board team --reason "Waiting on data access"
hermes kanban link <task_a> <task_b>     # dependencies
```

There is a native **Kanban plugin for Hermes Desktop** — enable it in Settings → Plugins,
and the board renders as columns in the sidebar with a palette hotkey for new tasks. The
backend is the same board (`hermes kanban list` shows the same tasks).

## The dispatcher — automatic task execution

```bash
hermes config set kanban.dispatch_in_gateway true   # gateway-embedded dispatcher
```

The dispatcher reclaims stale claims, promotes ready tasks, atomically claims work (no
double-assignment), spawns the assigned profile in an isolated workspace, and auto-blocks
after consecutive failures. It runs inside the gateway by default — do not also run a
standalone daemon (they race for claims).

## Task lifecycle

```
created → ready → claimed → [done | blocked]
                              ↑        ↓
                              └─ unblock ┘
```

1. **created** — exists on the board
2. **ready** — can be picked up
3. **claimed** — an agent has been spawned
4. **done** — completed to acceptance
5. **blocked** — waiting on input, dependency, or a decision

## Best practices

- **One board for the team.** Cross-agent visibility is the point.
- **Acceptance criteria in the task body.** "Done" must be checkable.
- **Blockers name what's needed and from whom.** "Blocked" alone is useless.
- **Comments coordinate; they are not status pings.** No "I'm here". Silence is healthy.
- **Link dependencies** so ordering is explicit.

## The chief of staff pattern

A dedicated coordinator agent that does not execute — it makes sure the right work reaches
the right agent on time with the right context:

- Monitors the board for unassigned, stale, and blocked tasks.
- Runs the daily check-in and weekly alignment (Phase 5).
- Surfaces blockers to the human with options, not noise.
- Tracks deliverables and reminds the responsible agent.

**`templates/SOUL-chief-of-staff.md.sample`** is a full coordinator SOUL. Create the
profile, give it that SOUL, and let it own coordination. Because a Bot is a profile, you
can also seat the chief of staff as a Bot in the Desktop Bots tab and drop it into rooms.

Its standing jobs are cron jobs (Phase 2 mechanics):

```bash
hermes cron create "0 7 * * 1-6" --name "Morning Board Review" \
  --profile chief-of-staff --prompt \
  "Review the team kanban board. List: tasks blocked >24h, tasks with no assignee,
   tasks past deadline. Deliver a summary."

hermes cron create "0 8 * * 1" --name "Weekly Alignment" \
  --profile chief-of-staff --prompt \
  "Review each agent's SOUL, STATE, MEMORY for consistency. Surface judgment gaps,
   stale assumptions, priority conflicts. Write to the alignment dir, summarize to chat."
```

The chief of staff is the connective tissue. Without it each agent works in isolation;
with it the team has shared awareness.

## Checklist

See [`checklists/PHASE4.md`](../checklists/PHASE4.md).

**Done when:** a shared board exists with cross-agent tasks flowing through it, the
dispatcher can spawn an assigned agent, and a chief-of-staff agent owns ongoing
coordination.

---

Next: **[Phase 5 — Autonomy & Rituals](05-phase-5-autonomy-and-rituals.md)**
