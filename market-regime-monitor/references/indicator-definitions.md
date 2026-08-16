# Indicator Definitions

Use these definitions to avoid vague macro language. State the data date and source for each indicator.

## Liquidity

| Indicator | Definition | Interpretation boundary |
|---|---|---|
| Fed Net Liquidity | Fed balance sheet minus Treasury General Account minus ON RRP | Rising is usually supportive; sharp weekly or 4-week declines can tighten risk liquidity |
| SOFR vs Fed Funds | SOFR compared with the FOMC target range, especially the upper bound | Persistent SOFR above the upper bound or unusual spikes suggest funding stress |
| MOVE Index | Treasury market implied volatility | High or rising MOVE can force duration and risk-parity deleveraging |
| Yen Carry Trade | USDJPY, US-Japan rate spread, and volatility proxy for funded leverage | Sharp JPY strength, falling rate spread, or volatility jump can signal carry unwind |
| USD/CNH | Offshore RMB exchange rate versus USD | Rising USD/CNH can reflect China outflow pressure or broad USD strength |
| HIBOR / HKD Liquidity | Hong Kong interbank rates, HKMA aggregate balance, and USDHKD pressure | High HIBOR or weak HKD liquidity can tighten HK equity conditions |
| China Policy Liquidity | PBOC OMO, MLF, LPR, RRR, credit aggregates, and fiscal-policy signals | Easing supports local liquidity; credit impulse matters more than a single operation |
| IG Credit Spread | Investment-grade OAS over Treasuries | Widening from a low base is an early risk-appetite warning; the direction matters more than the level |
| HY Credit Spread | High-yield OAS, plus the CCC minus BB gap | High yield usually leads equity drawdowns more reliably than equity volatility. Equity strength alongside HY widening is a divergence, not confirmation |
| Real Yield | 10-year TIPS yield, or the local real-rate proxy | Rising real yields compress long-duration multiples independently of earnings |
| Breakeven Inflation | Nominal minus real yield at 5y, 10y, and 5y5y | Separates a nominal-rate move into growth, inflation, and premium components |
| Term Premium | Long-yield decomposition, or 10s2s and 10s30s curve shape | A term-premium-led bear steepener pressures duration-sensitive equity even with sound growth data |
| Cross-Currency Basis | USD funding basis versus EUR, JPY, and CNH | Negative basis widening signals offshore dollar scarcity and transmits to Hong Kong and EM equity |

Credit definitions, single-name credit checks, and the credit-equity divergence
table are in `../../references/credit-and-cross-asset.md`. A liquidity read built
only on central-bank and funding-rate data is incomplete: credit spreads are where
risk appetite prices first.

## Sentiment And Positioning

| Indicator | Definition | Interpretation boundary |
|---|---|---|
| NAAIM Exposure | Weekly active-manager equity exposure survey | High exposure means crowding, not automatically an immediate sell signal |
| Institutional Allocation | Survey or custody-based equity allocation | Extremes imply limited marginal buyer or seller, depending on direction |
| Retail Net Buying | Retail brokerage or research-provider flow estimate | Extreme buying can signal chase; extreme selling can signal capitulation |
| Forward P/E | Index forward valuation versus history and rates | Expensive valuations reduce margin of safety but do not time reversals alone |
| Hedge Fund Leverage | Prime-broker gross/net leverage or public summaries | High leverage increases fragility; if unavailable, mark unavailable rather than guess |
| Market Breadth | Advance/decline, percent above moving averages, equal-weight versus cap-weight | Narrow leadership can indicate crowding under a strong index |
| Put/Call And Volatility Curve | Options positioning and VIX term structure | Panic requires fear or forced-selling evidence, not merely low bullish signals |

## Regional Proxies

- Hong Kong: southbound flows, HK short-selling turnover, Hang Seng / Hang Seng Tech valuation, buyback activity, HIBOR, USDHKD, and HKMA aggregate balance.
- A-share: northbound flows, margin financing balance, turnover, ETF flows, valuation percentile, policy liquidity, and industry breadth.
- Crypto: BTC/ETH spot, funding rates, open interest, ETF flows, and stablecoin liquidity where available.

## Boundaries

- Crypto, FX, and commodity indicators here are risk-appetite proxies only. Directional views on those assets are out of scope; see `../../references/skill-routing.md`.
- A single indicator is never enough for a strong regime call.
- A level without trend can be misleading; check latest level, weekly change, and 4-week direction when available.
- Survey and prime-broker data are delayed by design; do not call them real-time positioning.
