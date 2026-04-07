#!/usr/bin/env bash
set -euo pipefail

pre-commit run --all-files || true

git diff --quiet && exit 0

git config user.name "github-actions[bot]"
git config user.email "github-actions[bot]@users.noreply.github.com"
git add -A
git commit -m "chore: pre-commit autofix"
git push
