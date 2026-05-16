# Exposure Framework

Use this file to diagnose concentration and shared risk drivers. Use `quant-risk-framework.md` for the lightweight quantitative snapshot and `../../references/scoring-standard.md` for red-flag overrides.

## Exposure Dimensions

| Dimension | What To Check |
|---|---|
| Name concentration | Largest positions, top 3/top 5 share, single-name dependence |
| Sector / industry | Industry clusters, upstream/downstream overlap, same profit pool |
| Geography / listing venue | US, Hong Kong, A-share, ADR, offshore China, emerging markets |
| Currency | USD, HKD, CNH/CNY, JPY, EUR revenue/cost/debt exposure |
| Factor / style | Growth, value, quality, momentum, high beta, small cap, duration, cyclicality |
| Macro | Rates, USD liquidity, credit, commodities, inflation, China policy, global risk appetite |
| Earnings | Shared reporting season, guidance sensitivity, margin assumptions |
| Policy / regulation | Same regulator, subsidy, antitrust, export control, reimbursement, data rules |
| Liquidity / crowding | Low float, high short interest, crowded long, ETF/index flow, borrow cost |
| Thesis overlap | Multiple names depending on the same customer, product cycle, policy, or narrative |

## Concentration Flags

Use these as research flags, not hard rules:

- One name dominates portfolio impact.
- Top 3 names drive most downside scenario.
- Multiple names rely on the same valuation multiple expansion.
- Different tickers are actually the same factor bet.
- Currency or listing venue risk is hidden by company labels.
- "Diversified" watchlist is mostly one industry chain or one macro regime.
- Stress-period correlation is likely to rise across names that look unrelated in normal markets.
- Top 3/top 5 exposure, equal-weight watchlist impact, or shared catalyst exposure dominates the conclusion.

## Correlated Risk Cluster

For each cluster, state:

- Names affected.
- Shared driver.
- Evidence and date.
- Transmission channel.
- What data would reduce or increase the risk.

Do not assume low correlation from different sectors if the same macro or liquidity driver dominates.
