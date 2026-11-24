---
name: equity-research
description: Use when analyzing listed companies or stocks across US, Hong Kong, or A-share markets, including earnings reports, long-term holding quality, fundamentals, valuation, historical valuation bands, moat, cash flow, management, valuation-derived trigger levels, position review triggers, market-specific disclosure rules, or user questions phrased as whether a stock is worth buying, holding, adding, trimming, or exiting.
license: MIT
metadata:
  version: 0.11
---

# Equity Research

## Core Rule

Shared operating rules are in `../references/skill-contract.md`: public-market research only, no personalized investment advice, dated and sourced evidence, confidence and limits, and the exact disclaimer. Apply them to every output.

When the user asks in buy/sell/add/trim/exit terms, translate the answer into research labels, valuation ranges, staged review triggers, and thesis invalidation conditions. Do not prescribe a personal transaction, allocation, or exact position size.

## Skill Boundary

Use this skill for company quality, fundamentals, earnings, valuation, moat, regional disclosure checks, and single-stock research labels. For anything outside that scope, route through `../references/skill-routing.md`.

## Mode Selection

Choose the lightest mode that answers the user:

| User intent | Mode | Minimum input | Output depth |
|---|---|---|---|
| Long-term quality, Buffett-style, "worth holding" | `quick-value-score` | Ticker or company name, plus the latest annual or interim report | Six-dimension score plus key risks |
| Latest earnings, quarterly/annual report, guidance | `earnings-deepdive` | Ticker, reporting period, and the filing or release for that period | Key forces plus focused module analysis |
| "Is it cheap versus its own history?" / PE or PB band | `valuation-band` | Ticker, dated price, TTM earnings, and at least 3 years of trading history | Band position, percentile, slope, failure checks, and a valuation-band figure or table fallback; a cross-check, not a label |
| "Can I buy/sell/add/trim now?" | `decision-framework` | Ticker, dated current price, share count, net debt, and the latest cash flow statement | Research label, implied expectations, margin of safety, triggers |
| Broad or ambiguous stock analysis | Hybrid | Ticker or company name | Start with conclusion, then combine the needed modes |

If the minimum input cannot be obtained, drop to a lighter mode, name the missing input, and label the output as a partial read rather than filling the gap with an assumption.

If the company is a bank, insurer, broker, REIT, utility, highly cyclical commodity business, platform internet company, exporter, or pre-profit biotech, adjust the scoring and valuation criteria before rating and explain the adjustment.

## Region Selection

Infer the market from ticker, exchange, company name, or user wording. If unclear, ask one concise clarification.

| Region | Default primary evidence | Must watch |
|---|---|---|
| US | SEC 10-K/10-Q/8-K/DEF 14A, company IR, earnings call transcript | GAAP vs non-GAAP, SBC, buyback dilution, guidance quality |
| Hong Kong | Annual/interim reports, HKEXnews announcements, company IR, exchange filings | Southbound flows, placements, buybacks, AH premium, related-party deals |
| A-share | Annual/quarterly reports, exchange announcements, CNINFO, inquiry letters | Policy cycle, Northbound flows, margin financing, unlocks, one-off gains/losses |

## Reference Loading

Read only the references needed:

- For the shared operating, evidence, gate, freshness, and output contract, read `../references/skill-contract.md`.
- Required shared files: `../references/scoring-standard.md`, `../references/data-discipline.md`, `../references/skill-routing.md`, and `../references/review-and-calibration.md`.
- For leverage, maturity walls, covenants, cash runway, bond-implied stress, or credit-equity divergence, read `../references/credit-and-cross-asset.md`.
- For any probability, turnaround, margin-recovery, or guidance-reliability claim, read `../references/base-rates.md`.
- For confirmed red flags that support a negative thesis, or for a relative-value read against a peer, read `../references/short-and-relative-value.md`.
- For any multiple, fair value range, cheap-or-expensive judgement, or margin-of-safety claim, read `../references/implied-expectations.md` and solve for what the price requires before valuing the company.
- For any conclusion resting on reported profit, margin, growth, or cash conversion, read `../references/earnings-quality-screens.md` and compute the screens rather than describing the concern.
- For long-term holding quality, management assessment, M&A or issuance history, or any conclusion that credits future reinvestment, read `../references/capital-allocation-record.md` and build the sources-and-uses ledger before judging the record.
- For regional details, read `references/regional-market-guide.md`.
- For source priority, freshness TTL, and query patterns, read `references/data-sources.md`.
- For valuation methods, including a historical PE or PB band or percentile read, read `references/valuation-framework.md`; for a band, follow the Historical Valuation Band section.
- For sector-specific scoring, read `references/sector-adjustments.md`.
- For accounting, governance, dilution, and disclosure risks, read `references/red-flags.md`.

