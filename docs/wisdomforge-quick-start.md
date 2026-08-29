# WisdomForge Quick Start — 30 Minutes to Your First Sitting

**You are a parent.** You want to run a WisdomForge sitting with your child today,
not after reading a 268-line guide. This page gets you there in 30 minutes.

When you want depth — multi-child setups, profile sync, theological humility,
permission escalation — the [full parent-operator guide](wisdomforge-parent-operator.md)
is waiting. Right now, you just need to sit down with your kid and begin.

---

## What you need

- A Hermes Agent install (if you don't have one, the [Minimal Viable Team](minimal-viable-team.md)
  path covers it in 15 minutes — come back here when `hermes doctor` is clean)
- A child ready to learn
- 30 minutes

---

## Step 1 — Create a parent-operator profile (5 min)

```bash
hermes profile create wf-parent
```

Copy the WisdomForge parent-operator SOUL into the profile:

```bash
cp examples/souls/wisdomforge-parent-operator.md \
   ~/.hermes/profiles/wf-parent/SOUL.md
```

Edit the SOUL: replace the placeholder identity with your name and your
family's context. Keep the WisdomForge Role, Core Values, and Band Table
intact — those are non-negotiable.

Add a `USER.md` with real facts about you and your family (without child PII):

```bash
# ~/.hermes/profiles/wf-parent/memories/USER.md
# Your name, communication style, and the band(s) you are operating.
# Do NOT put your child's name, school, or photo here.
```

**Verify:**

```bash
hermes chat -p wf-parent -q "Who are you and what is your role?"
```

The reply should confirm: parent's assistant, not the child's teacher.

---

## Step 2 — Pick a band (2 min)

| Band | Ages | Sitting length | Ritual |
|------|------|----------------|--------|
| Little Thinkers | 5–10 | 15–20 min | Ask a Grown-Up |
| Young Minds | 11–14 | 25–30 min | Talk About It |
| Emerging Adults | 15–18 | 35–45 min | Practice/Reflect |
| Lifelong Learners | Adult | 40 min | Companion |

Go to [smfwisdomforge.com/start](https://smfwisdomforge.com/start) and pick the
band that matches your child's age. Navigate to a sitting — any subject that
looks interesting. You do not need to start at a particular point.

**One rule:** the band boundary is hard. A 7-year-old is Little Thinkers even if
they are "advanced." The bands are about permissions, not IQ.

---

## Step 3 — Read the parent briefing (5 min, child not in the room)

Every sitting page has a **parent briefing**. It tells you:

- The edge — what this sitting is really about
- The trap — the anticipated misreading children fall into
- What not to skip — the parts that matter most

Read it. If you are short on time, ask your profile:

```bash
hermes chat -p wf-parent -q "Summarize the parent briefing for [sitting name] in 3 sentences."
```

You can also query the research corpus for deeper background:

```bash
hermes chat -p wf-parent -q "Search smfwisdomforge.com/api/search for '[topic]' and give me a 3-sentence summary."
```

---

## Step 4 — Run the sitting (15–20 min)

Follow this order. Do not reorder it.

1. **Reading** — your child reads (or you read together for Little Thinkers)
2. **Big idea** — say it once. Let it land. Do not explain it.
3. **Try this** — hands-on. No model. This is the human-first part.
4. **Guide panel** — OPTIONAL. If you use it, the sitting page has a
   copy-to-clipboard prompt that sets up your child's band-locked profile.
   The guide hints. It does not answer.
5. **Dinner question** — ask it at dinner tonight. One sentence. Everyone answers.

**When to put the guide away:**

- If your child is engaged with the try-this, do not interrupt with the guide
- If your child asks a question the sitting does not cover, answer it yourself
- If the topic is tender (faith, evil, death), the guide is OFF — you are the
  person in the room

---

## Step 5 — After the sitting (3 min)

1. **If they say** — listen for the anticipated misreading the briefing warned
   you about. Use the parent reply as a starting point, not a script.
2. **Integrity rule** — name the house rule. Post it on the fridge if it helps.
3. **Mark complete** on the site (device-local — no account needed).

---

## You did it. What now?

You have run a WisdomForge sitting. The academy is the curriculum. You are the
teacher. Hermes is the assistant. That order matters.

When you are ready to go deeper:

| You want to... | Read |
|----------------|------|
| Set up a band-locked profile for your child | [Full guide § Setting Up a Child Profile](wisdomforge-parent-operator.md#setting-up-a-child-profile) |
| Manage multiple children | [Full guide § Multi-Child Families](wisdomforge-parent-operator.md#multi-child-families) |
| Understand the permission system | [Full guide § The Four-Band Permission System](wisdomforge-parent-operator.md#the-four-band-permission-system) |
| Handle Faith & Reason sittings | [Full guide § Theological Humility](wisdomforge-parent-operator.md#theological-humility-for-faith--reason-sittings) |
| Keep child profiles aligned with academy updates | [Full guide § Profile Sync](wisdomforge-parent-operator.md#profile-sync-keeping-child-profiles-aligned-with-the-academy) |
| Use the search API for deeper study | [Full guide § Using the Search API](wisdomforge-parent-operator.md#using-the-search-api) |

---

**Links**

- Academy: [smfwisdomforge.com](https://smfwisdomforge.com)
- Start page: [smfwisdomforge.com/start](https://smfwisdomforge.com/start)
- Kids profiles repo: [smfworks/wisdomforge-kids-Hermes-profiles](https://github.com/smfworks/wisdomforge-kids-Hermes-profiles)
- Full parent-operator guide: [wisdomforge-parent-operator.md](wisdomforge-parent-operator.md)