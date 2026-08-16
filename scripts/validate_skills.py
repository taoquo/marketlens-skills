#!/usr/bin/env python3
"""Structural validation for MarketLens skills.

Checks, per skill directory discovered under the repository root:
  - SKILL.md frontmatter (name, description, license, metadata.version)
  - every referenced reference file exists, and every reference file is routed to
  - agents/openai.yaml carries the required interface fields
  - the standard output blocks required by references/scoring-standard.md
  - dist/<skill>.skill matches the working tree byte for byte

Set REQUIRE_DIST=1 to fail when a package is missing (used in CI after build).
"""

from __future__ import annotations

import filecmp
import os
import re
import sys
import zipfile
from pathlib import Path
from tempfile import TemporaryDirectory

ROOT = Path(__file__).resolve().parent.parent
BACKTICK = chr(96)
NAME_RE = re.compile(r"^[a-z0-9]+(?:-[a-z0-9]+)*$")
FRONTMATTER_RE = re.compile(r"\A---\n(.*?)\n---", re.S)
REFERENCE_RE = re.compile(
    BACKTICK + r"((?:\.\./)?references/[^" + BACKTICK + r"]+\.md)" + BACKTICK
)
VERSION_RE = re.compile(r"^\d+\.\d+(?:\.\d+)?$")
MAX_DESCRIPTION = 1024

ALLOWED_FRONTMATTER_KEYS = {"name", "description", "license", "allowed-tools", "metadata"}
REQUIRED_AGENT_FIELDS = ("display_name:", "short_description:", "default_prompt:")
SHARED_REFERENCES = (
    "references/scoring-standard.md",
    "references/review-and-calibration.md",
    "references/data-discipline.md",
    "references/skill-routing.md",
)
STANDARD_OUTPUT_BLOCKS = (
    "## Red Flags",
    "## Decision Impact",
    "## What Would Change The View",
    "## Data Freshness",
    "## Evidence Sources",
    "## Disclaimer",
)
DISCLAIMER_TEXT = (
    "This is public-market research for reference only and does not constitute investment advice."
)


def discover_skills(root: Path) -> list[str]:
    """A skill is any top-level directory holding a SKILL.md."""
    return [
        path.parent.name
        for path in sorted(root.glob("*/SKILL.md"))
        if not path.parent.name.startswith(".")
    ]


def parse_frontmatter(text: str) -> dict[str, str]:
    """Parse the flat key/value frontmatter used by SKILL.md files.

    PyYAML is not guaranteed to be installed, and this frontmatter is a small
    flat mapping with one optional nested block, so a line parser is enough.
    """
    match = FRONTMATTER_RE.match(text)
    if not match:
        raise ValueError("missing or malformed YAML frontmatter")

    fields: dict[str, str] = {}
    parent = ""
    for raw_line in match.group(1).splitlines():
        if not raw_line.strip() or raw_line.lstrip().startswith("#"):
            continue
        if ":" not in raw_line:
            raise ValueError("unparsable frontmatter line: " + repr(raw_line))
        key, value = raw_line.split(":", 1)
        indented = key[:1].isspace()
        key = key.strip()
        value = value.strip().strip('"').strip("'")
        if indented:
            if not parent:
                raise ValueError("nested frontmatter key without parent: " + key)
            fields[parent + "." + key] = value
        elif value:
            fields[key] = value
            parent = ""
        else:
            fields[key] = ""
            parent = key
    return fields


def check_frontmatter(skill: str, text: str, errors: list[str]) -> None:
    try:
        fields = parse_frontmatter(text)
    except ValueError as exc:
        errors.append(f"{skill}: {exc}")
        return

    top_level = {key.split(".", 1)[0] for key in fields}
    unexpected = sorted(top_level - ALLOWED_FRONTMATTER_KEYS)
    if unexpected:
        errors.append(f"{skill}: unexpected frontmatter key(s): {', '.join(unexpected)}")

    name = fields.get("name", "")
    if name != skill:
        errors.append(f"{skill}: frontmatter name is {name!r}, expected {skill!r}")
    elif not NAME_RE.match(name):
        errors.append(f"{skill}: name must be hyphen-case")

    description = fields.get("description", "")
    if not description:
        errors.append(f"{skill}: missing description")
    elif len(description) > MAX_DESCRIPTION:
        errors.append(f"{skill}: description is {len(description)} chars, max {MAX_DESCRIPTION}")
    elif "<" in description or ">" in description:
        errors.append(f"{skill}: description cannot contain angle brackets")

    if not fields.get("license"):
        errors.append(f"{skill}: missing license in frontmatter")

    version = fields.get("metadata.version", "")
    if not version:
        errors.append(f"{skill}: missing metadata.version in frontmatter")
    elif not VERSION_RE.match(version):
        errors.append(f"{skill}: metadata.version {version!r} must look like 0.3 or 0.3.1")


