# Capture Idea

## Purpose

Capture the user software idea into durable intake docs and seed traceability.

## Status

waiting-for-idea

## Depends On

Nothing. First blocker.

## Files To Read

- [../../intake/raw-idea.md](../../intake/raw-idea.md)
- [../../intake/assumptions.md](../../intake/assumptions.md)
- [../../agent/skills/idea-intake.md](../../agent/skills/idea-intake.md)
- [../../execution/traceability.md](../../execution/traceability.md)

## Files To Touch

- [../../intake/raw-idea.md](../../intake/raw-idea.md)
- [../../intake/assumptions.md](../../intake/assumptions.md)
- [../../intake/open-questions.md](../../intake/open-questions.md)
- [../../intake/idea-to-contract.md](../../intake/idea-to-contract.md)
- [../../execution/traceability.md](../../execution/traceability.md)
- [../../current-state.md](../../current-state.md)
- [../current-blockers.md](../current-blockers.md)

## Focused Gate

```sh
python scripts/check-all.py
```

## Acceptance

- Raw idea saved in raw-idea.md (not placeholder text).
- Initial assumptions recorded with status.
- Traceability seeded with at least one row or explicit items.
- Blocker row 1 moves from waiting-for-idea to done or in-progress with evidence.

## Must Not

Invent product details without assumptions. Leave requirements only in chat.
