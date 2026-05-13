# Equity Research Data Sources

Use primary sources first. Use secondary platforms only to cross-check or fill gaps, and label them as secondary.

## US

- SEC EDGAR: 10-K, 10-Q, 8-K, DEF 14A, S-1/S-3/S-8, Form 4.
- Company IR: earnings releases, presentations, transcripts, supplemental metrics.
- Exchanges and market data: NASDAQ, NYSE, Cboe, FINRA short interest.
- Macro and rates: FRED, Federal Reserve, New York Fed, US Treasury.
- Secondary checks: Yahoo Finance, Koyfin, TIKR, Macrotrends, Finviz, analyst consensus sources.

## Hong Kong

- HKEXnews / Disclosure of Interests: announcements, annual/interim reports, circulars, shareholding disclosures.
- Company IR: presentations, results announcements, conference calls.
- Stock Connect: southbound flows and eligible-stock data from HKEX or exchange data vendors.
- Market/rates: HKMA, HIBOR fixings, USDHKD, sector index data.
- Secondary checks: AAStocks, ETNet, TradingView, company filings mirrored by financial platforms.

## A-Share

- CNINFO: listed company announcements, annual/semiannual/quarterly reports.
- Exchanges: Shanghai Stock Exchange, Shenzhen Stock Exchange, Beijing Stock Exchange, inquiry letters and replies.
- Company IR: investor relations activity records, presentations, performance briefings.
- Market structure: northbound flows, margin financing/securities lending, unlock calendars.
- Policy and macro: PBOC, NBS, CSRC, ministry/regulator policy releases.
- Secondary checks: Eastmoney, iFinD/同花顺, Wind/Choice if available, exchange or broker summaries.

## Source Discipline

- Record source date and reporting period separately.
- Prefer original currency and accounting standard, then convert only when needed.
- Do not mix trailing, forecast, and adjusted metrics without labeling them.
- If exact data cannot be found, write "not found from primary sources" and use a labeled estimate or omit the metric.

## Freshness TTL

Use these maximum ages unless the user explicitly asks for historical analysis:

| Data type | Freshness target | If stale |
|---|---|---|
| Stock price, market cap, FX | Latest trading day; intraday when making price-sensitive calls | Mark non-real-time and avoid precise action-price language |
| Company filings and reports | Latest official filing for the reporting period | Use the latest official filing and state the period clearly |
| Earnings call and guidance | Latest reported quarter or annual period | Reduce confidence if a newer release is pending or already announced |
| Consensus estimates and valuation multiples | Latest available snapshot, ideally within 7 trading days | Label as estimate and avoid over-precise valuation |
| Ownership, 13F, insider, pledges | Latest disclosure period | State lag explicitly; do not treat as real-time positioning |
| HK/A-share capital flows | Latest trading day when discussing current sentiment | Mark lag and avoid short-term timing calls |
| Policy, inquiry letters, major announcements | Latest official notice | Search for follow-up announcements before concluding |

## Cross-Check Rules

- Price-sensitive decisions: verify price and market cap from two sources.
- Reported financials: prefer company filing or exchange disclosure over data platforms.
- HK/A-share announcements: check exchange/CNINFO/HKEXnews before relying on media summaries.
- Forecast metrics: label provider and date; do not combine multiple providers without noting the mismatch.
- Conflicts: state both values, choose the primary source, and explain why.
