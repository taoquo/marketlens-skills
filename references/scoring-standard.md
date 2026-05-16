# Scoring Standard

Use this standard across MarketLens skills whenever a score, scorecard, rating, or research label is used.

## Purpose

Scores are research heuristics. They make comparisons explicit, but they are not a trading system, a buy/sell signal, a target weight, or a substitute for evidence.

Use scores to answer:

- Which item deserves more research attention?
- Which risk is severe enough to override the average?
- Which evidence gap limits confidence?
- Which label is defensible given the data?

Do not use scores to answer exact position size, personal allocation, or mechanical trade execution.

## Score Direction

For 0 to 3 scorecards:

| Score | Meaning |
|---:|---|
| 3 | Strong, attractive, safer, or clearly supportive |
| 2 | Usable or moderately supportive |
| 1 | Weak, mixed, or needs monitoring |
| 0 | Unproven, unavailable, high risk, or not investable as stated |

For risk dimensions, high score always means lower pressure or better controlled risk. If a dimension uses the opposite direction, rewrite it before scoring.

The market-regime `+1 / 0 / -1 / -2` model is an environment-pressure score. It is separate from 0 to 3 scorecards and must not be added to company, catalyst, industry, or portfolio totals.

## Confidence

| Confidence | Requirements |
|---|---|
| High | Fresh, dated evidence from primary or reputable sources; no unresolved conflict; conclusion gates passed |
| Medium | Evidence is usable but partly stale, proxy-based, secondary, or incomplete |
| Low | Evidence is stale, unavailable, mostly secondary, internally conflicting, or missing a key gate |

Low confidence caps the conclusion at watchlist, event watch, evidence-gap, or monitor closely. It cannot support strong action-style language.

## Data Quality

| Data status | Treatment |
|---|---|
| Fresh primary source | Full weight |
| Fresh reputable secondary source | Usable, but not the sole basis for a decisive conclusion |
| Stale source | Use with caveat and reduce confidence |
| Undated source | Do not score; mark unavailable |
| Unverifiable, wrong unit, or quantity anomaly | Exclude or mark proxy only |

Missing data is never bullish or bearish by itself. It is a confidence limit.

## Red Flag Overrides

Red flags cannot be averaged away by a high total score:

- Severe funding stress, Treasury liquidity stress, HKD/CNH funding pressure, or forced-flow risk.
- Unverified current price, market cap, filing, event date, or core financial metric for a price-sensitive conclusion.
- Material governance, accounting, dilution, related-party, pledge, or disclosure risk.
- Balance-sheet survival, refinancing, or liquidity risk before the thesis can play out.
- Event timing uncertainty or financial impact uncertainty for a high-conviction catalyst.
- Extreme crowding, high unwind risk, or implied move that already prices the event.
- Portfolio concentration, hidden factor overlap, or stress-period correlation that dominates stock-specific theses.
- Industry data with wrong unit, wrong period, or quantity-scale anomaly.

When a red flag is present, state it in `Red Flags`, downgrade the research label if needed, and name the evidence required to remove it.

## Research Labels

Use these labels consistently:

- `high-priority watch`: strong evidence, clear catalyst or risk/reward, and manageable risks.
- `add-candidate watch`: attractive if a price, valuation, catalyst, or evidence gate improves.
- `hold/watch`: thesis intact, but no clear new action signal.
- `trim-review`: valuation, crowding, concentration, or thesis deterioration warrants review.
- `exit-review`: kill condition, thesis break, governance issue, or unacceptable concentration warrants review.
- `avoid`: risk/reward, evidence quality, governance, balance sheet, or structural pressure is not acceptable.
- `evidence-gap`: data is insufficient for reliable classification.
- `event watch`: event exists, but timing, impact, pricing, or evidence is not strong enough.
- `monitor closely`: important setup with credible evidence but not enough edge for a stronger label.

Do not use labels to prescribe exact buying, selling, or allocation.

## Cross-Module Decision Chain

Use this sequence when multiple skills are relevant:

```text
Market Regime
  -> Sector / Industry Setup
    -> Company Quality And Valuation
      -> Catalyst / Timing
        -> Portfolio Role And Risk
          -> Research Label
```

The chain prevents one attractive score from overpowering the full decision context. A high-quality company can still be a `hold/watch` or `trim-review` if valuation, regime, event pricing, or portfolio concentration is unfavorable.

## Standard Output Blocks

Any output with a scorecard should include:

```markdown
## Score Summary
| Dimension | Score | Evidence | Confidence | Comment |
|---|---:|---|---|---|

## Red Flags
[Risks that cannot be offset by the total score.]

## Decision Impact
[How the score changes the research label, event watch, or risk response.]

## What Would Change The View
[Concrete upgrade or downgrade triggers.]
```

