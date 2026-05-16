#!/usr/bin/env bash
set -euo pipefail

ROOT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"
DIST_DIR="$ROOT_DIR/dist"
SKILLS=("equity-research" "market-regime-monitor" "sector-industry-research" "catalyst-event-monitor")

command -v zip >/dev/null 2>&1 || {
  echo "ERROR: zip is required" >&2
  exit 1
}

rm -rf "$DIST_DIR"
mkdir -p "$DIST_DIR"

for skill in "${SKILLS[@]}"; do
  if [[ ! -f "$ROOT_DIR/$skill/SKILL.md" ]]; then
    echo "ERROR: missing $skill/SKILL.md" >&2
    exit 1
  fi

  (
    cd "$ROOT_DIR"
    zip -qr "$DIST_DIR/$skill.skill" \
      "$skill/SKILL.md" \
      "$skill/agents/openai.yaml" \
      "$skill/references"
  )
  echo "Built dist/$skill.skill"
done
