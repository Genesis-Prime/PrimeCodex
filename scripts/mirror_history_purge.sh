#!/usr/bin/env bash
set -euo pipefail

REPO_URL=${1:-""}
if [[ -z "$REPO_URL" ]]; then
  echo "Usage: $0 <git-repo-url>" >&2
  exit 1
fi

if ! command -v git-filter-repo >/dev/null 2>&1; then
  echo "git-filter-repo not installed. Install it (apt-get install git-filter-repo)." >&2
  exit 1
fi

WORKDIR="$(pwd)"
MIRROR_DIR="repo-mirror-clean"

if [[ -d "$MIRROR_DIR" ]]; then
  echo "Removing existing $MIRROR_DIR"; rm -rf "$MIRROR_DIR";
fi

echo "Cloning mirror..."
git clone --mirror "$REPO_URL" "$MIRROR_DIR"
cd "$MIRROR_DIR"

echo "Rewriting history to remove .env"
git filter-repo --path .env --invert-paths

echo "Pruning originals & garbage collecting"
rm -rf .git/refs/original || true
git reflog expire --expire=now --all || true
git gc --prune=now --aggressive || true

echo "Force pushing rewritten history (all refs)"
git push --force --mirror

echo "Done. Now re-clone the repository fresh and verify:"
echo "  git clone $REPO_URL fresh-clone && cd fresh-clone && git log --oneline --all -- .env"
