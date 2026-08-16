# Earnings Quality Screens

The red-flag list in `../equity-research/references/red-flags.md` is qualitative:
it says receivables should not outgrow sales. That is correct and unusable, because
two analysts reading the same filing will disagree on whether the gap is material.
This file supplies the computed ratios, the thresholds, and the rule that turns a
threshold breach into a specific next step.

Every screen here is computable from a single filing plus the prior-year
comparative. None requires a data vendor. Grade inputs with
`data-discipline.md` and record each figure in the core figure check before using
it.

## How To Use These Screens

1. Compute the screens that apply to the business model. Skip the ones that do not, and say which were skipped and why.
2. Compare each result with the company own prior three to five years first, then with the peer set. A ratio without its own history is a number, not a signal.
3. A single breach is a question, not a conclusion. Count the breaches.
4. Convert each breach into a named verification task with the specific disclosure that would settle it.
5. State direction, not just level. A deteriorating ratio inside an acceptable band is more informative than a stable ratio outside it.

Ratios are screens. They locate where to read the filing; they never replace
reading it.

## Cash Conversion

The single most informative family. Accrual accounting allows profit without cash;
these screens measure the gap and its persistence.

| Screen | Formula | Concern threshold | What it means |
|---|---|---:|---|
| OCF to net income | Operating cash flow / net income | Below 0.8 for two or more consecutive years | Reported profit is not converting to cash on a sustained basis |
| FCF to net income | (OCF - capex) / net income | Below 0.5 with no growth-capex explanation | Cash generation depends on capex staying suppressed |
| Cash conversion trend | The three-year direction of OCF to net income | Declining three years running | Deterioration is structural rather than a timing effect |
| Accrual ratio, balance sheet | (Net operating assets end - start) / average net operating assets | Above 10 percent | Growth is landing on the balance sheet, not in cash |
| Accrual ratio, cash flow | (Net income - OCF - investing cash flow) / average total assets | Above 5 percent, or in the worst quintile of the peer set | The classic accrual anomaly measure; high accruals predict weaker future returns |
| Earnings persistence | Volatility of the accrual component versus the cash component | Accrual component is the larger and more volatile part | The earnings base is the part least likely to repeat |

For a genuine growth company, working capital build is expected. The test is whether
the build is proportional to growth, and whether it ever reverses. Ten years of
working capital absorption with no reversal is not a growth pattern.

## Working Capital And Revenue Quality

| Screen | Formula | Concern threshold | What it means |
|---|---:|---:|---|
| DSO | Receivables / revenue times 365 | Rising more than 15 percent year on year, or well above the peer set | Revenue may be pulled forward through channel or credit terms |
| DIO | Inventory / COGS times 365 | Rising more than 15 percent year on year | Demand is weakening, or obsolescence is being deferred |
| DPO | Payables / COGS times 365 | Rising sharply | Suppliers are financing the business; check for supply-chain finance |
| Cash conversion cycle | DSO plus DIO minus DPO | Lengthening while revenue growth slows | Working capital is absorbing cash exactly when it is least affordable |
| Receivables versus revenue growth | Receivables growth minus revenue growth | Above 10 percentage points | The revenue increment is on credit, not collected |
| Inventory versus revenue growth | Inventory growth minus revenue growth | Above 10 percentage points | Build is ahead of demand; a write-down risk is accumulating |
| Contract assets and unbilled | Unbilled receivables and contract assets as a share of revenue | Rising materially | Recognition is running ahead of billing |
| Deferred revenue direction | Change in deferred revenue versus revenue growth | Falling while revenue grows | Forward-looking demand is weaker than the reported top line |
| Allowance ratio | Bad-debt allowance / gross receivables | Falling while DSO rises | Provisioning is being relaxed as collection risk increases |
| Other receivables and prepayments | Balance and growth, plus counterparty disclosure | Large or fast-growing with thin disclosure | A common route for related-party value transfer in A-share and HK filings |

## Margin And Cost Capitalization

| Screen | Formula | Concern threshold | What it means |
|---|---|---:|---|
| Capitalization rate | Capitalized development or interest / total spend on it | Rising, or high versus peers | Current cost is being moved into future amortization |
| Depreciation adequacy | Depreciation / gross PP&E, versus stated useful lives | Falling, or lives extended | A margin gain purchased with an accounting estimate |
| Amortization of intangibles | Amortization / capitalized intangibles | Falling while the intangible balance rises | The cost is being deferred rather than incurred |
| Gross margin without explanation | Margin change decomposed into volume, price, mix, and cost | No decomposition possible | An unexplained margin change is the least reliable earnings input |
| Adjusted versus reported gap | (Adjusted earnings - reported) / reported | Above 20 percent, or widening | Check whether the same items recur every year |
| Recurring one-offs | Count of consecutive years with a material one-off item | Three or more years running | An item that appears every year is an operating cost |
| Non-operating profit share | Subsidies, fair-value gains, disposals, investment income / pre-tax profit | Above 20 percent | Reported profit is not from operations. Common in A-share filings |
| Effective tax rate swing | Year-on-year change in effective tax rate | More than 5 percentage points with no stated cause | A tax-driven earnings change is not an operating improvement |

