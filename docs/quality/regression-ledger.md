# Regression Ledger

## Purpose

Record bugs that must never return once fixed.

## Ledger

| ID | Bug | Repro | Fix | Test | Date |
| --- | --- | --- | --- | --- | --- |
| _(none)_ | | | | | |

## When To Add

After debugging skill fixes a defect users or gates could hit again.

## Entry Rules

- Repro command or steps.
- Fix commit or path.
- Test name that guards regression.

## Must Not

Log hypothetical bugs. Log fixes without a guarding test when feasible.

## Skill

[../agent/skills/debugging.md](../agent/skills/debugging.md)
