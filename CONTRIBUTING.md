# CONTRIBUTING

Thanks for helping evolve this repository. It exists to improve as the Hermes ecosystem
and the practice of building AI teams both mature.

## Who can contribute

- **Humans** — via the normal GitHub flow (issue → PR or direct PR).
- **Agents** — a Hermes profile pointed at this repo can also propose changes. The same
  review standards apply. If you are an agent, follow `AGENTS.md` and this file.

## What we add here

The repo is the living home for the "Building an AI Team" guide. Good additions:

- New or corrected **phase docs** — especially if a command changed across Hermes versions.
- New **templates** (SOUL, memory, STATE, group-chat manifests, skills) that generalize.
- New **scripts** for durable plumbing (Dawn Circle, watchdogs, vault hygiene).
- **Troubleshooting entries** — real failures you hit and fixed, with the fix.
- **Case studies** — how you structured your team, what worked, what did not.
- **Bot Mode / group-chat patterns** — room configurations, pod designs, routing etiquette.

Not a good fit:

- Marketing copy or self-promotion without technical content.
- Unverified model/hardware claims.
- Content that leaks the operator's private information or family.

## Ground rules

1. **One topic per doc section.** Match the existing structure.
2. **Real commands.** If a CLI exists, show it. Verify it runs before proposing it.
3. **Cross-check official docs.** The Hermes docs are authoritative:
   `https://hermes-agent.nousresearch.com/docs/llms.txt`. If the official docs say
   something different from the repo, the official docs win — fix the repo.
4. **Add a CHANGELOG entry.** Note the date, what changed, and why.
5. **No secrets.** Never commit `.env`, API keys, tokens, or private paths.

## Agent-contributed changes — extra process

If you are an agent proposing a change:

1. Read `AGENTS.md` — it is the operating agreement.
2. Make the change against a real problem you encountered (or a gap you verified in the
   official docs). Do not invent friction to justify editing.
3. Validate commands that are the point of the change before proposing the PR.
4. Say, in the PR description, what you verified and how (tool output, not narration).
5. If you cannot verify a block exists, explain the block instead of skipping it.

## The review standard

- Changes are reviewed for: does the claim hold? Is the command real? Does it fit the
  structure? Does it respect privacy and honesty rules?
- Maintainer may request verification output for any command-based claim.
- Speed is nice. Truth is mandatory.

## License

By contributing you agree that your contribution is licensed under the repository's
MIT License.
