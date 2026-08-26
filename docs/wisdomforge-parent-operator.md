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

## Multi-Child Families

If you have more than one child using WisdomForge, you need more than one child profile. Each child gets their own fresh, band-locked Hermes profile. The profiles do not share memory, skills, or configuration.

### One profile per child, one band per profile

- Each child profile is created separately using the kids repo setup prompt. Run the setup prompt once per child.
- A 7-year-old and a 15-year-old need different bands (`little` vs `emerging`). Their profiles have different tools, different rituals, different SOUL seeds. Do not stretch one profile across both children.
- If two children are in the same band (e.g., both ages 11–14), they still get separate profiles. The pairing line in each USER.md names the sitting that child is working on. Shared profiles conflate progress and blur the if-they-say calibration.

### Managing sibling profiles

| Concern | Rule |
|---------|------|
| Memory | Each profile has its own MEMORY.md. Do not copy one child's memory into another's. |
| Progress | Progress is device-local on the academy site (zustand + localStorage). Each child's progress is tracked separately if they use different browsers or devices. |
| Sitting assignment | Siblings can work on the same sitting or different sittings. If they work together (mixed-age table), use the youngest child's band for the ritual. |
| Tools | A younger child's profile never inherits an older child's tools. The band boundary is per-profile, not per-family. |
| The guide | The guide on each child's profile is band-locked. An emerging-band guide will not give little-band hints. Do not ask an older child's guide to help a younger child. |

### Running sittings with multiple children

1. **Same-band siblings**: they can sit together. One profile, one guide, one ritual. Take turns with the try-this.
2. **Mixed-band siblings**: run separate sittings. The readings, rituals, and durations differ by band. A 15-minute Little Thinkers sitting and a 40-minute Emerging Adults sitting are not the same session.
3. **Mixed-age dinner question**: the dinner question is designed for a mixed-age table. One question, everyone answers at their level. This is the one part that works across bands.

### When a child ages out of a band

When a child moves from one band to the next (e.g., Little Thinkers → Young Minds at age 11), create a new profile for the new band. Do not modify the old profile in place — the old profile's SOUL seed, tool set, and ritual are band-specific. The new profile is a fresh creation with the next band's seed. The child's interests and preferences can be carried over manually (durable interests, communication style), but the profile structure is new.

---

## Profile Sync: Keeping Child Profiles Aligned with the Academy

The WisdomForge academy evolves. New sittings are added, lesson content is updated, skills are revised. A child profile created in August may need updates by October. This section explains how to check alignment and what to update.

### What changes in the academy

| Change | Frequency | Impact on child profiles |
|--------|-----------|--------------------------|
| New sittings added to the catalog | Occasional | No action needed — the pairing line in USER.md names a specific sitting. New sittings are available when the parent chooses them. |
| Lesson content updated (readings, try-this, ifTheySay) | Occasional | No action needed — the child's guide reads from the sitting, not from the profile. Updates are automatic. |
| Kids repo skills updated (new versions, new skills) | Regular | Check the kids repo CHANGELOG.md. If a skill your child uses was updated, pull the latest version into the child's profile. |
| Band definitions changed (ritual, tools, permissions) | Rare | Review the child's profile against the updated BANDS.md. If the band's tool set or ritual changed, update the profile's config. |
| New skill added to the kids repo | Occasional | Optional. If the new skill is relevant (e.g., a subject-aligned skill for a sitting your child is working on), install it. If not, skip it. |

### Sync checklist (run monthly or when the kids repo has a new release)

1. **Read the kids repo CHANGELOG.md** — note any skill updates or new skills since your last sync.
2. **Check BANDS.md** — verify the band definitions haven't changed for your child's band.
3. **Check SKILLS.md** — see if any new skills are relevant to the sittings your child is working on.
4. **Update installed skills** — for each skill your child's profile has installed, compare the version in the child's profile against the kids repo version. If the repo version is newer, replace the child's copy.
5. **Verify with `check_repository.py`** — if the kids repo includes a profile validation script, run it against the child's profile to catch structural issues.
6. **Test with a synthetic exchange** — after updating, run a short practice exchange to verify the guide still responds correctly with the updated skills.

### What never changes

- The SOUL seed is fixed for the band. Do not replace it with a newer version unless the kids repo explicitly releases a new seed and documents the migration.
- The non-negotiables (fresh profile, no cloning, no child PII, hint-first, parent approval) are permanent. No sync changes these.
- The child's MEMORY.md is theirs. Do not overwrite it during sync. Add to it if the child's preferences have evolved, but never replace it with a template.

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

The academy is the curriculum. You are the teacher. Hermes is the assistant. That order matters.