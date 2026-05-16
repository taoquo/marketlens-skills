# Scoring Model

Use this model to make regime calls consistent. It is a research heuristic, not a trading system. Apply the shared rules in `../../references/scoring-standard.md` for confidence, red flags, and labels.

## Indicator Scores

| Status | Score | Meaning |
|---|---:|---|
| Supportive | +1 | Helps risk appetite, liquidity, or market resilience |
| Neutral | 0 | No clear directional pressure |
| Watch | -1 | Creates fragility or requires monitoring |
| Alert | -2 | Active stress, crowding, or forced-flow risk |

Score liquidity indicators and sentiment indicators separately. Do not combine the two axes until each axis has its own read.

This `+1 / 0 / -1 / -2` regime score is an environment-pressure score. It must not be added to 0 to 3 company quality, catalyst, industry, or portfolio scorecards.

## Axis Classification

| Axis score | Classification |
|---:|---|
| +2 or higher | Easy / supportive |
| -1 to +1 | Neutral / mixed |
| -2 to -3 | Tight or crowded |
| -4 or lower | Stress or euphoric/fragile |

For sentiment, negative scores mean crowded, euphoric, leveraged, or fragile. Washed-out sentiment can be supportive only when there is evidence of fear, capitulation, or forced selling that has already occurred.

## Data Weighting

- Fresh primary source: full weight.
- Fresh reputable secondary source: full weight for context, not as the sole basis for a strong call.
- Stale source: half weight and lower confidence.
- Undated source: do not score; list as unavailable.
- Paywalled survey summary: use only as secondary context unless the date and value are clear.

## Confidence

| Confidence | Requirements |
|---|---|
| High | At least two fresh indicators per axis, primary or reputable sources, no unresolved conflict |
| Medium | One axis is fresh and strong; the other is thin, partly stale, or proxy-based |
| Low | Data is mostly stale, secondary, unavailable, or internally conflicting |

Severe funding stress overrides a benign average. If SOFR, Treasury liquidity, HKD funding, CNH/FX pressure, or forced-flow risk shows acute stress, do not neutralize it with slower sentiment indicators.

## Asset Risk-Budget Impact

| Regime pressure | Research impact |
|---|---|
| Easy and washed out | Risk-budget language can be more constructive if data is fresh |
| Easy but crowded | Prefer quality, avoid chasing crowded beta, tighten trim triggers |
| Tight but washed out | Use staged and confirmation-based language; avoid leverage |
| Tight and crowded | Downgrade high beta, long duration, low liquidity, and crowded trades |
| Acute funding or FX stress | Red-flag override; cap confidence and avoid benign average language |

Use this impact table to inform other skills, but do not mechanically adjust their numeric scores.

## Conflict Handling

- State the conflict explicitly.
- Prefer fresher, more direct market prices over delayed surveys for tactical calls.
- Prefer primary official data over media summaries for liquidity and flows.
- Name the tie-breaker: the next release, market level, or flow data that would resolve the conflict.
