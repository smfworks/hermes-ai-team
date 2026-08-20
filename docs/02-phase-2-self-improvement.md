# Phase 2 — Self-Improvement: Skills, Curator, Nightly Research

**Goal:** make the agent learn from experience and work while you sleep.

This is where the agent stops being reactive and becomes genuinely self-improving. Two
mechanisms: **skills** (reusable procedures the agent writes from experience) and **cron**
(autonomous scheduled work including the "dream function" of nightly research).

## Skills — the self-improvement engine

A skill is a markdown file with YAML frontmatter in a folder under
`~/.hermes/profiles/<name>/skills/`. It is a proven procedure the agent follows when a
matching task comes up — instead of figuring it out from scratch each time.

**`templates/SKILL.md.sample`** shows the full structure. Key sections:

```markdown
---
name: <lowercase-hyphenated-name>
description: "When to use this — one or two sentences."
version: 1.0.0
---

# <Name>

## When to use
- ...

## Procedure
1. Step one (real commands)
2. Step two

## Pitfalls
- What commonly goes wrong

## Verification
- [ ] Checkable outcome
```

**How skills are created:**

1. **After a difficult task** — the agent recognizes a complex workflow it just completed
   and offers to save it. Accept.
2. **On request** — "Save that procedure as a skill called 'competitor-analysis'."

**The curator** does background skill maintenance — tracks usage, marks idle skills stale,
and archives stale ones (never deletes; always backs up first). Pinned skills are exempt.

```bash
hermes curator status    # usage stats
hermes curator run       # trigger a sweep
hermes curator pin <name> # protect a skill from archival
```

Enable the curator: `hermes config set curator.enabled true`.

## Cron — the dream function (nightly research)

Agents do not only research when asked. They research on a schedule, while you sleep, and
deliver findings by morning. This is the pattern that transforms a reactive assistant into
a proactive colleague.

```bash
# Nightly research at 3 AM
hermes cron create "0 3 * * *" \
  --name "Nightly Research — Market Scan" \
  --prompt "Scan [the sources] for new developments since yesterday. For each new finding,
write a structured note to ~/AgentVault/Research/market/ (date, source, summary, relevance).
If nothing changed, write a one-line 'no change' note."
```

### The `script` option — collect data first, cheaply

A cron job can run a script *before* the agent, and the script's output is injected as
context. The script does the free mechanical collection (e.g. fetch feeds via `requests`);
the agent does the analysis. This is the most token-efficient research pattern.

See [`scripts/market-scan.py`](../scripts/market-scan.py) for an example.

```bash
hermes cron create "0 3 * * *" \
  --name "Market Scan" \
  --script ~/path/to/scripts/market-scan.py \
  --prompt "Analyze the articles above. Write relevant ones to ~/AgentVault/Research/market/.
Flag anything needing immediate attention."
```

### The `no_agent` option — zero-token watchdogs

For pure monitoring that needs no reasoning, the script IS the job; empty stdout means
silence (nothing sent), non-zero exit sends an alert:

```bash
hermes cron create "*/15 * * * *" \
  --name "Uptime Check" \
  --no-agent \
  --script ~/path/to/scripts/uptime-check.py
```

### Cron management

```bash
hermes cron list | pause <id> | resume <id> | run <id> | edit <id> | remove <id>
```

**Invariants:** 3-minute hard interrupt per run; `.tick.lock` prevents duplicate ticks;
cron sessions skip memory injection by default (keeps them lightweight); deliveries are
framed with a header/footer.

## Assigning research domains

| Agent role | Research domain |
|---|---|
| Research analyst | New papers, market developments, competitor moves |
| Content strategist | Trending topics, content gaps, audience interests |
| Engineer | New libraries, security advisories, tool updates |
| Operations | Regulatory changes, process improvements, vendor news |

The vault compounds: after weeks you have a searchable knowledge base; after months, a
genuine institutional memory maintained by your AI team.

## Checklist

See [`checklists/PHASE2.md`](../checklists/PHASE2.md).

**Done when:** the agent has saved at least one skill from real work, the curator is
enabled, and one nightly research cron is running and producing vault notes you can read.

---

Next: **[Phase 3 — Second Agent](03-phase-3-second-agent.md)**
