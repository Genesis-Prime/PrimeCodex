# Copilot Coding Agent Configuration

This repository is configured for optimal use with GitHub Copilot Coding Agent. This document provides the configuration and context needed for effective AI-assisted development.

## Repository Overview

**PrimeCodex** is an experimental EMOTA Unity framework with OpenAI integration. It implements motivational dynamics through desire/fear systems and archetypal pattern activations.

### Core Architecture

- **Language**: Python 3.10+
- **Framework**: Custom EMOTA (Emotional-Motivational-Archetypal) system
- **Key Dependencies**: OpenAI API, PyYAML, JSONSchema
- **Testing**: pytest with JSON schema validation

### Project Structure

```
PrimeCodex/
├── emota/                  # Core EMOTA framework modules
│   ├── braid.py           # Desire/Fear dynamical system
│   ├── archetype.py       # Archetypal resonance engine
│   ├── unity.py           # Integration wrapper
│   ├── cathedral.py       # Macro-structural planning (placeholder)
│   ├── bridge.py          # Translation layer (placeholder)
│   └── memory.py          # Memory buffer (placeholder)
├── cli.py                 # Command-line interface
├── openai_connect.py      # OpenAI API client utilities
├── schema/                # JSON validation schemas
├── scripts/               # Utility scripts
└── tests/                 # Test suite
```

## Development Guidelines

### Code Style & Standards

1. **Python Standards**: Follow PEP 8 with clear, descriptive naming
2. **Documentation**: Add docstrings for complex logic and new modules
3. **Testing**: All new features require unit tests, avoid network I/O in tests
4. **Security**: Never commit secrets; use `.env` files (gitignored)

### Key Development Patterns

1. **Modular Design**: Each subsystem in `emota/` is self-contained
2. **Configuration-Driven**: Runtime parameters via YAML config files
3. **Mock-Friendly**: Network calls are mockable for testing
4. **CLI Integration**: New features should be accessible via CLI

### Testing Strategy

- **Unit Tests**: Use pytest with fixtures
- **Schema Validation**: JSON outputs validated against schemas
- **Mock Network**: OpenAI calls mocked unless `OPENAI_API_KEY` present
- **Secret Scanning**: Pre-commit hooks scan for API keys

## Copilot Integration Points

### 1. Development Workflow

When working on this codebase:
- Run `./scripts/setup_dev.sh` for quick environment setup
- Use `pytest` for testing before commits  
- Follow the development checklist in README.md
- Enable git hooks: `git config core.hooksPath .githooks`

### 2. Common Tasks

**Adding New EMOTA Subsystem:**
1. Create stub in `emota/` with proper docstring
2. Add unit tests with mocks for external dependencies
3. Update `emota/unity.py` integration if needed
4. Add CLI flags if user-facing

**OpenAI Integration:**
- Use `openai_connect.py` utilities for client management
- Always implement mock-friendly patterns
- Test without API keys using existing mock patterns

**Configuration Changes:**
- Update `emota/config.yaml` for new parameters
- Ensure backward compatibility with existing configs
- Add validation if introducing new config sections

### 3. Security Requirements

- **Never commit API keys or secrets**
- **Use `.env` files for local secrets (gitignored)**
- **Run secret scanning before commits**
- **Rotate keys immediately if accidentally committed**

### 4. Error Handling Patterns

```python
# Preferred pattern for API calls
try:
    result = api_call()
except SpecificException as e:
    logger.warning(f"Expected failure: {e}")
    return fallback_value
except Exception as e:
    logger.error(f"Unexpected error: {e}")
    raise
```

## Quick Reference

### Setup Commands
```bash
# Quick development setup
python -m venv .venv
source .venv/bin/activate
pip install -e .[dev]
git config core.hooksPath .githooks

# Run tests
pytest

# CLI usage
primecodex --goal 0.7 --threat 0.1 "example text"
```

### Important Files to Review

- `README.md` - Main documentation and quick start
- `SECURITY.md` - Security policies and incident response
- `CONTRIBUTING.md` - Contribution guidelines
- `pyproject.toml` - Project configuration and dependencies
- `.github/workflows/ci.yml` - CI/CD pipeline

### Context for AI Assistance

This is an **experimental research project** exploring emotional-motivational AI systems. The codebase is designed for:
- Rapid prototyping of EMOTA concepts
- Safe OpenAI API experimentation
- Modular architecture for easy extension
- Strong security practices for API key management

When suggesting changes, prioritize:
1. **Maintainability** - Clear, documented code
2. **Security** - Never expose secrets
3. **Testability** - Mock-friendly, unit-testable
4. **Modularity** - Preserve clean subsystem boundaries