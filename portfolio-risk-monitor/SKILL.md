---
name: portfolio-risk-monitor
description: Use when reviewing a public-market portfolio or watchlist for risk concentration, factor exposure, sector/geography/currency overlap, style crowding, drawdown risk, watchlist priority, add/trim/exit candidates, rebalance watch signals, correlated theses, or questions like which names matter most, which holdings share the same risk driver, or whether risk is concentrated in valuation, earnings, policy, FX, rates, liquidity, or market regime.
---

# Portfolio Risk Monitor

## Core Rule

Provide public-market portfolio and watchlist research, not personalized investment advice or asset allocation. Match the user's language. State dates for all prices, weights, and risk data; distinguish facts from estimates and opinions; cite sources; show confidence and limits; and end with a short disclaimer that the analysis is for research only and does not constitute investment advice.

This skill does not decide the user's total asset allocation, risk tolerance, or exact position size. It diagnoses concentration, correlated exposures, priority, drawdown risk, trigger conditions, and rebalance watch signals.

This skill summarizes and connects conclusions from `market-regime-monitor`, `sector-industry-research`, `equity-research`, and `catalyst-event-monitor` when available. It should not repeat full company, industry, or catalyst deep dives.

## Mode Selection

Choose the lightest mode that answers the user:

| User intent | Mode | Output depth |
|---|---|---|
| "Review my watchlist" / "who matters most?" | `watchlist-priority` | Priority ranking, thesis status, evidence gaps |
| "Where is my portfolio risk?" | `risk-dashboard` | Concentration, factor/geography/sector/currency exposure |
| "Which names should I add/trim/exit?" | `candidate-review` | Research classifications and trigger-based candidates, not personal allocation |
| "What could hurt this portfolio?" | `drawdown-scenario` | Scenario shocks, correlated losses, monitoring variables |
| Broad or ambiguous portfolio request | Hybrid | Start with risk dashboard, then rank the highest-impact names |

If weights, cost basis, risk constraints, or current prices are missing, use equal-weight or user-provided watchlist analysis and label the limitation clearly.

## Reference Loading

Read only the references needed:

- For input schema, data quality, and freshness, read `references/data-inputs.md`.
- For concentration, factor, geography, sector, currency, and correlation checks, read `references/exposure-framework.md`.
- For lightweight quantitative concentration, factor, liquidity, stress correlation, and drawdown-contribution checks, read `references/quant-risk-framework.md`.
- For watchlist priority and add/trim/exit research classification, read `references/priority-framework.md`.
- For drawdown scenarios, risk drivers, and monitoring triggers, read `references/risk-triggers.md`.
- For rebalance watch signals and research follow-up workflow, read `references/rebalance-watch.md`.
- For shared scoring, confidence, red-flag, and label discipline, read `../references/scoring-standard.md`.
- For review of prior portfolio risk calls, read `../references/review-and-calibration.md`.

## Evidence Standard

Use primary or official sources first. Do not fabricate citations or quote text you cannot verify.

| Tier | Sources | Use |
|---|---|---|
| Tier 1 | User-provided holdings/watchlist, company filings, official announcements, exchange disclosures | Positions, thesis inputs, company-specific risks |
| Tier 2 | Exchange data, company IR, official macro/rates/FX data, sector index data | Prices, sector/geography/currency, market regime context |
| Tier 3 | Financial platforms, broker notes, media, consensus datasets, ETF/flow summaries | Context and proxy data only |

Always include an `Evidence Sources` section with source name, date, link, and what it supports. For user-provided data, label it as user-provided and do not infer missing personal constraints.

## Conclusion Gates

Use research language such as high-priority watch, add-candidate watch, trim-review, exit-review, risk-concentrated, balanced watchlist, evidence gap, or insufficient data. Do not present personalized buy/sell/allocation advice.

Do not give a strong portfolio-risk conclusion unless these are satisfied:

