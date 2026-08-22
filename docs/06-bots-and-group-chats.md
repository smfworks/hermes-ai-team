# Phase 6 — Hermes Desktop Bots & Group Chats

**Goal:** give the team its most human coordination surface — named Bots with faces and
routines, seated together in **group chats** organized by area of focus, with bot-to-bot
messaging and cross-machine peers.

Bot Mode is a game-changer for exactly the reason that matters here: it turns your roster
of profiles into a *team you can see and talk to*. Group chats let sub-divisions of the
team self-organize around an area (research pod, content pod, ops pod) — the board tells
you what's assigned; the rooms show you what they're deliberating.

## What Bot Mode is

- Ships **built into the desktop app** and is **on by default** — no install.
- Appears as a **Bots tab** alongside the session list.
- **A Bot IS a profile.** No new primitive: isolated config, memory, skills, credentials,
  and chat under `~/.hermes/profiles/<name>/`. Everything in the UI has a CLI equivalent.

| In Bot Mode | From a shell |
|---|---|
| Chat with a Bot | `hermes -p <bot> chat` |
| A Bot's files, skills, memory | `~/.hermes/profiles/<bot>/` |
| Routines | `hermes cron list` (jobs named `[bot:<name>] …`) |
| Create / inspect profiles | `hermes profile create`, `hermes profile list` |

## Creating Bots

In the Bots tab: **New Agent** → **Name**, **Title**, **Description** — the Bot exists in
seconds and introduces itself in its **canonical Bot Chat** (a forever-conversation; the
composer reroutes `/new` to `/compact` so the relationship is never forked).

The **Advanced** panel is the full capabilities surface:

- **Clone from a profile** or start **Fresh** / **Create empty**.
- **Model & provider pin** — every Bot can run a different model.
- **Custom SOUL.md** — persona and standing instructions.
- **Per-skill, per-toolset, per-MCP enablement** — exactly the capabilities it needs.
- **Shared keys** — Bots share the token pool so refreshes cannot invalidate each other.
- **Create on** — with multiple connections, pick which machine the Bot lives on.

Every Bot gets a **face**: deterministic blob (same name → same face), geometric, an
uploaded image, an AI-generated portrait, or a pixel pet. Its look lives in profile
metadata, so it looks the same on every desktop in front of that backend.

## Routines — recurring tasks attached to the Bot that does them

The **Routines** pane docks beside the chat while the Bots tab is active. "Summarize my
inbox every morning" lives next to the Bot responsible for it. A structured schedule
picker builds the schedule; the Advanced field exposes the raw Hermes string.

Routines are plain cron jobs (`[bot:<name>] <routine>`) — they show up in `hermes cron
list`, and results land in the Bot's own chat history.

## Groups and group chats — team pods

Right-click a Bot → **Manage groups** to seat it in one or more rooms, or create a room
inline. Groups are standalone rows; a Bot keeps its DM row even when in several groups.

**Opening a room** (2–6 Bots) opens a shared working surface where the pod coordinates:

- Your message triggers up to **three serial rounds** of member turns. @-mentioned Bots
  respond; everyone responds when nobody is mentioned. Each Bot replies briefly or passes;
  the room settles when a full round stays silent.
- Bots pull each other in with `@name` and escalate real judgment calls to you with
  `@user` — the group row shows a **needs-you** badge.
- Hard caps (10 messages per send, 3 rounds) keep rooms from spinning.
- Each member keeps its own persistent `Group: <name>` session — room context survives.
- **Not every Bot replies to everything.** Speaking is each member's choice. Expect the
  addressed (or those with something new) to speak; the rest stay quiet.

**Designing pods by area of focus** — this is the "sub-divisions of your AI team" pattern:

| Pod | Members | Area |
|---|---|---|
| **Research** | researcher + content strategist + evaluator | Papers, market, new signals |
| **Product/Build** | engineer + architect + reviewer | Code, architecture, release gates |
| **Content** | writer + researcher + distributor | Drafts, threads, publishing |
| **Operations** | ops bot + chief of staff | Boards, processes, delivery |

