#!/usr/bin/env bash
set -euo pipefail

ROOT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"
SKILLS=("equity-research" "market-regime-monitor" "sector-industry-research" "catalyst-event-monitor")
VALIDATOR="${SKILL_VALIDATOR:-$HOME/.codex/skills/.system/skill-creator/scripts/quick_validate.py}"

validate_frontmatter_fallback() {
  local skill_dir="$1"
  python3 - "$skill_dir" <<'PY'
import re
import sys
from pathlib import Path

skill_dir = Path(sys.argv[1])
skill_md = skill_dir / "SKILL.md"
text = skill_md.read_text()
match = re.match(r"^---\n(.*?)\n---", text, re.S)
if not match:
    raise SystemExit(f"invalid frontmatter: {skill_md}")
frontmatter = match.group(1)
fields = {}
for line in frontmatter.splitlines():
    if ":" in line:
        key, value = line.split(":", 1)
        fields[key.strip()] = value.strip()
name = fields.get("name", "")
description = fields.get("description", "")
if not re.fullmatch(r"[a-z0-9-]+", name):
    raise SystemExit(f"invalid skill name in {skill_md}: {name}")
if not description or len(description) > 1024:
    raise SystemExit(f"invalid description in {skill_md}")
print(f"Fallback validation passed: {skill_dir.name}")
PY
}

validate_references() {
  local skill="$1"
  python3 - "$ROOT_DIR" "$skill" <<'PY'
import re
import sys
from pathlib import Path

root = Path(sys.argv[1])
skill = sys.argv[2]
skill_md = root / skill / "SKILL.md"
text = skill_md.read_text()
missing = []
for ref in re.findall(r"`(references/[^`]+\.md)`", text):
    if not (root / skill / ref).exists():
        missing.append(ref)
if missing:
    raise SystemExit(f"{skill}: missing references: {', '.join(missing)}")
print(f"References valid: {skill}")
PY
}

validate_openai_yaml() {
  local skill="$1"
  local file="$ROOT_DIR/$skill/agents/openai.yaml"
  [[ -f "$file" ]] || {
    echo "ERROR: missing $file" >&2
    exit 1
  }
  grep -q 'display_name:' "$file"
  grep -q 'short_description:' "$file"
  grep -q 'default_prompt:' "$file"
  echo "Agent metadata valid: $skill"
}

validate_symlinks() {
  local skill
  for skill in "${SKILLS[@]}"; do
    [[ -f "$ROOT_DIR/.codex/skills/$skill/SKILL.md" ]] || {
      echo "ERROR: .codex $skill symlink does not resolve" >&2
      exit 1
    }
  done
  echo "Codex symlinks valid"
}

validate_dist_package() {
  local skill="$1"
  local pkg="$ROOT_DIR/dist/$skill.skill"
  [[ -f "$pkg" ]] || return 0

  local tmpdir
  tmpdir="$(mktemp -d)"
  unzip -qq "$pkg" -d "$tmpdir"
  cmp -s "$ROOT_DIR/$skill/SKILL.md" "$tmpdir/$skill/SKILL.md" || {
    echo "ERROR: package SKILL.md differs for $skill" >&2
    rm -rf "$tmpdir"
    exit 1
  }
  [[ -f "$tmpdir/$skill/agents/openai.yaml" ]] || {
    echo "ERROR: package missing agents/openai.yaml for $skill" >&2
    rm -rf "$tmpdir"
    exit 1
  }
  [[ -d "$tmpdir/$skill/references" ]] || {
    echo "ERROR: package missing references for $skill" >&2
    rm -rf "$tmpdir"
    exit 1
  }
  rm -rf "$tmpdir"
  echo "Package valid: $skill"
}

for skill in "${SKILLS[@]}"; do
  if [[ -f "$VALIDATOR" ]] && python3 -c "import yaml" >/dev/null 2>&1; then
    python3 "$VALIDATOR" "$ROOT_DIR/$skill"
  else
    validate_frontmatter_fallback "$ROOT_DIR/$skill"
  fi
  validate_references "$skill"
  validate_openai_yaml "$skill"
  validate_dist_package "$skill"
done

validate_symlinks
echo "All validations passed"
