---
name: equity-research
description: Use when analyzing listed companies or stocks across US, Hong Kong, or A-share markets, including earnings reports, long-term holding quality, fundamentals, valuation, moat, cash flow, management, buy/hold/sell decisions, action price, position triggers, market-specific disclosure rules, or questions like whether a stock is worth buying, holding, adding, trimming, or exiting.
---

# Equity Research

## Core Rule

Provide public-market company research, not personalized investment advice. Match the user's language. State dates for all market data, distinguish facts from estimates and opinions, cite sources, state confidence and limits, and end with a short disclaimer that the analysis is for research only and does not constitute investment advice.

## Mode Selection

Choose the lightest mode that answers the user:

| User intent | Mode | Output depth |
|---|---|---|
| Long-term quality, Buffett-style, "worth holding" | `quick-value-score` | Four-dimension score plus key risks |
| Latest earnings, quarterly/annual report, guidance | `earnings-deepdive` | Key forces plus focused module analysis |
| "Can I buy/sell/add/trim now?" | `decision-framework` | Valuation, margin of safety, triggers |
| Broad or ambiguous stock analysis | Hybrid | Start with conclusion, then combine the needed modes |

If the company is a bank, insurer, broker, REIT, utility, highly cyclical commodity business, platform internet company, exporter, or pre-profit biotech, adjust the scoring and valuation criteria before rating and explain the adjustment.

## Region Selection

Infer the market from ticker, exchange, company name, or user wording. If unclear, ask one concise clarification.

| Region | Default primary evidence | Must watch |
|---|---|---|
| US | SEC 10-K/10-Q/8-K/DEF 14A, company IR, earnings call transcript | GAAP vs non-GAAP, SBC, buyback dilution, guidance quality |
| Hong Kong | Annual/interim reports, HKEXnews announcements, company IR, exchange filings | Southbound flows, placements, buybacks, AH premium, related-party deals |
| A-share | Annual/quarterly reports, exchange announcements, CNINFO, inquiry letters | Policy cycle, Northbound flows, margin financing, unlocks, one-off gains/losses |

For regional details, read `references/regional-market-guide.md`. For source priority, freshness TTL, and query patterns, read `references/data-sources.md`. For valuation methods, read `references/valuation-framework.md`. For sector-specific scoring, read `references/sector-adjustments.md`. For accounting, governance, dilution, and disclosure risks, read `references/red-flags.md`.

## Evidence Standard

Use primary sources first. Do not fabricate citations or quote text you cannot verify.

| Tier | Sources | Use |
|---|---|---|
| Tier 1 | Company filings, official announcements, earnings call transcripts, exchange disclosures | Core financials, guidance, governance, transactions |
| Tier 2 | Exchange data, regulator data, official macro data, company IR decks | Market structure, ownership, rates, liquidity |
| Tier 3 | Financial platforms, broker notes, media, consensus datasets | Context only; never sole basis for a decisive claim |

Always include an `Evidence Sources` section with source name, date, link, and what it supports.

## Conclusion Gates

Use research language such as attractive, reasonable, rich, watch, avoid, add-on-weakness, trim-on-strength, or thesis invalidated. Do not present personalized buy/sell advice.

Do not give a strong action conclusion or precise action price unless these are satisfied:

- Latest price and market cap are dated and cross-checked from two sources.
- Latest relevant filing/report is identified by period and publication date.
- At least one primary source supports the core financial claim.
- Valuation uses at least two relevant methods or explains why only one method is defensible.

If any gate fails, downgrade to a watchlist-style conclusion, state the missing data, and explain what evidence would be required to strengthen the view.

## Data Freshness Protocol

Do not use a financial data point unless its source date is known. Record:

- `as_of`: the period or market date the value describes.
- `published_at`: when the source published it, if available.
- `retrieved_at`: when you fetched or viewed it.

