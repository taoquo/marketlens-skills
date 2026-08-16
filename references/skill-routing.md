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

## Cross-Cutting References

Five shared files are not owned by any single skill because they change the
conclusion in more than one layer. Load them by trigger rather than by skill.

| File | Load when |
|---|---|
| `references/credit-and-cross-asset.md` | Leverage, refinancing, covenants, cash runway, or capital intensity is part of the thesis; the sector is property, financials, utilities, shipping, airlines, or pre-profit growth; or a market-wide risk-appetite read is being made |
| `references/base-rates.md` | Any probability, likelihood word, scenario weight, turnaround, approval, deal-completion, or margin-recovery claim appears |
| `references/short-and-relative-value.md` | The conclusion is negative and the user asks about the other side, a pair or hedge is discussed, red flags are confirmed rather than suspected, or a relative-value gap such as AH, ADR, or holdco discount is the subject |
| `references/implied-expectations.md` | Any multiple, fair value range, target level, cheap-or-expensive judgement, or margin-of-safety claim carries the conclusion; or a growth narrative needs to be tested against what the price already requires |
| `references/earnings-quality-screens.md` | A conclusion rests on reported profit, margin, or growth; cash conversion or working capital looks inconsistent with the income statement; or a red flag in the financial-quality family needs to be measured rather than described |

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

## Out Of Scope

MarketLens covers listed equity research and the risk framing around it. The
topics below are outside that coverage. Say so plainly, name the closest thing the
toolkit can do, and stop there rather than improvising a framework.

| Topic | Handling |
|---|---|
| Crypto and digital assets | Usable only as a risk-appetite and liquidity proxy in `market-regime-monitor`. No token, protocol, or valuation analysis |
| FX as a standalone view | Currencies are inputs to equity theses: translation, funding, carry unwind. No directional currency calls or hedging programmes |
| Commodity futures and physical trading | Prices are inputs to industry and margin analysis. No curve, roll-yield, basis, or futures positioning advice |
| Rates and bond selection | Rates and credit are inputs under `credit-and-cross-asset.md`. No duration positioning, bond picking, or credit relative value |
| Options pricing and volatility strategy | Implied move and IV context are inputs to event pricing. No structure selection, greeks management, or volatility strategy |
| Convertibles, warrants, structured products | Dilution and terms are inputs to equity analysis. No instrument-level pricing or arbitrage |
| Private companies, pre-IPO, venture | Out of scope. Public comparables are the closest available read |
| Fund, ETF, or manager selection | Out of scope, including allocation across funds |
| Portfolio optimization and position sizing | Deliberately excluded. `portfolio-risk-monitor` diagnoses exposure; it does not optimize weights. `trade-plan-risk-manager` frames relative risk in R units only |
| Tax, legal, and regulatory advice | Tax and transaction frictions are noted as return drags in `../equity-research/references/regional-market-guide.md`, not as planning advice |
| ESG ratings and sustainability scoring | Not covered as a scoring system. Environmental, social, and governance facts enter only where they are financially material: regulatory cost, licence risk, stranded assets, litigation, or governance red flags |
| Intraday and high-frequency execution | Out of scope. The shortest horizon supported is a dated catalyst window |
| Personal financial planning | Out of scope in every skill and every mode |

Degradation language for an out-of-scope request: name the boundary, offer the
in-scope adjacent read, and do not produce a scorecard for the out-of-scope part.
