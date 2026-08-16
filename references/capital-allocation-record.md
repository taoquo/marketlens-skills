# Capital Allocation Record

The capital-allocation items in `../equity-research/references/red-flags.md` are
qualitative: they say M&A should have a clear strategic fit and buybacks should not
merely offset compensation. Both are correct and unusable, because no threshold
decides when a fit is unclear or when a buyback is only treading water. This file
supplies the ledger, the computed returns, the promise-keeping record, and the rule
that turns a breach into a specific next step.

`earnings-quality-screens.md` asks whether the reported numbers can be trusted.
This file asks a different question of the same filings: over the last five years,
where did every dollar the company produced actually go, what did each destination
earn, and how often did management do what it said it would do. A company can pass
every earnings-quality screen and still destroy value by reinvesting at below its
cost of capital.

Every screen here is computable from five years of filings plus the proxy or
remuneration disclosure. None requires a data vendor. Grade inputs with
`data-discipline.md` and record each figure in the core figure check before using
it.

## How To Use These Screens

1. Build the ledger first. Without the sources-and-uses table the return screens have no denominator and the discussion drifts into anecdote about one acquisition.
2. Use a five-year window ending at the latest annual report. State the window. A single year of capital allocation is noise.
3. Compare each result with the company own prior window first, then with the peer set. Capital-allocation skill is a management attribute, so the relevant comparison is the same team over time.
4. Convert each breach into a named verification task with the specific disclosure that would settle it.
5. Separate what management chose from what the industry forced. A cyclical trough capex cut is not discipline, and a boom-time capacity build is not always empire building.

These screens judge decisions, not outcomes alone. A decision that was reasonable
on the information available and turned out badly is a different finding from a
decision that was unreasonable when it was made. State which one the evidence
supports.

## Sources And Uses Ledger

Build this over the full window. The two sides must reconcile, and the residual
must be explained rather than plugged.

| Sources over the window | Uses over the window |
|---|---|
| Cumulative operating cash flow | Maintenance capex |
| Proceeds from asset and business disposals | Growth capex |
| Net equity issued, gross issuance less buybacks removed to the uses side | Acquisitions net of cash acquired |
| Net new debt raised | Buybacks |
| Change in cash and equivalents, when drawn down | Dividends and other shareholder distributions |
| | Net debt repayment |
| | Change in cash and equivalents, when built up |

Maintenance versus growth capex is rarely disclosed. Use depreciation as the
maintenance proxy, state that it is a proxy, and check it against unit capacity or
store or fleet counts where the filing allows. Do not present the split as
disclosed when it is derived.

Three ratios follow directly from the ledger and frame everything below:

| Ratio | Formula | What it tells you |
|---|---|---|
| Reinvestment rate | (Growth capex + acquisitions) / cumulative NOPAT | How much of the earnings stream was bet on future growth rather than returned |
| Shareholder return rate | (Buybacks + dividends) / cumulative FCF | How much reached shareholders, and whether distributions exceeded internal generation |
| External funding dependence | (Net equity issued + net new debt) / total sources | Whether the growth was self-funded or bought with other people capital |

A high reinvestment rate is neither good nor bad by itself. It is a magnifier: it
multiplies whatever the incremental return turns out to be, in either direction.
Read it together with the first row of the next table and never on its own.

## Return On Allocated Capital

| Screen | Formula | Concern threshold | What it means |
|---|---|---:|---|
| ROIIC over the window | Change in NOPAT over the window / change in invested capital, lagged one year | Below WACC | The growth spending destroyed value even if reported earnings rose |
| ROIIC dual-basis ratio | ROIIC including goodwill / ROIIC excluding goodwill and acquired intangibles | Below 0.9 | Acquisitions are systematically diluting the return on capital |
| Incremental capital productivity | Change in revenue / change in invested capital | Declining three years running | Marginal investment efficiency is decaying while spending continues |
| Goodwill and acquired intangibles share | (Goodwill + acquired intangibles) / invested capital | Above 30 percent | The asset base was bought rather than built, so the return record is an acquisition record |
| Cumulative impairment rate | Cumulative goodwill and intangible impairment / cumulative acquisition consideration | Above 10 percent | Acquisitions have been systematically overpriced, admitted after the fact |
| Post-acquisition ROIC | Group ROIC three years after each material acquisition versus the year before | Down more than 2 percentage points | The deal diluted returns regardless of the accretion claimed at announcement |
| Buyback timing percentile | Weighted average repurchase price as a percentile of the trading range over the same period | Above the 60th percentile | Management bought its own stock in the upper part of its own range |
| Buyback net effect | Buyback spend / stock-based compensation over the same period | Below 1.0 | The buyback is a compensation offset, not a return of capital |
| Net dilution | Diluted share count CAGR over the window | Positive despite an active buyback | The share count expanded on a net basis, so per-share claims need restating |
| Buyback implied expectations | The `implied-expectations.md` read at the time of the largest repurchase years | `demanding` or worse while repurchasing | Management valuation judgement contradicts the framework, so weight its other judgements accordingly |
| Dividend sustainability | FCF / dividends paid, plus the funding source in years below 1.0 | Below 1.2, or funded by new debt | The distribution is consuming the balance sheet |
| Idle cash | Cash and equivalents above stated operating and committed needs / total assets | Above 20 percent for three years with no stated use | Leaving capital unallocated is also an allocation decision |