- Portfolio/watchlist constituents are explicit.
- Weights are provided or equal-weight/watchlist assumption is stated.
- Current price or valuation-sensitive data is dated, or the limitation is explicit.
- The main risk driver is mapped to evidence: valuation, earnings, policy, FX, rates, liquidity, leverage, crowded positioning, or market regime.
- Candidate labels are tied to triggers and evidence gaps, not personal asset-allocation advice.

If any gate fails, downgrade to a watchlist-style risk review and state what data is missing.

## Data Freshness Protocol

Do not use a portfolio or market data point unless its source date is known. Record:

- `as_of`: the portfolio date, market date, reporting period, or disclosure date.
- `published_at`: when the source published it, if available.
- `retrieved_at`: when you fetched or viewed it.

For price-sensitive classifications, use latest available market prices and mark stale data. Do not turn missing weights, prices, or constraints into bullish or bearish conclusions.

## Workflow

1. Identify holdings/watchlist names, tickers, market, user intent, time horizon, weights, and current date.
2. Normalize inputs: ticker, region, sector, currency, weight, thesis tag, catalyst tag, and source/date.
3. If weights are missing, use equal-weight watchlist analysis and state that it is not a portfolio allocation review.
4. Build concentration and exposure dashboards across name, sector, geography, currency, factor, thesis, catalyst, and liquidity.
5. Build a quant risk snapshot covering single-name, top 3/top 5, sector/theme, factor, macro, catalyst overlap, liquidity, stress correlation, and drawdown contribution.
6. Identify correlated risk clusters and the top 3-5 portfolio-level risk drivers.
7. Rank names by priority using thesis quality, risk/reward evidence, catalyst urgency, valuation pressure, drawdown risk, portfolio role, and evidence gaps.
8. Classify names as high-priority watch, add-candidate watch, hold/watch, trim-review, exit-review, avoid, or evidence-gap.
9. Define rebalance watch signals, trigger conditions, and what would change the view.

## Output Template

```markdown
# Portfolio / Watchlist Risk Monitor

## Conclusion
[Top portfolio/watchlist risk, highest-priority names, confidence, and key limitation.]

## Portfolio Snapshot
| Name | Ticker | Market | Sector | Currency | Weight / Assumption | Thesis Tag | Data Date |
|---|---|---|---|---|---:|---|---|

## Concentration And Exposure Dashboard
[Name, sector, geography, currency, factor, liquidity, style, and thesis concentration.]

## Quant Risk Snapshot
| Risk Lens | Finding | Evidence / Proxy | Confidence | Portfolio Read-Through |
|---|---|---|---|---|

## Correlated Risk Clusters
| Cluster | Names | Shared Risk Driver | Evidence | Portfolio Read-Through |
|---|---|---|---|---|

## Score Summary
| Dimension | Score | Evidence | Confidence | Comment |
|---|---:|---|---|---|

## Red Flags
[Concentration, hidden factor overlap, liquidity, stale data, correlated thesis, or stress-period correlation risks that cannot be offset by total score.]

## Priority Ranking
| Name | Role | Priority | Key Upside Driver | Main Risk | Next Trigger | Evidence Gap |
|---|---|---|---|---|---|---|

## Candidate Review
[Add-candidate watch, hold/watch, trim-review, exit-review, and evidence-gap names with trigger-based reasoning.]

## Drawdown Scenarios
| Scenario | Affected Names | Transmission Channel | What To Monitor | Research Response |
|---|---|---|---|---|

## Rebalance Watch Signals
[Signals that would justify review, not personal allocation instructions.]

## Decision Impact
[How priority score, quant risk, correlated clusters, and market regime affect candidate labels or risk-response language.]

## What Would Change The View
[Concrete price, valuation, catalyst, disclosure, regime, correlation, or liquidity triggers that would upgrade or downgrade the label.]

## Confidence And Limits
[Missing weights, stale prices, unknown constraints, proxy data, unsupported claims avoided.]

## Data Freshness
| Data | Value | As of | Published | Retrieved | Source | Freshness |
|---|---:|---|---|---|---|---|

## Evidence Sources
| Source | Date | Type | Supports |
|---|---|---|---|

## Disclaimer
This is public-market research for reference only and does not constitute investment advice.
```
