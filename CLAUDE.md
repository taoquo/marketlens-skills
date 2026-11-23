# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## What this repository is

MarketLens is a **skill repository**, not an application. It ships six Markdown-defined
research skills for AI agents (equity, market regime, sector/industry, catalyst events,
portfolio risk, trade planning) plus a shared `references/` layer. There is no package
manifest, runtime, or application build. The "code" that matters is the prose, its
cross-references, and the structural contract enforced by `scripts/validate_skills.py`.

A skill is any top-level directory containing `SKILL.md`. Discovery is dynamic, so
adding or removing a skill directory requires no script or CI edit.

## Commands

```bash
# Structural validation: frontmatter, reference routing, output blocks, agent metadata
bash scripts/validate-skills.sh

# Rebuild the distributable zip packages in dist/ (gitignored)
bash scripts/build-skills.sh

# CI order: validate, build, then require dist/*.skill to match the tree byte for byte
REQUIRE_DIST=1 bash scripts/validate-skills.sh

# Re-render one example (writes .pdf and .png beside the .html)
bash scripts/render-examples.sh examples/marketlens-v09-equity-research-nvda.html

# Render a point-in-time PE band from a CSV (standard library only)
python3 scripts/pe_band_chart.py \
  --input examples/data/nvda-pe-ttm-illustrative.csv \
  --output pe-band.svg
```

`scripts/validate-skills.sh` is only a wrapper around `python3 scripts/validate_skills.py`;
there is no unit-test suite. To check one skill, run the validator and read the
per-skill `ERROR:` lines — the validator always scans all discovered skills.

Rendering requires `pdftoppm` plus a WeasyPrint Python with `PIL` and `pypdf`
(default path `~/.codex/skills/folio/.venv-weasy/bin/python`, override with
`FOLIO_WEASY_PYTHON`). `scripts/stack_pages.py` stitches paginated renders into the
single continuous `.png`.

## Architecture: layered content model

Each `SKILL.md` follows the same section skeleton (`Core Rule`, `Skill Boundary`,
`Mode Selection`, `Reference Loading`, `Evidence Standard`, `Conclusion Gates`,
`Data Freshness Protocol`, `Workflow`, `Output Template`). Domain knowledge lives in
the skill's own `references/`; cross-cutting rules live in the top-level `references/`
and are loaded through `../references/...`.

The shared layer is not optional prose — it is the product's consistency mechanism:

- `references/skill-contract.md` — the operating contract every skill routes: core rule,
  mandatory shared routes, evidence tiers, conclusion-gate behavior, the three timestamps
  and five freshness grades, and the six mandatory output blocks in order. `SKILL.md`
  keeps only domain-specific deltas.
- `references/skill-routing.md` — ownership table (which skill owns what), trigger table
  for the six cross-cutting files, and the out-of-scope list. A new skill needs one
  routing entry, not edits across every other skill.
- `references/scoring-standard.md` — 0–3 scorecard direction, confidence, data-quality
  weighting, red-flag overrides, the nine research labels, label layering from each
  skill's domain read, and the binding cross-module **chain constraints**.
- `references/data-discipline.md` — the three timestamps, the closed freshness enum
  (`Fresh` / `Lagged` / `Stale` / `Undated` / `Unavailable`), evidence tiers, core-figure
  check, unit/currency/calendar rules, and user-input classification.
- `references/review-and-calibration.md` — review cadence and the append-only
  `research-log/` convention (gitignored; never create it without asking).
- `implied-expectations.md`, `earnings-quality-screens.md`, `capital-allocation-record.md`,
  `credit-and-cross-asset.md`, `base-rates.md`, `short-and-relative-value.md` — cross-cutting
  analytical methods loaded by trigger, not by skill.

The decision chain is `Market Regime -> Sector/Industry -> Company Quality & Valuation ->
Catalyst/Timing -> Portfolio Role & Risk -> Research Label`. Upstream layers only tighten
a downstream label, never loosen it.

## Invariants enforced by the validator

Editing content without these breaks CI:

1. **Frontmatter** — `name` must equal the directory name and be hyphen-case; `description`
   is required, ≤1024 chars, and cannot contain `<` or `>`; `license` and
   `metadata.version` are required, and the version must equal `VERSION`. The parser is
   hand-rolled flat YAML: use only flat keys plus the nested `metadata.version`. No lists,
   multiline strings, or nested maps.