ROIIC is the load-bearing screen and the most abusable one, because both the
numerator and the denominator can be defined several defensible ways. Three rules
are mandatory. Report it on both bases, including and excluding goodwill. Report
both a three-year and a five-year window. Never report a single-year ROIIC; mark it
unavailable instead, because one year of working-capital or capex timing dominates
the ratio.

The dual-basis screen is a ratio rather than a spread on purpose. Including goodwill
enlarges the denominator, so the with-goodwill figure is always the lower of the two
and a percentage-point spread would flag every high-return business while missing the
acquisitive low-return one it is meant to catch. A ratio is scale-invariant: 0.53 on
an 8 percent base is the finding, and 0.93 on a 135 percent base is not.

## Promises Kept And Incentive Alignment

Capital allocation is a series of stated intentions. The record of whether those
intentions were met is observable, cheap to build, and rarely built.

| Screen | How to compute it | Concern threshold | What it means |
|---|---|---:|---|
| Guidance hit rate | Share of guided metrics met or beaten over 8 to 12 quarters | Below 60 percent | Management forecasts are not usable as a modelling input |
| Milestone slippage | Median delay of announced capacity, launch, or project dates | More than two quarters | Execution timelines need a standing haircut |
| Strategic priority drift | Count of stated top-priority changes over three years | Two or more reversals | There is no allocation policy, only a sequence of reactions |
| Compensation on capital efficiency | Whether the incentive plan includes ROIC, ROE, EVA, or relative TSR | No capital-efficiency metric present | Management is paid for size, so expect size |
| Insider ownership depth | Shares held outright, excluding unvested options, as a multiple of annual salary | Below 1 times | Downside is not shared |
| Insider net activity | Net insider buy or sell over the trailing 12 months | Sustained net selling while the company repurchases | The company is buying what its own officers are selling |
| Controlling-shareholder pledge | Pledged shares / shares held by the controlling holder | Above 30 percent | Forced-sale risk sits above the operating business |

The guidance hit rate is the same instrument as the `Company Self-History First`
section of `base-rates.md`. Build it once, per the construction rules there, and
use it in both places. This file supplies the threshold and the allocation
consequence; it does not restate the method.

Only observable facts belong in this table: the metric names in the incentive plan,
the share counts, the pledge percentage, the committee composition. Adjectives about
management quality are not screens and must stay out of them.

## Overlap With Earnings Quality

Six screens already exist in the `Balance Sheet And Capital Integrity` table of
`earnings-quality-screens.md`: share count trend, SBC intensity, ROIC versus WACC,
goodwill share, impairment absence, and related-party share. Compute them there and
carry the results here. Do not restate the formulas or count a breach twice in the
two aggregate reads.

The division is by purpose. Earnings quality asks whether the reported figures can
be relied on. This file asks whether the decisions behind them were competent. The
same goodwill balance is an impairment risk in one reading and an acquisition
track record in the other.

## Sector Substitutions

The screens above assume a business that reinvests in its own operations. Replace
them where the model differs, and say which were replaced.

| Sector | Do not use | Use instead |
|---|---|---|
| Banks | ROIIC, invested capital, growth capex | Retained-earnings growth versus RWA growth, capital return under the regulatory buffer, loan-book growth by vintage versus subsequent credit cost, acquisition of deposit franchises versus organic gathering cost |
| Insurers | ROIIC, capex split | Incremental new business value per unit of capital deployed, reserve strengthening as an admission of prior pricing, buyback versus solvency headroom |
| REITs and property | Maintenance capex proxy from depreciation | Development yield on cost versus current cap rate, disposal price versus carrying value, land-bank replacement cost versus current selling price, equity issuance below NAV |
| Utilities | ROIIC on a group basis | Return on the regulated asset base additions versus the allowed return, unregulated diversification returns, capex funded by equity issuance at a discount |
| Pre-revenue biotech | All return-based screens | Cash per program advanced, dilution per stage of progress, licensing terms retained versus given away, runway at each raise |
| Commodity producers | Single-window ROIIC | Full-cycle return on the last capex wave, reserve replacement cost per unit versus the acquisition alternative, counter-cyclicality of the buyback and capex timing |
| Serial acquirers | Group ROIC alone | Deal-level cash-on-cash return where disclosed, organic versus acquired growth split, acquisition multiple paid versus the company own trading multiple |

