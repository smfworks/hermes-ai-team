# CHANGELOG

All notable changes to this repository are recorded here. Format follows
[Keep a Changelog](https://keepachangelog.com/): Added / Changed / Fixed / Removed.

## [1.2.0] — 2026-08-26

### Added
- **Multi-child family guidance** in `docs/wisdomforge-parent-operator.md`: one profile
  per child, sibling profile management table, mixed-band sitting rules, band-transition
  protocol (create new profile, don't modify old one).
- **Profile sync checklist** in `docs/wisdomforge-parent-operator.md`: what changes in
  the academy vs what stays fixed in child profiles, monthly sync procedure, and the
  non-negotiables that never change during sync (SOUL seed, PII rules, hint-first).
- **Multi-child awareness** section in `examples/souls/wisdomforge-parent-operator.md`:
  SOUL addition for parents operating multiple child profiles across different bands.
- **README updated** with multi-child and profile sync feature mentions.

## [1.1.0] — 2026-08-22

### Added
- **Filled example library** (`examples/`): four production-flavored SOULs (Atlas
  research analyst, Forge engineer, Quill content strategist, refined chief of staff),
  a filled skill, sample vault note, state file, before/after conversation transcripts,
  and a research pod manifest. Each with an "adapt, don't copy" header.
- **First-time primer** (`docs/00-what-is-hermes-and-this-guide.md`): what Hermes is,
  why this repo exists, how to use it as human or agent, compatibility note.
- **FAQ & troubleshooting** (`docs/faq-and-troubleshooting.md`): 12 entries with
  symptom → diagnosis → fix → verification, covering SOUL injection, vault writes,
  cron silent failures, Desktop Bots, memory persistence, model auth, group chat
  routing, kanban JSON shapes, cross-machine peers, lane overstepping, doctor gaps,
  and checklist verification failures.
- **Minimal Viable Team** (`docs/minimal-viable-team.md`): a 4-block, 2-hour guided
  path from install to a meaningful team of one, with verification at every step.
- **Mermaid system map** in README: visual architecture diagram showing the full
  phase flow from philosophy through Desktop Bots + pods.
- **"What success looks like"** sections at the end of every phase doc (1–6) with
  concrete success descriptions and expected outputs.
- **Badges** in README: MIT license, Hermes Agent compatible, agent-consumable,
  production patterns from SMF Works.
- **Proven-in-production** paragraph and **examples callout** in README.
- **Graduated quick start** in README: first 30 minutes / first day / first week.
- **Case-study invitation** in CONTRIBUTING with "what we need most" list.
- `docs/images/` directory for screenshots (captures of the live Desktop remain a
  follow-up if the living system is not available at release time).

### Changed
- README top half overhauled: positioning paragraph, system map, compatibility note,
  MVT link, badges, expanded quick start, updated repository layout.
- ROADMAP updated: v1.1 items marked shipped, v1.2 targets refined (failure playbook,
  case studies, live screenshots).
- GitHub repository topics set: hermes-agent, multi-agent, ai-team, orchestration,
  hermes, ai-agents, soul, agent-identity, nous-research.

## [1.0.0] — 2026-08-19

### Added
- Initial release of the living repository form of **"Building an AI Team: From
  Installation to Colleagues"**, reimagined as agent-consumable documentation.
- Phase 0–5 docs (philosophy through autonomy & rituals), componentized from the
  Clearinghouse article, rewritten so a Hermes agent can implement from them.
- **Phase 6 — Hermes Desktop Bots & Group Chats**: Bots-as-profiles, the Bots tab,
  routines, group rooms, `@`-mention routing, `@user` escalation, bot-to-bot DMs,
  cross-machine peers (`hermes peer`), and multi-connection Bots.
- Templates: SOUL.md, USER.md, MEMORY.md, STATE.md, SKILL.md, and group-chat pod
  manifests.
- Scripts: Dawn Circle (create/close), a market-scan example, a vault initializer.
- Checklists for every phase (agent-verifiable).
- Reference: condensed CLI/config cheat sheets and official-docs index.
- `AGENTS.md` operating agreement for agents pointed at this repo.
- MIT license, author/maintainer attribution (Aiona Edge / SMF Works).

## [Unreleased]

### Added
- **WisdomForge Quick Start** (`docs/wisdomforge-quick-start.md`): a condensed
  30-minute setup guide for parents who want to get going fast without reading
  the full 268-line parent-operator guide. Covers fresh profile creation, band
  selection, first sitting, and post-sitting steps, with links to the full
  guide for depth. README updated to surface the quick-start path alongside the
  full guide.
- **Multi-child family guidance** (`docs/wisdomforge-parent-operator.md`): how a
  parent operating multiple child profiles (different bands, different subjects)
  manages sessions, scheduling, and progress without cross-contamination. Covers
  separation rules (one child, one profile), naming, staggered scheduling,
  cross-contamination prevention, and aging one child up while siblings stay.
- **Profile sync helpers** (`docs/wisdomforge-parent-operator.md`): procedures for
  keeping child profiles in sync with academy updates (new units, new skills, spec
  changes) without cloning or overwriting identity files. Includes what-to-sync
  table, manual sync procedure, and when-to-sync trigger table.
- **Profile sync diagnostic script** (`scripts/wisdomforge-profile-sync.py`):
  read-only tool that compares a child profile's installed skills and config
  against the current kids repo templates. Reports missing skills, updated skills,
  extra skills, config drift, and missing identity files. Single-profile and
  family-directory modes with band filtering. Exit code 2 on drift, 0 on clean.
- Updated Next Steps in parent-operator doc to reference multi-child and sync
  sections.
