# Idea To Contract

## Purpose

Map each raw idea item to product contract, architecture contract, task, and
acceptance evidence.

## Mapping Columns

| Idea Item | Product Path | Architecture Path | Task Path | Acceptance | Status |
| --- | --- | --- | --- | --- | --- |
| _(waiting-for-idea)_ | | | | | waiting-for-idea |

## Rules

- Every idea item maps to a task or explicit out-of-scope record.
- Product behavior lives under [../product/](../product/README.md).
- Implementation shape lives under [../architecture/](../architecture/README.md).
- Executable work lives under [../execution/tasks/](../execution/tasks/README.md).
- Status must be honest: waiting-for-idea, design-only, not-started, etc.

## Seed Flow

After [raw-idea.md](raw-idea.md) is filled, add one row per major requirement.
Mirror the matrix in [../execution/traceability.md](../execution/traceability.md).

## Status

waiting-for-idea. Matrix is empty until intake task 00 completes.
