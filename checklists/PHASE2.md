# Phase 2 Checklist — Self-Improvement (Skills, Curator, Nightly Research)

**Reference:** [`docs/02-phase-2-self-improvement.md`](../docs/02-phase-2-self-improvement.md)

- [ ] At least one skill was saved from real work (not an exercise): `find`
      `~/.hermes/profiles/<name>/skills -name SKILL.md` returns ≥1 with frontmatter
      (name, description, procedure, verification)
- [ ] Skill description is self-contained so it can be matched on future tasks
- [ ] `hermes curator status` runs; curator enabled
      (`hermes config get curator.enabled` → true)
- [ ] A nightly-research cron exists: `hermes cron list` shows a `0 3 * * *` (or similar)
      job with a research prompt
- [ ] The cron's vault path matches the actual vault from Phase 1
- [ ] Optional (recommended): a research cron uses `--script` for collection
- [ ] If any cron is `--no-agent`, its script is executable and runs clean
      (verified once, not assumed)

**Ways to verify the nightly loop works:**
- `hermes cron run <id>` fires once immediately; after it completes, confirm a dated
  vault note exists under `Research/` (not just an empty promise)
- Confirm the note has the required fields (date, source, summary)

**Done when:** a skill exists and was used again successfully, the curator is on, and one
nightly cron produced a real vault note.
