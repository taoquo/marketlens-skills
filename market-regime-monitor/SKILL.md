---
name: market-regime-monitor
description: Use when assessing market environment, liquidity, sentiment, positioning, greed/fear, overheating, de-risking, hedging, Fed liquidity, SOFR, MOVE, yen carry trade, NAAIM, institutional allocation, retail flows, valuation crowding, hedge fund leverage, or how macro and sentiment conditions affect US stocks, Hong Kong stocks, A-shares, technology shares, or crypto risk assets.
---

# Market Regime Monitor

## Core Rule

Assess the market regime using two axes: liquidity conditions and sentiment/positioning crowding. Match the user's language, state dates for all data, cite sources, show confidence and conflicting evidence, and frame output as research guidance rather than personalized investment advice.

Translate risk-on, de-risking, hedge, or exposure questions into market-regime labels, risk-budget language, and monitoring triggers. Do not prescribe personal allocation, cash levels, hedges, or position sizes.

## Skill Boundary

Use this skill for market environment, liquidity, sentiment, positioning, and cross-market transmission. Use `sector-industry-research` for industry cycle and sector expression. Use `equity-research` for single-company fundamentals and valuation. Use `catalyst-event-monitor` for event-specific risk/reward. Use `portfolio-risk-monitor` for portfolio concentration, correlated exposures, and watchlist priority.

## Mode Selection

Choose the lightest mode that answers the user:

| User intent | Mode | Output depth |
|---|---|---|
| "How is liquidity?" / Fed, SOFR, MOVE, FX stress | `liquidity-scan` | Liquidity dashboard, red flags, causal channel |
| "Is sentiment crowded or washed out?" | `sentiment-scan` | Positioning dashboard, valuation crowding, confidence |
| "What is the market regime?" | `regime-score` | Two-axis score, matrix label, asset impact |
| Hong Kong, A-share, China, yen carry, cross-asset spillover | `cross-market-transmission` | Transmission channel, proxies, regional limits |
| Review a prior market call | `prior-call-review` | Regime error, timing error, data-quality error |
| Broad or ambiguous market request | Hybrid | Start with regime score, then analyze the binding axis |

## Reference Loading

Read only the references needed:

- For shared confidence, red-flag, and label discipline, read `../references/scoring-standard.md`.
- For review of prior regime calls, read `../references/review-and-calibration.md`.
- For source priority, freshness TTL, regional proxies, and fallback rules, read `references/data-sources.md`.
- For formulas and interpretation boundaries, read `references/indicator-definitions.md`.
- For scoring and confidence caps, read `references/scoring-model.md`.
- For Hong Kong, A-share, China, or cross-market transmission, read `references/regional-transmission.md`.

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

The regime score is an environment-pressure score, not a 0 to 3 company, catalyst, industry, or portfolio score. Use it to adjust risk-budget language and research labels, not to mechanically add or subtract from other scorecards.

Confidence is High only when both axes have fresh, cross-checked evidence and no unresolved conflict. Use Medium when one axis is weaker or partly stale. Use Low when data is thin, mostly secondary, materially delayed, or conflicting.

## Risk Regime Matrix

Combine the two axes before assigning regime label impact.

| Liquidity | Sentiment / Positioning | Regime | Research label impact |
|---|---|---|---|
| Easy | Washed out | Risk-on recovery | Risk-budget language can shift toward staged risk-on watch |
| Easy | Crowded | Late-cycle melt-up risk | Quality-hold/watch, trim-review, and hedge-review labels tighten |
| Tight | Washed out | Volatile bottoming | Leverage-sensitive assets remain cautious watch; staged review only |
| Tight | Crowded | Fragile / de-risking | High-beta, crowded, and low-liquidity assets move toward trim-review or hedge-review language |
| Neutral | Neutral | Balanced | Maintain neutral watch language and monitor inflection points |

If indicators conflict, state the conflict and identify which data point would resolve it.

Strong conclusions must include:

- Causal Channel: how the indicators affect funding, discount rates, risk appetite, flows, or forced selling.
- Alternative Explanation: what else could explain the observed market behavior.
- What Would Change The View: 3-5 concrete data triggers that would invalidate or upgrade the conclusion.

## Regime Impact Discipline

When the regime is tight, crowded, fragile, or de-risking, downgrade risk-budget language for high beta, long-duration growth, crowded momentum, low-liquidity, high-leverage, and policy-sensitive assets. Use `monitor closely`, `trim-review`, `evidence-gap`, or cautious watchlist language unless fresh evidence shows a specific offsetting catalyst.

Severe funding stress, Treasury liquidity stress, HKD funding pressure, CNH/FX pressure, or forced-flow risk is a red-flag override. Do not neutralize it with slower sentiment data or a benign average.

## Workflow

1. Identify market scope: US, Hong Kong, A-share, global, technology, crypto, or cross-asset.
2. Collect latest available liquidity and sentiment indicators, recording dates and data lag.
3. Classify each indicator as supportive, neutral, watch, or alert.
4. Score liquidity and sentiment separately, then map the two axes into the risk regime matrix.
5. Explain the causal channel and asset impact for the user's scope: US equities, HK equities, A-shares, growth/tech, defensives, rates, USD, or crypto.
6. Identify red-flag overrides, asset groups that require downgraded risk-budget language, and monitoring triggers for the next 1-4 weeks.
7. If reviewing a prior call, use `../references/review-and-calibration.md` to separate regime error, timing error, and data-quality error.

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

## Score Summary
| Dimension | Score | Evidence | Confidence | Comment |
|---|---:|---|---|---|

## Red Flags
[Funding, Treasury liquidity, HKD/CNH/FX, forced-flow, crowding, or data-quality risks that cannot be averaged away.]

## Causal Channel
[How funding, rates, FX, flows, valuation, leverage, or positioning transmit into the user's market scope.]

## Alternative Explanation
[Other plausible explanation for current asset behavior and why it is weaker/stronger.]

## Asset Impact
[Impact on the user's market scope, with emphasis on beta, duration, leverage, and crowded trades.]

## Positioning Bias And Triggers
[Research label impact, hedge-review or cash-buffer language if relevant, and 3-5 concrete monitoring triggers.]

## Decision Impact
[How the regime affects risk-budget language, high beta, duration, crowded trades, liquidity risk, and cross-market exposure.]

## What Would Change The View
[3-5 data releases or market levels that would invalidate, soften, or strengthen the regime call.]

## Evidence Sources
| Source | Date | Type | Supports |
|---|---|---|---|

## Disclaimer
This is public-market research for reference only and does not constitute investment advice.
```
