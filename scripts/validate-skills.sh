#!/usr/bin/env bash
# Thin wrapper so CI and humans keep one entry point.
# Set REQUIRE_DIST=1 to fail when dist/*.skill packages are missing.
set -euo pipefail

ROOT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"
exec python3 "$ROOT_DIR/scripts/validate_skills.py" "$@"
