# FAQ and Troubleshooting

Seeded from production-flavored failures. Expand this file when reality disagrees
with the docs. Each entry is symptom → diagnosis → fix → verification.

Official docs win on conflicts: https://hermes-agent.nousresearch.com/docs/llms.txt

Related cheat sheet: [`../reference/hermes-commands.md`](../reference/hermes-commands.md)

---

### 1. SOUL.md exists but does not affect behavior

**Symptom:** You wrote a SOUL. The agent still answers as a generic assistant, or
ignores its name and lanes.

**Diagnosis:** Hermes loads `SOUL.md` from `HERMES_HOME` (default `~/.hermes/SOUL.md`),
not from the project directory you happened to launch in. A named profile loads
`~/.hermes/profiles/<name>/SOUL.md`. An empty, unreadable, or injection-blocked
SOUL falls back to the built-in default identity. A `/personality` overlay can
also drown the default voice for that session.

**Fix:**

```bash
echo "${HERMES_HOME:-$HOME/.hermes}"
ls -l ~/.hermes/SOUL.md ~/.hermes/profiles/*/SOUL.md
hermes -p <name> chat -q "State your name, role, and lanes in two sentences."
```

Put the file at the profile home, not in the git checkout. Use
`/personality none` if a session overlay is active.

**Verification:** A **fresh** session states the name and lanes from the file you
edited. If it still recites the built-in Hermes default, the file is not on the
path that instance is using.

---

### 2. Agent knows the vault path but never writes there

**Symptom:** The agent talks about `~/AgentVault` and never creates a file, or
writes into the repo / `/tmp` instead.

**Diagnosis:** The path may be in MEMORY.md as a fact, but the agent was never
asked to write, wrote relative to the session cwd, or the tree does not exist.

**Fix:**

```bash
bash scripts/init-vault.sh
find ~/AgentVault -type d | sort
# Then, in chat: "Write a test note to ~/AgentVault/Research/test-note.md
# using the Phase 1 vault format. Then show me ls of that file."
ls -l ~/AgentVault/Research/test-note.md
```

**Verification:** `cat` of the stated absolute path returns real content with
Date / Source / Summary. A chat-only summary is not a vault note.

---

### 3. Cron jobs list but produce no output

**Symptom:** `hermes cron list` shows the job. Nothing arrives. No vault note.
No error you noticed.

**Diagnosis:** Cron is ticked by the **gateway daemon**. If the gateway is down,
jobs sit. Prompts that are not self-contained fail quietly. Model/provider auth
can fail at fire time. `--no-agent` jobs with empty stdout are *supposed* to be
silent.

**Fix:**

```bash
hermes gateway status
hermes cron status
hermes cron list
hermes cron run <id-or-name>
hermes cron runs <id-or-name> --limit 5
ls -lt ~/.hermes/cron/output/<job_id>/
```

If gateway is not running: `hermes gateway install` (once) then
`hermes gateway start`. Rewrite the prompt so it names the vault path, the
domain, and what "done" looks like.

**Verification:** `hermes cron runs` shows a terminal state (`completed` or
`failed`, not a silent blank). A completed research job leaves a dated file
under the vault.

---

### 4. Desktop Bots tab is missing, empty, or CLI profiles do not appear

**Symptom:** You created a profile with `hermes profile create` and the Desktop
Bots tab is blank, or there is no Bots tab.

**Diagnosis:** Bot Mode lives in the Desktop app. The gateway/Desktop process
must be running against the same Hermes home as the CLI. A profile that exists
on disk is not automatically a Bot until Desktop Bot Mode has it.

**Fix:**

```bash
hermes profile list
hermes gateway status
hermes desktop
```

Confirm you are not pointing Desktop at a different `HERMES_HOME`. Create or
enable the Bot from the Bots tab (see official Bot Mode docs).

**Verification:** `hermes profile list` shows the name, and the Bots tab shows
the same name with a face. Chat via `hermes -p <name> chat -q "Who are you?"`
returns that Bot's identity.

---

### 5. USER.md / MEMORY.md does not persist across sessions

**Symptom:** You told the agent to remember something. The next chat forgot it.

**Diagnosis:** Memory is a **frozen snapshot** injected at session start. Writes
during a session land on disk immediately but do not appear in the prompt until
the **next** session. Files live under `~/.hermes/memories/` (default home) or
`~/.hermes/profiles/<name>/memories/`. Character limits are hard
(MEMORY 2,200 / USER 1,375); a full store rejects the add instead of silently
keeping it. Two processes sharing one Hermes home will corrupt each other's
memory — give the second agent its own profile.

**Fix:**

```bash
ls -l ~/.hermes/memories/ ~/.hermes/profiles/*/memories/
hermes memory status
# Start a *new* session after the write, then ask for the fact.
```

