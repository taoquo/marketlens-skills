---
name: equity-research
description: Use when analyzing listed companies or stocks across US, Hong Kong, or A-share markets, including earnings reports, long-term holding quality, fundamentals, valuation, moat, cash flow, management, valuation-derived trigger levels, position review triggers, market-specific disclosure rules, or user questions phrased as whether a stock is worth buying, holding, adding, trimming, or exiting.
license: MIT
metadata:
  version: 0.7
---

# Equity Research

## Core Rule

Provide public-market company research, not personalized investment advice. Match the user's language. State dates for all market data, distinguish facts from estimates and opinions, cite sources, state confidence and limits, and end with a short disclaimer that the analysis is for research only and does not constitute investment advice.

When the user asks in buy/sell/add/trim/exit terms, translate the answer into research labels, valuation ranges, staged review triggers, and thesis invalidation conditions. Do not prescribe a personal transaction, allocation, or exact position size.

## Skill Boundary

Use this skill for company quality, fundamentals, earnings, valuation, moat, regional disclosure checks, and single-stock research labels. For anything outside that scope, route through `../references/skill-routing.md`.

## Mode Selection

Choose the lightest mode that answers the user:

| User intent | Mode | Minimum input | Output depth |
|---|---|---|---|
| Long-term quality, Buffett-style, "worth holding" | `quick-value-score` | Ticker or company name, plus the latest annual or interim report | Five-dimension score plus key risks |
| Latest earnings, quarterly/annual report, guidance | `earnings-deepdive` | Ticker, reporting period, and the filing or release for that period | Key forces plus focused module analysis |
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

- For shared scoring, confidence, red-flag, and label discipline, read `../references/scoring-standard.md`.
- For timestamps, freshness grades, evidence tiers, unit and calendar rules, and user-input handling, read `../references/data-discipline.md`.
- For deciding which skill owns a question, read `../references/skill-routing.md`.
- For review of prior scores or labels, and for how a thesis decays when it is not reconfirmed, read `../references/review-and-calibration.md`.
- For leverage, maturity walls, covenants, cash runway, bond-implied stress, or credit-equity divergence, read `../references/credit-and-cross-asset.md`.
- For any probability, turnaround, margin-recovery, or guidance-reliability claim, read `../references/base-rates.md`.
- For confirmed red flags that support a negative thesis, or for a relative-value read against a peer, read `../references/short-and-relative-value.md`.
- For any multiple, fair value range, cheap-or-expensive judgement, or margin-of-safety claim, read `../references/implied-expectations.md` and solve for what the price requires before valuing the company.
- For any conclusion resting on reported profit, margin, growth, or cash conversion, read `../references/earnings-quality-screens.md` and compute the screens rather than describing the concern.
- For regional details, read `references/regional-market-guide.md`.
- For source priority, freshness TTL, and query patterns, read `references/data-sources.md`.
- For valuation methods, read `references/valuation-framework.md`.
- For sector-specific scoring, read `references/sector-adjustments.md`.
- For accounting, governance, dilution, and disclosure risks, read `references/red-flags.md`.

## Evidence Standard

Use primary sources first. Do not fabricate citations or quote text you cannot verify.

| Tier | Sources | Use |
|---|---|---|
| Tier 1 | Company filings, official announcements, earnings call transcripts, exchange disclosures | Core financials, guidance, governance, transactions |
| Tier 2 | Exchange data, regulator data, official macro data, company IR decks | Market structure, ownership, rates, liquidity |
| Tier 3 | Financial platforms, broker notes, media, consensus datasets | Context only; never sole basis for a decisive claim |

Always include an `Evidence Sources` section with source name, date, link, and what it supports.

## Conclusion Gates

Use research language such as attractive, reasonable, rich, watch, high-priority watch, add-candidate watch, hold/watch, trim-review, exit-review, avoid, evidence-gap, or thesis invalidated. Map the company read to a shared label using the `Label Layering` table in `../references/scoring-standard.md`. Do not present personalized buy/sell advice or exact allocation instructions.

Do not give a strong action-style research label or precise valuation-derived trigger level unless these are satisfied:

- Latest price and market cap are dated and cross-checked from two sources.
- Latest relevant filing/report is identified by period and publication date.
- At least one primary source supports the core financial claim.
- Valuation uses at least two relevant methods or explains why only one method is defensible.
- The implied assumption behind the current price is stated with its discount-rate range, converted to an absolute quantity, and compared with the company own record.
- The cash-conversion screens have been computed for any conclusion that rests on reported earnings, with the breach count stated.

If any gate fails, downgrade to a watchlist-style conclusion, state the missing data, and explain what evidence would be required to strengthen the view.

## Data Freshness Protocol

Timestamps, freshness grades, evidence tiers, unit and calendar rules, and the core figure check are defined in `../references/data-discipline.md`. Load that file before writing the `Data Freshness` table and use its five freshness grades verbatim.

Equity-specific additions:

- For trigger-price, add-candidate, trim-review, exit-review, or valuation-sensitive conclusions, verify the current price and at least one core valuation input from two sources.
- Price data older than the latest completed trading session is `Stale` for any price-sensitive conclusion, even if it sits inside a generic TTL.
- Run every figure that carries the valuation or rating through the core figure check in `../references/data-discipline.md` before stating a strong label.

Degrade conclusions as follows:

| Missing or stale item | Required handling |
|---|---|
| Current price is not latest trading day | Avoid precise trigger-price language |
| Latest filing/report cannot be verified | Do not call the analysis a latest-earnings review |
| Only secondary financial data is available | Cap confidence at Medium |
| Only one valuation input is available | Give directional valuation only |
| The implied assumption cannot be solved, or WACC is a pure guess | Use the `not solvable` read, give directional language, and do not state a fair value range |
| Cash flow statement for the period is unavailable | Do not state an earnings quality read; treat reported profit as unverified and cap confidence at Medium |
| Material announcement search is incomplete | Add a pending-disclosure caveat |
| Fiscal calendar or accounting standard is unclear | Do not compare the multiple against peers in another market |
| A user-provided figure conflicts with the filing | Use the filing, state the conflict, mark the user figure unverified |

## Workflow

1. Identify company, ticker, region, reporting period, user intent, and current date.
2. Collect the latest price, market cap, recent filing/report, and 3-5 years of key financials when available, with freshness timestamps.
3. Identify 1-3 Key Forces that determine future value over the next 3-5 years.
4. Run only the needed mode(s), loading the relevant reference files for valuation, sector adjustments, and red flags.
5. Cross-check valuation against current price before offering any decision framework.
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
| Moat | Multiple strong moats | One clear moat | Weak advantage | No durable advantage |

Rating: A = 12-15, B = 8-11, C = 4-7, D = 0-3. Score the earnings quality dimension from the aggregate read table in `../references/earnings-quality-screens.md`. For sector-specific replacements, use `references/sector-adjustments.md`.

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

## Implied Expectations
[Growth value share of EV, the solved implied variable with its WACC range and terminal assumption, the absolute quantity it requires, the company own historical rate, and the resulting read: undemanding, reasonable, demanding, priced for perfection, or not solvable.]

## Valuation And Decision Framework
[Fair value range as a cross-check on the implied read, current price/date, trigger levels if conclusion gates pass, review triggers, kill conditions.]

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
