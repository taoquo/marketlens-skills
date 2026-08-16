# Scoring Standard

Use this standard across MarketLens skills whenever a score, scorecard, rating, or research label is used.

Timestamps, freshness grades, evidence tiers, unit and calendar rules, and
user-input handling live in `data-discipline.md`. Load it alongside this file: a
score is only as good as the grade of the data behind it.

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

Freshness grades, evidence tiers, and the core figure check are defined in
`data-discipline.md`. This table only states how those grades affect a score.

| Data status | Treatment |
|---|---|
| `Fresh`, Tier 1 or Tier 2 | Full weight |
| `Fresh`, Tier 3 | Usable, but not the sole basis for a decisive conclusion |
| `Lagged` | Full weight for structural reads; not usable as a current-condition read |
| `Stale` | Half weight, cap confidence at Medium, avoid precise level language |
| `Undated` | Do not score; mark unavailable |
| `Unavailable`, wrong unit, or a quantity-scale anomaly | Exclude or mark proxy only |

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

## Label Layering

The nine labels above are the shared vocabulary. Skills also use domain reads
that describe a specific layer of the chain. A domain read is not a research
label on its own; it must map to one before the output states a stance.

| Layer | Domain read produced by the skill | Maps to |
|---|---|---|
| Market regime | Risk-on recovery, balanced, volatile bottoming, late-cycle melt-up risk, fragile / de-risking | A risk-budget modifier, not a label. It caps or releases the labels below |
| Sector / industry | Improving, resilient, cyclical recovery, late-cycle, crowded, pressured, structurally challenged | `high-priority watch` when improving or resilient; `hold/watch` when late-cycle; `trim-review` or `avoid` when crowded, pressured, or structurally challenged |
| Company | Rating A/B/C/D, attractive, reasonable, rich | `high-priority watch` or `add-candidate watch` when attractive; `hold/watch` when reasonable; `trim-review` when rich; `avoid` when the balance sheet, governance, or structure fails |
| Catalyst | Hard catalyst, soft catalyst, narrative catalyst, noise, priority catalyst | `high-priority watch` for a priority hard catalyst; `event watch` when timing, pricing, or gap is weak; `monitor closely` in between |
| Post-event | Thesis strengthened, neutral, delayed, impaired, broken, crowded unwind | Strengthened raises the prior label by one step; delayed holds it; impaired or crowded unwind moves to `trim-review`; broken moves to `exit-review` |
| Portfolio | Risk-concentrated, balanced watchlist | Not a name-level label. `risk-concentrated` forces at least one name into `trim-review` or `exit-review` |
| Trade plan | Tradable setup, conditional setup, risk too high, plan violated, thesis intact, thesis impaired, thesis broken | `tradable setup` requires the upstream label to be `high-priority watch` or `add-candidate watch`; otherwise use `conditional setup` or `monitor closely`. `risk too high` maps to `avoid` |

When a domain read has no defensible mapping because evidence is missing, use
`evidence-gap` rather than the nearest optimistic label.

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

### Chain Constraints

These constraints are binding. They are what makes the chain a mechanism rather
than a diagram. Each one names the upstream evidence that caps the downstream
label.

| Upstream condition | Downstream constraint |
|---|---|
| Regime is fragile, de-risking, or shows acute funding/FX stress | No `high-priority watch` on high-beta, long-duration, leveraged, low-liquidity, or crowded names. Cap at `monitor closely` unless a name-specific offsetting catalyst is dated and sourced |
| Regime is easy but crowded | Add-candidate language requires a valuation or price gate, not momentum |
| Industry is structurally challenged or oversupplied | A company inside it cannot exceed `hold/watch` on industry exposure alone. Any stronger label must rest on company-specific evidence that is independent of the industry trend |
| Company valuation is rich versus the fair value range | No `add-candidate watch`. Use `hold/watch` or `trim-review` |
| Catalyst is fully priced, crowded, or has a demanding implied move | No `high-priority watch` driven by that catalyst. Use `event watch` |
| Portfolio already holds the same risk driver at high concentration | A new name in the same cluster cannot be `add-candidate watch`. State the overlap and use `monitor closely` or `evidence-gap` |
| Any layer is `evidence-gap` | The final label cannot be stronger than `monitor closely`, and the output must name the missing evidence |

Upstream layers can only tighten a label, never loosen one. If an upstream
input is unavailable, say so and treat the layer as neutral rather than
supportive.

### Chain Provenance

When a conclusion depends on an upstream layer, state where that input came
from: a prior MarketLens output with its date, a user-provided view, or an
assumption made in this run. An assumed layer cannot support a strong label.

## Standard Output Blocks

Every MarketLens output must include these blocks, in this order at the end of the
report: `Red Flags`, `Decision Impact`, `What Would Change The View`, `Data Freshness`,
`Evidence Sources`, and `Disclaimer`. Use this exact disclaimer sentence:

```text
This is public-market research for reference only and does not constitute investment advice.
```

Any output with a 0-3 scorecard must additionally include:

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

Skills that judge quality without a numeric scorecard may replace `Score Summary` with a
named read table, such as the `Setup Quality` table in `trade-plan-risk-manager`. The
other blocks stay mandatory.
