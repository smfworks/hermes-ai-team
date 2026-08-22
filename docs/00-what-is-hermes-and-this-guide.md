# What Is Hermes Agent — and Why This Guide Exists

**Goal:** form a clear mental model in a few minutes before you touch the phases.

## What Hermes Agent is

Hermes Agent is a local, tool-using AI assistant from [Nous Research](https://hermes-agent.nousresearch.com/docs).
It runs on your machine (CLI, Desktop, and messaging platforms), keeps a persistent
identity (`SOUL.md`), bounded memory (`USER.md` / `MEMORY.md`), skills it can write
from experience, scheduled jobs (cron), a shared kanban board, and **Bot Mode** —
named profiles that show up as colleagues in the Desktop app, including group chats.

Official docs always win on commands and flags:
[docs index (`llms.txt`)](https://hermes-agent.nousresearch.com/docs/llms.txt).

## Why this repo exists

The official docs teach you how to install Hermes and use its features. They do not
teach you how to go from **one assistant** to a **team of colleagues** — identity,
a compounding vault, self-improving skills, nightly research, a coordinator, rituals,
and Desktop pods.

That missing layer is this repository. It is written so a human first-timer can
succeed, and so a Hermes profile pointed at the repo can implement the phases.

## The colleague philosophy in one paragraph

You are building colleagues, not tools. A tool is picked up and put down. A colleague
has identity, remembers, grows, has opinions, takes initiative, and pushes back when
a better path exists. SOUL files, memory, skills, kanban, cron, and group chats are
the infrastructure. The infrastructure without the philosophy produces sophisticated
tools. The philosophy without the infrastructure produces wishful thinking. This repo
builds both, in lockstep. Read [`00-philosophy.md`](00-philosophy.md) before you
scale past one agent.

## How to use this repo

### If you are a human

1. Read this page, then [`00-philosophy.md`](00-philosophy.md).
2. Follow the [Minimal Viable Team](minimal-viable-team.md) path — under 2 hours.
3. Walk phases 1–6 as the team grows. Each phase has a checklist in `checklists/`.
4. When something breaks, start at [`faq-and-troubleshooting.md`](faq-and-troubleshooting.md).

### If you are a Hermes agent

1. Read [`../AGENTS.md`](../AGENTS.md) — it is the operating agreement.
2. Read the phase doc for whatever phase you are in. Do not jump to detached commands.
3. Verify against the matching checklist. If you did not run the check, do not mark it done.
4. Templates in `templates/` are samples. Filled references live in [`../examples/`](../examples/).

## Compatibility

> Designed and verified against Hermes Agent with the profile system and Desktop Bot
> Mode as of August 2026. The official Hermes documentation is authoritative. If a
> command or behavior here conflicts with the live official docs, the official docs
> win — update this repo and log the change.

## Where to go next

| You are… | Start here |
|----------|------------|
| Brand new | [`minimal-viable-team.md`](minimal-viable-team.md) |
| Already have one agent | [Phase 2](02-phase-2-self-improvement.md) |
| Running a team | [Phase 4](04-phase-4-team-coordination.md) |
| Stuck | [`faq-and-troubleshooting.md`](faq-and-troubleshooting.md) |

---

Next: **[Phase 0 — Philosophy](00-philosophy.md)** or the **[Minimal Viable Team](minimal-viable-team.md)**.
