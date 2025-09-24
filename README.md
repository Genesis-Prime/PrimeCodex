# PrimeCodex

Experimental EMOTA Unity framework and OpenAI integration sandbox.

## 🤖 GitHub Copilot Onboarding

**New to this repository?** For streamlined development with AI assistance:

1. **Quick Setup**: Run `./scripts/setup_dev.sh` for automated environment setup
2. **Read**: [COPILOT_AGENT.md](COPILOT_AGENT.md) for AI development guidelines  
3. **Configure**: Copy `.env.template` to `.env` and add your OpenAI API key (optional)
4. **Explore**: Use issue templates for bug reports, features, or Copilot tasks

### Key Files for AI Context
- `COPILOT_AGENT.md` - Complete development guide and context
- `CONTRIBUTING.md` - Contribution guidelines
- `SECURITY.md` - Security policies and secret management
- `emota/` - Core EMOTA framework modules

## Quick Start

```bash
python -m venv .venv
source .venv/bin/activate
pip install -e .[dev]
cp emota/config.yaml emota/config.local.yaml  # (optional override)
export OPENAI_API_KEY=your-key  # optional if running OpenAI example
python openai_connect.py
primecodex --goal 0.6 --threat 0.2 "Exploring an uncertain landscape"
```

## Installation
Editable dev install (preferred for iteration):
```bash
pip install -e .[dev]
```
Or basic runtime only:
```bash
pip install .
```

## CLI Usage
```bash
primecodex --goal 0.7 --threat 0.1 --novelty 0.3 "Encountering a new opportunity"
```
Read experience text from stdin:
```bash
echo "Entering a dark corridor" | primecodex --goal 0.4 --threat 0.5 --pretty
```

## Architecture (Text Diagram)
```
Experience → Motivational Braid (desire,fear,valence,tension)
            ↘ Archetypal Resonance (serpent/flame/void/unity balance)
             ↘ Future: Cathedral / Dimensional Bridge / Memory Layers
Output: Unified state snapshot (policy, braid code, archetypal mode)
```

### Core Modules
- `emota/braid.py` – Desire/Fear dynamical system with hysteresis bits.
- `emota/archetype.py` – Resonance engine mapping motivational dynamics to archetypal pattern activations.
- `emota/unity.py` – Integration wrapper (now supports `config_path`).
- `emota/cathedral.py` – Placeholder for macro-structural planning layer.
- `emota/bridge.py` – Placeholder for symbolic/sub-symbolic translation layer.
- `emota/memory.py` – Placeholder episodic/short-term memory buffer.

### Configuration
Runtime parameters load from `emota/config.yaml` by default. Provide an alternate file via CLI `--config` or `EMOTA_CONFIG` (future) or pass `config_path` to `EMOTAUnityEngine`.

## OpenAI Example
Located in `openai_connect.py`. Uses `OPENAI_API_KEY`. Tests mock live calls unless key exported.

## Testing
```bash
pytest
```
Includes CLI JSON schema validation (`schema/cli_output.schema.json`).
Live OpenAI call test skipped if `OPENAI_API_KEY` absent.

## Development Checklist
- Add new subsystem stub in `emota/`
- Add unit tests (avoid network I/O)
- Update README architecture if conceptual model changes
- Run `pytest` before commit
- **For AI-assisted development**: Follow patterns in `COPILOT_AGENT.md`
- **Code quality**: Run `ruff check .` and `ruff format .` before commit
- **Security**: Enable git hooks with `git config core.hooksPath .githooks`

## Security & Secrets
Never commit `.env`. The repository provides:
- `.githooks/pre-commit` secret pattern scanner (enable with `git config core.hooksPath .githooks`).
- `scripts/cleanup_secrets.sh` (fresh clone interactive history rewrite)
- `scripts/mirror_history_purge.sh` (automated mirror purge)

### If a Secret Was Committed
1. Rotate key immediately.
2. Perform mirror purge (see below) in a clean environment.
3. Force push rewritten history.
4. Fresh-clone and verify absence: `git log --all -- .env` returns nothing.

### Mirror Purge Summary
```bash
./scripts/mirror_history_purge.sh git@github.com:your-org/PrimeCodex.git
# then fresh clone & verify
```

## Roadmap
- Memory layering & temporal weaving
- Adaptive policy arbitration
- Extended archetypal harmonic analytics
- Cathedral planning engine
- Dimensional bridge translation layer

## Contributing
See `CONTRIBUTING.md` and `CODE_OF_CONDUCT.md`.

## License
Internal experimental use (no open license declared). Contact maintainer before external distribution.

---
Generated state snapshots are experimental and not safety-audited.