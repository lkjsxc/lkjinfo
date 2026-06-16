# Skill: Test Gate

## Purpose

Add tests and run focused verification for a behavior slice.

## Trigger

A task acceptance requires tests or a focused gate.

## Context

- [../../quality/test-strategy.md](../../quality/test-strategy.md)
- [../../quality/definition-of-done.md](../../quality/definition-of-done.md)
- Task focused gate section
- [../../agent/honest-state.md](../../agent/honest-state.md)

## Procedure

1. Identify the behavior owner from source-map.
2. Add tests at that owner level.
3. Label synthetic fixtures test-only.
4. Run the task focused gate; capture one-line output.
5. Record evidence in done-log when task completes.

## Checks

Task focused gate. `python scripts/check-all.py` when docs change too.

## Must Not

Assert behavior the system lacks. Import test fixtures into product paths.

## Handoff

Quote actual gate output. List tests added and commands not run with reasons.