**Verification:** The new session's system-prompt memory header shows the fact,
or the agent recalls it without being re-told. If the write failed, the memory
tool error (limit exceeded) is the truth — consolidate and retry.

---

### 6. Model or provider auth fails after creating a new profile

**Symptom:** The new profile cannot chat. 401 / missing key / provider not
configured.

**Diagnosis:** Profiles share the main token pool by default, but a profile can
still be pinned to a provider whose key is missing from `~/.hermes/.env`.
`hermes doctor` being clean does not prove every provider works.

**Fix:**

```bash
hermes doctor
hermes model
hermes auth   # or check ~/.hermes/.env for the provider key — do not print secrets
hermes -p <name> chat -q "ping"
```

**Verification:** The one-shot chat returns a model reply, not an auth error.

---

### 7. Group chat rounds do not trigger, or @mentions are ignored

**Symptom:** You send a message in a Desktop group chat and nobody answers, or
only the wrong Bot answers.

**Diagnosis:** Un-mentioned messages run a round across seated Bots. `@name`
targets one member. `@user` escalates to the human. Members must be local Bots
or Bots from a registered Connection. A room with one member is not a pod.

**Fix:** Confirm the group exists in Desktop Bot Mode, that 2–6 Bots are seated,
and that you used the Bot's actual name. Re-read
[`06-bots-and-group-chats.md`](06-bots-and-group-chats.md) and the official
Bot Mode page.

**Verification:** An `@atlas` message is answered only by Atlas. An un-mentioned
prompt gets a round from the seated members.

---

### 8. Kanban JSON shape surprises (`show` vs `list`)

**Symptom:** A script that verifies a Dawn Circle card (or any task) crashes or
thinks the card is missing after a successful create/close.

**Diagnosis:** Learned in production: `hermes kanban show <id> --json` wraps the
task under a `task` key. `hermes kanban list --json` returns flat task dicts.
Naive parsers fail silently. This caused seven silent days of failed
verification on the original Dawn Circle close script.

**Fix:** Unwrap both shapes. Copy the pattern in
[`../scripts/dawn-circle-close.py`](../scripts/dawn-circle-close.py)
(`_unwrap_task()`).

**Verification:** `hermes kanban show <id> --json` and
`hermes kanban list --json` both yield a dict with `title` after unwrap.

---

### 9. Cross-machine peer DM fails

**Symptom:** `hermes peer dm` errors, times out, or the remote Bot never sees
the message.

**Diagnosis:** The peer must expose the API server platform. You need its URL
and `API_SERVER_KEY` stored locally (in `~/.hermes/.env`, not in git). Both
gateways must be up.

**Fix:**

```bash
hermes peer list
hermes gateway status
hermes peer add <name> --url http://host:port --key <API_SERVER_KEY>
hermes peer dm <name> "ping from the other machine"
```

**Verification:** `hermes peer list` shows the peer; `dm` prints a reply from
the remote agent.

---

### 10. New agents overstep their lanes or become hyperactive

**Symptom:** The research agent edits systemd units. The chief of staff starts
writing the paper. Cron jobs spam status pings.

**Diagnosis:** The SOUL's "do not touch" section is vague, or missing. Initiative
without a silence rule becomes noise. A coordinator SOUL that also "helps with
the work" will abandon the board.

**Fix:** Tighten lanes using [`../examples/souls/`](../examples/souls/) as
taste, not copy-paste. Add an explicit "ask first" list and "silence is
healthy." Change the SOUL; do not override it in chat and hope it sticks.

**Verification:** In a fresh session, ask "What will you refuse to do without
asking?" The answer matches the file. A coordinator asked to "just write the
post" declines and assigns it.

---

### 11. `hermes doctor` is clean but later steps fail

**Symptom:** Doctor reports no missing required dependencies. Cron, Desktop, or
profiles still fail.

**Diagnosis:** Doctor checks core install health. It does not prove the gateway
is running, Bot Mode is configured, a profile has a SOUL, or a cron prompt is
self-contained.

**Fix:**

```bash
hermes doctor
hermes gateway status
hermes cron status
hermes profile list
hermes -p <name> chat -q "ping"
```

Then run the **phase checklist** against real state.

**Verification:** Each feature-specific command returns a healthy status, not
just `doctor`.

---

### 12. Checklist items look done but real state fails

**Symptom:** Every box is checked. A second agent (or you, tomorrow) cannot find
the SOUL, the vault, or the cron output.

**Diagnosis:** Boxes were filled by assumption or narration. AGENTS.md forbids
this. "Done" means a command or file listing you actually ran.

**Fix:** Re-run every verification command in `checklists/PHASE*.md`. Capture
output. If a block exists (credential, permission, missing Desktop), write the
block down — do not check the box.

**Verification:** An independent session can reproduce every checked item from
disk and CLI output alone.
