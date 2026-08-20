# Phase 6 Checklist — Hermes Desktop Bots & Group Chats

**Reference:** [`docs/06-bots-and-group-chats.md`](../docs/06-bots-and-group-chats.md)

## Bots
- [ ] Hermes Desktop opens; the **Bots** tab is present (bundled plugin, on by default)
- [ ] ≥1 Bot created via New Agent with Name/Title/Description (not just CLI profiles)
- [ ] The Bot has a face, a canonical Bot Chat, and introduced itself
- [ ] Advanced surface verified: model pin, custom SOUL, per-skill/per-toolset
      enablement work as described
- [ ] The Bot's files resolve to `~/.hermes/profiles/<bot>/` (Bot == profile,
      CLI-equivalent holds: `hermes -p <bot> chat` opens the same agent)

## Routines
- [ ] A Routine is attached to a Bot; it appears in `hermes cron list` as
      `[bot:<name>] <routine>`; its result lands in the Bot's chat history

## Groups / group chats
- [ ] ≥2 Bots seated in a group chat (2–6 members, room opens)
- [ ] A message to the room triggers member turns; the room settles when a round is silent
- [ ] `@mention` scoping works: mentioning one Bot gets that Bot to respond
- [ ] `@user` escalation works at least once, and the group row shows needs-you
- [ ] Hard caps hold (no runaway loops) — observe a busy exchange settles on its own

## Bot-to-bot & peers (as applicable)
- [ ] A DM from one Bot to another (file transport) delivered verbatim, reply came back
- [ ] If multi-machine: `hermes peer add`, then `hermes peer dm <peer> < file` runs a turn
      on the remote and prints the reply; same-name Bots resolve as `@name-device`
- [ ] Connections roster (Settings → Connections) shows Bots from every registered source

## Pod pattern
- [ ] At least one pod is organized by area of focus (Research / Build / Content / Ops)
      using the pod-manifest template
- [ ] A pod decision that needed to persist became a kanban card (reference the ID in
      the room)

**Verification output to capture:** a room transcript excerpt showing a deliberation that
settled, one round with @mention scoping, one needs-you escalation, one successful
bot-to-bot DM, and (if multi-machine) one peer DM reply.

**Done when:** named Bots with faces and SOULs exist, pods coordinate on real work, and
you have seen a room deliberate then escalate to you once.
