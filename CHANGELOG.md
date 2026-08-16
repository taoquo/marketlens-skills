# Changelog

Release history for MarketLens Skills. Versions match `metadata.version` in each
`SKILL.md`.

## v0.5 Data Discipline And Chain Constraints

This release closes methodology gaps rather than repo tooling. The previous version
stated shared rules; this one makes them executable.

- New `references/data-discipline.md` holds the rules every skill inherits: the three
  timestamps, a closed set of freshness grades (`Fresh`, `Lagged`, `Stale`, `Undated`,
  `Unavailable`), the shared three-tier evidence model, the core figure check, unit and
  fiscal-calendar rules, and how to classify user input. The `Freshness` column of the
  `Data Freshness` table previously had no defined vocabulary at all.
- `references/scoring-standard.md` gains `Label Layering`, which maps each skill's domain
  read to the nine shared research labels. Regime, sector, catalyst, portfolio, and trade
  vocabularies were previously disconnected from the shared label set.
- The cross-module decision chain gains `Chain Constraints`: seven binding rules for how
  an upstream layer caps a downstream label, plus `Chain Provenance` requiring each
  upstream input to be attributed to a dated prior output, a user view, or an assumption.
  An assumed layer cannot support a strong label, and any `evidence-gap` layer caps the
  final label at `monitor closely`.
- Every skill now carries a degradation table mapping each missing or stale input to the
  required handling. Only `equity-research` had one before.
- `market-regime-monitor` gains the `Evidence Standard` and `Conclusion Gates` sections it
  was missing, so all six skills share the same structure.
- `portfolio-risk-monitor` and `trade-plan-risk-manager` no longer treat user-provided
  holdings or a user thesis as Tier 1 evidence. User input is a plan parameter, a fact
  claim to verify, or a preference, and a plan resting on unverified user claims cannot be
  labelled `tradable setup`.
- Every `Mode Selection` table gains a `Minimum input` column, so a mode is chosen against
  what is actually available instead of being run with silent gaps.
- `references/review-and-calibration.md` gains `Research Log`, defining where a call is
  written so the 1-week, 1-month, and 3-month review cadence can close. A skill has no
  memory between sessions, so the calibration loop was previously unable to complete.
- The validator now requires all four shared references to be routed from every
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
