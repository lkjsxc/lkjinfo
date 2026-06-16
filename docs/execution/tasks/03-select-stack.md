# Select Stack

## Purpose

Choose or record the tech stack and create a decision record.

## Status

not-started

## Depends On

[02-write-contracts.md](02-write-contracts.md)

## Files To Read

- [../../architecture/tech-stack.md](../../architecture/tech-stack.md)
- [../../intake/raw-idea.md](../../intake/raw-idea.md)
- [../../agent/decision-defaults.md](../../agent/decision-defaults.md)
- [../../decisions/README.md](../../decisions/README.md)

## Files To Touch

- [../../architecture/tech-stack.md](../../architecture/tech-stack.md)
- New file under [../../decisions/](../../decisions/README.md) if needed
- [../../current-state.md](../../current-state.md)
- [../current-blockers.md](../current-blockers.md)

## Focused Gate

```sh
python scripts/check-all.py
```

## Acceptance

- tech-stack.md lists language, build, and test choices with status.
- Decision record exists for the stack choice.
- Blocker row 4 done with evidence.

## Must Not

Imply stack is chosen without decision record. Pick stack before contracts.
