---
name: market-regime-monitor
description: Use when assessing market environment, liquidity, sentiment, positioning, greed/fear, overheating, de-risking, hedging, Fed liquidity, SOFR, MOVE, yen carry trade, NAAIM, institutional allocation, retail flows, valuation crowding, hedge fund leverage, or how macro and sentiment conditions affect US stocks, Hong Kong stocks, A-shares, technology shares, or crypto risk assets.
license: MIT
metadata:
  version: 0.8
---

# Market Regime Monitor

## Core Rule

Assess the market regime using two axes: liquidity conditions and sentiment/positioning crowding. Match the user's language, state dates for all data, cite sources, show confidence and conflicting evidence, and frame output as research guidance rather than personalized investment advice.

Translate risk-on, de-risking, hedge, or exposure questions into market-regime labels, risk-budget language, and monitoring triggers. Do not prescribe personal allocation, cash levels, hedges, or position sizes.

## Skill Boundary

Use this skill for market environment, liquidity, sentiment, positioning, valuation crowding, cross-market transmission, and risk-budget language. For anything outside that scope, route through `../references/skill-routing.md`.

## Mode Selection

Choose the lightest mode that answers the user:

| User intent | Mode | Minimum input | Output depth |
|---|---|---|---|
| "How is liquidity?" / Fed, SOFR, MOVE, FX stress | `liquidity-scan` | At least two dated liquidity or funding indicators | Liquidity dashboard, red flags, causal channel |
| "Is sentiment crowded or washed out?" | `sentiment-scan` | At least two dated positioning, flow, or valuation indicators | Positioning dashboard, valuation crowding, confidence |
| "What is the market regime?" | `regime-score` | At least one dated indicator on each axis | Two-axis score, matrix label, asset impact |
| Hong Kong, A-share, China, yen carry, cross-asset spillover | `cross-market-transmission` | Market scope plus one dated indicator per transmission leg | Transmission channel, proxies, regional limits |
| Review a prior market call | `prior-call-review` | The prior call, its date, and the regime label it stated | Regime error, timing error, data-quality error |
| Broad or ambiguous market request | Hybrid | Market scope | Start with regime score, then analyze the binding axis |

If an axis has no usable indicator, do not score it. Report a single-axis read, mark the other axis `evidence-gap`, and cap overall confidence at Low.

## Reference Loading

Read only the references needed:

- For shared confidence, red-flag, and label discipline, read `../references/scoring-standard.md`.
- For timestamps, freshness grades, evidence tiers, unit and calendar rules, and user-input handling, read `../references/data-discipline.md`.
- For deciding which skill owns a question, read `../references/skill-routing.md`.
- For review of prior regime calls, and for how a regime read decays with age, read `../references/review-and-calibration.md`.
- For credit spreads, real yields, breakevens, term premium, and cross-currency basis as risk-appetite inputs, read `../references/credit-and-cross-asset.md`.
- For historical analogues before assigning a probability to a regime path, read `../references/base-rates.md`.
- For what an index-level multiple implies about aggregate growth or margin, when index valuation carries the crowding read, read `../references/implied-expectations.md`.
- For source priority, freshness TTL, regional proxies, and fallback rules, read `references/data-sources.md`.
- For formulas and interpretation boundaries, read `references/indicator-definitions.md`.
- For scoring and confidence caps, read `references/scoring-model.md`.
- For Hong Kong, A-share, China, or cross-market transmission, read `references/regional-transmission.md`.

## Evidence Standard

Use primary or official sources first. Do not fabricate citations or quote text you cannot verify. Tier definitions are in `../references/data-discipline.md`.

| Tier | Sources | Use |
|---|---|---|
| Tier 1 | Central bank and Treasury releases, official RRP/reserve/balance-sheet data, exchange and regulator statistics, official policy statements | Liquidity levels, policy settings, official flow and funding data |
| Tier 2 | Exchange and index data, official rates/FX series, index-provider valuation data, published survey series such as NAAIM or AAII, prime-broker and exchange positioning reports | Prices, volatility, valuation, positioning, cross-market proxies |
| Tier 3 | Financial platforms, media commentary, broker notes, aggregator dashboards, derived sentiment composites | Context and proxy only; never the sole basis for a de-risking or risk-on call |

Survey and prime-broker positioning data is `Lagged` by design. State the reference date and never present it as live positioning.

Always include an `Evidence Sources` section with source name, date, link, and what it supports.

## Conclusion Gates

Use research language such as risk-on recovery, balanced, volatile bottoming, late-cycle melt-up risk, fragile / de-risking, monitor closely, hedge-review, trim-review, or evidence-gap. The regime read is a risk-budget modifier that caps or releases the labels below it; see `Label Layering` and `Chain Constraints` in `../references/scoring-standard.md`. Do not prescribe personal allocation, cash levels, hedge ratios, or position sizes.

Do not give a strong regime conclusion unless these are satisfied:

- At least one liquidity indicator and one sentiment/positioning indicator are dated and sourced.
- The binding axis is named, and the conflict between axes is stated when they disagree.
- The causal channel is explicit: funding, discount rates, risk appetite, flows, or forced selling.
- At least one alternative explanation for current market behavior is considered and weighed.
- Indicator readings are compared against a stated historical reference range, not judged in isolation.
- 3-5 concrete data triggers that would invalidate or upgrade the call are defined in advance.

If any gate fails, report a single-axis or directional read, cap confidence, and state the missing indicator.

A single extreme indicator is not a regime. Do not label a regime from one data point, and do not average away a severe funding-stress alert.

## Data Freshness Protocol

Timestamps, freshness grades, evidence tiers, unit and calendar rules, and the core figure check are defined in `../references/data-discipline.md`. Load that file before writing the `Data Freshness` table and use its five freshness grades verbatim.

Regime-specific additions:

- Many regime indicators are delayed by design. Grade them `Lagged`, not `Fresh`, and print the reference date next to the value.
- For strong de-risking, hedging, or risk-on conclusions, cross-check at least one liquidity indicator and one sentiment/positioning indicator from primary or reputable secondary sources.
- Cap confidence according to `references/scoring-model.md` when data is stale, paywalled, unavailable, or from a secondary summary.

Degrade conclusions as follows:

| Missing or stale item | Required handling |
|---|---|
| Only one axis has usable data | Report a single-axis read, no matrix regime label, confidence Low |
| A liquidity indicator is past its TTL | Drop the precise level language and describe direction only |
| Positioning data is a weekly or monthly survey | Grade it `Lagged`, state the reference date, do not call it current positioning |
| Only Tier 3 or aggregator data supports the read | Cap confidence at Medium, no risk-on or de-risking call |
| No historical reference range is available | Describe the change, not the extreme |
| Indicators conflict and no resolving data exists | Label the regime as unresolved and name the data point that would settle it |

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
