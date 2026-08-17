# Changelog

Release history for MarketLens Skills. Versions match `metadata.version` in each
`SKILL.md`.

## v0.8 Capital Allocation: Where The Cash Went, And Whether The Promises Held

v0.7 made the reported numbers and the valuation method testable. Both still stopped
at the income statement. This release adds the one question a long-term holder
actually needs answered: over five years, where did every dollar the company
produced go, what did each destination earn, and how many times did management do
what it said it would do. A company can pass every earnings-quality screen and still
destroy value by reinvesting below its cost of capital.

- New `references/capital-allocation-record.md`. The capital-allocation red flags previously
  said M&A should have a clear strategic fit and buybacks should not merely offset
  compensation, which no threshold decides. The file starts with a five-year sources-and-uses
  ledger whose two sides must reconcile, with depreciation as the declared maintenance-capex
  proxy, and derives three framing ratios: reinvestment rate against cumulative NOPAT,
  shareholder return rate against cumulative FCF, and external funding dependence. Twelve
  return screens then measure what the spending earned: ROIIC over the window, the gap between
  the with-goodwill and ex-goodwill bases, incremental capital productivity, goodwill and
  acquired intangibles as a share of invested capital, cumulative impairment against cumulative
  acquisition consideration, post-acquisition ROIC change, buyback timing as a percentile of the
  company own trading range, buyback spend against SBC, net dilution, the implied-expectations
  read at the time of the largest repurchases, dividend coverage and its funding source, and
  idle cash. ROIIC carries three mandatory rules: both bases, both a three-year and a five-year
  window, and no single-year figure. Seven further screens measure stated intentions against
  outcomes: guidance hit rate, milestone slippage, strategic priority drift, whether the
  incentive plan contains any capital-efficiency metric, insider ownership depth excluding
  unvested options, insider net activity against company repurchases, and controlling-shareholder
  pledge. A sector table replaces the return screens for banks, insurers, REITs, utilities,
  pre-revenue biotech, commodity producers, and serial acquirers. An A-share section treats the
  performance-of-undertakings and use-of-raised-funds disclosures as primary evidence, because
  they are the only place any market publishes a project-level allocation audit, and a shortfall
  stated there is `Confirmed` rather than suspected. `Aggregate Read` maps the breach count to
  `disciplined`, `adequate`, `value-leaking`, and `destructive`, and an interaction table converts
  each read into the reinvestment credit the valuation may take.
- Overlap with `earnings-quality-screens.md` is declared rather than duplicated. Six screens
  already live there: share count trend, SBC intensity, ROIC versus WACC, goodwill share,
  impairment absence, and related-party share. They are computed once and carried over, and a
  breach is never counted in both aggregate reads. The division is by purpose: earnings quality
  asks whether the reported figures can be relied on, this file asks whether the decisions
  behind them were competent.
- `references/scoring-standard.md` adds capital allocation as a label layer and four binding
  chain constraints: `value-leaking` blocks `add-candidate watch`; `destructive` caps the label
  at `hold/watch` and forces a no-growth or replacement valuation anchor; a guidance hit rate
  below threshold forces any management-guidance forecast to be rebuilt on the company own
  historical rate; and a high reinvestment rate with ROIIC below WACC and demanding implied
  expectations caps the label at `avoid`. A new red-flag override covers reinvestment that keeps
  expanding while its incremental return sits below WACC.
- `equity-research`: `quick-value-score` goes from five dimensions to six, with the new
  Capital allocation dimension scored from the aggregate read. Rating bands are rebased to
  A = 15-18, B = 10-14, C = 5-9, D = 0-4. The output template adds
  `Capital Allocation And Management Record` before `Implied Expectations`, because ROIIC is an
  input to the reverse valuation rather than a comment on it. A conclusion gate requires the
  ledger to reconcile and ROIIC to be reported on both bases over two windows; two degradation
  rows mark the dimension unavailable when history is under three years or remuneration
  disclosure is aggregated only.
- `red-flags.md`: the Capital Allocation And Dilution section now routes to the computed
  screens, gains two items for below-WACC reinvestment and repeated unmet commitments, and the
  confirmation table maps the four allocation reads to `Watch`, `Suspected`, and failure, with
  the two A-share disclosures named as `Confirmed` without further work.
