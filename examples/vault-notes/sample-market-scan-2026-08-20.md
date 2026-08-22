# Sample Market Scan: Open-Weight Agent Harnesses, August 2026

**Date:** 2026-08-20
**Source:** Vendor release notes and public GitHub tags (composite scan)
**Tags:** research, market, competitor, agent-harness

## Summary
Open-weight agent harnesses continue to converge on the same stack: persistent
identity files, bounded memory, scheduled jobs, and a shared task board. The
differentiator is no longer "can it call tools" — it is whether the team can
compound knowledge and stay honest about what it verified.

## Key Findings
- Identity files (SOUL / personality) are now treated as first-class prompt
  slots, not optional flavor text.
- Scheduled jobs that skip a self-contained prompt still fail silently in
  production. Gateway health is the usual missing check.
- Shared kanban plus a coordinator role reduces chat noise more than adding
  another generalist profile.

## Relevance to Your Organization
If you already have one capable agent, the next hour of work is identity +
vault + one scheduled research job — not a sixth profile. Use this note as a
template: cite primary sources, keep findings short, and name the next action.

## Sources
- [Hermes Agent docs index](https://hermes-agent.nousresearch.com/docs/llms.txt)
- [This repository's Phase 1 vault format](../../docs/01-phase-1-first-agent.md)
