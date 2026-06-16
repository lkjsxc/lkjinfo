# AGENTS.md

## Purpose

Entry point for coding agents working in this repository. Read this file first.

## What This Kit Is

lkjinfo is a repository-local operating system for agents. Copy it into a
project root, describe a software idea, and follow [docs/](docs/README.md).

## Non-Negotiable Rules

1. [docs/](docs/README.md) is the contract. Update docs and code together,
   including [docs/current-state.md](docs/current-state.md).
2. Every file stays at or below 50 lines. See
   [docs/repository/line-limits.md](docs/repository/line-limits.md).
3. Honest state only. See [docs/agent/honest-state.md](docs/agent/honest-state.md).
4. Synthetic fixtures are test-only. Unrun gates did not pass.
5. Chat is not durable state. The repository stores the next task.

## Read Order

1. [docs/current-state.md](docs/current-state.md)
2. [docs/agent/README.md](docs/agent/README.md)
3. [docs/execution/current-blockers.md](docs/execution/current-blockers.md)
4. The chosen task under [docs/execution/tasks/](docs/execution/tasks/README.md)
5. The matching skill under [docs/agent/skills/](docs/agent/skills/README.md)
6. Contracts named by the task and skill

## Task Routing

- If the user names a task, do that task.
- Otherwise take the first open blocker in
  [docs/execution/current-blockers.md](docs/execution/current-blockers.md).
- New idea: run
  [docs/execution/tasks/00-capture-idea.md](docs/execution/tasks/00-capture-idea.md).
- Every requirement becomes an objective, assumption, open question,
  out-of-scope item, or task. None may remain only in chat.

## Verification

Run `python scripts/check-all.py`. See
[docs/operations/verification.md](docs/operations/verification.md).
Passing gates print exactly one line: `ok <gate>`.

## Handoff

Follow [docs/agent/handoff.md](docs/agent/handoff.md). Report evidence with
next step: task path, files, gate, acceptance line.
