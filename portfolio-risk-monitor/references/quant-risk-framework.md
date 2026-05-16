# Quant Risk Framework

Use this file to add lightweight quantitative discipline to portfolio and watchlist risk reviews.

## Purpose

This framework identifies concentration, shared exposures, and stress-period correlation. It is not an optimizer and does not produce personal allocation targets.

## Required Checks

| Check | What to measure or estimate | Required caveat |
|---|---|---|
| Single-name concentration | Largest position or equal-weight assumption | If weights are missing, label as watchlist only |
| Top 3 / Top 5 concentration | Share of portfolio or assumed watchlist impact | Do not infer personal constraints |
| Sector / theme exposure | Clustered industry, theme, value chain, or profit pool | Different tickers can be the same risk |
| Factor exposure | Growth, value, quality, momentum, high beta, duration, small cap, cyclicality | Use proxy labels if factor data is unavailable |
| Macro exposure | Rates, USD liquidity, credit, commodities, inflation, China policy, FX | State the transmission channel |
| Catalyst overlap | Multiple names depending on the same event, customer, policy, or revision cycle | Shared catalyst can reduce diversification |
| Liquidity risk | Low float, thin trading, high borrow cost, ETF/index flow, forced selling risk | Mark unavailable if no dated data |
| Stress correlation | Correlations likely to rise under funding, policy, or risk-off stress | Use qualitative estimate if no return data |
| Drawdown contribution | Names or clusters likely to drive the largest downside scenario | Use scenario logic, not exact loss forecasts, when data is thin |

## Quant Risk Snapshot

Use this structure:

```markdown
## Quant Risk Snapshot
| Risk Lens | Finding | Evidence / Proxy | Confidence | Portfolio Read-Through |
|---|---|---|---|---|
```

## Stress Scenario Discipline

Each scenario should include:

- Shock driver: valuation, earnings, policy, FX, rates, liquidity, crowding, or balance sheet.
- Affected names or clusters.
- Transmission channel.
- Leading indicator.
- Expected correlation behavior.
- Research response: monitor, trim-review, exit-review, hedge review, or evidence-gap.

Do not output exact hedge size or rebalance percentage.

## Missing Data Handling

- Missing weights: use equal-weight watchlist assumption and state it is not a portfolio allocation review.
- Missing prices: avoid price-sensitive candidate labels.
- Missing factor data: use transparent proxy labels.
- Missing liquidity data: mark liquidity risk unavailable and lower confidence.
- Missing correlation history: use cluster logic and label it qualitative.

