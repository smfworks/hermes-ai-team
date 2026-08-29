# Minimal Viable Parent-Operator — 30 Minutes to Your First Sitting

You want to run a WisdomForge sitting with your child, not build a multi-agent team. This guide gets you there in 30 minutes — one Hermes profile, one child profile, one sitting. No phases, no kanban, no group chats.

If you want the full team-building path later, it's in [Minimal Viable Team](minimal-viable-team.md) and the phase docs. But you don't need it to start.

---

## What you'll have at the end

- One adult Hermes profile configured as a WisdomForge parent-operator
- One band-locked child profile (if you choose to use the guide)
- Your first sitting completed

## Prerequisites

- Linux, macOS, or WSL with a terminal
- A Hermes Agent install (`curl -fsSL https://hermes-agent.nousresearch.com/install.sh | bash`)
- An API key for at least one provider (or a local model via Ollama)
- About 30 minutes

If install is failing, see the [official installation guide](https://hermes-agent.nousresearch.com/docs/getting-started/installation).

---

## Block 1 — Set up your adult profile (0–10 min)

```bash
hermes setup
hermes doctor
```

Verify `hermes doctor` is clean. Then create a profile for yourself:

```bash
hermes profile create parent
```

Write a SOUL that tells Hermes it's a WisdomForge parent-operator. Start from the template:

```bash
cp examples/souls/wisdomforge-parent-operator.md ~/.hermes/profiles/parent/SOUL.md
```

Edit the SOUL — replace placeholder names with your context. The key sections to keep intact: WisdomForge Role, Core Values, The Four Bands, and the "what I do not do" list. These are the safety constraints.

Create a minimal USER.md:

```bash
cat > ~/.hermes/profiles/parent/USER.md << 'EOF'
I am the parent operating WisdomForge for my family.
I want help preparing sittings, not replacing me as teacher.
EOF
```

**Verify:**
```bash
hermes -p parent chat -q "Confirm you understand your role as a WisdomForge parent-operator."
```

The response should reference the parent-operator role, not claim to be a teacher or a child's friend.

---

## Block 2 — Pick a sitting and prepare (10–20 min)

1. Go to [smfwisdomforge.com/start](https://smfwisdomforge.com/start) and pick your child's age band.

2. Browse to a sitting. For a first sitting, we recommend:
   - **Little Thinkers (5–10):** AI → "A Tool, Not a Person"
   - **Young Minds (11–14):** Thinking → "How to Think"
   - **Emerging Adults (15–18):** Philosophy → "Circle You Control" (Stoics)
   - **Adult:** AI → "Education in the Age of AI"

3. Read the **parent briefing** on the sitting page. This is your 5-minute prep. The briefing tells you the edge, the trap, and what not to skip.

4. Read the **hard edges** — 2–4 things you must not do or must not skip.

5. Ask your adult profile to summarize if you're short on time:
   ```bash
   hermes -p parent chat -q "Summarize the parent briefing for the WisdomForge sitting 'Circle You Control' in 3 sentences."
   ```

6. Read the **if they say** section — these are the anticipated misreadings and how to respond. You're looking for these during the sitting.

You are now prepared. Do not start the child's session yet.

---

## Block 3 — Optional: set up the child's guide (20–30 min)

The Hermes guide is optional. Sittings work with zero AI — the reading, try-this, and dinner question are all human activities. If you want the guide, set up a band-locked child profile.

**The setup prompt** (also at [smfwisdomforge.com/hermes](https://smfwisdomforge.com/hermes)):

```text
I'd like your help designing a private, child-facing Hermes profile for one
WisdomForge age band. Read and follow START-HERE.md, BANDS.md, and DECISIONS.md
from the WisdomForge kids Hermes kit. Ask the band first. Propose conservative
defaults. Show the full design. Create a fresh profile. Do not clone my adult
profile.
```

The kids profiles repo is at [smfworks/wisdomforge-kids-Hermes-profiles](https://github.com/smfworks/wisdomforge-kids-Hermes-profiles). Clone it so the setup agent can read the files:

```bash
git clone https://github.com/smfworks/wisdomforge-kids-Hermes-profiles ~/wisdomforge-kids
```

Send the setup prompt from your adult profile:

```bash
hermes -p parent chat -q "I'd like your help designing a private, child-facing Hermes profile for one WisdomForge age band. Read and follow START-HERE.md, BANDS.md, and DECISIONS.md from ~/wisdomforge-kids. Ask the band first."
```

The setup agent will ask you the band, propose conservative defaults, show the full design, and wait for your approval before creating the profile.

**Critical rules:**
1. Fresh profile only. Never clone your adult profile into a child profile.
2. Band-locked. The profile stays in one age band.
3. Tool-poor. Fewer tools than yours.
4. No child PII. No names, school, photos, or location in the profile.
5. You approve every tool addition and permission change.

If you have multiple children, create a separate profile for each. See the "Multi-Child Families" section in the [parent-operator guide](wisdomforge-parent-operator.md).

---

## Block 4 — Run the sitting

You're prepared. The child is ready. Here's the order:

1. **Parent briefing** — you already read this. Don't re-read it with the child.
2. **Reading** — the child reads (or you read together for Little Thinkers).
3. **Big idea** — say it once. Let it land. Don't explain it.
4. **Try this** — hands-on. No model. This is the human-first part.
5. **Guide panel** — OPTIONAL. If you set up a child profile in Block 3, use the "Light this sitting" bridge on the sitting page to copy the USER.md line and opening prompt. If you didn't set up a profile, skip this.
6. **Dinner question** — ask it at dinner. One sentence. Mixed-age table.
7. **If they say** — listen for the anticipated misreading. Use the parent reply as a starting point, not a script.
8. **Integrity rule** — name it. Post it if it helps.
9. **Mark complete** on the site (device-local — no account needed).

### When to put the guide away

- If the child is engaging with the try-this, don't interrupt with the guide.
- If the child asks a question the sitting doesn't cover, answer it yourself first.
- If the topic is tender (Faith & Reason, the problem of evil, death), the guide is OFF. You are the person in the room.
- The guide is a tool, not a teacher. You are the teacher.

---

## After the first sitting

You did it. Here's what to do next:

1. **Reflect** — what worked? What didn't? What did your child say that surprised you?
2. **Pick the next sitting** — the site's progress tracker remembers what you completed.
3. **Explore deeper** — use the search API to study a figure or topic more:
   ```
   hermes -p parent chat -q "Search smfwisdomforge.com/api/search for 'epictetus dichotomy control' and summarize the key findings."
   ```
4. **If you want the full team** — the [Minimal Viable Team](minimal-viable-team.md) guide and the phase docs in this repo build out a multi-agent operation. But you don't need them to run sittings. You just proved that.

---

## Quick reference

| What | Where |
|------|-------|
| Academy site | [smfwisdomforge.com](https://smfwisdomforge.com) |
| Pick a band | [smfwisdomforge.com/start](https://smfwisdomforge.com/start) |
| Hermes setup | [smfwisdomforge.com/hermes](https://smfwisdomforge.com/hermes) |
| Method | [smfwisdomforge.com/method](https://smfwisdomforge.com/method) |
| Parents guide | [smfwisdomforge.com/parents](https://smfwisdomforge.com/parents) |
| Kids profiles repo | [smfworks/wisdomforge-kids-Hermes-profiles](https://github.com/smfworks/wisdomforge-kids-Hermes-profiles) |
| This repo (adult team) | [smfworks/hermes-ai-team](https://github.com/smfworks/hermes-ai-team) |
| Full parent-operator guide | [wisdomforge-parent-operator.md](wisdomforge-parent-operator.md) |
| Hermes docs | [hermes-agent.nousresearch.com/docs](https://hermes-agent.nousresearch.com/docs) |

The academy is the curriculum. You are the teacher. Hermes is the assistant. That order matters.