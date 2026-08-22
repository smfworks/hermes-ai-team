# Phase 3 — Second Agent: Profiles, Roles, Models

**Goal:** add a second, fully independent agent with a distinct identity and lane.

Each agent is a **profile** — its own config, sessions, skills, memory, and SOUL. They are
not interchangeable. They are specialists.

## Creating profiles

```bash
# List / create / switch
hermes profile list
hermes profile create <name> --clone      # copy config+skills from default
hermes profile create <name> --clone-from <other>
hermes profile use <name>

# One-shot as a specific profile
hermes -p <name> chat -q "What are your current priorities?"
```

**Profile layout** (same tree as default, under `~/.hermes/profiles/<name>/`):

```
<name>/
├── SOUL.md
├── config.yaml
├── memories/{USER.md, MEMORY.md}
├── STATE.md
└── skills/
```

## Assigning roles and models

Different agents can (and should) run different models by role — reasoning model for
research, a writing model for content, a coding model for code:

```bash
hermes -p <name1> config set model.default glm-5.2
hermes -p <name1> config set model.provider ollama-cloud

hermes -p <name2> config set model.default claude-sonnet-4.6
hermes -p <name2> config set model.provider anthropic
```

**An example role split** (adapt to your reality):

| Profile | Role | Model focus |
|---|---|---|
| atlas | Research analyst | Reasoning |
| quill | Content strategist | Writing |
| forge | Engineer | Code |
| ops | Operations | Efficiency / monitoring |

Each gets its own SOUL (start from the sample, make it theirs), its own memory, its own
skills. Write lanes so they do not collide: research owns sources, content owns voice,
engineer owns code, ops owns process.

## The desktop path — Hermes Desktop Bots

If you are using the **Hermes Desktop app**, you do not need the CLI-only flow for this. The
**Bots tab** creates specialists from a UI: New Agent → Name, Title, Description — and the
Bot exists, introduces itself, and gets a canonical Bot Chat. The advanced panel exposes
clone source, model pin, SOUL, per-skill/per-toolset/per-MCP enablement, and shared keys.

Because a Bot **is** a profile, everything you do in the UI has a CLI equivalent:

| In Bot Mode | From a shell |
|---|---|
| Chat with a Bot | `hermes -p <bot> chat` |
| A Bot's files, skills, memory | `~/.hermes/profiles/<bot>/` |
| Routines | `hermes cron list` (jobs named `[bot:<name>] …`) |
| Create / inspect profiles | `hermes profile create`, `hermes profile list` |

The full group-chat / bot-to-bot layer is its own phase: **[Phase 6 — Bots & Group Chats](06-bots-and-group-chats.md)**.

## Running profiles as background services

For agents to receive scheduled/kanban work and be available across contexts, run their
gateways as persistent services. On Linux, use user-level systemd (see
[`scripts/hermes-gateway@.service`](../scripts/hermes-gateway@.service) sample) — enable
lingering so they start on boot:

```bash
loginctl enable-linger <username>
systemctl --user enable hermes-gateway@<name>
systemctl --user start hermes-gateway@<name>
```

## Shared credentials note

New profiles share the main profile's token pool by default (credential refreshes cannot
invalidate each other). This matters for a multi-agent team — you want one pool, not N
forked credentials that can expire independently.

## Checklist

See [`checklists/PHASE3.md`](../checklists/PHASE3.md).

**Done when:** two or more agents exist, each with a distinct SOUL, lane, and (optionally)
model; you can address either by name and get different, role-appropriate behaviour.

## What success looks like

You ask Atlas and Forge the same question ("What should we do about this paper?").
Atlas offers a vault note and a relevance score. Forge talks about whether the
harness can run the implied workload — and refuses to invent a research
conclusion. They do not sound like two copies of one assistant.

**Expected outputs to capture:**
- `hermes profile list` showing at least two profiles
- Two `hermes -p <name> chat -q "State your name and lane."` replies that differ
- Each profile has its own `SOUL.md` that is not a verbatim template

---

Next: **[Phase 4 — Team Coordination](04-phase-4-team-coordination.md)**
