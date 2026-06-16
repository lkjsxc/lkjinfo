# Recovery

## Purpose

What to do when checks fail, links break, files exceed 50 lines, or state disagrees.

## check-lines Fails

Split the named file by ownership. Re-run `python scripts/check-lines.py`.

## check-markdown / check-readmes / check-links Fail

Fix shape, TOC links, or broken relative paths. Re-run the failing gate.

## check-skills / check-tasks Fail

Align headings with [../../templates/](../../templates/task.md). Fix blocker links.

## check-trace Fails

Ensure traceability has rows or waiting-for-idea. Every open blocker has a task.

## State Disagreement

If docs and code disagree, fixing the disagreement is the first task per
[../current-state.md](../current-state.md).

## Stale Blockers

Update current-blockers.md and active-session.md before handoff.
