# GitHub Copilot Coding Agent Onboarding

This document defines how automated coding agents (including GitHub Copilot “Coding Agent” workflows) must interact with the PrimeCodex repository.

## Core Principles
- Determinism: All changes must keep tests green (`pytest -q`).
- Type Safety: Pyright must report zero errors (`pyright`).
- Security First: Never add secrets, API keys, or credential patterns. Do not touch `.env`.
- Minimal Surface: Change only what is required for the task/issue.
- Traceability: Every PR references exactly one tracked issue (except urgent security hotfixes).
- Schema Stability: Maintain backward compatibility with `schema/cli_output.schema.json` unless the issue explicitly authorizes a breaking change.

## Workflow Summary
1. Create a branch from `main` using naming convention (see below).
2. Implement focused changes with small, logically grouped commits.
3. Run local validation (tests + typing + lint) before opening PR.
4. Open PR using template; ensure checklist completed.
5. Await human review for merge authorization.

## Branch Naming Conventions
Pattern: `type/short-kebab-summary` where `type` ∈ {`feat`,`fix`,`chore`,`docs`,`refactor`,`test`,`ci`,`security`}.
Examples:
- `feat/memory-layering`
- `fix/archetype-phase-drift`

Agent-created branches MUST include an issue reference in the first commit body line: `Refs #<issue-number>`.

## Commit Message Guidelines
Format (Conventional Core subset): `type(scope)?: summary`
Examples:
- `feat(memory): add temporal window stitching`
- `fix(cli): correct default novelty handling`

Body (if present) SHOULD include:
- Rationale (why)
- Implementation notes (how)
- Constraints or follow-ups (future)

Include `BREAKING:` prefix in body lines if schema or public CLI flags change.

## Required Local Validation Steps
Agents must (simulate) executing the following before PR creation:
```bash
pytest -q
pyright
```
(If these commands would fail, do not open PR; instead adjust changes.)

Optional fast subset while iterating:
```bash
pytest -k unity -q
```

## File & Code Boundaries
- Do not modify history rewrite scripts unless security issue.
- Avoid editing `SECURITY.md` except for vetted security tasks.
- Keep `openai_connect.py` lazy instantiation pattern intact.
- Preserve typing markers (`emota/py.typed`).

## Adding Dependencies
1. Justify necessity in PR body.
2. Prefer stdlib first.
3. If accepted, update only `pyproject.toml`; regenerate lock (future if added). Add minimal version pin.
4. Add import usage tests.

## JSON Schema / CLI Contract Changes
- Must update `schema/cli_output.schema.json` + regenerate example in PR body.
- Provide migration notes.
- Bump minor version (or major if breaking) in `CHANGELOG.md`.

## Testing Guidelines
- No network I/O in unit tests (OpenAI calls must be mocked or skipped).
- Add focused tests for new logic; do not overfit.
- Keep test runtime lean (<5s aggregate ideal).

## Logging & Telemetry
- Use `logging_utils.configure_logger` for new entry points.
- New structured fields must not break existing JSON parsing assumptions; additive only.

## Memory & Persistence
- Maintain backward-compatible shape of stored episodic entries.
- If structure changes, include upgrade path or auto-migration logic with tests.

## Security Rules
- No plaintext secrets or tokens.
- Do not weaken `.gitignore`.
- Secret-like additions (e.g., `API_KEY=` patterns) will be rejected.

## PR Review Checklist (See Template)
Agent must self-certify all checklist items. Failing checks => human rejection.

## Labels (Recommended)
Agents may apply:
- `area:memory`, `area:cli`, `area:architecture`, `area:security`
- `type:feature`, `type:fix`, `type:refactor`, `type:docs`

## Failure / Rollback
If a change introduces instability:
1. Open `fix/` branch referencing the original PR.
2. Add regression test first.
3. Patch minimal code to restore green state.

## Escalation
Security or data integrity concerns MUST halt automation and require explicit human approval before proceeding.

---
This onboarding spec may evolve; agents should diff against `main` before large multi-file operations to reduce drift.