## Evidence Standard

Tier definitions and the decisive-claim rule are in `../references/data-discipline.md` and `../references/skill-contract.md`. Domain sources:

| Tier | Sources | Use |
|---|---|---|
| Tier 1 | Company filings, official announcements, earnings call transcripts, exchange disclosures | Core financials, guidance, governance, transactions |
| Tier 2 | Exchange data, regulator data, official macro data, company IR decks | Market structure, ownership, rates, liquidity |
| Tier 3 | Financial platforms, broker notes, media, consensus datasets | Context only; never sole basis for a decisive claim |

## Conclusion Gates

Map the company read to a shared label using the `Label Layering` table in `../references/scoring-standard.md`, and apply the shared gate rules in `../references/skill-contract.md`. Do not present personalized buy/sell advice or exact allocation instructions.

Domain-specific gates. Do not give a strong action-style research label or precise valuation-derived trigger level unless these are satisfied:

- Latest price and market cap are dated and cross-checked from two sources.
- Latest relevant filing/report is identified by period and publication date.
- At least one primary source supports the core financial claim.
- Valuation uses at least two relevant methods or explains why only one method is defensible.
- A historical valuation band is a cross-check, not a standalone valuation method. It does not satisfy the two-method gate and cannot support a strong action label by itself.
- The implied assumption behind the current price is stated with its discount-rate range, converted to an absolute quantity, and compared with the company own record.
- The cash-conversion screens have been computed for any conclusion that rests on reported earnings, with the breach count stated.
- For a long-term holding or reinvestment-driven conclusion, the capital-allocation ledger reconciles, ROIIC is reported on both bases over two windows, and the aggregate allocation read is stated.

If any gate fails, apply the downgrade rule in `../references/skill-contract.md` and name the evidence that would strengthen the view.

## Data Freshness Protocol

Apply the timestamp, freshness, and core-figure rules in `../references/data-discipline.md` and `../references/skill-contract.md`. Domain additions:

Equity-specific additions:

- For trigger-price, add-candidate, trim-review, exit-review, or valuation-sensitive conclusions, verify the current price and at least one core valuation input from two sources.
- Price data older than the latest completed trading session is `Stale` for any price-sensitive conclusion, even if it sits inside a generic TTL.
- Run every figure that carries the valuation or rating through the core figure check in `../references/data-discipline.md` before stating a strong label.
- A vendor PE/PB history is Tier 3. Reconcile the TTM denominator to filings and the price to a second source before using the band for a valuation-sensitive conclusion; otherwise cap confidence at Medium.

Degrade conclusions as follows:

| Missing or stale item | Required handling |
|---|---|
| Current price is not latest trading day | Avoid precise trigger-price language |
| Latest filing/report cannot be verified | Do not call the analysis a latest-earnings review |
| Only secondary financial data is available | Cap confidence at Medium |
| Only one valuation input is available | Give directional valuation only |
| The implied assumption cannot be solved, or WACC is a pure guess | Use the `not solvable` read, give directional language, and do not state a fair value range |
| Cash flow statement for the period is unavailable | Do not state an earnings quality read; treat reported profit as unverified and cap confidence at Medium |
| Fewer than three years of cash flow and invested capital data | Do not state an ROIIC or allocation read; mark the capital-allocation dimension unavailable |
| Remuneration or insider-holding disclosure is unavailable or aggregated only | Mark the incentive-alignment screens unavailable rather than inferring alignment from the total pay figure |
| Material announcement search is incomplete | Add a pending-disclosure caveat |
| Fiscal calendar or accounting standard is unclear | Do not compare the multiple against peers in another market |
| A user-provided figure conflicts with the filing | Use the filing, state the conflict, mark the user figure unverified |

