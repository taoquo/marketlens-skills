# Portfolio Data Inputs

Use this file to normalize a portfolio or watchlist before risk review.

## Minimum Inputs

Required:

- Names or tickers.
- Market or listing venue when ambiguous.
- Current date and requested time horizon.

Useful but optional:

- Weights or position sizes.
- Cost basis and holding period.
- User's thesis tag for each name.
- Currency, sector, geography, and account-level constraints.
- Existing action intent: observe, add-candidate, trim-review, exit-review.

Do not infer personal risk tolerance, net worth, liquidity needs, tax situation, or exact position sizing unless the user provides it.

## Normalized Table

Use this table when inputs are messy:

| Name | Ticker | Market | Sector | Currency | Weight | Source | Data Date | Notes |
|---|---|---|---|---|---:|---|---|---|

If weights are missing, state: "Equal-weight watchlist assumption; this is not a true portfolio allocation review."

## Data Freshness

| Data type | Freshness target | If stale |
|---|---|---|
| Position weights | User-provided date | Mark as stale if older than user's portfolio date |
| Prices and market cap | Latest trading day for price-sensitive conclusions | Avoid precise add/trim levels |
| Sector/geography/currency | Latest company profile or filing | Use as structural data with date |
| Valuation multiples | Latest available snapshot, ideally within 7 trading days | Label as estimate |
| Earnings/filings | Latest official reporting period | State period clearly |
| Flows, short interest, liquidity | Latest official or reputable release | Mark lag and reduce tactical confidence |

## Source Rules

- User-provided weights override inferred weights.
- Official company and exchange data override financial platforms.
- For ADR/H-share/A-share duplicates, avoid double-counting economic exposure.
- For ETFs or funds, use holdings if available; otherwise classify as fund exposure and mark lower granularity.
- For private or unlisted assets, include only if the user provides enough information and label as out-of-scope for market data.
