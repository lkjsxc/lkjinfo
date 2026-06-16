# Bootstrap Project

## Purpose

Create app source skeleton only after contracts and stack exist.

## Status

not-started

## Depends On

[03-select-stack.md](03-select-stack.md)

## Files To Read

- [../../architecture/source-map.md](../../architecture/source-map.md)
- [../../architecture/tech-stack.md](../../architecture/tech-stack.md)
- [../../repository/code-style.md](../../repository/code-style.md)
- [../../agent/skills/implementation-slice.md](../../agent/skills/implementation-slice.md)

## Files To Touch

- App paths named in source-map (new directories and entry files).
- [../../architecture/source-map.md](../../architecture/source-map.md)
- [../../current-state.md](../../current-state.md)

## Focused Gate

Stack-specific build or compile command recorded in this task when stack known.
Until then: `python scripts/check-all.py`

## Acceptance

- Skeleton compiles or runs per stack gate named in task update.
- source-map lists app areas with owners.
- No fake logic in skeleton; honest empty or minimal entry only.
- Blocker row 5 done with evidence.

## Must Not

Delete existing project files in Mode 2. Add product behavior beyond skeleton.