- The other five skills load the file by trigger: acquisition, buyback, dividend, and
  equity-raise events in `catalyst-event-monitor`; shared reinvestment-dependent theses as a risk
  cluster in `portfolio-risk-monitor`; peer ranking on return-on-incremental-capital in
  `sector-industry-research`, which also adds a capital-allocation comparison dimension; and the
  guidance-hit-rate haircut on plans that depend on management delivery in
  `trade-plan-risk-manager`. `review-and-calibration.md` adds capital-allocation error as a
  fourteenth attribution category, and `equity-research/references/data-sources.md` adds the
  market-specific primary sources for each screen.
- All six skills move to `metadata.version: 0.8`. Examples rebuilt as `marketlens-v08-*`.
- Example completeness pass. Every case now carries a `Data Freshness` section, which none of
  them had before, with the three timestamps from `references/data-discipline.md` and one of the
  five closed grades per input, so each stated confidence cap traces back to a named lagged or
  missing input rather than to prose. The market-regime case also gained the `Decision Impact`
  block it was missing, mapping the -3 axis total into what each downstream layer is and is not
  allowed to conclude. Both READMEs add a Coverage table recording the one-case-per-skill mapping
  and stating that `Evidence Sources` and `Disclaimer` are carried by the typeset footer.

## v0.7 Valuation: What The Price Requires, And Whether The Earnings Are Real

v0.6 widened what the toolkit could look at. This release fixes the two places where
a conclusion was still allowed to rest on an unexamined number: the valuation method
itself, and the reported earnings a multiple is applied to. Two cross-cutting
references are added, loaded by trigger.

- New `references/implied-expectations.md`. Valuation was previously stated as a set of
  methods with a caveat about ranges, which lets a forward DCF hide its conclusion inside
  WACC and terminal growth. The file inverts the question. `Growth Value Share` splits EV
  into the no-growth component at `NOPAT / WACC` and the growth component, with four bands
  and a mandatory explicit EV bridge. A six-step reverse DCF procedure fixes the observables,
  requires a WACC range instead of a point, solves for exactly one variable, and forces the
  solved variable into an absolute quantity such as terminal-year revenue, unit volume, or
  implied market share, because percentages hide impossibility. The value-driver identity
  `P/E = (1 - g / ROIC) / (r - g)` keeps growth and returns internally consistent: at r = 9
  percent, 30x implies about 7.3 percent perpetual growth at 15 percent ROIC and about 8.1
  percent at 8 percent ROIC. A table reads each common multiple as an implied statement,
  including the check that 12x EV/Sales against a mature 15x EV/EBIT implies an 80 percent
  steady-state EBIT margin. A business-type table names what to solve for when a reverse DCF
  does not fit: banks, insurers, REITs, regulated utilities, cyclicals, pre-profit platforms,
  and pre-revenue biotech. Margin of safety is restated as the distance between the implied
  assumption and the historical record, with five reads from `undemanding` to `not solvable`
  and the label effect of each.
- New `references/earnings-quality-screens.md`. The red-flag list said receivables should not
  outgrow sales, which is correct and unusable because two analysts will disagree on
  materiality. This file supplies computed ratios, thresholds, and the rule that converts a
  breach into a named verification task. Every screen is computable from one filing plus the
  prior-year comparative, with no data vendor. Cash conversion covers OCF and FCF to net
  income, the three-year direction, and both the balance-sheet and cash-flow accrual ratios.
  Working capital covers DSO, DIO, DPO, the conversion cycle, receivables and inventory growth
  gaps, contract assets, deferred-revenue direction, the allowance ratio, and other receivables
  and prepayments as the common related-party route in A-share and HK filings. Cost
  capitalization covers the capitalization rate, depreciation adequacy, the adjusted-to-reported
  gap, recurring one-offs, non-operating profit share, and tax-rate jumps. Balance-sheet
  integrity covers goodwill to equity, absent impairment, asset turns, ROIC against WACC, share
  count, SBC intensity, off-balance-sheet obligations, and related-party share. A sector table
  states which screens do not apply to banks, insurers, REITs, utilities, pre-profit biotech,
  and commodity producers, and what replaces them. `Aggregate Read` maps the breach count to
  four bands, capping confidence at Medium from two breaches and capping the fundamental label
  at `hold/watch` from four.