## A-Share Primary Disclosures

A-share filings disclose two things that no other market requires, and both are
first-order evidence here rather than supporting detail.

| Disclosure | What it gives you | How to use it |
|---|---|---|
| Performance of undertakings, the commitments section of the annual report | A named list of commitments by the company, controlling shareholder, and directors, with a stated fulfilment status | Read it as the promise-keeping record directly. It removes the need to reconstruct commitments from transcripts |
| Use of raised funds and the benefit realization of funded projects | Project-level committed return against realized return, with the shortfall reason | Treat it as disclosed project-level ROIIC. It is the closest thing any market provides to a per-project allocation audit |

Where these sections show repeated unfulfilled commitments or projects consistently
below their committed benefit, the finding is `Confirmed` under the confirmation
table in `../equity-research/references/red-flags.md`, not suspected, because the
company stated the shortfall itself.

## Aggregate Read

Count the breaches across the ledger ratios, the return screens, and the promise
screens. Do not count an overlap screen already counted in the earnings-quality
read.

| Breaches | Read | Required handling |
|---:|---|---|
| 0 to 1 | `disciplined` | Note it. A disciplined record is a reason to weight management guidance more heavily |
| 2 to 3 | `adequate` | Name the specific disclosure that would resolve each, and cap confidence at Medium on any forecast that relies on management plans |
| 4 to 6 | `value-leaking` | No `add-candidate watch`. Route through `Confirmation Status` in `../equity-research/references/red-flags.md` and apply a stated quality discount in valuation |
| 7 or more | `destructive` | Cap at `hold/watch` or lower. Value the business on a no-growth or replacement basis, because the reinvestment stream cannot be assumed to add value |

Weight the return screens above the promise screens, and weight persistence above
level. A management team with two breaches that have worsened for three years is a
worse allocator than one with five stable, disclosed, and explained breaches. The
adjustment is bounded at one band in either direction, and it must name the screens
that moved it. Without that bound the weighting rule becomes an escape hatch that can
produce any read from any breach count.

## Interaction With Valuation

Capital allocation enters valuation through the reinvestment assumption, which is
where most of the terminal value lives. `implied-expectations.md` solves for what
the price requires; this file decides whether the company is entitled to the
reinvestment credit that requirement contains.

The reinvestment credit is set by the return screens, not by the aggregate read.
The aggregate read sets the label cap and the confidence cap. When the two sides
disagree, which is common in a high-return business that distributes badly, report
them separately and say which side drives which conclusion. A company can earn the
full reinvestment credit and still cap at `adequate` because it repurchased stock
at the top of its own range.

| Allocation read | Effect on the valuation input |
|---|---|
| `disciplined` | Reinvestment can be credited at the historical ROIIC. Growth spending is a value driver in the model |
| `adequate` | Credit reinvestment at WACC, not at historical ROIIC. Growth becomes value-neutral |
| `value-leaking` | Credit reinvestment below WACC, or model the growth capex as a cash cost with no return |
| `destructive` | Switch the anchor to a no-growth or replacement-value basis and state that the going-concern reinvestment premium has been removed |

The dangerous combination is a high reinvestment rate with a low ROIIC and a
demanding implied expectation. The price is paying for growth, the company is
funding growth, and the growth is destroying value. That configuration caps the
label at `avoid` regardless of the reported earnings trend.

## Boundaries

- These screens judge allocation, not integrity. A breach is not an allegation of self-dealing, and the output must not use that language.
- Attribution to a specific acquisition requires segment or acquisition-level disclosure. Without it, use the group ROIC trajectory plus the cumulative impairment rate as a proxy, label it a proxy, and do not draw a confirmatory conclusion from it.
- Never state a computed ratio without its inputs, window, and accounting standard. Invested capital definitions differ across regimes and must be stated.
- Where a filing does not disclose an input, mark the screen unavailable rather than estimating it. Hong Kong remuneration disclosure is the coarsest of the three markets, so the compensation and insider-depth screens are frequently unavailable there and must be marked so rather than inferred from the total figure.
- Management tenure bounds the read. Do not attribute a predecessor allocation record to a team appointed inside the window; split the window at the transition and say so.
- The thresholds are starting points calibrated on large-cap developed-market data. State the threshold used, and adjust with a reason for small caps, early-stage companies, and different capital-market regimes.
