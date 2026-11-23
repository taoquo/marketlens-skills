#!/usr/bin/env python3
"""Structural validation for MarketLens skills.

Checks, per skill directory discovered under the repository root:
  - SKILL.md frontmatter (name, description, license, metadata.version)
  - every referenced reference file exists, and every reference file is routed to
  - every shared file in the top-level references/ directory is routed by a skill
  - agents/openai.yaml carries the required interface fields
  - the standard output blocks required by references/skill-contract.md, in order
  - VERSION, every SKILL.md metadata.version, and CHANGELOG.md agree
  - README example coverage and image paths, in both languages
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
CONTRACT_REFERENCE = "../references/skill-contract.md"
VERSION_PATH = ROOT / "VERSION"
CHANGELOG_PATH = ROOT / "CHANGELOG.md"
EXAMPLES_DIR = ROOT / "examples"
OUTPUT_TEMPLATE_RE = re.compile(
    r"^## Output Template\s*\n+```markdown\n(.*?)\n```", re.S | re.M
)
COVERAGE_ROW_RE = re.compile(r"^\|\s*`([a-z0-9-]+)`\s*\|\s*`([^`]+)`\s*\|", re.M)
IMAGE_REF_RE = re.compile(r"\((examples/[^)]+\.png)\)")
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


def check_frontmatter(
    skill: str, text: str, expected_version: str | None, errors: list[str]
) -> None:
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
    elif expected_version and version != expected_version:
        errors.append(
            f"{skill}: metadata.version {version!r} does not match VERSION {expected_version!r}"
        )


def check_references(skill: str, text: str, errors: list[str]) -> None:
    routed = set(REFERENCE_RE.findall(text))
    for ref in sorted(routed):
        path = ROOT / ref[3:] if ref.startswith("../") else ROOT / skill / ref
        if not path.is_file():
            errors.append(f"{skill}: referenced file does not exist: {ref}")

    if CONTRACT_REFERENCE not in routed:
        errors.append(f"{skill}: SKILL.md must route to {CONTRACT_REFERENCE}")

    for shared in SHARED_REFERENCES:
        if "../" + shared not in routed:
            errors.append(f"{skill}: SKILL.md must route to ../{shared}")

    for path in sorted((ROOT / skill / "references").glob("*.md")):
        rel = "references/" + path.name
        if rel not in routed:
            errors.append(f"{skill}: {rel} exists but SKILL.md never loads it")


def check_shared_reference_use(routed: set[str], errors: list[str]) -> None:
    """No shared reference should sit in the repo without a skill that loads it.

    SHARED_REFERENCES covers the files every skill must route. This catches the
    rest: a cross-cutting file loaded by trigger still needs at least one caller,
    otherwise it is dead weight that drifts out of date.
    """
    for path in sorted((ROOT / "references").glob("*.md")):
        rel = "../references/" + path.name
        if rel not in routed:
            errors.append(f"references/{path.name} exists but no SKILL.md loads it")


def check_output_blocks(skill: str, text: str, errors: list[str]) -> None:
    match = OUTPUT_TEMPLATE_RE.search(text)
    if not match:
        errors.append(f"{skill}: missing a fenced markdown Output Template")
        return

    template = match.group(1)
    positions: list[tuple[int, str]] = []
    for block in STANDARD_OUTPUT_BLOCKS:
        found = re.search(r"^" + re.escape(block) + r"$", template, re.M)
        if not found:
            errors.append(f"{skill}: output template is missing {block!r}")
        else:
            positions.append((found.start(), block))

    if len(positions) == len(STANDARD_OUTPUT_BLOCKS):
        ordered = [block for _, block in sorted(positions)]
        if ordered != list(STANDARD_OUTPUT_BLOCKS):
            errors.append(
                f"{skill}: output blocks are out of order: {' -> '.join(ordered)}"
            )

    if DISCLAIMER_TEXT not in template:
        errors.append(
            f"{skill}: output template disclaimer wording does not match the shared text"
        )


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


def read_expected_version(errors: list[str]) -> str | None:
    if not VERSION_PATH.is_file():
        errors.append("VERSION file is missing")
        return None
    version = VERSION_PATH.read_text(encoding="utf-8").strip()
    if not VERSION_RE.match(version):
        errors.append(f"VERSION {version!r} must look like 0.3 or 0.3.1")
        return None
    return version


def check_changelog(expected_version: str | None, errors: list[str]) -> None:
    if not expected_version:
        return
    if not CHANGELOG_PATH.is_file():
        errors.append("CHANGELOG.md is missing")
        return
    text = CHANGELOG_PATH.read_text(encoding="utf-8")
    match = re.search(r"^## v(\d+\.\d+(?:\.\d+)?)", text, re.M)
    if not match:
        errors.append("CHANGELOG.md has no release heading")
    elif match.group(1) != expected_version:
        errors.append(
            f"CHANGELOG.md latest release is v{match.group(1)}, "
            f"expected v{expected_version}"
        )


def check_examples(skills: list[str], errors: list[str]) -> None:
    readme = ROOT / "README.md"
    readme_zh = ROOT / "README.zh-CN.md"
    if not readme.is_file() or not readme_zh.is_file():
        errors.append("README.md and README.zh-CN.md are required for example coverage")
        return

    en_text = readme.read_text(encoding="utf-8")
    zh_text = readme_zh.read_text(encoding="utf-8")
    en_rows = COVERAGE_ROW_RE.findall(en_text)
    zh_rows = COVERAGE_ROW_RE.findall(zh_text)

    cases = {case for _, case in en_rows}
    covered_skills = {skill for skill, _ in en_rows}
    for skill in skills:
        if skill not in covered_skills:
            errors.append(f"{skill}: README coverage table has no example case")

    for case in sorted(cases):
        for suffix in (".html", ".pdf", ".png"):
            if not (EXAMPLES_DIR / (case + suffix)).is_file():
                errors.append(f"examples/{case}{suffix} is missing")

    if set(en_rows) != set(zh_rows):
        errors.append("README.md and README.zh-CN.md coverage tables differ")

    html_cases = {path.stem for path in EXAMPLES_DIR.glob("*.html")}
    for case in sorted(html_cases - cases):
        errors.append(f"examples/{case}.html has no coverage row in README.md")

    for path, text in ((readme, en_text), (readme_zh, zh_text)):
        for rel in IMAGE_REF_RE.findall(text):
            if not (ROOT / rel).is_file():
                errors.append(f"{path.name} references missing {rel}")


def main() -> int:
    require_dist = os.environ.get("REQUIRE_DIST") == "1"
    skills = discover_skills(ROOT)
    if not skills:
        print("ERROR: no skill directories found", file=sys.stderr)
        return 1

    errors: list[str] = []
    expected_version = read_expected_version(errors)
    check_changelog(expected_version, errors)

    routed_shared: set[str] = set()
    for skill in skills:
        text = (ROOT / skill / "SKILL.md").read_text(encoding="utf-8")
        check_frontmatter(skill, text, expected_version, errors)
        check_references(skill, text, errors)
        check_output_blocks(skill, text, errors)
        check_agent_metadata(skill, errors)
        check_package(skill, errors, require_dist)
        routed_shared.update(REFERENCE_RE.findall(text))

    check_shared_reference_use(routed_shared, errors)
    check_examples(skills, errors)

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
