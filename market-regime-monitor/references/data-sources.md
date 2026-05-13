# Market Regime Data Sources

Use this file to choose sources and proxies. Prefer official or primary publisher data. Note data dates and lag.

## Global / US Liquidity

- Fed total assets: Federal Reserve H.4.1 release or FRED series.
- Treasury General Account: US Treasury Daily Treasury Statement.
- ON RRP: New York Fed overnight reverse repo operation data.
- SOFR: New York Fed SOFR publication.
- Fed Funds range: Federal Reserve FOMC target range.
- MOVE Index: ICE/BofA MOVE data where available; otherwise TradingView or reputable market data/news.
- US-Japan carry: USDJPY spot, US 2Y Treasury yield, Japan 2Y government bond yield, BOJ policy releases.

## US Sentiment / Positioning

- NAAIM Exposure Index: NAAIM official publication.
- Institutional allocation: State Street investor confidence/allocation data, BofA fund manager survey, or other clearly labeled survey sources.
- Retail flows: JPMorgan or Vanda Research reports if available; otherwise labeled media summaries.
- S&P 500 Forward P/E: FactSet Earnings Insight, Yardeni, Bloomberg/Reuters summaries, or index data vendors.
- Hedge fund leverage: Goldman Sachs or Morgan Stanley prime brokerage summaries; if unavailable, label as stale or unavailable.

## Hong Kong And China Proxies

- Southbound and northbound Stock Connect flows: HKEX, SSE, SZSE, or financial data platforms that mirror exchange data.
- HKD liquidity: HKMA aggregate balance, HIBOR, USDHKD, Exchange Fund data.
- China liquidity/policy: PBOC open market operations, MLF/LPR, RRR changes, credit aggregates, NBS macro releases.
- A-share sentiment: margin financing balance, turnover, new account activity where available, valuation percentile, ETF flows.
- HK sentiment: Hang Seng / Hang Seng Tech valuation, short-selling turnover, southbound concentration, buyback activity.

## Crypto Risk Proxy

- BTC/ETH prices and volume: CoinGecko, CoinMarketCap, TradingView.
- Funding and leverage: CoinGlass, Binance/OKX data.
- ETF flows: Farside, SoSoValue, issuer reports, Bloomberg summaries.

## Fallback Rules

- If a real-time value is unavailable, use the most recent known value and date it clearly.
- If a private survey is paywalled, use a reputable public summary and mark it as secondary.
- Do not interpolate missing values unless the method is stated.
- Do not convert a missing indicator into a bullish or bearish signal; mark it unavailable and reduce confidence.

## Freshness TTL

Use these maximum ages for current-regime analysis:

| Data type | Freshness target | If stale |
|---|---|---|
| SOFR, ON RRP, TGA, USDJPY, major FX | Latest published business day | Mark lag; avoid intraday stress claims |
| Fed balance sheet | Latest weekly H.4.1 release | State release date and weekly nature |
| MOVE, VIX, index price, rates | Latest trading day | Mark non-real-time if older |
| NAAIM | Latest weekly release | Do not call it "today's positioning" |
| Institutional allocation / fund manager surveys | Latest survey period | Label survey lag and reduce confidence |
| Retail flows | Latest available report, ideally within 1 week | Mark if based on media summary |
| Hedge fund leverage | Latest prime brokerage report | Treat as unavailable if no date is found |
| HK/A-share flows, margin financing, HIBOR | Latest trading day or official release day | Mark stale before making tactical calls |
| China policy liquidity and macro releases | Latest official release | State reporting period and next release risk |

## Cross-Check Rules

- Liquidity conclusion: verify at least two of Fed/Treasury/RRP/SOFR/MOVE/carry indicators.
- Sentiment conclusion: verify at least two independent positioning or valuation indicators.
- Regional market conclusion: include at least one global liquidity signal and one local proxy.
- If indicators conflict, keep the regime label lower-confidence and name the tie-breaker to monitor.