## Workflow

1. Identify company, ticker, region, reporting period, user intent, and current date.
2. Collect the latest price, market cap, recent filing/report, and 3-5 years of key financials when available, with freshness timestamps.
3. Identify 1-3 Key Forces that determine future value over the next 3-5 years.
4. Run only the needed mode(s), loading the relevant reference files for valuation, sector adjustments, and red flags.
5. Cross-check valuation against current price before offering any decision framework. If the user asks for a historical valuation band, use the rolling point-in-time method in `references/valuation-framework.md`; a full-sample band is descriptive only.
6. Keep company quality, valuation, catalyst/timing, market regime, and portfolio role separate before assigning the final research label.
7. Output score summary, red flags, decision impact, review triggers, kill conditions, monitoring variables, and confidence limits.

## `quick-value-score`

Score each dimension from 0 to 3. Use total score only as a research shorthand, not as a mechanical buy signal.

| Dimension | 3 points | 2 points | 1 point | 0 points |
|---|---|---|---|---|
| ROE / ROIC durability | High and stable for 3+ years | Good but uneven | Average or cyclical | Weak or unstable |
| Balance sheet safety | Net cash or low leverage | Manageable leverage | Needs monitoring | High refinancing or solvency risk |
| Free cash flow quality | FCF consistently covers earnings | Usually cash generative | Volatile conversion | Negative or poor conversion |
| Earnings quality | 0-1 screen breaches, all explained | 2-3 breaches, each with a named verification task | 4-6 breaches, or a deteriorating trend | 7+ breaches, or the cash flow statement is unavailable |
| Capital allocation | `disciplined`: ROIIC above WACC, no net dilution, promises kept | `adequate`: 2-3 breaches, each disclosed and explained | `value-leaking`: 4-6 breaches, or ROIIC trending toward WACC | `destructive`: 7+ breaches, or ROIIC below WACC while spending expands |
| Moat | Multiple strong moats | One clear moat | Weak advantage | No durable advantage |

Rating: A = 15-18, B = 10-14, C = 5-9, D = 0-4. Score the earnings quality dimension from the aggregate read table in `../references/earnings-quality-screens.md`, and the capital allocation dimension from the aggregate read table in `../references/capital-allocation-record.md`. Do not count a screen twice when it appears in both files. For sector-specific replacements, use `references/sector-adjustments.md`.

A high quality score does not create an action conclusion by itself. Compare company quality with valuation, catalyst timing, market regime, and portfolio role before using action-style research labels.

## `earnings-deepdive`

Lead with the conclusion. Cover these modules only to the depth needed by the Key Forces:

- Revenue scale and quality: segment growth, recurring mix, geography, customer concentration.
- Profitability: gross/operating/net margin, GAAP vs adjusted gap, SBC or one-off items.
- Cash flow and capital allocation: OCF, FCF, capex, buybacks, dividends, M&A, dilution.
- Guidance and management signals: guidance vs consensus, tone shift, execution history.
- Competitive position: market share, product strength, pricing power, new business validation.
- Governance and ownership: insider behavior, major holders, related-party issues, pledges or placements.
- Earnings quality: cash conversion, accrual ratio, working capital versus revenue growth, capitalization and one-off dependence, with the breach count.
- Valuation: what the price implies, then at least two relevant methods, scenario range, sensitivity, margin of safety.

For tech or growth companies, explicitly test whether the market narrative is backed by revenue, users, contracts, or verifiable product adoption. For any company, check `references/red-flags.md` before forming the final view.

## `valuation-band`

Use when the user asks whether the current multiple is cheap or expensive against the company's own history, or asks for a PE/PB percentile or historical band. This is a valuation-layer cross-check, not a standalone research mode.

