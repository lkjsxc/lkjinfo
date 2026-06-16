# Verification Gate

## Purpose

Install project-specific checks and make check-all authoritative for the app.

## Status

not-started

## Depends On

[05-first-vertical-slice.md](05-first-vertical-slice.md)

## Files To Read

- [../../operations/verification.md](../../operations/verification.md)
- [../../operations/ci.md](../../operations/ci.md)
- [../../agent/skills/test-gate.md](../../agent/skills/test-gate.md)
- [../../../scripts/check-all.py](../../../scripts/check-all.py)

## Files To Touch

- [../../../scripts/](../../../scripts/check-all.py) if new gates needed
- [../../operations/verification.md](../../operations/verification.md)
- [../../operations/ci.md](../../operations/ci.md)
- [../done-log.md](../done-log.md)

## Focused Gate

```sh
python scripts/check-all.py
```

## Acceptance

- check-all passes and is documented as the pre-handoff gate.
- CI doc says to run check-all.
- Project-specific tests wired into focused gates if required.
- Blocker row 7 done. done-log records evidence.

## Must Not

Claim check-all passes without running it. Skip kit checks when extending gates.