def check_references(skill: str, text: str, errors: list[str]) -> None:
    routed = set(REFERENCE_RE.findall(text))
    for ref in sorted(routed):
        path = ROOT / ref[3:] if ref.startswith("../") else ROOT / skill / ref
        if not path.is_file():
            errors.append(f"{skill}: referenced file does not exist: {ref}")

    for shared in SHARED_REFERENCES:
        if "../" + shared not in routed:
            errors.append(f"{skill}: SKILL.md must route to ../{shared}")

    for path in sorted((ROOT / skill / "references").glob("*.md")):
        rel = "references/" + path.name
        if rel not in routed:
            errors.append(f"{skill}: {rel} exists but SKILL.md never loads it")


def check_output_blocks(skill: str, text: str, errors: list[str]) -> None:
    for block in STANDARD_OUTPUT_BLOCKS:
        if block not in text:
            errors.append(f"{skill}: output template is missing {block!r}")
    if DISCLAIMER_TEXT not in text:
        errors.append(f"{skill}: disclaimer wording does not match the shared text")


def check_agent_metadata(skill: str, errors: list[str]) -> None:
    path = ROOT / skill / "agents" / "openai.yaml"
    if not path.is_file():
        errors.append(f"{skill}: missing agents/openai.yaml")
        return
    content = path.read_text(encoding="utf-8")
    for field in REQUIRED_AGENT_FIELDS:
        if field not in content:
            errors.append(f"{skill}: agents/openai.yaml missing {field}")


def diff_trees(source: Path, target: Path, label: str) -> list[str]:
    """Compare every file the packager is expected to ship."""
    source_files = {
        path.relative_to(source).as_posix()
        for path in source.rglob("*")
        if path.is_file() and not path.name.startswith(".")
    }
    target_files = {
        path.relative_to(target).as_posix() for path in target.rglob("*") if path.is_file()
    }

    messages = []
    for missing in sorted(source_files - target_files):
        messages.append(f"package is missing {label}/{missing}")
    for extra in sorted(target_files - source_files):
        messages.append(f"package has stale {label}/{extra}")
    for shared in sorted(source_files & target_files):
        if not filecmp.cmp(source / shared, target / shared, shallow=False):
            messages.append(f"package copy of {label}/{shared} is out of date")
    return messages


def check_package(skill: str, errors: list[str], require_dist: bool) -> None:
    package = ROOT / "dist" / f"{skill}.skill"
    if not package.is_file():
        if require_dist:
            errors.append(f"{skill}: dist/{skill}.skill is missing; run scripts/build-skills.sh")
        return

    with TemporaryDirectory() as tmp:
        extracted = Path(tmp)
        with zipfile.ZipFile(package) as archive:
            archive.extractall(extracted)

        for subject in (skill, "references"):
            target = extracted / subject
            if not target.is_dir():
                errors.append(f"{skill}: package missing {subject}/")
                continue
            for message in diff_trees(ROOT / subject, target, subject):
                errors.append(f"{skill}: {message}")


def main() -> int:
    require_dist = os.environ.get("REQUIRE_DIST") == "1"
    skills = discover_skills(ROOT)
    if not skills:
        print("ERROR: no skill directories found", file=sys.stderr)
        return 1

    errors: list[str] = []
    for skill in skills:
        text = (ROOT / skill / "SKILL.md").read_text(encoding="utf-8")
        check_frontmatter(skill, text, errors)
        check_references(skill, text, errors)
        check_output_blocks(skill, text, errors)
        check_agent_metadata(skill, errors)
        check_package(skill, errors, require_dist)

    if errors:
        for error in errors:
            print(f"ERROR: {error}", file=sys.stderr)
        print(f"{len(errors)} problem(s) across {len(skills)} skill(s)", file=sys.stderr)
        return 1

    print(f"Validated {len(skills)} skills: {', '.join(skills)}")
    print("dist packages required" if require_dist else "dist packages checked when present")
    return 0


if __name__ == "__main__":
    sys.exit(main())