- The two files are joined by a matrix in `earnings-quality-screens.md`. Quality read crossed
  with implied expectations makes the dangerous cell explicit: weak quality plus demanding
  expectations, where the accrual reversal arrives exactly when the growth assumption is being
  tested. Questionable quality plus low expectations is named as a value trap rather than a
  cheap stock.
- `references/scoring-standard.md` adds two prerequisites ahead of the scoring rules: a
  valuation must state what the price implies before it states a view, and a conclusion resting
  on reported profit must pass the screens first. `Label Layering` gains the valuation and
  earnings-quality reads, `Red Flag Overrides` gains two entries, and `Chain Constraints` gains
  three: demanding implied expectations block `add-candidate watch`, four or more screen breaches
  cap the fundamental label at `hold/watch`, and questionable quality with demanding expectations
  caps at `avoid`.
- `equity-research/SKILL.md` moves from four scoring dimensions to five, adding earnings quality
  with the rating bands rescaled to A = 12-15, B = 8-11, C = 4-7, D = 0-3. `decision-framework`
  now requires share count, net debt, and the latest cash flow statement as minimum input. The
  output template gains `## Earnings Quality` and `## Implied Expectations` ahead of the existing
  valuation block, which is restated as a cross-check on the implied read. Two conclusion gates
  and two degradation rows are added: an unsolvable implied assumption returns `not solvable`,
  and an unavailable cash flow statement means no quality read and confidence capped at Medium.
- `equity-research/references/valuation-framework.md` requires the reverse pass before the forward
  pass and the cash-conversion screens before any multiple. `DCF Discipline` adds three rules,
  including that a forward DCF cannot be the primary method when terminal value exceeds 70 percent
  of EV. `Relative Valuation` now translates a multiple into its implied assumption before
  comparing it. `Margin Of Safety` is rewritten around the implied-assumption distance with four
  required outputs.
- `equity-research/references/red-flags.md` ties `Suspected` status to a computed screen breach
  rather than a narrative concern, and states that financial-quality flag status follows the breach
  count. `sector-adjustments.md` now points at the sector substitution tables in both new files and
  requires the output to say which screens were skipped and which implied variable replaced the
  default.
- The other five skills route to the new files by trigger. `sector-industry-research` adds implied
  assumption and earnings quality as peer-comparison dimensions. `catalyst-event-monitor` adds the
  check for whether an event only delivers what the price already implies, and a post-event step
  that decomposes the result into volume, price, mix, cost, accrual, capitalization, one-off, and
  tax before judging the thesis. `portfolio-risk-monitor` adds two concentration flags: several
  holdings needing above-history growth is one duration bet, and two holdings breaching the same
  screen is usually one accounting practice. `trade-plan-risk-manager` rewrites the edge dimension
  around whether the price already contains the thesis, since the most common false edge is
  research that arrives at the consensus embedded in the price.
- `references/review-and-calibration.md` adds implied-expectation and earnings-quality error types,
  and two decay conditions: the price now implying a more demanding assumption than at the original
  date forces a re-solve, and a new reporting period expires the earnings-quality read.
- The six `examples/` cases are rebuilt against v0.7 and renamed from `marketlens-v03-*` to
  `marketlens-v07-*`. Each case now carries the new blocks rather than only the new wording: the
  equity case adds `Earnings Quality` and `Implied Expectations` with a three-WACC reverse DCF, the
  regime case adds the credit and rates axis and moves to the four-point axis scale, the sector case
  ranks peers by implied assumption and reads each multiple as an implied statement, the catalyst case
  adds the already-priced gate and the eight-source post-event decomposition, the portfolio case adds
  the credit, direction, implied-assumption, and earnings-quality exposure dimensions with the two new
  concentration flags, and the trade-plan case is downgraded to `monitor closely` because its upside
  case restates the price-implied assumption, with liquidity graded on the four-band scale.
- New `scripts/render-examples.sh` and `scripts/stack_pages.py` build both artefacts from each
  example HTML: an A4-paginated `.pdf` for reading, and a single continuous `.png` for preview, so
  two-column sections are no longer split by page breaks.

## v0.6 Coverage: Credit, Base Rates, And The Short Side

v0.5 made the shared rules executable. This release closes gaps in what the toolkit
can analyse at all. Three cross-cutting references are added, loaded by trigger
rather than by skill.