Treat stale or undated data as lower confidence. For action-price, add/trim/exit, or valuation-sensitive conclusions, verify the current price and at least one core valuation input from two sources. Do not turn missing data into a bullish or bearish signal; mark it unavailable and explain the impact on confidence.

Degrade conclusions as follows:

| Missing or stale item | Required handling |
|---|---|
| Current price is not latest trading day | Avoid precise action-price language |
| Latest filing/report cannot be verified | Do not call the analysis a latest-earnings review |
| Only secondary financial data is available | Cap confidence at Medium |
| Only one valuation input is available | Give directional valuation only |
| Material announcement search is incomplete | Add a pending-disclosure caveat |

## Workflow

1. Identify company, ticker, region, reporting period, user intent, and current date.
2. Collect the latest price, market cap, recent filing/report, and 3-5 years of key financials when available, with freshness timestamps.
3. Identify 1-3 Key Forces that determine future value over the next 3-5 years.
4. Run only the needed mode(s), loading the relevant reference files for valuation, sector adjustments, and red flags.
5. Cross-check valuation against current price before offering any action framework.
6. Output action triggers, kill conditions, monitoring variables, and confidence limits.

## `quick-value-score`

Score each dimension from 0 to 3. Use total score only as a research shorthand, not as a mechanical buy signal.

| Dimension | 3 points | 2 points | 1 point | 0 points |
|---|---|---|---|---|
| ROE / ROIC durability | High and stable for 3+ years | Good but uneven | Average or cyclical | Weak or unstable |
| Balance sheet safety | Net cash or low leverage | Manageable leverage | Needs monitoring | High refinancing or solvency risk |
| Free cash flow quality | FCF consistently covers earnings | Usually cash generative | Volatile conversion | Negative or poor conversion |
| Moat | Multiple strong moats | One clear moat | Weak advantage | No durable advantage |

Rating: A = 10-12, B = 7-9, C = 4-6, D = 0-3. For sector-specific replacements, use `references/sector-adjustments.md`.

## `earnings-deepdive`

Lead with the conclusion. Cover these modules only to the depth needed by the Key Forces:

- Revenue scale and quality: segment growth, recurring mix, geography, customer concentration.
- Profitability: gross/operating/net margin, GAAP vs adjusted gap, SBC or one-off items.
- Cash flow and capital allocation: OCF, FCF, capex, buybacks, dividends, M&A, dilution.
- Guidance and management signals: guidance vs consensus, tone shift, execution history.
- Competitive position: market share, product strength, pricing power, new business validation.
- Governance and ownership: insider behavior, major holders, related-party issues, pledges or placements.
- Valuation: at least two relevant methods, scenario range, sensitivity, margin of safety.

For tech or growth companies, explicitly test whether the market narrative is backed by revenue, users, contracts, or verifiable product adoption. For any company, check `references/red-flags.md` before forming the final view.

## `decision-framework`

When asked what to do, provide:

- Research classification: watchlist, attractive, reasonable, rich, trim-on-strength, exit-review, or avoid.
- Fair value range and action price: derive from valuation first, then compare with current price.
- Entry or exit cadence: staged actions only; avoid all-in language.
- Add/trim/exit triggers: concrete metrics, dates, prices, or business events.
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

## Valuation And Action Framework
[Fair value range, current price/date, action levels if conclusion gates pass, triggers, kill conditions.]

## Regional And Market-Specific Checks
[US/HK/A-share disclosure, ownership, capital flow, policy, or accounting issues.]

## Red Flags And Thesis Breakers
[Material accounting, governance, dilution, policy, financing, or disclosure risks.]

## Confidence And Limits
[Confidence level, missing data, stale data, unsupported claims avoided, and what would change the view.]

## Data Freshness
| Data | Value | As of | Published | Retrieved | Source | Freshness |
|---|---:|---|---|---|---|---|

## Evidence Sources
| Source | Date | Type | Supports |
|---|---|---|---|

## Disclaimer
This is public-information research for reference only and does not constitute investment advice.
```
