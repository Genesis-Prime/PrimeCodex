# PrimeCodex GitHub Copilot Instructions

**ALWAYS follow these instructions first and fallback to search or bash commands only when you encounter unexpected information that does not match the info here.**

PrimeCodex is an experimental EMOTA Unity framework with OpenAI integration, written in Python. It provides a CLI tool for processing experiences through motivational and archetypal analysis systems.

## Bootstrap & Environment Setup

### Initial Setup
Set up the development environment:
```bash
python -m venv .venv
source .venv/bin/activate
pip install --upgrade pip
pip install --timeout 300 -r requirements.txt
```
**Time: ~20 seconds. NEVER CANCEL - Network downloads may take time.**

### Enable Git Hooks (Security)
```bash
git config core.hooksPath .githooks
```
This enables pre-commit secret scanning to prevent accidental commit of API keys.

### Configuration (Optional)
```bash
cp emota/config.yaml emota/config.local.yaml  # Override defaults if needed
```

## Building & Testing

### Core Validation Commands
**ALWAYS run these commands before committing changes:**

```bash
# Run all tests - NEVER CANCEL: Allow up to 2 minutes for full test suite
pytest -q
# Expected time: ~1 second (current), but allow up to 120 seconds timeout

# Type checking - NEVER CANCEL: Allow up to 5 minutes for type analysis  
pyright
# Expected time: ~2.5 seconds (current), but allow up to 300 seconds timeout
# IMPORTANT: pyright exits with code 1 due to 3 type errors in archetype.py and test_openai_connect.py
# These are non-blocking - tests pass despite these type errors
# Do not treat pyright exit code 1 as a failure in this codebase
```

### Fast Iteration Testing
For quick validation during development:
```bash
# Run unity-focused tests only
pytest -k unity -q
# Expected time: <1 second
```

### Installation Issues
**CRITICAL**: `pip install -e .[dev]` fails due to package discovery issues and network timeouts.

**ALWAYS use this validated approach:**
```bash
pip install --timeout 300 -r requirements.txt
```

**If network timeouts occur, increase timeout and add retries:**
```bash
pip install --timeout 600 --retries 5 -r requirements.txt
```

**Installation takes ~20 seconds when network is stable, but may take up to 10 minutes with network issues. NEVER CANCEL.**

## Running the Application

### CLI Usage
Run the main CLI application:
```bash
# Direct execution (always works)
python cli.py --goal 0.6 --threat 0.2 "Exploring an uncertain landscape"

# With pretty printing
python cli.py --goal 0.4 --threat 0.5 --pretty "Sample experience"

# Reading from stdin
echo "Entering a dark corridor" | python cli.py --goal 0.4 --threat 0.5 --pretty
```
**Time: <0.1 seconds per execution**

### Module Entry Point
Note: `python -m primecodex` does NOT work due to package configuration. Always use `python cli.py` instead.

### OpenAI Integration Testing
```bash
python openai_connect.py
```
**Time: ~0.4 seconds (works without API key for basic testing)**

Optional: Export `OPENAI_API_KEY=your-key` for live API testing, but all tests mock API calls by default.

## Manual Validation Scenarios

**CRITICAL: Always test these scenarios after making changes to ensure functionality:**

### Scenario 1: Basic CLI Experience Processing
```bash
python cli.py --goal 0.6 --threat 0.2 "Exploring an uncertain landscape"
```
**Expected**: JSON output with motivational_state and archetypal_resonance sections. Should show policy "approach" and dominant pattern.

### Scenario 2: High-Threat Scenario
```bash
python cli.py --goal 0.4 --threat 0.5 "Entering a dark corridor"
```
**Expected**: JSON output showing policy "investigate" and higher fear values in motivational_state.

### Scenario 3: Pretty-Printed Output
```bash
echo "Test experience" | python cli.py --goal 0.5 --threat 0.3 --pretty
```
**Expected**: Well-formatted JSON output with proper indentation.

### Scenario 4: Schema Validation
```bash
pytest test_cli_schema.py -v
```
**Expected**: Schema validation passes, confirming CLI output matches JSON schema.

## Timing & Performance Expectations

**CRITICAL TIMING INFORMATION:**
- **Environment Setup**: 20 seconds normally, up to 10 minutes with network issues (NEVER CANCEL - Allow 15 minutes timeout)
- **Test Suite**: 1 second current, allow up to 2 minutes (NEVER CANCEL)
- **Type Checking**: 2.5 seconds current, allow up to 5 minutes (NEVER CANCEL)  
- **CLI Execution**: <0.1 seconds per command
- **OpenAI Integration**: 0.4 seconds (basic test without API)

**NEVER CANCEL any build, test, or validation commands.** Set appropriate timeouts:
- Installation commands: 900+ seconds timeout (15 minutes)
- pytest: 120+ seconds timeout  
- pyright: 300+ seconds timeout

## Project Structure & Key Files

### Core Components
- `cli.py` - Main CLI entry point and argument parsing
- `emota/unity.py` - Main integration engine (EMOTAUnityEngine)
- `emota/braid.py` - Desire/Fear motivational dynamics system
- `emota/archetype.py` - Archetypal pattern analysis engine
- `emota/memory.py` - Memory persistence system
- `emota/config.yaml` - Runtime configuration parameters