- New `references/credit-and-cross-asset.md`. Equity is the junior claim, but no skill
  read credit. The market-level table adds IG and HY spreads, real yields, breakevens,
  term premium, cross-currency basis, bank lending conditions, and the issuance window.
  The single-name table adds the maturity ladder, cost of new debt, covenant headroom,
  liquidity sources, rating trajectory, structural seniority, and contingent claims. A
  credit-equity divergence table states what each pattern means, and a sector table names
  where an equity conclusion without a credit read is incomplete rather than merely less
  precise.
- New `references/base-rates.md`. `Probability Discipline` previously required evidence
  before assigning a probability but never said where the historical rate comes from.
  This file defines reference-class construction, a table of common classes for approvals,
  deal completion, guidance reliability, cycle duration, margin recovery, turnarounds,
  capacity cycles, and post-event drift, a company-self-history-first rule, a recording
  table that keeps the unadjusted rate visible next to the adjusted estimate, and six
  named failure modes including reference-class shopping.
- New `references/short-and-relative-value.md`. Every framework read one direction, so a
  confirmed accounting problem could only lower confidence in a long. This file adds seven
  short thesis types with their evidence bars and typical failures, nine feasibility checks
  covering borrow, recall, crowding, carry, corporate action, and venue rules, asymmetry
  rules reflecting unbounded loss and time decay, squeeze conditions, five short-side reads
  where `avoid only` is the default, six relative-value pair types with the constraints
  that make a spread structurally persistent, and an expression comparison table.
- `references/scoring-standard.md` adds the short and relative-value reads to `Label
  Layering`, and three new `Chain Constraints`: a maturity, covenant, or runway limit inside
  the thesis horizon caps the label at `monitor closely`; credit weakening while equity holds
  is a red flag; and a probability without a reference class is replaced by directional
  language.
- `references/review-and-calibration.md` adds `Thesis Decay`. A label that has not been
  reconfirmed is no longer intact by default: a passed catalyst window downgrades one step,
  two review windows without new primary evidence cap at `monitor closely`, price moving
  toward the thesis without fundamental follow-through reduces rather than raises confidence,
  and an open log entry past its own review window cannot be a Tier 1 input. Error
  attribution adds base-rate, credit or funding, and decay errors.
- `references/skill-routing.md` adds `Cross-Cutting References` with the trigger for each new
  file, and `Out Of Scope`: crypto, standalone FX, commodity futures, bond selection, options
  strategy, convertibles, private companies, fund selection, portfolio optimization, tax and
  legal advice, ESG scoring, intraday execution, and personal financial planning. Each row
  names the in-scope adjacent read instead of leaving the model to improvise.
- `market-regime-monitor/references/indicator-definitions.md` gains seven credit and rates
  indicators. The liquidity axis previously had no credit-spread input at all, which is the
  clearest single risk-appetite signal.
- `equity-research/references/red-flags.md` gains `Confirmation Status`. A confirmed flag is
  information about the company, not about the analysis, so it now routes to a specific next
  step instead of only deducting confidence.
- `equity-research/references/regional-market-guide.md` gains `Frictions And Net Return`:
  dividend withholding, transaction taxes, Stock Connect access constraints, short-side rules,
  FX hedging cost, and settlement mechanics. Cross-venue comparison was previously stated gross.
- `trade-plan-risk-manager/references/risk-and-execution.md` gains `Tradability Thresholds`,
  replacing "liquid enough for the horizon" with four bands and a highest-allowed label for
  each, judged on free float rather than market cap, with spread measured against the stop
  distance. Unmeasured liquidity caps at `conditional setup`.
- `sector-industry-research/references/peer-comparison.md` adds the `Structural loser`
  classification and `Relative Value Within The Peer Set`. Most industry shifts have two sides.
- `portfolio-risk-monitor/references/exposure-framework.md` adds credit-funding and direction
  exposure dimensions, plus flags for shared refinancing windows, hedges that share the driver
  they claim to offset, and gross exposure treated as diversified because net looks small.
- `catalyst-event-monitor/references/scenario-framework.md` requires the base-rate table
  whenever scenario probabilities appear.
- The validator now fails when a file in the top-level `references/` directory is not routed
  by any `SKILL.md`, so a cross-cutting file cannot sit in the repo drifting out of date.

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
