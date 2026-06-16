# Agent Maintenance

## Purpose

Self-maintenance of the lkjinfo instruction system.

## Triggers

- Stale docs or broken links found during a session.
- Files approaching the 50-line cap.
- Repeated friction suggesting a new or sharper skill.
- Preventable errors that checks do not yet catch.

## Actions

- Fix stale docs in the same session when cheap; otherwise add a blocker row.
- Split files by ownership before they hit 50 lines.
- Add or update skills under [skills/](skills/README.md).
- Extend scripts under [../../scripts/](../../scripts/check-all.py) when a
  preventable defect is found.

## Skill

Use [skills/maintenance.md](skills/maintenance.md) for procedure detail.

## Must Not

Weaken honest-state or line-cap rules during maintenance.
