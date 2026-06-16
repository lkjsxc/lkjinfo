# Skill: Data Slice

## Purpose

Persistence, schemas, migrations, and data ownership changes.

## Trigger

A task touches storage, schemas, migrations, or data lifecycle.

## Context

- [../../architecture/data.md](../../architecture/data.md)
- [../../architecture/domain-model.md](../../architecture/domain-model.md)
- [../../agent/decision-defaults.md](../../agent/decision-defaults.md)

## Procedure

1. Update data.md and domain-model.md before schema code.
2. Name data owner per entity. Document deletion behavior.
3. Implement migration or store with explicit error paths.
4. Add tests with test-only fixtures; never leak into product.
5. Run task focused gate.

## Checks

Task focused gate. Data contract updated in same change.

## Must Not

Fake persisted data in product. Delete user data without surfacing behavior.

## Handoff

Schema paths, migration commands run, gate output.
