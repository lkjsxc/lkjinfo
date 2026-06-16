# Commit Protocol

## Purpose

How agents commit work and align commits with handoff evidence.

## When Git Is Available

- Commit small verified slices after focused gate passes.
- Message states what changed and why in one or two sentences.
- Include docs, source, and tests for the same contract in one commit when
  they belong together.

## Handoff Alignment

Commit scope must match [../agent/handoff.md](../agent/handoff.md):
- Docs updated listed in handoff must be in the commit or a named prior commit.
- Commands run in handoff must match commands actually executed.

## When Git Is Unavailable

Still update handoff, [../current-state.md](../current-state.md), blockers,
tasks, and [../execution/done-log.md](../execution/done-log.md).

## Must Not

Do not commit secrets. Do not claim tested behavior without gate evidence.