## Balance Sheet And Capital Integrity

| Screen | Formula | Concern threshold | What it means |
|---|---|---:|---|
| Goodwill share | Goodwill / total assets and / equity | Above 30 percent of equity | Impairment can remove equity without any cash event |
| Impairment absence | Years since any impairment, against segment performance | No impairment while a segment underperforms | A recognition delay, not an absence of loss |
| Asset turnover | Revenue / average total assets | Declining while capex rises | New capital is not producing revenue |
| ROIC versus WACC | NOPAT / invested capital, against cost of capital | Below WACC while capex grows | Growth is destroying value, so the reinvestment thesis fails |
| Share count trend | Diluted share count over three years | Rising while buybacks are announced | Buybacks are offsetting compensation, not reducing the count |
| SBC intensity | Stock-based compensation / revenue and / OCF | High and rising | Cash flow flattered by a real, non-cash cost |
| Off-balance-sheet obligations | Leases, guarantees, JV commitments, factoring, supply-chain finance | Present and material | Leverage understated by reported debt alone |
| Related-party share | Related-party revenue, purchases, and balances / totals | Material or rising | Revenue quality and pricing independence are both in question |

## Sector Substitutions

The screens above assume an industrial or commercial model. Replace them where the
model differs, and say which were replaced.

| Sector | Do not use | Use instead |
|---|---|---|
| Banks | OCF to net income, DSO, DIO | Provision coverage, NPL formation rate, restructured and special-mention migration, credit cost versus through-cycle average, NIM decomposition, capital ratio trend |
| Insurers | Accrual ratios, working capital | Reserve development, assumption changes and their earnings effect, new business margin, expense overrun, investment-yield dependence |
| REITs and property | Net income based ratios | Same-store NOI, maintenance versus development capex split, capitalized interest, fair-value gains as a share of profit, presale collection and delivery ratio |
| Utilities | Asset turnover | Regulated asset base growth versus allowed return, capitalized cost recovery, deferred regulatory assets |
| Pre-revenue biotech | All revenue-based ratios | Cash runway in quarters, R&D versus G&A split, milestone versus collaboration revenue mix, dilution history |
| Commodity producers | Single-year margin | Cost per unit versus the industry curve, sustaining versus growth capex, reserve life and replacement rate, hedge book effect on realized price |

## Aggregate Read

Count the breaches across the families above and treat the count as the signal. A
single ratio can always be explained; a pattern across independent families is
harder to explain away.

| Breaches | Read | Required handling |
|---:|---|---|
| 0 to 1 | Clean, or one explainable item | Note it and continue |
| 2 to 3 | Watch | Name the specific disclosure that would resolve each, and cap confidence at Medium |
| 4 to 6 | Suspected quality problem | Route through `Confirmation Status` in `../equity-research/references/red-flags.md`. No label above `hold/watch` on fundamentals |
| 7 or more | Quality failure until disproven | `avoid` or `evidence-gap`. Consider an accounting thesis under `short-and-relative-value.md` only after its feasibility checks |

Weight breaches by direction and persistence rather than counting them equally. Two
breaches that have deteriorated for three consecutive years outrank five that are
stable and disclosed. State the weighting used.

## Interaction With Valuation

Earnings quality and implied expectations multiply rather than add. Poor quality
plus demanding expectations is the most dangerous combination in the framework,
because the accrual reversal arrives exactly when the growth assumption is being
tested.

| Quality read | Demanding expectations | Undemanding expectations |
|---|---|---|
| Clean | Valuation risk only. State what must be true | The constructive case, if quality and evidence gates pass |
| Watch | No `add-candidate watch`. Resolve quality first | Possible value case; the quality question is the whole thesis |
| Suspected or failed | Cap at `avoid`. Do not treat the multiple as support | A value trap until quality is resolved, not a cheap stock |

## Boundaries

- These are screens on reported figures. A breach is not an allegation of fraud, and the output must not use that language.
- Never state a computed ratio without its inputs, period, and accounting standard. Cross-standard comparison of accrual ratios requires an explicit note.
- Where a filing does not disclose an input, mark the screen unavailable rather than estimating it.
- The thresholds are starting points calibrated on large-cap developed-market data. State the threshold used, and adjust with a reason for small caps, high-growth companies, and different accounting regimes.

