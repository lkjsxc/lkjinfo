# Principles

## Purpose

Design principles for the future product and for agents building it.

## Principles

1. **Honest state:** product code shows real data or explicit real states only.
   See [../agent/honest-state.md](../agent/honest-state.md).
2. **Small files:** every repository file stays at or below 50 lines.
3. **User-value slices:** ship the narrowest end-to-end behavior that helps a user.
4. **Explicit scope:** in-scope and out-of-scope are written, not implied.
5. **Evidence before claims:** gates must run; missing evidence is not absence.
6. **Docs and code move together:** contracts update in the same change as code.
7. **Task continuity:** the next executable task is always visible in the repo.

## Status

implemented for the instruction kit. Product-specific principles extend after intake.

## Application

Agents apply these during contract design and every implementation slice.
