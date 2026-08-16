# Skill Routing

Use this file to decide which MarketLens skill owns a question. Each SKILL.md
states what it owns and points here for everything else, so a new skill only
needs one routing entry instead of an edit in every other SKILL.md.

## Ownership Table

| Skill | Owns | Does not own |
|---|---|---|
| `market-regime-monitor` | Liquidity, sentiment, positioning, valuation crowding, cross-market transmission, risk-budget language | Single-company analysis, industry structure, dated events, portfolio holdings, trade plans |
| `sector-industry-research` | Industry cycle, supply and demand, value chain, profit pools, policy and technology shifts, peer maps, industry-to-stock read-through | Market-wide regime, company-specific valuation, event timing, portfolio construction, trade plans |
| `equity-research` | Company quality, fundamentals, earnings, valuation, moat, regional disclosure checks, single-stock research labels | Market regime, industry structure, event timing, portfolio-level exposure, trade plans |
| `catalyst-event-monitor` | Dated catalysts, event materiality, expectation gaps, market-implied pricing, scenario trees, post-event thesis updates | Baseline company quality, industry cycle, market regime, portfolio exposure, full trade plans |
| `portfolio-risk-monitor` | Concentration, correlated exposures, risk clusters, quantitative risk snapshot, priority ranking, drawdown scenarios, rebalance watch | Company fundamentals, industry structure, market regime, event timing, per-trade execution |
| `trade-plan-risk-manager` | Setup quality, entry and invalidation triggers, risk-unit framing, execution checks, post-trade review | Original company, industry, market, event, or portfolio research |

## Routing Rules

- Answer from the owning skill first. Pull other skills in only when their input
  changes the conclusion.
- When a question spans skills, follow the decision chain in
  `references/scoring-standard.md` rather than merging scores.
- `trade-plan-risk-manager` consumes the other skills. It should synthesize their
  outputs and must not redo full research unless a missing input blocks the plan.
- If no skill owns the question, say so and answer with the general research
  discipline in `references/scoring-standard.md`.
- Never route a question into personalized advice. Every skill stays at research
  labels, conditional triggers, and monitoring language.
