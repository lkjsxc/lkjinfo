# Verification

## Purpose

Gate commands that decide whether work is done.

## Gates

Run from repository root:

| Gate | Command |
| --- | --- |
| check-lines | `python scripts/check-lines.py` |
| check-markdown | `python scripts/check-markdown.py` |
| check-readmes | `python scripts/check-readmes.py` |
| check-links | `python scripts/check-links.py` |
| check-skills | `python scripts/check-skills.py` |
| check-tasks | `python scripts/check-tasks.py` |
| check-trace | `python scripts/check-trace.py` |
| check-all | `python scripts/check-all.py` |

## Rule

A gate that did not run did not pass. See [../agent/honest-state.md](../agent/honest-state.md).

## Output

See [quiet-output.md](quiet-output.md).

## Status

Kit gates are implemented. Project-specific gates extend in task 06.
