# Handoff

## Purpose

Evidence-based session end. Handoff is evidence, not narrative.

## Final Report Order

1. What changed and why (two sentences or fewer).
2. Docs updated (paths).
3. Source and tests touched (paths).
4. Commands run with actual one-line results (`ok <gate>` or failure tail).
5. Commands not run with reasons.
6. Current task status.
7. Next executable step: task path, files to touch, gate, acceptance line.

## Rules

- Never claim a gate passed without running it.
- Failure handoffs name evidence, hypothesis, and where to resume.
- Numbers over adjectives: "check-links fails on 3 files" beats "mostly passing".
- Put durable facts in repo files, not only in chat.

## Continuity

Next session starts from [../current-state.md](../current-state.md) and
[../execution/current-blockers.md](../execution/current-blockers.md).
