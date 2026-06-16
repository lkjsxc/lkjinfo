# First Vertical Slice

## Purpose

Implement the smallest useful end-to-end behavior for one user journey.

## Status

not-started

## Depends On

[04-bootstrap-project.md](04-bootstrap-project.md)

## Files To Read

- [../../product/user-journeys.md](../../product/user-journeys.md)
- [../../product/surfaces.md](../../product/surfaces.md)
- [../../architecture/source-map.md](../../architecture/source-map.md)
- Matching slice skill: ui, api, or data under [../../agent/skills/](../../agent/skills/README.md)

## Files To Touch

- Source and test paths named in traceability for the chosen journey.
- [../../product/surfaces.md](../../product/surfaces.md)
- [../../current-state.md](../../current-state.md)

## Focused Gate

Stack-specific test command for the slice plus `python scripts/check-lines.py`

## Acceptance

- One journey works end to end with real behavior or explicit real states.
- Tests prove success and at least one failure path.
- Surface status updated with evidence. Blocker row 6 done.

## Must Not

Fake data or placeholder success. Implement multiple journeys in one task.
