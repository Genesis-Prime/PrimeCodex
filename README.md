# PrimeCodex

Unified space for two experimental tracks:

1. **EMOTA Unity Sandbox** – motivational dynamics, archetypal resonance, and OpenAI integration experiments.
2. **GenesisPrime Toolkit** – a high-performance prime number exploration library and command-line interface.

Both tracks now live together so the project history remains intact while enabling cross-pollination between algorithmic tooling and affective simulations.

## Repository Layout

| Path | Purpose |
|------|---------|
| `emota/` | EMOTA Unity engine components (braid dynamics, archetypes, unity integration).
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
pip install -e .[dev]
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
python prime_cli.py check 97
python prime_cli.py generate --count 20
python prime_cli.py factors 84
python prime_cli.py range 10 30
```

## Feature Highlights

### EMOTA Unity

- Desire/Fear braid oscillator with hysteresis bits (`emota/braid.py`).
- Archetypal resonance engine projecting braid state into serpent/flame/void/unity axes (`emota/archetype.py`).
- Unity wrapper coordinating configuration and state snapshots (`emota/unity.py`).
- Extensible placeholders for cathedral planning and symbolic bridges.
- Configurable via YAML, overridable through `--config` or direct engine parameters.

### GenesisPrime Toolkit

- Optimised primality testing with 6k±1 heuristics.
- Sieve of Eratosthenes and sequential generators.
- Factorisation, twin-prime detection, and navigation helpers (next/previous primes).
- Comprehensive CLI covering check, generate, factor, range, next/prev, twin, and stats commands.
- In-memory caching for repeated queries.

## Testing

```bash
pytest
```

- OpenAI integration tests auto-skip when `OPENAI_API_KEY` is absent.
- GenesisPrime includes demonstration routines in `examples.py` and `quickstart.py` for manual smoke checks.

## Development Notes

- Maintain code style and typing as introduced in `emota/` modules.
- When extending GenesisPrime, keep algorithms deterministic and document complexity considerations.
- Update this README when a new subsystem (EMOTA) or algorithm family (GenesisPrime) is introduced.
- Secrets: never commit `.env` files. Use the scripts in `scripts/` for incident response if needed.

## Licensing & Conduct

See `LICENSE`, `CODE_OF_CONDUCT.md`, and `CONTRIBUTING.md` for contribution guidelines and usage terms.

---

This unified branch retains both experimental lines so historical exploration, numerical tooling, and affective modelling can advance together.
