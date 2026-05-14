---
name: market-regime-monitor
description: Use when assessing market environment, liquidity, sentiment, positioning, greed/fear, overheating, de-risking, hedging, Fed liquidity, SOFR, MOVE, yen carry trade, NAAIM, institutional allocation, retail flows, valuation crowding, hedge fund leverage, or how macro and sentiment conditions affect US stocks, Hong Kong stocks, A-shares, technology shares, or crypto risk assets.
---

# Market Regime Monitor

## Core Rule

Assess the market regime using two axes: liquidity conditions and sentiment/positioning crowding. Match the user's language, state dates for all data, cite sources, show confidence and conflicting evidence, and frame output as research guidance rather than personalized investment advice.

Read `references/data-sources.md` for source priority, freshness TTL, regional proxies, and fallback rules. Read `references/indicator-definitions.md` for formulas and interpretation boundaries. Read `references/scoring-model.md` before assigning the risk regime. Read `references/regional-transmission.md` for Hong Kong, A-share, China, or cross-market transmission.

## Data Freshness Protocol

Do not use a market indicator unless its data date is known. Record:

- `as_of`: the market date or release period.
- `published_at`: when the source published it, if available.
- `retrieved_at`: when you fetched or viewed it.

Many regime indicators are delayed by design. Label stale data, reduce confidence, and never convert missing data into a bullish or bearish signal. For strong de-risking, hedging, or risk-on conclusions, cross-check at least one liquidity indicator and one sentiment/positioning indicator from primary or reputable secondary sources.

If data is stale, paywalled, unavailable, or from a secondary summary, show it as a limitation and cap confidence according to `references/scoring-model.md`.

## Regime Axes

### 1. Liquidity Dashboard

Use this axis to judge whether money and funding conditions are supportive or restrictive.

| Indicator | Primary question | Signal |
|---|---|---|
| Fed Net Liquidity | Is the Fed/Treasury/RRP complex adding or draining liquidity? | Rising = supportive; sharp weekly drop = restrictive |
| SOFR vs Fed Funds | Is overnight funding stressed? | Above upper bound by 10bp+ = stress |
| MOVE Index | Is Treasury volatility forcing deleveraging? | Above 130 = severe bond volatility |
| Yen Carry Trade | Is hidden global leverage unwinding? | Sharp JPY strength or narrowing US-JP spread = risk-off |

For Hong Kong and A-share questions, also check USD/CNH, HKD HIBOR, southbound/northbound flows, China policy liquidity, reserve requirement or MLF/LPR signals when relevant.

### 2. Sentiment Dashboard

Use this axis to judge whether investor positioning and valuation are crowded, neutral, or washed out.

| Indicator | Primary question | Signal |
|---|---|---|
| NAAIM Exposure | Are active managers already fully exposed? | High exposure = crowded |
| Institutional Allocation | Are institutions near historical equity extremes? | High allocation = limited marginal buyer |
| Retail Net Buying | Is retail chasing or capitulating? | Extreme buying = overheated; heavy selling = washed out |
| Forward P/E | Is valuation stretched versus history and rates? | High multiple = lower margin of safety |
| Hedge Fund Leverage | Could forced deleveraging amplify volatility? | High leverage = fragility |

Never label "0 overheating warnings" as panic. Panic requires evidence of fear, capitulation, forced selling, or washed-out positioning.

## Scoring And Confidence

Classify each indicator as supportive, neutral, watch, or alert, then score it using `references/scoring-model.md`. Keep liquidity and sentiment as separate axes before combining them. Do not average away a severe funding-stress alert.

Confidence is High only when both axes have fresh, cross-checked evidence and no unresolved conflict. Use Medium when one axis is weaker or partly stale. Use Low when data is thin, mostly secondary, materially delayed, or conflicting.

## Risk Regime Matrix

Combine the two axes before recommending stance.

| Liquidity | Sentiment / Positioning | Regime | Research stance |
|---|---|---|---|
| Easy | Washed out | Risk-on recovery | Gradual risk add can be considered |
| Easy | Crowded | Late-cycle melt-up risk | Hold quality, tighten trims and hedges |
| Tight | Washed out | Volatile bottoming | Avoid leverage, add only in stages |
| Tight | Crowded | Fragile / de-risking | Reduce beta, raise cash, hedge tail risk |
| Neutral | Neutral | Balanced | Maintain exposure, monitor inflection points |

If indicators conflict, state the conflict and identify which data point would resolve it.

Strong conclusions must include:

- Causal Channel: how the indicators affect funding, discount rates, risk appetite, flows, or forced selling.
- Alternative Explanation: what else could explain the observed market behavior.
- What Would Change The View: 3-5 concrete data triggers that would invalidate or upgrade the conclusion.

## Workflow

1. Identify market scope: US, Hong Kong, A-share, global, technology, crypto, or cross-asset.
2. Collect latest available liquidity and sentiment indicators, recording dates and data lag.
3. Classify each indicator as supportive, neutral, watch, or alert.
4. Score liquidity and sentiment separately, then map the two axes into the risk regime matrix.
5. Explain the causal channel and asset impact for the user's scope: US equities, HK equities, A-shares, growth/tech, defensives, rates, USD, or crypto.
6. Provide alternative explanations and monitoring triggers for the next 1-4 weeks.

If reliable data is unavailable, say so and use the nearest defensible proxy instead of guessing.

## Output Template

```markdown
# Market Regime Monitor

## Conclusion
[Risk regime, confidence, and the main reason.]

## Data Freshness
| Data | Value | As of | Published | Retrieved | Source | Freshness |
|---|---:|---|---|---|---|---|

## Liquidity Dashboard
| Indicator | Latest | Date | Status | Read-through |
|---|---:|---|---|---|

## Sentiment Dashboard
| Indicator | Latest | Date | Status | Read-through |
|---|---:|---|---|---|

## Risk Regime Score
[Liquidity axis score/confidence] x [sentiment axis score/confidence] => [regime and overall confidence].

## Causal Channel
[How funding, rates, FX, flows, valuation, leverage, or positioning transmit into the user's market scope.]

## Alternative Explanation
[Other plausible explanation for current asset behavior and why it is weaker/stronger.]

## Asset Impact
[Impact on the user's market scope, with emphasis on beta, duration, leverage, and crowded trades.]

## Positioning Bias And Triggers
[Research stance, hedging/cash bias if relevant, and 3-5 concrete monitoring triggers.]

## What Would Change The View
[3-5 data releases or market levels that would invalidate, soften, or strengthen the regime call.]

## Evidence Sources
| Source | Date | Type | Supports |
|---|---|---|---|

## Disclaimer
This is public-market research for reference only and does not constitute investment advice.
```
