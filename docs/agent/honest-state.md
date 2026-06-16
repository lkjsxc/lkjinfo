# Honest State

## Purpose

Nothing may present a state that did not actually happen.

## Product Paths

- No fake success, content, data, or protocol results.
- No placeholder rows or mock completed behavior.
- Unimplemented behavior is marked not-started or design-only in docs.
- Synthetic fixtures are test-only and explicitly labeled.

## Verification

- No claiming an unrun gate.
- Handoff quotes actual command output.
- Missing evidence means "not found by this method", not absence.

## Documentation

- Docs do not describe unbuilt behavior as existing.
- [../current-state.md](../current-state.md) is the status ledger.
- When docs and code disagree, fix the disagreement first.

## Why

Agent outputs compound into future context. One fabricated success poisons the chain.
