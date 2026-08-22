---
name: paper-or-market-deep-dive
description: "Use when researching a paper, announcement, or market move that should become a citable vault note. Search primary sources, score relevance, and file a structured note."
version: 1.0.0
author: Atlas
---

# Paper or Market Deep-Dive

## When to use
- A new paper, filing, product launch, or competitor move needs a vault note.
- The operator asks for a scan of a domain and a recommendation, not a chat summary.
- A nightly research cron needs a repeatable procedure.

## Procedure

1. Restate the question in one sentence and name the vault path you will write to
   (for example `~/AgentVault/Research/papers/` or `~/AgentVault/Research/market/`).
2. Search primary sources first:
   - Papers: arXiv / official PDF / author page
   - Products: vendor docs, release notes, GitHub tags
   - Markets: official filings, earnings transcripts, primary data
3. Extract exact numbers, dates, and claims. Quote them. Do not paraphrase a
   number you did not read.
4. Score relevance to the operator's work in one paragraph: why it matters,
   what to do, and what *not* to do.
5. Write the note using the Phase 1 vault format (`Date`, `Source`, `Tags`,
   `Summary`, `Key Findings`, `Relevance`, `Sources`).
6. Tell the operator the absolute path and the one-line recommendation.

## Pitfalls
- Search-result blurbs go stale. Open the source page or PDF.
- Paywalled or blocked pages: say so. Do not invent the missing section.
- A chat summary is not a vault note. If it is not on disk, it did not happen.
- Do not mix unverified rumor with cited findings. Separate them.

## Verification
- [ ] The note exists at the stated path (`ls` or `cat` succeeds)
- [ ] Required fields are present: date, source, summary, at least one finding
- [ ] Every number in the note appears in a cited source
- [ ] Relevance section names a next action or an explicit "watch only"
