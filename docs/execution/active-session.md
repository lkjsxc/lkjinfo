# Active Session

## Purpose

Hold current session state so the next agent does not depend on chat.

## Status

No active session.

## Fields

When a session runs, fill:

| Field | Value |
| --- | --- |
| Task | |
| Reason | |
| Skill | |
| Files Read | |
| Files Touched | |
| Gate | |
| Next Action | |

## Update Rule

Write this file at loop step 3 in [../agent/work-loop.md](../agent/work-loop.md).
Clear or update at handoff.
