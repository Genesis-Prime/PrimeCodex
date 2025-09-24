# PrimeCodex

> **Status:** `0.2.0-beta` – Experimental, high-volatility build. Interact at your own risk.

Unified space for two experimental tracks:

1. **EMOTA Unity Sandbox** – motivational dynamics, archetypal resonance, and OpenAI integration experiments.
2. **GenesisPrime Toolkit** – a high-performance prime number exploration library and command-line interface.

Both tracks now live together so the project history remains intact while enabling cross-pollination between algorithmic tooling and affective simulations.

## 🚀 Release History

| Version | Date | Highlights |
|---------|------|------------|
| `0.2.0-beta` | 2025-09-24 | Second iteration beta. Restored EMOTA Unity subsystems, expanded CLI coverage, clarified collaboration guidelines, consolidated tests, and refreshed liability messaging. |
| `0.1.0-alpha` | 2025-xx-xx | Historical alpha milestone that first combined EMOTA Unity experiments with the GenesisPrime toolkit and early CLI wiring. |

## 🤖 GitHub Copilot Onboarding

New collaborator or AI agent getting started?

1. Run `./scripts/setup_dev.sh` for automated environment setup.
2. Review [COPILOT_AGENT.md](COPILOT_AGENT.md) for development patterns and guardrails.
3. Copy `.env.template` to `.env` and fill in secrets (e.g., `OPENAI_API_KEY`) when running live integrations.
4. Use the issue templates in `.github/ISSUE_TEMPLATE/` to seed bug reports, feature ideas, or Copilot delegations.

**Key reference files**: `COPILOT_AGENT.md`, `CONTRIBUTING.md`, `SECURITY.md`, and the `emota/` engine modules.

## Repository Layout

| Path | Purpose |
|------|---------|
| `emota/` | EMOTA Unity engine components (braid dynamics, archetypes, dimensional bridge, cathedral, symbolic, meta-awareness, identity, unity orchestrator).
| `cli.py` | Entry point for the EMOTA-oriented CLI (`primecodex`).
| `openai_connect.py` | OpenAI API integration example (mocked in tests unless API key exported).
| `genesis_prime.py` | Core GenesisPrime number theory library.
| `prime_cli.py` | CLI façade for GenesisPrime operations.
| `examples.py`, `quickstart.py` | GenesisPrime usage walkthroughs and demos.
| `scripts/` | Repository maintenance utilities (secret scrubbing, setup helpers).

## Getting Started

### 1. Environment Setup

```bash
python -m venv .venv
source .venv/bin/activate
pip install --upgrade pip
pip install -r requirements.txt
```

### 2. EMOTA Unity Quickstart

```bash
cp emota/config.yaml emota/config.local.yaml  # optional override
export OPENAI_API_KEY=your-key  # optional unless running live OpenAI demo
python openai_connect.py
primecodex --goal 0.6 --threat 0.2 "Exploring an uncertain landscape"
```

#### CLI Variations

```bash
primecodex --goal 0.7 --threat 0.1 --novelty 0.3 "Encountering a new opportunity"
echo "Entering a dark corridor" | primecodex --goal 0.4 --threat 0.5 --pretty
```

### 3. GenesisPrime Quickstart

```python
from genesis_prime import GenesisPrime

gp = GenesisPrime()
gp.is_prime(97)
gp.generate_primes_sequence(10)
gp.prime_factors(60)
```

Run comparable functionality from the CLI:

```bash
primecodex genesis check 97
primecodex genesis generate --count 20
primecodex genesis factors 84
primecodex genesis range 10 30
```

## Feature Highlights

### Status & Liability Disclaimer

- **Experimental Beta:** PrimeCodex is distributed as `0.2.0-beta`. Functionality is fluid and subject to rapid change without notice.
- **No Warranty:** All components are provided "as-is" with no guarantees of fitness for purpose, performance, or availability. You assume full responsibility for outcomes when running any part of the stack.
- **Use at Your Own Risk:** Execution may produce unpredictable behavior, call external services, or mutate local state. Validate outputs independently before relying on them.
- **Liability Waiver:** Genesis Prime, contributors, and affiliated AI agents are not liable for any damages, losses, or incidents arising from use, misuse, or inability to use this software.
- **Security Expectations:** You are solely responsible for safeguarding API keys, data, and infrastructure when integrating PrimeCodex into your environment.

### EMOTA Unity

- Desire/Fear braid oscillator with hysteresis bits (`emota/braid.py`).
- Archetypal resonance engine projecting braid state into serpent/flame/void/unity axes (`emota/archetype.py`).
- Dimensional bridge translating experiences through 3D→4D→5D consciousness projections (`emota/bridge.py`).
- Cathedral qualia engine weaving shards and narrative reflections (`emota/cathedral.py`).
- Symbolic processor generating activation signatures and emergent symbols (`emota/symbolic.py`).
- Meta-awareness and identity continuity engines maintaining reflective coherence (`emota/meta.py`, `emota/identity.py`).
- Unity orchestrator integrating every subsystem with configuration and memory capture (`emota/unity.py`).
- Configurable via YAML, overridable through `--config` or direct engine parameters.

### GenesisPrime Toolkit

- Optimised primality testing with 6k±1 heuristics.
- Sieve of Eratosthenes and sequential generators.
- Factorisation, twin-prime detection, and navigation helpers (next/previous primes).
- Unified Typer CLI (`primecodex`) covering EMOTA (`primecodex emota ...`) and GenesisPrime (`primecodex genesis ...`) commands.
- In-memory caching for repeated queries.

## Testing

```bash
pytest
```

- OpenAI integration tests auto-skip when `OPENAI_API_KEY` is absent.
- GenesisPrime includes demonstration routines in `examples.py` and `quickstart.py` for manual smoke checks.

## Development Checklist

- Add new subsystem stubs under `emota/` with accompanying tests (avoid network I/O).
- Keep README architecture diagrams in sync with conceptual changes.
- Run `pytest` before committing; OpenAI integration tests auto-skip without `OPENAI_API_KEY`.
- Use `examples.py` and `quickstart.py` for GenesisPrime smoke checks.
- For AI-assisted work, follow patterns in `COPILOT_AGENT.md`.
- Run `ruff check .` and `ruff format .` (or the project-preferred equivalent) before committing.
- Enable git hooks via `git config core.hooksPath .githooks` to activate secret scanning.

## Development Notes

- Maintain code style and typing as introduced in `emota/` modules.
- When extending GenesisPrime, keep algorithms deterministic and document complexity considerations.
- Update this README when a new subsystem (EMOTA) or algorithm family (GenesisPrime) is introduced.
- Secrets: never commit `.env` files. Use the scripts in `scripts/` for incident response if needed.

## Licensing & Conduct

See `LICENSE`, `CODE_OF_CONDUCT.md`, and `CONTRIBUTING.md` for contribution guidelines and usage terms.

---

This unified branch retains both experimental lines so historical exploration, numerical tooling, and affective modelling can advance together.