2. **Reference routing** — references are detected only when written as backticked paths
   like `` `../references/foo.md` `` or `` `references/foo.md` ``. Every file a skill ships
   must be routed in its `SKILL.md`; every shared file in `references/` must be routed by
   at least one skill; every skill must route `../references/skill-contract.md` plus the
   four mandatory shared files (`scoring-standard`, `review-and-calibration`,
   `data-discipline`, `skill-routing`).
3. **Output blocks** — the validator extracts the fenced `## Output Template` and requires
   `## Red Flags`, `## Decision Impact`, `## What Would Change The View`,
   `## Data Freshness`, `## Evidence Sources`, and `## Disclaimer` to appear there in that
   relative order, plus the exact disclaimer sentence
   `This is public-market research for reference only and does not constitute investment advice.`
   Other domain blocks may sit between them.
4. **Agent metadata** — `agents/openai.yaml` must contain `display_name:`,
   `short_description:`, and `default_prompt:`.
5. **Version consistency** — `VERSION`, every `SKILL.md` `metadata.version`, and the latest
   `## vX.Y` heading in `CHANGELOG.md` must agree.
6. **Example coverage** — both READMEs must map every skill to a case in the coverage
   table; `examples/<case>.html`, `.pdf`, and `.png` must exist; every `examples/*.html`
   must have a coverage row; every README image path must resolve.
7. **Dist packages** — with `REQUIRE_DIST=1`, each `dist/<skill>.skill` must exist and its
   extracted contents must match the working tree byte for byte, including the shared
   `references/` copy. Always rebuild after editing skill or shared reference files.

## Content conventions that validation does not catch

- **Version is repo-wide and single-sourced.** Bump `VERSION`, every `SKILL.md`
  `metadata.version`, and the top `CHANGELOG.md` heading together. The current release is
  0.10; the examples are the six English v0.9 cases in `examples/marketlens-v09-*` plus the
  v0.10 valuation-band case in `examples/marketlens-v010-*`, with NVIDIA as the core case,
  until methodology or example content changes again.
- **Shared rules live in `skill-contract.md`.** Do not re-add the core-rule, evidence-tier,
  gate, freshness, routing, or output-block boilerplate to individual `SKILL.md` files.
  Keep only the domain-specific Core Rule, evidence sources, gates, degradation table,
  workflow, and output template.
- **Historical valuation bands are a valuation-layer cross-check.** The method lives in
  `equity-research/references/valuation-framework.md`, not in a new skill or a top-level shared
  file. It uses rolling, point-in-time windows; a full-sample band is descriptive only and
  cannot support a standalone action label. The repo utility is `scripts/pe_band_chart.py`
  (dependency-free, not packaged into `dist/`); the user guide is `docs/valuation-band.md`
  with a Chinese mirror at `docs/valuation-band.zh-CN.md`. The typeset case uses a Folio
  `line-chart` fixture (`examples/data/nvda-pe-band-folio.json`) filled through
  `embed-drawing`; the utility remains the standalone fallback.
- **No duplicated screening.** A screen computed in one file is carried into another, not
  recomputed or counted twice (e.g. share count, SBC intensity, goodwill share are counted
  once between earnings quality and capital allocation). Breach counts feed aggregate reads
  and label caps; changing a threshold means updating every table that references it.
- **Cross-file consistency.** Thresholds, label names, freshness grades, and chain
  constraints appear in multiple files. Change one place and grep the repo for the old
  wording before finishing.
- **Docs parity.** `README.md` and `README.zh-CN.md` are maintained in parallel; the English
  README is the source of truth for skill tables and example coverage.
- **Examples are typeset deliverables**, not templates: hand-written inline-CSS HTML in
  English using the Folio visual language (parchment ground, cinnabar accent, Charter).
  Each case should still exercise the current release's gates and carry the six mandatory
  blocks (in typeset form, `Evidence Sources` and `Disclaimer` may live in the footer).

## Adding or renaming a skill

Create `<name>/SKILL.md` with valid frontmatter, add `<name>/agents/openai.yaml`, add
`<name>/references/*.md` and route each from `SKILL.md`, route
`../references/skill-contract.md` plus the four mandatory shared files, include the six
output blocks in order and the exact disclaimer, add one ownership row to
`references/skill-routing.md`, add a case to both README coverage tables, build packages,
and run the full validate/build/REQUIRE_DIST sequence. `dist/`, `reports/`, `tmp/`,
`research-log/`, and `.codex/` are gitignored.
