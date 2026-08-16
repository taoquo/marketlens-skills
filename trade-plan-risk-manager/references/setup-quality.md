# Setup Quality

Use this file to decide whether a research thesis is tradable, conditional, monitor-only, or too weak. Use `../../references/scoring-standard.md` for shared labels and confidence rules.

## Setup Quality Dimensions

Score each dimension from 0 to 3. Scores are research heuristics, not a trading system.

| Dimension | 3 | 2 | 1 | 0 |
|---|---|---|---|---|
| Thesis clarity | Clear driver and falsifiable thesis | Clear but partly proxy-based | Broad narrative | Vague or unfalsifiable |
| Edge / expectation gap | Variant view is evidence-backed, and the price does not already imply it | Some evidence of mispricing | Mostly consensus | No identifiable edge, or the upside case is what the price already requires |
| Timing | Catalyst or data window is defined | Timing likely but loose | Timing uncertain | No timing anchor |
| Asymmetry | Upside/downside path is favorable and bounded | Usable but not exceptional | Mixed or hard to bound | Downside dominates |
| Regime alignment | Regime supports the setup | Neutral regime | Regime is a headwind | Severe regime red flag |
| Liquidity / execution | Deep band, low friction, clear instrument | Adequate band, some slippage | Thin band, gappy, or constrained | Impaired band, not executable as stated |
| Invalidation clarity | Concrete stop-error and review triggers | Mostly clear | Loose or discretionary | No invalidation |

## Labels

| Label | Meaning |
|---|---|
| Tradable setup | Gates passed, evidence is fresh, risk is bounded, and invalidation is clear |
| Conditional setup | Potential exists, but one or more evidence, price, event, or regime gates must improve |
| Monitor closely | Important setup, but edge, timing, or risk is not yet strong enough |
| Event watch | Event matters, but expectation gap or implied move is not favorable enough |
| Evidence-gap | Missing or stale data blocks a reliable plan |
| Risk too high | Liquidity, gap risk, crowding, leverage, or thesis downside is not acceptable as stated |

For a negative thesis, use the short-side reads in
`../../references/short-and-relative-value.md` rather than stretching these labels.
A short setup requires everything a long setup requires, plus verified borrow,
float, and crowding data, plus a tighter invalidation because loss is unbounded and
carry accrues.

## Red-Flag Overrides

Downgrade the setup if any of these are present:

- Current price, event date, or core thesis data is missing for a price-sensitive plan.
- Invalidation condition is undefined.
- Event gap risk can dominate planned risk.
- The liquidity band is thin, impaired, or unmeasured for the intended horizon, per the thresholds in `risk-and-execution.md`.
- A maturity, covenant test, or cash-runway limit falls inside the plan horizon without a stated funding path.
- Any probability in the plan lacks a reference class, per `../../references/base-rates.md`.
- The upside case restates an assumption the current price already implies, per `../../references/implied-expectations.md`. That is not an edge, it is agreement.
- The thesis rests on reported earnings whose cash conversion has not been checked, per `../../references/earnings-quality-screens.md`.
- Market regime is fragile and the setup depends on beta, leverage, or crowded momentum.
- The thesis depends on a single unverified rumor or media-only claim.
- Portfolio overlap makes the trade redundant with an existing risk cluster.

## Interpretation

A high-quality long-term thesis is not automatically a tradable setup. A tradable setup needs a time window, evidence trigger, bounded downside path, and a plan for what would prove it wrong.

The most common false edge is a well-researched thesis that matches what the price
already implies. State the implied assumption and the variant view side by side; if
they are the same statement, the setup is `monitor closely` at best no matter how
good the research is.
