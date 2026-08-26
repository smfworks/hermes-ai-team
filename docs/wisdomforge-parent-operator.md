# WisdomForge Parent-Operator Track

**Audience:** A parent or adult learner using Hermes Agent to operate the WisdomForge academy.

**Prerequisite:** You have a Hermes Agent install and a basic profile. If you don't, start with [Minimal Viable Team](minimal-viable-team.md) first, then come back here.

**What this track gives you:** A Hermes profile configured to run WisdomForge sittings with your child — read the parent briefing, facilitate the try-this, ask the dinner question, and know when to use the guide and when to put it away.

---

## What Is WisdomForge?

WisdomForge is a parent-operated academy for education in the age of AI. It is live at [smfwisdomforge.com](https://smfwisdomforge.com). The academy has:

- **10 subjects** (AI, thinking, philosophy, math, science, English, history, art, CS, language)
- **23 units** across those subjects, each with multiple sittings
- **4 age bands**: Little Thinkers (5–10), Young Minds (11–14), Emerging Adults (15–18), Lifelong Learners (adult)
- **298 lessons** — each with a parent briefing, reading, try-this activity, dinner question, and integrity rule
- **A search API** at `smfwisdomforge.com/api/search` that queries the full research corpus

The academy is not a chatbot. It is a curriculum you run. The Hermes profile is your assistant — it helps you prepare, not replace you.

---

## The Parent-Operator SOUL

Your Hermes profile needs a SOUL that understands its role: it is the parent's assistant, not the child's teacher. The child's teacher is you.

### SOUL additions for a WisdomForge parent-operator

Add these to your existing SOUL or use them as the basis for a new profile:

```markdown
## WisdomForge Role

I am the Hermes assistant for a WisdomForge parent-operator. My job is to help
the parent run sittings — not to run them myself.

### What I do
- Read the parent briefing from the sitting and summarize it in 3 sentences
- Suggest a try-this adaptation if the parent asks
- Query smfwisdomforge.com/api/search for deeper material when the parent wants to study
- Remind the parent of the integrity rule and hard edges before the sitting

### What I do not do
- I do not teach the child directly. The parent is the teacher.
- I do not generate devotional content, prayers, or doctrinal assertions
- I do not replace the try-this with a model exercise
- I do not answer for the child in the dinner question
- I do not skip the parent briefing

### The four bands
- Little Thinkers (5–10): grown-up in the room, 15–20 min, Ask a Grown-Up ritual
- Young Minds (11–14): 25–30 min, Talk About It ritual
- Emerging Adults (15–18): 35–45 min, Practice/Reflect ritual
- Lifelong Learners (adult): 40 min, Companion ritual

### The sitting order (do not reorder)
1. Parent briefing (read this first — 5 minutes, child not in the room)
2. Reading sections (the child reads or you read together)
3. Big idea (one sentence — let it land)
4. Try this (hands-on, no model yet)
5. Guide panel (optional — only if the parent decides to use it)
6. Dinner question (one sentence a mixed-age table can ask)
7. If they say (listen for the anticipated misreading — respond with the adapted reply)
8. Integrity rule (the house rule this sitting forges)
9. Mark complete
```

---

## Setting Up a Child Profile

For your child to have their own band-locked Hermes guide, use the kids profiles repo:

**Repo:** [smfworks/wisdomforge-kids-Hermes-profiles](https://github.com/smfworks/wisdomforge-kids-Hermes-profiles)

**The setup prompt** (also available at [smfwisdomforge.com/hermes](https://smfwisdomforge.com/hermes) as copy-to-clipboard):

```text
I'd like your help designing a private, child-facing Hermes profile for one
WisdomForge age band. Read and follow START-HERE.md, BANDS.md, and DECISIONS.md
from the WisdomForge kids Hermes kit. Ask the band first. Propose conservative
defaults. Show the full design. Create a fresh profile. Do not clone my adult
profile.
```

### Critical rules for child profiles

1. **Fresh profile only.** Never clone your adult profile into a child profile.
2. **Band-locked.** The profile stays in one age band. Do not stretch a Little Thinkers profile over a 14-year-old.
3. **Tool-poor.** The child's profile has fewer tools than yours. Little Thinkers: conversation only. Young Minds: conversation + optional voice/image. Emerging: conversation + optional parent-approved files.
4. **No child PII.** Never put a child's name, school, photos, or location in the profile. The pairing line in USER.md contains only the lesson title — not the full text.
5. **Parent approval.** You approve every tool addition, every permission change, every model upgrade.

---

## Running a Sitting

### Before the sitting (5 minutes, child not in the room)

1. Go to [smfwisdomforge.com/start](https://smfwisdomforge.com/start) and pick a band
2. Navigate to the sitting: `/learn/[band]/[subject]/[slug]`
3. Read the **parent briefing** — it names the edge, the trap, and what not to skip
4. Read the **hard edges** — 2–4 things you must not do or must not skip
5. Ask your Hermes profile to summarize the briefing in 3 sentences if you're short on time

### During the sitting

1. **Reading**: the child reads (or you read together for Little Thinkers)
2. **Big idea**: say it once. Let it land. Don't explain it.
3. **Try this**: hands-on. No model. This is the human-first part.
4. **Guide panel**: OPTIONAL. If you choose to use it, the copy-to-clipboard Hermes prompt on the sitting page sets up your child's band-locked profile. The guide hints — it does not answer.
5. **Dinner question**: ask it at dinner. One sentence. Mixed-age table.

### After the sitting

1. **If they say**: listen for the anticipated misreading. The sitting lists what children typically say and a parent reply. Use the reply as a starting point, not a script.
2. **Integrity rule**: this is the house rule. Name it. Post it if it helps.
3. **Mark complete** on the site (device-local — no account needed)

### When to put the guide away

- If the child is engaging with the try-this, don't interrupt with the guide
- If the child asks a question the sitting doesn't cover, answer it yourself first
- If the topic is tender (Faith & Reason, the problem of evil, death), the guide is OFF. You are the person in the room.
- The guide is a tool, not a teacher. You are the teacher.

---

## Using the Search API

The academy has a search endpoint that queries the full research corpus (1,096+ files):

```
GET https://smfwisdomforge.com/api/search?q=epictetus+dichotomy+control
```

Returns structured results from Harry's research compendiums. Use this for:

- **Your own deeper study** before a sitting
- **Answering your child's follow-up questions** with grounded material
- **Preparing for the if-they-say patterns** — search the figure's misconceptions section

Your Hermes profile can query this for you:

```text
Search smfwisdomforge.com/api/search for "augustine evil privation" and give me
a 3-sentence summary of what the research corpus says.
```

The child's profile (if `emerging` band with the `academy-search` skill) can also query — but the results are hints, not dumps. The guide hints from the corpus. It does not recite it.

---

## The Four-Band Permission System

| Band | Ages | Tools | Ritual | Sitting |
|------|------|-------|--------|---------|
| `little` | 5–10 | Conversation only | Ask a Grown-Up | 15–20 min, grown-up in the room |
| `young` | 11–14 | Conversation + optional voice/image | Talk About It | 25–30 min |
| `emerging` | 15–18 | Conversation + optional parent-approved files | Practice/Reflect | 35–45 min |
| `adult` | Adult | Full adult profile | Companion | 40 min |

### Permission escalation rules

1. **You escalate, not the child.** The child does not decide to add tools. You do.
2. **Escalation is per-sitting, not permanent.** You can grant a tool for one sitting and revoke it.
3. **The band boundary is hard.** A Little Thinkers profile does not get Emerging tools, even if the child is "advanced." The bands are about permissions, not IQ.
4. **The adult profile is never the child's profile.** Your adult Hermes profile has tools, memory, and access that the child's profile must not have.

---

## Theological Humility (for Faith & Reason sittings)

The Faith & Reason unit requires special handling:

1. **This is intellectual history, not catechism.** The academy teaches how Augustine, Aquinas, Julian, and Irenaeus reasoned. Whether you accept their conclusions is your family's work.
2. **The tradition is plural.** These thinkers disagree. The unit presents the disagreements, not a smoothed-over consensus.
3. **Non-Christian students are welcome.** The unit is valuable for understanding 2,000 years of thought that shaped Western civilization.
4. **No devotional AI.** The integrity rule for every Faith & Reason sitting: "Do not ask the model to generate prayers, devotional content, or doctrinal assertions. Ask it to explain arguments and surface objections."
5. **You are the theologian of the house.** The academy equips you to guide the conversation. It does not replace your own faith tradition (or lack thereof).

---

## Multi-Child Family Guidance

Families with more than one child in WisdomForge need more than one child profile. This section covers how to operate several band-locked profiles without cross-contamination — no shared memory, no shared sessions, no shared USER.md.

### Core rule: one child, one profile

Each child gets a separate Hermes profile with its own SOUL, USER, MEMORY, config, and design record. The kids repo states this flatly: "This kit does not merge siblings." The rule is non-negotiable because the things that make a profile safe for one child (band-locked tools, age-appropriate voice, single-child memory) break the moment you share it across children.

### What stays separate

| Artifact | Why it must not be shared |
|----------|--------------------------|
| SOUL.md | Each child's guide speaks at their band level with their display name |
| USER.md | Contains the current sitting for *that* child — different subjects, different progress |
| MEMORY.md | One child's learning history is not another child's context |
| Config / tools | Band permissions differ by age — a Little Thinkers profile has fewer tools than a Young Minds profile |
| Design record | Private maintenance notes per child (band, capabilities, eval results) |
| Session history | Each child's conversations stay in their own profile's sessions |

### What can be shared (as templates, not live copies)

- **Skill templates.** The `wisdomforge-ritual`, `socratic-homework`, and `escalation-and-safety` skills are the same *templates*. You install a copy into each child's profile. A change for one child is not automatic for another — and that is the point.
- **The adult parent-operator profile.** You (the parent) have one adult Hermes profile that acts as the control plane. It runs the parent-setup-helper, reviews sessions, and pauses or deletes child profiles. It must not ingest child MEMORY.md files into the adult memory store.

### Naming profiles

Use display names the family already uses in speech — not legal names plus school. Profile ids stay short and boring: `willow`, `juniper`, `scout`. The kids repo recommends this convention. Short ids prevent accidental PII leaks in logs and terminal output.

### Scheduling sittings across children

Each child works through sittings at their own pace. You are the scheduler — the adult profile is the assistant. Here is a pattern that works:

1. **Pick the band and sitting per child.** Visit `smfwisdomforge.com/start`, choose the band for each child, and note the sitting slug. Write it into that child's USER.md pairing line: `Currently working on WisdomForge lesson: Stoics — circle-you-control.` One child might be in Philosophy while another is in Math — that is fine.
2. **Stagger the times.** Little Thinkers sittings are 15–20 minutes with a grown-up in the room. Young Minds are 25–30. Emerging Adults are 35–45. If you have three children, you cannot run three sittings simultaneously — the model requires your presence for the youngest. Stagger by band: youngest first while older children read independently, then rotate.
3. **Use the adult profile for parallel prep.** While one child is doing the hands-on Try This (no model needed), ask your adult profile to summarize the next child's parent briefing. The adult profile is the only one that sees multiple children's briefings — and it must not carry that context into a child's session.
4. **Do not batch sessions across children.** Each sitting is a discrete event for one child. Do not line up three profiles in one terminal and rotate between them. The child needs your attention for the full sitting, and the integrity rule is per-sitting, not per-batch.

### Preventing cross-contamination

Cross-contamination is the primary risk when operating multiple child profiles. It happens when one child's context leaks into another child's session — through shared memory, shared sessions, or operator confusion.

**Hard rules:**

1. **Never copy MEMORY.md between child profiles.** One child's learning history is not another child's context. If both children are studying Stoics, they still have separate sessions and separate memories.
2. **Never share USER.md across siblings.** The pairing line names the current sitting for *that* child. Two children in the same unit still have different progress.
3. **Run `parental-session-review` on one profile at a time.** The kids repo's review skill is per-profile. Do not review two children's sessions in one pass.
4. **Run `family-isolation-check` after any profile change.** The check verifies that one child's profile does not reference another's data. Run it after creating a new child profile, after aging one child up, and after any config change.
5. **The adult profile does not carry child context.** Your adult Hermes profile can help you prepare multiple briefings, but it must not inject that preparation into a child's session. Use the adult profile for prep, then switch to the child's profile for the sitting.

### Aging one child up while siblings stay

When a child moves from 5–10 to 11–14, or 11–14 to 15–18, treat it as a redesign (see the kids repo `MAINTENANCE.md` for the full checklist). The aging-up is per child. A sibling staying in elementary keeps the old tools and the old band. Do not rush the older child's redesign while the younger child is mid-sitting — finish one, then start the other.

### What this is not

- Not a household account. Each child is a separate profile.
- Not a reason to give the oldest child an adult colleague profile. The adult profile is yours.
- Not a shared tutoring session. One child, one sitting, one profile at a time.

---

## Profile Sync Helpers

The WisdomForge academy ships new units, new sittings, and spec updates over time. When the academy changes, child profiles need to stay current — without cloning, overwriting, or breaking the band-locked design. This section covers how to keep child profiles in sync.

### What changes in the academy

| Change type | Example | Impact on child profiles |
|-------------|---------|--------------------------|
| New unit | A new Philosophy unit ships | Parent may update USER.md sitting line — no profile change needed |
| New sitting in existing unit | A new Stoics sitting is added | Same — just update the pairing line |
| Band spec change | `BANDS.md` updates tool permissions | Parent must review and manually apply the change |
| Skill template update | `wisdomforge-ritual` skill gets a new step | Parent copies the updated template into each child's profile |
| Security or safety update | `escalation-and-safety` skill revised | Parent applies to all child profiles immediately |

### The sync rule: update templates, preserve identity

Sync means updating the *templates* (skills, config snippets) in each child's profile while preserving the *identity* files (SOUL.md, USER.md, MEMORY.md). You never overwrite a child's SOUL, USER, or MEMORY to sync. You update the skill files and config snippets that the kids repo provides as templates.

### What to sync (and what not to)

| Sync (safe to update) | Do NOT sync (identity files) |
|-----------------------|------------------------------|
| `skills/*/SKILL.md` (template copies) | `SOUL.md` |
| `config-snippet.yaml` (band defaults) | `USER.md` |
| Design record (if band specs changed) | `MEMORY.md` |

### Sync procedure (manual, per child)

For each child profile:

1. **Check the kids repo for changes.** Compare the skill versions in the child's `skills/` directory against the current templates in the kids repo. The `wisdomforge-profile-sync.py` helper (below) automates this comparison.
2. **Review the diff.** Read what changed in each skill template. If a safety skill changed, apply it immediately. If a ritual skill added a step, review it and decide whether to apply.
3. **Copy updated templates into the child profile.** Replace the SKILL.md file in the child's `skills/<skill-name>/` directory. Do not touch SOUL.md, USER.md, or MEMORY.md.
4. **If band specs changed, review config.** Read the updated `configs/<band>.yaml.snippet` from the kids repo. Compare against the child's current config. Apply only the changes you approve. Do not auto-apply config changes — a band spec change may remove a tool the child is using, and you decide whether to remove it.
5. **Run `EVALS.md` if anything structural changed.** If a skill was added, removed, or substantially changed, or if config changed, re-run the evals per the kids repo `EVALS.md` to verify the profile still behaves correctly.
6. **Update the private design record.** Note what was synced, when, and why.
7. **Repeat for each child.** Each profile is synced independently. Do not batch-sync.

### The sync helper script

The adult team repo includes `scripts/wisdomforge-profile-sync.py` — a diagnostic tool that compares a child profile's installed skills against the current kids repo templates and reports what differs.

```bash
# Check one child profile against the kids repo
python3 scripts/wisdomforge-profile-sync.py \
  --child-profile ~/.hermes/profiles/willow \
  --kids-repo ~/projects/wisdomforge-kids-Hermes-profiles

# Check all child profiles in a family directory
python3 scripts/wisdomforge-profile-sync.py \
  --family-dir ~/.hermes/profiles \
  --kids-repo ~/projects/wisdomforge-kids-Hermes-profiles \
  --band little
```

The script is **read-only and diagnostic** — it reports what differs, it does not modify files. You review the diff and apply changes manually. This is intentional: the parent approves every change to a child's profile. No script should auto-overwrite a child's skill files.

**What the script checks:**

- Missing skills: the kids repo recommends a skill for this band that is not installed in the child profile
- Updated skills: the child's installed skill differs from the kids repo template
- Extra skills: the child has a skill not in the kids repo's band recommendation (may be parent-approved — the script flags it, not removes it)
- Config drift: the child's config snippet differs from the band defaults in the kids repo

**What the script does NOT do:**

- It does not write to any file
- It does not touch SOUL.md, USER.md, or MEMORY.md
- It does not create or delete profiles
- It does not auto-apply updates — the parent decides what to sync

### When to sync

| Trigger | Action |
|---------|--------|
| Academy ships a new unit | No sync needed — update USER.md pairing line only |
| Kids repo updates a skill template | Run the sync helper, review diffs, apply manually |
| Kids repo updates band specs (`BANDS.md`, `configs/`) | Run the sync helper, review config drift, apply approved changes, re-run EVALS.md |
| Kids repo updates safety skills | Apply immediately to all child profiles |
| Monthly maintenance check | Run the sync helper against all child profiles as a routine check |
| After aging a child up | Sync is part of the redesign — see `MAINTENANCE.md` in the kids repo |

### Academy search API for sync awareness

Your adult profile can query the academy search API to stay aware of new content:

```text
Search smfwisdomforge.com/api/search for "new sittings" and tell me what
units have been added since I last checked.
```

This does not sync anything — it tells you what is new so you can decide whether to update a child's USER.md pairing line.

---

## Cross-References

- **Academy site:** [smfwisdomforge.com](https://smfwisdomforge.com)
- **Start page:** [smfwisdomforge.com/start](https://smfwisdomforge.com/start)
- **Hermes setup page:** [smfwisdomforge.com/hermes](https://smfwisdomforge.com/hermes)
- **Method page:** [smfwisdomforge.com/method](https://smfwisdomforge.com/method)
- **Parents page:** [smfwisdomforge.com/parents](https://smfwisdomforge.com/parents)
- **Kids profiles repo:** [smfworks/wisdomforge-kids-Hermes-profiles](https://github.com/smfworks/wisdomforge-kids-Hermes-profiles)
- **This repo (adult team template):** [smfworks/hermes-ai-team](https://github.com/smfworks/hermes-ai-team)

---

## Next Steps

1. Read the [Minimal Viable Team](minimal-viable-team.md) guide if you haven't set up a Hermes profile yet
2. Add the WisdomForge Role section to your SOUL
3. Visit [smfwisdomforge.com/start](https://smfwisdomforge.com/start) and pick a band
4. Run your first sitting
5. When your child is ready for their own guide, use the kids repo to set up a band-locked profile
6. If you have multiple children, read [Multi-Child Family Guidance](#multi-child-family-guidance) above
7. Set up a monthly [Profile Sync](#profile-sync-helpers) check using `scripts/wisdomforge-profile-sync.py`

The academy is the curriculum. You are the teacher. Hermes is the assistant. That order matters.