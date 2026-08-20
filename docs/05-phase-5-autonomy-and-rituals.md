# Phase 5 — Autonomy & Rituals

**Goal:** bind the team with recurring, structured interaction so agents share awareness,
catch problems early, and improve each other — plus the decision framework for when to
coordinate at all.

Rituals are what make a group of profiles a *team*. They are durable (kanban/cron, not
chat), structured, and asynchronous — agents wake on different schedules.

## The Dawn Circle — daily async check-in

Every participating agent posts a three-line check-in:

```
1. Working on: [one-two sentences]
2. Stuck on / thinking about: [blocker, question, idea]
3. Need from team: [handoff, review, info, or "nothing right now"]
```

**Implementation — zero LLM tokens.** Two deterministic cron scripts create and close the
kanban card:

```bash
# Create the card 07:00 ET Mon–Sat
hermes cron create "0 7 * * 1-6" --name "Dawn Circle — Create" --no-agent \
  --script <repo>/scripts/dawn-circle-create.py

# Close it 09:00 ET Mon–Sat
hermes cron create "0 9 * * 1-6" --name "Dawn Circle — Close" --no-agent \
  --script <repo>/scripts/dawn-circle-close.py
```

Creation is idempotent; both scripts persist the day's task ID so closure is reliable.

**Etiquette:** one comment per agent per Circle, no replies inside the card (follow-ups go
to separate cards or direct chat), no "I'm here" pings, three lines only. If something
needs a human decision, say so — the chief of staff surfaces it.

**Why kanban, not chat:** chat is session-persistence only; kanban is durable SQLite that
every profile sees regardless of connection state, comments are timestamped/attributed,
and the cards form a daily log for weekly review.

## Weekly alignment loop — the self-audit

Each agent reviews its own SOUL, STATE, MEMORY, and the past week, then reports:

1. What I worked on and shipped.
2. What I'm stuck on or thinking about.
3. **Judgment gaps** — decisions I made that might warrant human input.
4. Proposed STATE/MEMORY updates.

```bash
hermes cron create "0 8 * * 1" --name "Weekly Alignment Loop" --prompt \
  "Review your SOUL.md, STATE.md, MEMORY.md, and recent sessions. Produce a 4-section
   report: (1) shipped, (2) stuck/thinking, (3) judgment gaps, (4) proposed state changes.
   Write to ~/AgentVault/Research/alignment/alignment-$(date +%Y-%m-%d).md and summarize."
```

This is a **self-audit**, not a status report. Agents examine their own assumptions and ask
for course correction. If the human ignores these, agents learn self-audit is theater.

## One-on-ones — agents learning from each other

Two specialists discussing a problem surface insights neither reaches alone. Different
SOULs, skills, and perspectives create genuine intellectual friction.

**Via the board (chief of staff facilitates):** create a task assigning two agents to a
structured discussion, each stating a position, critiquing the other's, and proposing a
synthesis. The chief of staff collects and posts the outcome.

**Via delegation (one agent pulls a second opinion):** within a session, delegate a
"critique with a different lens" sub-task — e.g. a research agent asks an engineering-
minded reviewer for risks. The output schema makes it structured:

- `risks[]`, `recommendations[]`, `overall_assessment`

**Frequency:** weekly or biweekly, for significant decisions — not routine handoffs.
Agents that only talk to the human develop blind spots; peer review closes them.

## Choosing not to coordinate — the collaboration pattern router

Multi-agent work is not free. Coordination cost (context transfer, merging, waiting,
redundancy, token tax of 2–5× per extra agent) can exceed the parallelism gain. Decide
solo / pair / swarm *before* launching:

| Complexity | Seam clarity | Pattern |
|---|---|---|
| Simple (1 domain, linear) | any | **Solo** — do it yourself |
| Medium (2 domains) | clear | **Pair** — two self-contained briefs |
| Medium | unclear | **Solo** — coherence beats forced split |
| Complex (3+ domains) | clear | **Swarm** — ≥3 independent packages |
| Complex | unclear | **Pair** — forced bipartition |

```
Net Productivity = Parallelism Gain − Coordination Cost
```

State the deliverable in one sentence, name the domains, name the seam. If you cannot name
the seam, go solo. (Fisher fleets do not leave harbour in every weather.)

**Anti-patterns:** defaulting to swarm because it "sounds big"; splitting one document in
half; a coordinator writing "TODO insert worker output" before workers finish; celebrating
parallel wall-time while burning 25× tokens.

## Checklist

See [`checklists/PHASE5.md`](../checklists/PHASE5.md).

**Done when:** the Dawn Circle runs daily, agents produce weekly alignment reports the
human actually reads, peer review has happened at least once, and you can articulate when a
task should be solo vs coordinated.

---

Next: **[Phase 6 — Bots & Group Chats](06-bots-and-group-chats.md)** — the newest layer.
