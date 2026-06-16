# Traceability

## Purpose

Matrix mapping idea items to contracts, tasks, gates, and status.

## Matrix

| Idea Item | Contract Path | Task Path | Gate | Status |
| --- | --- | --- | --- | --- |
| _(none)_ | | | | waiting-for-idea |

## Rules

- Every idea item must map to a task or explicit out-of-scope record.
- Every open blocker must have a task path in
  [current-blockers.md](current-blockers.md).
- Update this file when intake seeds rows in
  [../intake/idea-to-contract.md](../intake/idea-to-contract.md).

## Waiting State

waiting-for-idea is explicit until task 00 completes. Empty matrix alone is
not sufficient; the status column must say waiting-for-idea.

## Status

waiting-for-idea
