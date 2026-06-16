# Line Limits

## Purpose

Every file in the repository is capped at 50 lines. No exceptions.

## Rules

- Target 35-45 lines so future edits have room.
- Split by ownership, not arbitrary halving.
- There are no generated-file exceptions.
- Split before reaching 50 lines when adding behavior.

## Enforcement

```sh
python scripts/check-lines.py
```

Passing output: `ok check-lines`.

## Split Recipe

1. Identify the owning concept.
2. Create a directory with README if the topic grows.
3. Move detail to child files; parent README links children.
4. Update [../architecture/source-map.md](../architecture/source-map.md) if
   source areas change.

## Decision

See [../decisions/0002-file-line-cap.md](../decisions/0002-file-line-cap.md).
