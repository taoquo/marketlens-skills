---
name: equity-research
description: Use when analyzing listed companies or stocks across US, Hong Kong, or A-share markets, including earnings reports, long-term holding quality, fundamentals, valuation, moat, cash flow, management, buy/hold/sell decisions, action price, position triggers, market-specific disclosure rules, or questions like whether a stock is worth buying, holding, adding, trimming, or exiting.
---

# Equity Research

## Core Rule

Provide public-market company research, not personalized investment advice. Match the user's language. State dates for all market data, distinguish facts from estimates, cite sources, and end with a short disclaimer that the analysis is for research only and does not constitute investment advice.

## Mode Selection

Choose the lightest mode that answers the user:

| User intent | Mode | Output depth |
|---|---|---|
| Long-term quality, Buffett-style, "worth holding" | `quick-value-score` | Four-dimension score plus key risks |
| Latest earnings, quarterly/annual report, guidance | `earnings-deepdive` | Key forces plus focused module analysis |
| "Can I buy/sell/add/trim now?" | `decision-framework` | Valuation, margin of safety, triggers |
| Broad or ambiguous stock analysis | Hybrid | Start with conclusion, then combine the needed modes |

If the company is a bank, insurer, broker, REIT, utility, or highly cyclical commodity business, adjust the scoring criteria before rating and explain the adjustment.

## Region Selection

Infer the market from ticker, exchange, company name, or user wording. If unclear, ask one concise clarification.

| Region | Default primary evidence | Must watch |
|---|---|---|
| US | SEC 10-K/10-Q/8-K/DEF 14A, company IR, earnings call transcript | GAAP vs non-GAAP, SBC, buyback dilution, guidance quality |
| Hong Kong | Annual/interim reports, HKEXnews announcements, company IR, exchange filings | Southbound flows, placements, buybacks, AH premium, related-party deals |
| A-share | Annual/quarterly reports, exchange announcements, CNINFO, inquiry letters | Policy cycle, Northbound flows, margin financing, unlocks, one-off gains/losses |

For regional details, read `references/regional-market-guide.md`. For source priority, freshness TTL, and query patterns, read `references/data-sources.md`.

## Evidence Standard

Use primary sources first. Do not fabricate citations or quote text you cannot verify.

| Tier | Sources | Use |
|---|---|---|
| Tier 1 | Company filings, official announcements, earnings call transcripts, exchange disclosures | Core financials, guidance, governance, transactions |
| Tier 2 | Exchange data, regulator data, official macro data, company IR decks | Market structure, ownership, rates, liquidity |
| Tier 3 | Financial platforms, broker notes, media, consensus datasets | Context only; never sole basis for a decisive claim |

Always include an `Evidence Sources` section with source name, date, link, and what it supports.

## Data Freshness Protocol

Do not use a financial data point unless its source date is known. Record:

- `as_of`: the period or market date the value describes.
- `published_at`: when the source published it, if available.
- `retrieved_at`: when you fetched or viewed it.

Treat stale or undated data as lower confidence. For action-price, buy/sell/add/trim, or valuation-sensitive conclusions, verify the current price and at least one core valuation input from two sources. Do not turn missing data into a bullish or bearish signal; mark it unavailable and explain the impact on confidence.

## Workflow

1. Identify company, ticker, region, reporting period, user intent, and current date.
2. Collect the latest price, market cap, recent filing/report, and 3-5 years of key financials when available, with freshness timestamps.
3. Identify 1-3 Key Forces that determine future value over the next 3-5 years.
4. Run only the needed mode(s), giving more depth to modules tied to the Key Forces.
5. Cross-check valuation against current price before recommending any action.
6. Output action triggers, kill conditions, and monitoring variables.

## `quick-value-score`

Score each dimension from 0 to 3. Use total score only as a research shorthand, not as a mechanical buy signal.

| Dimension | 3 points | 2 points | 1 point | 0 points |
|---|---|---|---|---|
| ROE / ROIC durability | High and stable for 3+ years | Good but uneven | Average or cyclical | Weak or unstable |
| Balance sheet safety | Net cash or low leverage | Manageable leverage | Needs monitoring | High refinancing or solvency risk |
| Free cash flow quality | FCF consistently covers earnings | Usually cash generative | Volatile conversion | Negative or poor conversion |
| Moat | Multiple strong moats | One clear moat | Weak advantage | No durable advantage |

Rating: A = 10-12, B = 7-9, C = 4-6, D = 0-3. For banks, insurers, brokers, REITs, and utilities, replace unsuitable metrics with sector-standard safety and return metrics.

## `earnings-deepdive`

Lead with the conclusion. Cover these modules only to the depth needed by the Key Forces:

- Revenue scale and quality: segment growth, recurring mix, geography, customer concentration.
- Profitability: gross/operating/net margin, GAAP vs adjusted gap, SBC or one-off items.
- Cash flow and capital allocation: OCF, FCF, capex, buybacks, dividends, M&A, dilution.
- Guidance and management signals: guidance vs consensus, tone shift, execution history.
- Competitive position: market share, product strength, pricing power, new business validation.
- Governance and ownership: insider behavior, major holders, related-party issues, pledges or placements.
- Valuation: at least two relevant methods, scenario range, sensitivity, margin of safety.

For tech or growth companies, explicitly test whether the market narrative is backed by revenue, users, contracts, or verifiable product adoption.

## `decision-framework`

When asked what to do, provide:

- Position classification: watchlist, starter, core, trim, exit, or avoid.
- Fair value range and action price: derive from valuation first, then compare with current price.
- Entry or exit cadence: staged actions only; avoid all-in language.
- Add/trim/exit triggers: concrete metrics, dates, prices, or business events.
- Kill conditions: what would invalidate the thesis.

Do not provide personalized allocation across the user's total assets unless the user gives risk tolerance, horizon, portfolio context, and constraints.

## Output Template

```markdown
# [Company] ([Ticker]) Equity Research

## Conclusion
[Recommended research stance first: buy/hold/watch/trim/avoid style language, confidence, and why.]

## Key Forces
[1-3 decisive forces, each tied to evidence.]

## Fundamentals And Earnings
[Focused findings from the selected mode.]

## Valuation And Action Framework
[Fair value range, current price/date, action price, triggers, kill conditions.]

## Regional And Market-Specific Checks
[US/HK/A-share disclosure, ownership, capital flow, policy, or accounting issues.]

## Data Freshness
| Data | Value | As of | Published | Retrieved | Source | Freshness |
|---|---:|---|---|---|---|---|

## Evidence Sources
| Source | Date | Type | Supports |
|---|---|---|---|

## Disclaimer
This is public-information research for reference only and does not constitute investment advice.
```
