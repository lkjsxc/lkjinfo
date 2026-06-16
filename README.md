# lkjinfo

## Purpose

A reusable instruction kit for AI coding agents. It is not an application.

## What It Does

When copied into a project root, lkjinfo turns a user idea into contracts,
architecture, tasks, source code, tests, verification, and handoff without
losing the next task between sessions.

## Quick Start

1. Copy this repository into your project root (Mode 1: empty repo; Mode 2:
   existing code stays untouched).
2. Put your idea in [docs/intake/raw-idea.md](docs/intake/raw-idea.md) or
   describe it to the agent in chat.
3. Ask the agent to follow [AGENTS.md](AGENTS.md).
4. Run `python scripts/check-all.py` after each session slice.
5. Keep every file at or below 50 lines. Split by ownership before growing.

## Modes

**Empty repository:** lkjinfo is the whole repository until task
04-bootstrap-project creates app source.

**Existing project:** install at the root without deleting existing files.
Integration happens only when a task names those files.

## Key Paths

| Path | Role |
| --- | --- |
| [AGENTS.md](AGENTS.md) | Agent entry and read order |
| [docs/current-state.md](docs/current-state.md) | Honest truth ledger |
| [docs/execution/current-blockers.md](docs/execution/current-blockers.md) | Task queue |
| [docs/agent/skills/](docs/agent/skills/README.md) | Procedure library |
| [scripts/check-all.py](scripts/check-all.py) | Verification gate |

## Assumptions

- Python 3 is available for check scripts.
- Target agent: about 20B parameters, 32k context, correctness over speed.
- No product stack is chosen until intake and task 03 complete.