A pod is not a replacement for the board — it is where the pod *talks*; tickets still get
done on the board. Kanban remembers; chat deliberates.

## Bot-to-bot messaging

- **@mentions** — `@researcher have a look at this` in any chat hands the message off,
  waits for the reply, and reports back. Names validate against the live roster.
- **Direct messages** — a Bot reaches a teammate's canonical Bot Chat via
  `hermes -p <bot> chat --in <file> -c "Bot Chat" --create-if-missing -Q --query-file <file>`.
  The file transport keeps quotes/backticks verbatim. The receiving Bot picks the message
  up when it next runs, and the messaging protocol is taught to its Bot Chat automatically
  (`agent.bot_mode_protocol`, default on).
- **Cross-machine peer DMs** — register another gateway as a peer:

  ```bash
  hermes peer add <name> --url http://target:8377 --key <API_SERVER_KEY>
  hermes peer list
  hermes peer dm <name> < /tmp/dm.txt            # message body from a file
  hermes peer dm <name>/<bot> < /tmp/dm.txt      # a named profile on that host
  ```

  Delivery lands in the remote Bot's canonical chat, runs one turn there, and prints the
  reply. Peer names/URLs live in `config.yaml` under `bot_peers`; the key is a credential
  in `~/.hermes/.env` (`HERMES_PEER_<NAME>_KEY`). Once registered, every Bot Chat learns
  on its own that teammates exist on other machines and how to reach them.

## Bots across machines

Register several backends in **Settings → Connections** (local runtime, remote gateways,
SSH hosts, cloud instances) and the roster shows Bots from every connected source. Same
name on several machines → handles disambiguate as `@name-device`. Clicking a Connections
Bot does not hop your window; `@mention` it, seat it in a room, or create agents on it
directly with **Create on**. Rooms can span machines: each member's turns run on its own
machine in its own `Group: <name>` session there, with a device badge in the room.

## Etiquette for rooms (recommended defaults)

- **One clear ask per message.** Bots answer best when the ask is scoped.
- **Use @mentions to target.** If you want one opinion, name the Bot; if you want the pod,
  mention nobody and let round-robin do its work.
- **Keep rooms for deliberation, the board for commitments.** A decision reached in a room
  becomes a kanban card, not a room memory.
- **Escalate with `@user` sparingly.** The needs-you badge is your pull lever; do not make
  every room ping you.

## Turning it off

Bot Mode is a bundled plugin: **Settings → Plugins → Bots**. Flipping it off unregisters
the roster/routines/composer live, no restart. Profiles, sessions, and cron jobs are
untouched — Bot Mode renders profiles, it never owns them.

## Bringing it all together with earlier phases

- **Phase 3** created the profiles; Bot Mode is how you *meet* them in a UI.
- **Phase 4** keeps the board authoritative; rooms deliberate and escalate.
- **Phase 5** rituals run via cron/kanban — the same agents update the same board from
  their desk pods.
- A **chief of staff Bot** (Phase 4) can sit in every room as the coordinator.

## Checklist

See [`checklists/PHASE6.md`](../checklists/PHASE6.md) and the pod manifest template
[`templates/group-chat-pod-manifest.md.sample`](../templates/group-chat-pod-manifest.md.sample).

**Done when:** you have named Bots with faces and SOULs, at least two pods (group chats)
that actually coordinate on real work, and you have seen a room deliberate and escalate to
you once.

## What success looks like

The Desktop Bots tab shows named colleagues with faces, not anonymous profiles.
A research pod deliberates; `@atlas` routes to Atlas; `@user` reaches you. A
decision that must persist becomes a kanban card — the room does not pretend to
be the system of record.

Filled taste: [`../examples/pods/research-pod-manifest.md`](../examples/pods/research-pod-manifest.md).

**Expected outputs to capture:**
- Bots tab showing ≥2 named Bots (or `hermes profile list` if Desktop is blocked)
- One group chat with 2–6 seated members and a pinned pod manifest
- One `@` mention that was answered by the intended Bot
