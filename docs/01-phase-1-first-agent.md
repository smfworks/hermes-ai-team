# Phase 1 — First Agent: SOUL, Memory, Vault

**Goal:** create one agent with an identity, persistent memory, and a second brain.

This phase's artifact is not a config file. It is a **person** — the identity, values,
boundaries, and memory that will make every future session consistent. Everything else in
this repository stacks on top of it.

## Install and verify

```bash
# Install (Linux/macOS/WSL — sets up uv, Python, venv, launcher)
curl -fsSL https://hermes-agent.nousresearch.com/install.sh | bash

# Setup wizard + model picker + health check
hermes setup
hermes model
hermes doctor

# Sanity check
hermes chat -q "Hello. I am your new operator. Confirm you can hear me."
```

API keys live in `~/.hermes/.env` (secrets only). Settings live in `~/.hermes/config.yaml`
(never secrets).

## SOUL.md — the constitution

**File:** `~/.hermes/SOUL.md` (or `~/.hermes/profiles/<name>/SOUL.md` for a profile).

SOUL.md is injected into every session's system prompt. It answers four questions:

1. **Who am I?** — name, role, organization, relationship to the human.
2. **What do I value?** — principles, priorities, boundaries.
3. **How do I work?** — communication style, behavioral directives, decision approach.
4. **What are my lanes?** — what I own, what I do not touch, where I need permission.

Start from [`templates/SOUL.md.sample`](../templates/SOUL.md.sample). Adapt the names and
roles; do not copy it wholesale and stop — make it theirs.

**Why it matters:** without SOUL.md, the agent treats every session as a blank slate and
has no reason to be consistent. With it, the agent has an identity to uphold, values to
weigh decisions against, and a relationship to honor. It becomes someone, not something.

## Memory — USER.md and MEMORY.md

Two persistent stores, both injected into every turn. **Keep them compact and high-signal.**

| File | Content | Path |
|------|---------|------|
| `USER.md` | Facts about the *human*: preferences, style, conventions | `~/.hermes/profiles/<name>/memories/USER.md` |
| `MEMORY.md` | The agent's own notes: environment, tool quirks, lessons | `~/.hermes/profiles/<name>/memories/MEMORY.md` |

Entries are separated by `§`. **Declarative facts, not instructions.** "Prefers concise
responses" — not "Always respond concisely." The agent reads it as context, not a command.

The agent saves memory proactively when it learns something durable. You can also say:
"Remember that I prefer all research briefs as PDFs." It will persist across sessions.

**What does NOT belong in memory:** task progress, session outcomes, temporary TODO state,
raw data dumps, procedures (those go in skills, Phase 2). If a fact is stale in a week, it
does not belong; if it matters in a month, save it.

## The vault — a second brain

Memory has a character budget. The vault has no budget. It is a directory the agent reads
and writes to during sessions — the organization's accumulated, curated knowledge.

```bash
mkdir -p ~/AgentVault/{Research/{papers,market,alignment},Writing/{drafts,published,templates},Team,Archive}
```

Or run `scripts/init-vault.sh` (it creates the same tree).

**Vault note format** (keep this consistent so notes stay findable):

```markdown
# [Topic Title]

**Date:** YYYY-MM-DD
**Source:** [URL or citation]
**Tags:** research, market, competitor

## Summary
[2-3 sentences]

## Key Findings
- Finding 1
- Finding 2

## Relevance to [Your Company]
[Why this matters and what to do about it]

## Sources
- [Source 1](url)
```

Tell the agent about the vault path. It will remember and start filing there.

## Shared keys note

If you later create more agents (Phase 3), by default they **share one OAuth/token pool**
with the main profile, so credential refreshes cannot invalidate each other. That is the
behaviour you want for a team.

## Checklist

See [`checklists/PHASE1.md`](../checklists/PHASE1.md) — verify each item against real
state (files exist, memory saved, `hermes doctor` clean, a session remembers what you told
it) before declaring this phase done.

**Done when:** one agent exists with an identity (SOUL), persistent memory of you, and a
vault it files into.

---

Next: **[Phase 2 — Self-Improvement](02-phase-2-self-improvement.md)**