- Load `references/valuation-framework.md` and follow `Historical Valuation Band`.
- Require positive, comparable TTM earnings and at least 750 trading days of history; prefer 1,250 days or one full cycle.
- Use a trailing point-in-time window at each date. A full-sample band is descriptive only and cannot be used as a signal or in a backtest.
- Report position, percentile, slope, the EPS/PE decomposition of the price move, and the failure checks: structural break, denominator collapse or peak, one-offs, negative earnings, corporate actions, and rates.
- When the user asks for a visual, produce the Valuation Band figure defined in `references/valuation-framework.md`; if the host cannot render, use the table fallback.
- Map the result to the five valuation reads in `../references/implied-expectations.md`, then to a label through `../references/scoring-standard.md`. The band alone cannot support `add-candidate watch` or `trim-review`.
- If the user asks what to do, continue into `decision-framework`; do not turn the band into a buy/sell instruction.

## `decision-framework`

When asked what to do, translate the request into a research framework:

- Research classification: high-priority watch, add-candidate watch, hold/watch, trim-review, exit-review, avoid, or evidence-gap.
- Implied expectations: what the current price requires, and whether the company record supports it.
- Fair value range and trigger levels: derive from valuation first, then compare with current price.
- Review cadence: staged review language only; avoid all-in or transaction-prescriptive language.
- Add-candidate, trim-review, or exit-review triggers: concrete metrics, dates, prices, or business events.
- Kill conditions: what would invalidate the thesis.

Do not provide personalized allocation across the user's total assets unless the user gives risk tolerance, horizon, portfolio context, and constraints.

## Output Template

```markdown
# [Company] ([Ticker]) Equity Research

## Conclusion
[Research stance first: attractive/reasonable/rich/watch/avoid style language, confidence, and why.]

## Key Forces
[1-3 decisive forces, each tied to evidence.]

## Fundamentals And Earnings
[Focused findings from the selected mode.]

## Earnings Quality
[Computed screens with inputs and period, breach count and direction, aggregate read, and the specific disclosure that would resolve each breach. State which screens were skipped or substituted for the business model.]

## Capital Allocation And Management Record
[Sources-and-uses ledger over the stated window with the two sides reconciled, the three ledger ratios, ROIIC on both bases over three and five years, buyback timing and net dilution, guidance hit rate and milestone slippage, incentive alignment facts, and the aggregate read: disciplined, adequate, value-leaking, or destructive. State the reinvestment credit this read permits in the valuation below.]

## Implied Expectations
[Growth value share of EV, the solved implied variable with its WACC range and terminal assumption, the absolute quantity it requires, the company own historical rate, and the resulting read: undemanding, reasonable, demanding, priced for perfection, or not solvable.]

## Valuation And Decision Framework
[Fair value range as a cross-check on the implied read, current price/date, trigger levels if conclusion gates pass, review triggers, kill conditions. If a historical band is used, state the multiple and denominator convention, window and observations, band method and coverage, current position/percentile/slope, the EPS/PE decomposition of the price move, failure checks, and that it is a cross-check rather than a standalone label. If the user wants a visual, include the Valuation Band figure; otherwise include the same fields as a table.]

## Score Summary
| Dimension | Score | Evidence | Confidence | Comment |
|---|---:|---|---|---|

## Regional And Market-Specific Checks
[US/HK/A-share disclosure, ownership, capital flow, policy, or accounting issues.]

## Red Flags
[Material accounting, governance, dilution, policy, financing, or disclosure risks.]

## Decision Impact
[How quality, valuation, catalyst/timing, market regime, and portfolio role affect the research label.]

## What Would Change The View
[Concrete business, valuation, event, regime, or disclosure triggers that would upgrade or downgrade the view.]

## Confidence And Limits
[Confidence level, missing data, stale data, and unsupported claims avoided.]

## Data Freshness
| Data | Value | As of | Published | Retrieved | Source | Freshness |
|---|---:|---|---|---|---|---|

## Evidence Sources
| Source | Date | Type | Supports |
|---|---|---|---|

## Disclaimer
This is public-market research for reference only and does not constitute investment advice.
```
