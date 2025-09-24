#!/usr/bin/env bash
set -euo pipefail

if ! command -v git-filter-repo >/dev/null 2>&1; then
  echo "git-filter-repo not installed. Install it first (e.g., apt-get install git-filter-repo)." >&2
  exit 1
fi

echo "WARNING: This will rewrite history. Ensure you are in a fresh clone and have backups."
read -p "Type 'YES' to continue: " CONFIRM
if [[ "$CONFIRM" != "YES" ]]; then
  echo "Aborted."; exit 1; fi

SECRET_PATHS=(".env")
FILTER_ARGS=()
for p in "${SECRET_PATHS[@]}"; do
  FILTER_ARGS+=(--path "$p" --invert-paths)
done

echo "Rewriting history to remove: ${SECRET_PATHS[*]}"
git filter-repo "${FILTER_ARGS[@]}"

echo "Removing tags referencing old commits (local)"
git tag | xargs -r git tag -d

echo "Force pushing cleaned history"
git push --force --all

echo "Force pushing tags (now empty or recreated)"
git push --force --tags

echo "Done. Re-enable protections and rotate any exposed secrets."