### Testing Files
- `test_emota_unity.py` - Core engine tests (3 tests)
- `test_cli_schema.py` - CLI output schema validation
- `test_archetype_coherence.py` - Archetypal system tests
- `test_memory_persistence.py` - Memory system tests
- `test_openai_connect.py` - OpenAI integration tests (2 tests)

### Configuration Files
- `pyproject.toml` - Python project configuration and dependencies
- `pyrightconfig.json` - TypeScript/Python type checker configuration
- `requirements.txt` - Direct dependency installation (use this for reliable installs)
- `.github/workflows/ci.yml` - CI pipeline with tests and secret scanning

### Security & Scripts
- `.githooks/pre-commit` - Secret pattern scanner (blocks commits with API keys)
- `scripts/cleanup_secrets.sh` - Interactive history rewrite tool
- `scripts/mirror_history_purge.sh` - Automated mirror history purge

## Validation Workflow

**Before committing any changes, ALWAYS run:**
```bash
# 1. Run full test suite
pytest -q

# 2. Type check (IMPORTANT: Exit code 1 is expected due to 3 known type errors - not a failure)
pyright

# 3. Test core CLI functionality
python cli.py --goal 0.6 --threat 0.2 "Test experience"

# 4. Validate schema compliance
pytest test_cli_schema.py -v
```

**CRITICAL**: Do not fail validation workflows due to pyright's exit code 1 - this is expected in this codebase.

## Common Development Tasks

### Adding New Dependencies
1. Add to `requirements.txt` (preferred) or `pyproject.toml`
2. Justify necessity in PR
3. Prefer stdlib first
4. Test installation: `pip install --timeout 300 -r requirements.txt`

### Modifying CLI Output
1. Update `schema/cli_output.schema.json` if structure changes
2. Test schema validation: `pytest test_cli_schema.py`
3. Update version in `CHANGELOG.md` for breaking changes

### Working with Memory System
```bash
# Test with persistent memory
python cli.py --memory-path state/memory.json --goal 0.5 "Experience with memory"
```

### Debugging with Structured Logs
```bash
python cli.py --json-logs --log-level DEBUG --goal 0.4 "Debug experience" 2>&1 | jq .
```

## CI/CD Integration

The GitHub Actions workflow (`.github/workflows/ci.yml`) runs:
1. Python 3.12 setup
2. Dependency installation via `pip install -e .[dev]` 
3. `pytest` test execution
4. Gitleaks secret scanning (non-blocking)
5. Basic secret pattern grep

**Note**: CI uses `pip install -e .[dev]` while local development should use `pip install -r requirements.txt` for reliability.

## Security Considerations

**NEVER commit secrets:**
- `.env` files are git-ignored and scanned by pre-commit hooks
- Use `OPENAI_API_KEY` environment variable, never hardcode keys
- Git hooks are enabled via `git config core.hooksPath .githooks`

**If a secret is accidentally committed:**
1. Rotate the key immediately
2. Use `scripts/cleanup_secrets.sh` for interactive cleanup
3. Use `scripts/mirror_history_purge.sh` for automated purging

## Error Conditions & Workarounds

### Known Issues
1. **Package Installation**: `pip install -e .[dev]` may fail due to setuptools/network issues
   - **Workaround**: Use `pip install --timeout 600 --retries 5 -r requirements.txt`

2. **Module Entry Point**: `python -m primecodx` doesn't work
   - **Workaround**: Always use `python cli.py` directly

3. **Type Errors**: pyright shows 3 errors in archetype.py and test_openai_connect.py
   - **Status**: Non-blocking, tests pass despite type errors
   - **Important**: pyright exits with code 1, but this is expected - not a build failure

4. **Network Timeouts**: pip install may timeout in sandboxed environments
   - **Workaround**: Use longer timeouts (600+ seconds) and retry multiple times

### Network Issues
**CRITICAL**: Network timeouts are common in sandboxed environments.

**For persistent network failures, try:**
```bash
# Increase timeout significantly and add retries
pip install --timeout 600 --retries 5 -r requirements.txt

# If still failing, try installing packages individually:
pip install --timeout 600 openai python-dotenv PyYAML jsonschema pytest python-json-logger
```

**Never give up on network timeouts - keep retrying with longer timeouts up to 10 minutes.**

## Reference Command Outputs

### Repository Root Contents
```
.git/ .githooks/ .github/ .vscode/ emota/ scripts/ schema/
CHANGELOG.md CODE_OF_CONDUCT.md CONTRIBUTING.md 
COPILOT_AGENT_ONBOARDING.md LICENSE POST_PURGE_CHECKLIST.md 
README.md SECURITY.md cli.py emota_unity.py openai_connect.py
pyproject.toml pyrightconfig.json requirements.txt
test_*.py files
```

### Sample CLI Output Structure
```json
{
  "identity": "Prime",
  "content": "user input text",  
  "inputs": {"goal_value": 0.6, "threat_level": 0.2, "novelty": 0.0, "uncertainty": 0.0},
  "motivational_state": {
    "desire": 0.5, "fear": 0.18, "valence": 0.32, "tension": 0.09,
    "policy": "approach", "braid_code": 0
  },
  "archetypal_resonance": {
    "dominant_pattern": "Serpent of Stillness",  
    "serpent_activation": 0.48, "flame_activation": 0.42,
    "void_activation": 0.07, "unity_activation": 0.03,
    "resonance_mode": "flowing", "harmonic_frequency": 0.09
  }
}
```

This structure is validated against `schema/cli_output.schema.json`.