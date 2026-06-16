# Skill: Debugging

## Purpose

Reproduce, isolate, fix, and record a defect with evidence.

## Trigger

A gate fails, a user reports incorrect behavior, or docs and code disagree.

## Context

- [../../quality/regression-ledger.md](../../quality/regression-ledger.md)
- [../../agent/honest-state.md](../../agent/honest-state.md)
- Relevant task and contracts

## Procedure

1. Reproduce with a minimal command or test.
2. Record exact failure output in active-session or task file.
3. Isolate the owning module per source-map.
4. Fix with the narrowest change; add regression test.
5. Run focused gate and check-all if docs moved.
6. Add regression-ledger row if the bug must never return.

## Checks

Focused repro test plus task gate.

## Must Not

Mask failures with fake success. Close task without acceptance evidence.

## Handoff

Repro command, fix path, gate output, regression-ledger update if any.
