## Post-Purge Repository Sanity Checklist

This checklist ensures the secret purge (removal of `.env` from history) is fully complete and the repository is in a safe, maintainable state.

### 1. Fresh Clone Verification
```bash
git clone https://github.com/Genesis-Prime/PrimeCodex.git primecodex-clean
cd primecodex-clean
git log --all -- .env   # EXPECT: no output
grep -R "OPENAI_API_KEY" -n . || echo "No key remnants"
```

### 2. Enable Local Protections
```bash
git config core.hooksPath .githooks
```
Confirm the pre-commit hook runs by staging a file and committing (it should scan for patterns like `sk-` or `OPENAI_API_KEY=`).

### 3. Recreate Local Environment
```bash
python -m venv .venv
source .venv/bin/activate
pip install -e .[dev]
cp emota/config.yaml emota/config.local.yaml  # optional overrides
```

### 4. Restore / Rotate Secrets
1. Generate a NEW OpenAI key (previous key considered compromised).
2. Add to local `.env` (do NOT commit):
   ```bash
   echo "OPENAI_API_KEY=sk-xxxx" > .env
   ```
3. Source it or restart your shell: `export $(grep -v '^#' .env | xargs)` (optional if using `python-dotenv`).
4. Test connectivity:
   ```bash
   python openai_connect.py
   ```

### 5. Run Test Suite
```bash
pytest
```
The OpenAI test will be skipped unless the key is present; with key it uses a mocked completion (no live call unless you remove the monkeypatch logic).

### 6. Inspect CI (After First New Push)
Ensure GitHub Actions workflow (`.github/workflows/ci.yml`) runs and passes.

### 7. (Optional) Strengthen Secret Scanning
Add one of:
```bash
pip install detect-secrets && detect-secrets scan > .secrets.baseline
```
Or integrate `gitleaks` / `trufflehog` in CI.

### 8. Tag a Clean Baseline (Optional)
```bash
git tag -a v0.1.0-clean -m "Clean history baseline"
git push origin v0.1.0-clean
```

### 9. Remove Old Working Directory
Delete any pre-purge clones to avoid accidental recommit of orphaned objects.

### 10. Future Hygiene
- Never add `.env` via `git add -A` (hook helps, not guarantees).
- Keep dependencies pinned (see `pyproject.toml`).
- Avoid network calls in tests (use mocks).

---
If any anomaly appears (e.g., secret still reported by GitHub), repeat purge using a mirror clone and verify no forks reintroduced the blob.
