# Changelog

Release history for MarketLens Skills. Versions match `metadata.version` in each
`SKILL.md`.

## v0.4 Toolchain And Shared Routing

- CI now actually runs. `.github/` is no longer git-ignored, and the workflow
  validates, builds packages, then re-validates with `REQUIRE_DIST=1`.
- Validation moved into `scripts/validate_skills.py`, which checks frontmatter
  (`name`, `description`, `license`, `metadata.version`), reference routing in both
  directions, the standard output blocks, exact disclaimer wording, and a
  byte-for-byte comparison between each `dist/*.skill` package and the working tree.
- `scripts/build-skills.sh` and the validator discover skills from the directory
  layout, so adding a skill no longer requires editing a hardcoded list.
- New `references/skill-routing.md` holds the ownership table and routing rules.
  Each `SKILL.md` now states only what it owns and points here, replacing the
  cross-referenced boundary blocks that had to be updated in every skill.
- `references/scoring-standard.md` states which output blocks are mandatory for all
  skills and which apply only to outputs that carry a 0-3 scorecard.
- Disclaimer wording is identical across all six skills, and every `SKILL.md`
  carries `license` and `metadata.version`.
- Install instructions now cover the shared `references/` directory, which the
  skills load through `../references/...` and which earlier docs omitted.

## v0.3 Scoring And Trading Discipline

Unified the scoring and research-label system across all skills:

- shared scoring rules define 0-3 score direction, confidence, data quality,
  red-flag overrides, and allowed research labels;
- market-regime scores remain separate environment-pressure scores and are used to
  adjust risk-budget language, not to mechanically change company or portfolio
  totals;
- catalyst work separates event importance from trade setup through consensus view,
  variant view, market-implied expectation, implied move, risk/reward read,
  invalidating evidence, and post-event review window;
- portfolio work adds a lightweight quantitative risk snapshot covering
  concentration, top 3/top 5 exposure, factor/theme overlap, liquidity, stress
  correlation, and drawdown contribution;
- trade plan work converts research labels into conditional setup quality,
  entry/review triggers, risk-unit framing, execution checks, and post-trade review;
- all score-based outputs include `Score Summary`, `Red Flags`, `Decision Impact`,
  and `What Would Change The View`;
- research can be reviewed through a calibration loop covering original score,
  evidence, 1-week/1-month/3-month outcomes, error attribution, and rule updates.

## v0.2 Research Discipline

Added stricter conclusion gates:

- equity research must downgrade conclusions when price, filings, valuation inputs,
  or primary sources are missing;
- sector research must downgrade conclusions when industry scope, dated
  demand/supply evidence, peer set, or primary sources are missing;
- catalyst research must downgrade conclusions when event timing, source quality,
  expectation baseline, or post-event review criteria are missing;
- portfolio research must downgrade conclusions when holdings, weights/assumptions,
  price dates, or risk-driver evidence are missing;
- valuation work includes sector-specific methods for financials, REITs, cyclicals,
  platforms, exporters, and pre-profit biotech;
- market regime calls use indicator scoring, confidence levels, conflict handling,
  causal channels, and explicit view-change triggers.
