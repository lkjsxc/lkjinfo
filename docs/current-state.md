# Current State

## Purpose

Honest truth ledger for lkjinfo. Update this file when behavior or status moves.

## Summary

| Area | Status |
| --- | --- |
| Instruction kit (docs, scripts, templates) | implemented |
| Product application | waiting-for-idea |
| App source code | not-started |
| Product contracts | waiting-for-idea |
| Architecture contracts | waiting-for-idea |

No product app has been specified yet. The queue is
[execution/current-blockers.md](execution/current-blockers.md).

## Status Values

implemented, waiting-for-idea, design-only, not-started, blocked,
out-of-scope, open-question.

## Implementation Rule

Behavior is implemented only when source, tests, docs, and gate evidence agree.
If docs and code disagree, fixing the disagreement is the first task.

## Honesty Rules

- No fake success, placeholder product behavior, or unrun gate claims.
- Missing evidence means "not found by this method", not absence.
- Synthetic fixtures are test-only.

## Next Step

First open blocker: capture the user idea per
[execution/tasks/00-capture-idea.md](execution/tasks/00-capture-idea.md).
