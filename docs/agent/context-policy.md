# Context Policy

## Purpose

Help a ~20B parameter agent with 32k context work without losing tasks.

## Read Narrow

- Prefer README routing over full-tree reading.
- Open only files named by the task and skill.
- Summarize long discoveries into the proper ledger file.

## Durable State

- Active task lives in [../execution/active-session.md](../execution/active-session.md).
- Next work lives in [../execution/current-blockers.md](../execution/current-blockers.md).
- Never depend on chat for durable state.

## File Size

Every file is <= 50 lines. This keeps many contracts loadable in one session.

## When Context Grows

Update ledgers before continuing implementation. Split files approaching the cap.

## Optimization

Correctness, evidence, and task continuity over speed.
