# Skill: Idea Intake

## Purpose

Convert a raw user idea into goals, assumptions, questions, and traceability.

## Trigger

The user describes a new software idea or raw-idea.md is empty.

## Context

- [../../intake/raw-idea.md](../../intake/raw-idea.md)
- [../../intake/assumptions.md](../../intake/assumptions.md)
- [../../intake/open-questions.md](../../intake/open-questions.md)
- [../../intake/idea-to-contract.md](../../intake/idea-to-contract.md)
- [../../execution/traceability.md](../../execution/traceability.md)

## Procedure

1. Save the idea verbatim in raw-idea.md.
2. Extract goals, non-goals, constraints, users, surfaces, risks, unknowns.
3. Add assumptions with accepted or open-question status.
4. Split blocking vs non-blocking questions.
5. Seed idea-to-contract and traceability rows.
6. Update current-state and blocker row 1 status.

## Checks

`python scripts/check-all.py`

## Must Not

Invent product details the user did not state without labeling assumptions.
Leave requirements only in chat.

## Handoff

Name next task 01-normalize-requirements with acceptance evidence.
