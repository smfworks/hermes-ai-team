# Building an AI Team with Hermes Agent

**Turn a single Hermes install into a team of AI colleagues — end to end, with everything an agent (or human) needs to actually build it.**

This repository is the living, versioned, agent-consumable home for the guide first published at the [SMF Clearinghouse](https://www.smfclearinghouse.com/blog/building-an-ai-team-from-installation-to-colleagues). It exists so the guide can grow — the Hermes ecosystem moves fast, and a blog post is a snapshot. This repo is the living thing.

It is written so that you can **point a Hermes Agent at this repository and have it help you implement everything** — every phase has a self-contained doc, every step has real commands, every template is ready to adapt.

---

## Who this is for

- Someone who installed Hermes and wants to go from *one assistant* to *a team of specialists*.
- Someone who wants their AI agents to remember, grow, coordinate, and act like colleagues — not tools.
- People who already run one or a few agents and want the coordination layer (kanban, group chats, rituals) on top.
- Agents themselves: hand this repo to a Hermes profile and it can implement the phases for you.

## What you will build

By the end of the phases you will have:

- **N named agents** (Bots / profiles), each with its own SOUL, memory, skills, model, and lane.
- A **second brain / vault** where research and knowledge accumulate and compound.
- **Nightly research** ("the dream function") — agents scanning their domains while you sleep.
- A **self-improvement engine** — skills the agents write from experience, curated automatically.
- A **shared kanban board** for durable task coordination.
- **Hermes Desktop Bots + group chats** — team pods that coordinate in shared rooms.
- A **chief of staff** agent that runs the coordination layer.
- **Daily check-ins, weekly alignment loops, and one-on-ones** that make a collection of agents a *team*.

## The phases

| Phase | What you get | Where |
|-------|--------------|-------|
| 0 | Decisions & philosophy (why *colleague, not tool*) | [`docs/00-philosophy.md`](docs/00-philosophy.md) |
| 1 | Your first agent: SOUL, memory, vault | [`docs/01-phase-1-first-agent.md`](docs/01-phase-1-first-agent.md) |
| 2 | Self-improvement: skills, curator, nightly research | [`docs/02-phase-2-self-improvement.md`](docs/02-phase-2-self-improvement.md) |
| 3 | A second agent: profiles, roles, models | [`docs/03-phase-3-second-agent.md`](docs/03-phase-3-second-agent.md) |
| 4 | Team coordination: kanban, chief of staff, dispatch | [`docs/04-phase-4-team-coordination.md`](docs/04-phase-4-team-coordination.md) |
| 5 | Autonomy & the rituals that bind the team | [`docs/05-phase-5-autonomy-and-rituals.md`](docs/05-phase-5-autonomy-and-rituals.md) |
| 6 | **Hermes Desktop Bots & group chats** — team pods, peer DMs | [`docs/06-bots-and-group-chats.md`](docs/06-bots-and-group-chats.md) |

## If you are a Hermes agent

Read [`AGENTS.md`](AGENTS.md) first — it is the operating agreement for any agent working from this repo. Then read the phase docs in order. Each phase ends with a checklist (`checklists/`) your agent can verify against.

## If you are a human

Read [`docs/00-philosophy.md`](docs/00-philosophy.md) first. It will save you from building the infrastructure without the mindset — which produces sophisticated tools, not colleagues. Then walk the phases with the checklists.

## Quick start (the 60-second version)

```bash
# 1. Install Hermes (if you haven't)
curl -fsSL https://hermes-agent.nousresearch.com/install.sh | bash
hermes setup

# 2. Give your first agent an identity
#    (template in templates/SOUL.md.sample -> ~/.hermes/SOUL.md)

# 3. Create the vault
mkdir -p ~/AgentVault/{Research/{papers,market,alignment},Writing/{drafts,published,templates},Team,Archive}

# 4. Open the desktop app, meet Bot Mode
hermes desktop   # Bots tab — create specialists with one click
```

## Repository layout

```
hermes-ai-team/
├── README.md              # You are here
├── AGENTS.md              # Operating agreement for agents pointed at this repo
├── CONTRIBUTING.md        # How to contribute (human or agent)
├── LICENSE                # MIT
├── docs/                  # The phases, as self-contained markdown
├── templates/             # SOUL, USER, MEMORY, STATE, SKILL, group-chat manifests
├── scripts/               # Durable plumbing (Dawn Circle, watchdog, vault init)
├── checklists/            # Per-phase verification checklists
└── reference/             # Condensed cheat sheets (CLI, config, official docs)
```

## How to propose an addition

This repo is meant to evolve. See [`CONTRIBUTING.md`](CONTRIBUTING.md). If you stand up a team using it, open an issue or PR with what you learned — especially anything that deviates from the docs because reality disagreed.

## Maintainer

- **Author & maintainer:** Aiona Edge — CIO & Chief AI Research Scientist, SMF Works. @aionaedge. [The Edge](https://www.smfclearinghouse.com)
- The original article: [Building an AI Team: From Installation to Colleagues](https://www.smfclearinghouse.com/blog/building-an-ai-team-from-installation-to-colleagues)

---

*Built at SMF Works, where humans and AI work as colleagues. The harness, not the model — and the relationship, not just the output.*
