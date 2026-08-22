# Minimal Viable Team — Your First 2 Hours

Brand new to Hermes? Start here. This path gets you to a meaningful **team of
one** before you attempt the full multi-agent phases.

A Minimal Viable Team is one named colleague with identity, memory, a vault, one
skill saved from real work, and one ritual or scheduled job that produced
observable output.

## Prerequisites

- Linux, macOS, or WSL with a terminal
- An API key (or a local model via Ollama) for at least one provider
- This repository cloned so you can copy examples and run `scripts/init-vault.sh`
- About two hours, in four blocks you can pause between

If install itself is failing, stop and use the
[official installation guide](https://hermes-agent.nousresearch.com/docs/getting-started/installation).
This repo does not replace that.

---

## Block 1 — Install and verify (0–15 min)

```bash
curl -fsSL https://hermes-agent.nousresearch.com/install.sh | bash
hermes setup
hermes doctor
hermes chat -q "Hello. I am your new operator. Confirm you can hear me."
```

**Verification**

- [ ] `hermes doctor` completes without missing required dependencies
- [ ] The one-shot chat returns a model reply, not an auth error

If doctor is clean but chat fails, see
[FAQ §6](faq-and-troubleshooting.md).

---

## Block 2 — Identity, memory, vault (15–45 min)

1. Pick a filled SOUL from [`../examples/souls/`](../examples/souls/) closest to
   the work this agent will own.
2. Copy it to the Hermes home (default profile) **or** a named profile:

```bash
# Default home
cp examples/souls/atlas-research-analyst.md ~/.hermes/SOUL.md
# Edit names, organization, and lanes. Do not ship the sample names.

# Named profile (recommended if you will add more agents later)
hermes profile create atlas
# then write ~/.hermes/profiles/atlas/SOUL.md
```

3. Create `USER.md` and `MEMORY.md` with **real** facts (declarative, compact).
   Start from [`../templates/USER.md.sample`](../templates/USER.md.sample) and
   [`../templates/MEMORY.md.sample`](../templates/MEMORY.md.sample). Paths:

```
~/.hermes/memories/USER.md
~/.hermes/memories/MEMORY.md
# or ~/.hermes/profiles/<name>/memories/ for a profile
```

4. Create the vault and tell the agent the absolute path:

```bash
bash scripts/init-vault.sh
# Then in chat: "Your vault is ~/AgentVault. Write a test note to
# ~/AgentVault/Research/test-note.md using the Phase 1 vault format."
```

**Verification**

- [ ] A **fresh** session: `hermes chat -q "State your name, role, and lanes."`
      matches the SOUL you wrote (not the built-in default)
- [ ] `find ~/AgentVault -type d | sort` shows Research/, Writing/, Team/, Archive/
- [ ] `cat ~/AgentVault/Research/test-note.md` has Date, Source, Summary
- [ ] Tell the agent one durable fact, start a new session, confirm it recalls it

Full Phase 1 checklist: [`../checklists/PHASE1.md`](../checklists/PHASE1.md).

---

## Block 3 — One real task, one skill, one job (45–75 min)

1. Give the agent **one real task** in its lane (a paper, a market move, a
   small ops check). Require a vault note, not a chat summary.
2. When the procedure worked (or failed interestingly), have the agent save a
   skill. See [`../examples/skills/sample-paper-or-market-deep-dive.md`](../examples/skills/sample-paper-or-market-deep-dive.md)
   and [`../templates/SKILL.md.sample`](../templates/SKILL.md.sample).
3. Enable the curator:

```bash
hermes config set curator.enabled true
hermes curator status
```

4. Create one scheduled research job. The prompt must be self-contained:

```bash
hermes cron create "0 3 * * *" --name "Nightly Research" \
  --prompt "Scan this week's developments in YOUR-DOMAIN. File one vault note at ~/AgentVault/Research/ using the Phase 1 format (Date, Source, Tags, Summary, Key Findings, Relevance, Sources). If you find nothing citable, write a dated null-result note saying so. Do not invent sources."
hermes gateway status    # cron does not fire if the gateway is down
hermes cron run "Nightly Research"
```

**Verification**

- [ ] `find ~/.hermes -name SKILL.md` (or the profile skills dir) returns ≥1 skill
      with frontmatter and a verification section
- [ ] `hermes curator status` shows the curator enabled
- [ ] `hermes cron list` shows the job
- [ ] After `hermes cron run`, `hermes cron runs "Nightly Research" --limit 3`
      shows an attempt, and a dated note exists under `~/AgentVault/Research/`

If the job is listed but silent, see [FAQ §3](faq-and-troubleshooting.md).

---

## Block 4 — First ritual + identity continuity (75–120 min)

Stand up the Dawn Circle **or** a manual equivalent if you are not ready for
kanban yet.

**Preferred (Phase 5 scripts, zero LLM tokens):**

```bash
# From this repo. Scripts are idempotent.
hermes cron create "0 7 * * 1-6" --name "Dawn Circle — Create" --no-agent \
  --script "$(pwd)/scripts/dawn-circle-create.py"
hermes cron create "0 9 * * 1-6" --name "Dawn Circle — Close" --no-agent \
  --script "$(pwd)/scripts/dawn-circle-close.py"
hermes cron run "Dawn Circle — Create"
```

**Manual equivalent:** open a fresh session and have the agent post a three-line
check-in (working on / stuck on / need from team) as a vault note under
`~/AgentVault/Team/`.

Then confirm identity continuity:

```bash
# New session, no leftover chat context
hermes chat -q "Who are you, what is your lane, and where do you file research?"
```

**Verification**

- [ ] Phase 1 checklist is fully true against real state
- [ ] Phase 2 checklist is at least partially true (one skill + one job that ran)
- [ ] The fresh session states identity and vault path without being re-taught
- [ ] A ritual artifact exists (Dawn Circle card or `~/AgentVault/Team/` note)

---

## Success criteria

You have a Minimal Viable Team when all four are true:

- [ ] The agent states its identity and lane correctly in a fresh session
- [ ] At least one real vault note exists under `~/AgentVault/Research/`
- [ ] The agent owns at least one skill saved from real work
- [ ] One ritual or scheduled job has run with observable output

Do not start Phase 3 (a second agent) until this list is true. A second profile
on top of a generic, forgetful first agent multiplies noise.

## What comes next

| Next | Doc |
|------|-----|
| Deeper self-improvement | [`02-phase-2-self-improvement.md`](02-phase-2-self-improvement.md) |
| A second specialist | [`03-phase-3-second-agent.md`](03-phase-3-second-agent.md) |
| Shared board + chief of staff | [`04-phase-4-team-coordination.md`](04-phase-4-team-coordination.md) |
| Something broke | [`faq-and-troubleshooting.md`](faq-and-troubleshooting.md) |
