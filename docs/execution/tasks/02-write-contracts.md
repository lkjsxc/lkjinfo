# Write Contracts

## Purpose

Write vision, product, and architecture contracts before any app source.

## Status

not-started

## Depends On

[01-normalize-requirements.md](01-normalize-requirements.md)

## Files To Read

- [../../vision/README.md](../../vision/README.md)
- [../../product/README.md](../../product/README.md)
- [../../architecture/README.md](../../architecture/README.md)
- [../../agent/skills/contract-design.md](../../agent/skills/contract-design.md)

## Files To Touch

- Vision, product, and architecture files listed in traceability.
- [../../current-state.md](../../current-state.md)
- [../../execution/traceability.md](../../execution/traceability.md)

## Focused Gate

```sh
python scripts/check-markdown.py
python scripts/check-readmes.py
python scripts/check-links.py
```

## Acceptance

- Product surfaces and journeys drafted with honest statuses.
- Architecture overview, domain, data, interfaces drafted.
- All touched docs pass focused gates. Blocker row 3 done with evidence.

## Must Not

Mark surfaces implemented. Write source code in this task.
