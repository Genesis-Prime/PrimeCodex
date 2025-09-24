# Security Policy

> **Disclaimer:** PrimeCodex `0.2.0-beta` is experimental software provided without warranty. You assume all risks associated with operating, securing, or integrating this code—including any data loss, downtime, or security incidents that may result.

## Secret Management
- Never commit secrets (API keys, tokens, credentials) to the repository.
- Use a local `.env` file that is listed in `.gitignore`.
- Rotate any secret immediately if it was committed at any point.

## Incident Response (Secret Leak)
1. Revoke/rotate the exposed key in the provider dashboard.
2. Remove the secret from the code and configuration.
3. Purge it from git history using a fresh clone:
   ```bash
   git clone <repo> repo-clean && cd repo-clean
   git filter-repo --path .env --invert-paths
   git push --force --all
   git push --force --tags
   ```
4. Add/update `.gitignore` to prevent recurrence.
5. Document the incident in this file or internal tracker.

### Mirror Purge (Preferred Automated Process)
```bash
./scripts/mirror_history_purge.sh git@github.com:your-org/PrimeCodex.git
git clone git@github.com:your-org/PrimeCodex.git fresh && cd fresh
git log --all -- .env  # should show nothing
```

If any ref still exposes the file, repeat ensuring no forks reintroduce the blob.

## Reporting Vulnerabilities
Open an issue with minimal details or email the maintainer. Provide steps to reproduce.

## Recommended Tools
- `git-secrets` or pre-commit hooks for scanning.
- GitHub secret scanning alerts.

## Key Rotation Guidance
- Create new key.
- Update local `.env`.
- Deploy new environments.
- Revoke old key after verification.

## Additional Hardening
- Principle of least privilege for API keys.
- Avoid long-lived tokens where possible.
