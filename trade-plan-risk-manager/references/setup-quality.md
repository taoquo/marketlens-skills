# Setup Quality

Use this file to decide whether a research thesis is tradable, conditional, monitor-only, or too weak. Use `../../references/scoring-standard.md` for shared labels and confidence rules.

## Setup Quality Dimensions

Score each dimension from 0 to 3. Scores are research heuristics, not a trading system.

| Dimension | 3 | 2 | 1 | 0 |
|---|---|---|---|---|
| Thesis clarity | Clear driver and falsifiable thesis | Clear but partly proxy-based | Broad narrative | Vague or unfalsifiable |
| Edge / expectation gap | Variant view is evidence-backed and not fully priced | Some evidence of mispricing | Mostly consensus | No identifiable edge |
| Timing | Catalyst or data window is defined | Timing likely but loose | Timing uncertain | No timing anchor |
| Asymmetry | Upside/downside path is favorable and bounded | Usable but not exceptional | Mixed or hard to bound | Downside dominates |
| Regime alignment | Regime supports the setup | Neutral regime | Regime is a headwind | Severe regime red flag |
| Liquidity / execution | Liquid, low friction, clear instrument | Usable with some slippage | Thin, gappy, or constrained | Not executable as stated |
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

## Red-Flag Overrides

Downgrade the setup if any of these are present:

- Current price, event date, or core thesis data is missing for a price-sensitive plan.
- Invalidation condition is undefined.
- Event gap risk can dominate planned risk.
- Liquidity is too thin for the intended horizon.
- Market regime is fragile and the setup depends on beta, leverage, or crowded momentum.
- The thesis depends on a single unverified rumor or media-only claim.
- Portfolio overlap makes the trade redundant with an existing risk cluster.

## Interpretation

A high-quality long-term thesis is not automatically a tradable setup. A tradable setup needs a time window, evidence trigger, bounded downside path, and a plan for what would prove it wrong.
