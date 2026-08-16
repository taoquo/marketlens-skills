#!/usr/bin/env bash
set -euo pipefail

ROOT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"
DIST_DIR="$ROOT_DIR/dist"

# Discover skills instead of hardcoding them: a skill is any top-level
# directory that contains a SKILL.md.
SKILLS=()
while IFS= read -r skill_md; do
  SKILLS+=("$(basename "$(dirname "$skill_md")")")
done < <(find "$ROOT_DIR" -mindepth 2 -maxdepth 2 -name SKILL.md -not -path "*/.*" | sort)

if ((${#SKILLS[@]} == 0)); then
  echo "ERROR: no skill directories found" >&2
  exit 1
fi

command -v zip >/dev/null 2>&1 || {
  echo "ERROR: zip is required" >&2
  exit 1
}

rm -rf "$DIST_DIR"
mkdir -p "$DIST_DIR"

for skill in "${SKILLS[@]}"; do
  (
    cd "$ROOT_DIR"
    zip -qr "$DIST_DIR/$skill.skill" \
      "$skill/SKILL.md" \
      "$skill/agents/openai.yaml" \
      "$skill/references" \
      "references" \
      -x '.*' '*/.*'
  )
  echo "Built dist/$skill.skill"
done

echo "Built ${#SKILLS[@]} packages: ${SKILLS[*]}"
