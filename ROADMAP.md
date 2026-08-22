# Roadmap

This repository is a living document. The roadmap tracks what this guide covers today and
where it is heading. Items move between sections as they land.

## Shipped (v1.0)
- Phase 0 — Philosophy (colleague, not tool)
- Phase 1 — First agent: SOUL, memory, vault
- Phase 2 — Self-improvement: skills, curator, nightly research
- Phase 3 — Second agent: profiles, roles, models
- Phase 4 — Team coordination: kanban, chief of staff, dispatch
- Phase 5 — Autonomy & rituals: Dawn Circle, alignment, 1:1s, collaboration router
- Phase 6 — Hermes Desktop Bots & Group Chats: pods, routines, bot-to-bot, peers
- Templates, scripts, reference, and per-phase agent-verifiable checklists

## Shipped (v1.1)
- [x] **Filled example library** — four SOULs (research, engineering, content, chief of
      staff), a sample skill, vault note, state file, conversation transcripts, and pod
      manifest in `examples/`.
- [x] **First-time survival kit** — "What is Hermes and this guide" primer, FAQ with 12
      troubleshooting entries, Minimal Viable Team 2-hour guided path.
- [x] **Visual system map** — Mermaid architecture diagram in README.
- [x] **README overhaul** — positioning, badges, graduated quick start, examples callout.
- [x] **"What success looks like"** — concrete success + expected outputs at end of every
      phase doc.
- [x] **Authority signals** — GitHub topics, compatibility note, proven-in-production.
- [x] **Case-study invitation** in CONTRIBUTING.

## In progress / planned
- [ ] **Evaluation phase** — measuring team health: model cost/quality tracking on the
      shared harness (meta-harness), throughput per agent, ritual participation. The
      SMF meta-harness work will seed this.
- [ ] **Multi-machine teams** — deeper guidance on Bots across connections and
      cross-machine peer DMs beyond the basics (topology patterns, latency, failure).
- [ ] **Publishing flow** — how an AI team ships content end-to-end (vault note → draft →
      review → publish → measure), including the X/OpenClaw and Clearinghouse paths.

## Next (v1.2 target)
- [ ] **Failure-mode playbook** — promote FAQ entries into a structured playbook for the
      most common ways team setups break (dispatch model config, token exhaustion,
      credential drift, room non-participation), each with the fix we actually applied.
- [ ] **Community case studies** — standups from people who used this repo, submitted
      via CONTRIBUTING, with what deviated from the docs and why.
- [ ] **Live screenshots** — Desktop Bots tab, a pod mid-deliberation, kanban, vault,
      SOUL continuity, Dawn Circle card. Blocked until a capture of the living system
      is available on the maintainer machine.

## Backlog / someday
- [ ] Formal skill pack for "spin up an AI team" — a Hermes skill bundle an agent loads
      to bootstrap the whole repo-driven setup autonomously.
- [ ] Sample pod manifests for 5–8 common team shapes (solo founder, agency, product
      SaaS, research lab, legal, medical-adjacent ops) beyond the four core pods.
- [ ] Migration guide for teams already running agents informally (no SOUL, no board)
      who want to adopt this structure without a clean-slate reinstall.

## Contribution themes
If you are contributing, the highest-value additions today are: the failure-mode
playbook entries (from real pain), evaluation metrics that actually worked for you, and
any pod/room pattern that surprised you by working well. See CONTRIBUTING.md.
