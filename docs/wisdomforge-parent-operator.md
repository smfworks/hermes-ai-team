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