---
name: sector-industry-research
description: Use when analyzing sectors, industries,产业链, peer groups, industry cycles, supply-demand, inventory, pricing, capacity, profit pools, policy or technology disruption, competitive structure, subsector scorecards, industry beta, sector rotation, trade expression, catalysts, stop-loss/stop-error triggers, or questions like which companies benefit most from an industry trend across US, Hong Kong, or A-share markets.
license: MIT
metadata:
  version: 0.10
---

# Sector Industry Research

## Core Rule

Shared operating rules are in `../references/skill-contract.md`: public-market research only, no personalized investment advice, dated and sourced evidence, confidence and limits, and the exact disclaimer. Apply them to every output.

Judge the industry field first, then hand named stocks and final single-stock conclusions to company-level work. Follow the cross-module chain in `../references/scoring-standard.md`: market regime -> sector / industry setup -> company quality and valuation -> catalyst / timing -> portfolio role and risk -> research label.

## Skill Boundary

Use this skill for sector setup, industry cycle, supply and demand, value-chain structure, profit pools, policy/technology disruption, peer maps, and industry-to-stock read-through. For anything outside that scope, route through `../references/skill-routing.md`.

## Mode Selection

Choose the lightest mode that answers the user:

| User intent | Mode | Minimum input | Output depth |
|---|---|---|---|
| "How is this industry doing?" / sector quick view | `cycle-scan` | Industry and geography, plus one dated demand and one dated supply or price indicator | Cycle stage, key indicators, 3-5 monitoring variables |
| Industry deep dive or产业链 analysis | `industry-deepdive` | Industry, geography, and value-chain segment, plus dated demand, capacity, and pricing data | Supply-demand, pricing, capacity, value chain, policy, technology |
| Compare leaders and beneficiaries | `peer-map` | A defined peer set with stated inclusion and exclusion rules | Peer set, factor exposure, winners/losers, valuation context |
| "How to express this view?" / trading read-through | `research-to-trade` | The industry view being expressed, plus its cycle stage and key forces | Trader view, best expression, catalysts, stop-error conditions |
| "Which stock benefits?" / sector expression question | Hybrid | Industry and geography | Start with industry conclusion, then list candidate types and evidence needed before single-stock calls |

If neither a demand nor a supply indicator can be dated, do not assign a cycle stage. Describe the structure and name the data required.

If the industry has regulated, balance-sheet-driven, capital-intensive, commodity-like, digital/platform, consumer/channel, export-driven, policy-heavy, or science/technology-risk characteristics, adjust the indicators before judging and explain the adjustment.

## Evidence Standard

Tier definitions and the decisive-claim rule are in `../references/data-discipline.md` and `../references/skill-contract.md`. Domain sources:

| Tier | Sources | Use |
|---|---|---|
| Tier 1 | Government/regulator data, exchange disclosures, company filings, official industry association releases | Demand, output, capacity, policy, company segment data |
| Tier 2 | Exchange/market data, customs/trade data, rates/FX, company IR, official price indices | Flows, pricing, margins, regional transmission |
| Tier 3 | Broker notes, expert calls, media, data vendors, consensus datasets | Context only; never sole basis for a decisive conclusion |

## Reference Loading

Read only the references needed:

- For source priority, TTL, and cross-check rules, read `references/data-sources.md`.
- For cycle stage, supply-demand, inventory, pricing, and capacity, read `references/industry-cycle-framework.md`.
- For产业链, profit pools, bargaining power, and margin transmission, read `references/value-chain-framework.md`.
- For peer-set construction, winner/loser classification, and valuation context, read `references/peer-comparison.md`.
- For policy, regulation, subsidy, localization, export control, and technology disruption, read `references/policy-and-technology.md`.
- For trader view, subsector scorecards, catalysts, stop-error conditions, and research-to-trade mapping, read `references/research-to-trade.md`.
- For the shared operating, evidence, gate, freshness, and output contract, read `../references/skill-contract.md`.
- Required shared files: `../references/scoring-standard.md`, `../references/data-discipline.md`, `../references/skill-routing.md`, and `../references/review-and-calibration.md`.
- For cycle-duration, capex-cycle, and share-shift base rates before any probability or timing claim, read `../references/base-rates.md`.
- For the displaced side of an industry shift, and for pairs within a peer set, read `../references/short-and-relative-value.md`.
- For capital-intensive industries where cost of debt and refinancing set returns on new capacity, read `../references/credit-and-cross-asset.md`.
- For what a sector multiple implies about industry growth, terminal margin, or mid-cycle earnings, read `../references/implied-expectations.md`.
- For comparing earnings quality across a peer set, or for testing whether a cyclical peak is accrual-driven, read `../references/earnings-quality-screens.md`.
- For ranking which peers converted the same industry conditions into return on incremental capital, or for judging an industry-wide capacity build, read `../references/capital-allocation-record.md`.

## Conclusion Gates

Map the industry read to a shared label using the `Label Layering` table in `../references/scoring-standard.md`, and apply the shared gate rules in `../references/skill-contract.md`. Do not present personalized buy/sell advice, exact allocation instructions, or transaction-prescriptive trade expression.

Domain-specific gates. Do not give a strong sector research label, ranked beneficiaries, or precise stock-selection conclusion unless these are satisfied:

- Industry scope and geography are explicit.
- At least one demand indicator and one supply/capacity/pricing indicator are dated.
- At least one primary or official source supports the core industry claim.
- Peer comparison uses a defined peer set and explains inclusion/exclusion.
- If naming stock beneficiaries, the analysis separates industry exposure from company-specific execution and valuation.
- Core figures are checked against original wording, unit, period, and source link; quantity-scale anomalies are caveated or excluded.

If any gate fails, apply the downgrade rule in `../references/skill-contract.md` and name the evidence that would strengthen the view.

Industry research provides expression, risk conditions, and evidence requirements. It does not replace company valuation, event risk/reward, or portfolio position review.

## Data Freshness Protocol

Apply the timestamp, freshness, and core-figure rules in `../references/data-discipline.md` and `../references/skill-contract.md`. Domain additions:

Industry-specific additions:

- Most industry data lags by design. Grade monthly output, customs, inventory, and survey series as `Lagged` and print the reference period.
- Keep the `Data Check` audit trail for every core figure that carries a conclusion.
- State whether a figure is production, shipment, installation, order, or revenue based. These are different quantities and are not interchangeable.

Degrade conclusions as follows:

| Missing or stale item | Required handling |
|---|---|
| Only a demand indicator is dated | Describe demand direction only, no cycle-stage label |
| Only a supply or capacity indicator is dated | Describe supply direction only, no cycle-stage label |
| Pricing or spread data is unavailable | No margin-transmission or profit-pool conclusion |
| Inventory data is unavailable | Do not call a restock or destock phase |
| Peer set cannot be defined from disclosed segments | No winner/loser ranking; list candidate types instead |
| Only broker or expert-call data supports a core figure | Mark it `Proxy only` and cap confidence at Medium |
| A figure shows a quantity-scale anomaly | Mark it `Use with caveat` or `Exclude`; never smooth it into the narrative |

## Workflow

1. Identify industry, value-chain segment, geography, user intent, time horizon, and current date.
2. Collect dated demand, supply/capacity, inventory, pricing, margin, policy, and peer data as needed.
3. Rebuild the data-check table for core figures and exclude or caveat quantity-scale anomalies.
4. Classify the cycle stage and name the 1-3 Key Forces that will drive the industry over the next 1-3 years.
5. Map the value chain and identify where profit pools, pricing power, and bottlenecks sit.
6. Build a subsector or segment scorecard when the industry has multiple drivers or mixed cycles.
7. Build a focused peer set, separating structural leaders, bottleneck suppliers, cyclical beneficiaries, high-beta challengers, value traps, and watchlist-only names.
8. Translate the research into a trader view: current phase, trading state, best expression, main risk, upgrade triggers, cooldown triggers, and stop-error conditions.
9. Map industry phase -> profit pool -> best expression -> catalyst window -> stop-error -> portfolio overlap.
10. Connect industry read-through to listed companies only after checking exposure, execution, balance sheet, and valuation caveats.
11. Output score summary, red flags, decision impact, monitoring variables, thesis breakers, and confidence limits.

## Output Template

```markdown
# [Industry / Sector] Research

## Conclusion
[Industry research label, cycle stage, confidence, and the main reason.]

## Key Forces
[1-3 decisive forces tied to evidence.]

## Trader View
[Current industry phase, trading state, best expression, main risk, positioning implication.]

## Cycle And Supply-Demand
[Demand, pricing, inventory, capacity, utilization, order/backlog, margins.]

## Value Chain And Profit Pools
[Who has bargaining power, margin pass-through, bottlenecks, substitutes.]

## Subsector Scorecard
| Segment | Demand | Supply Constraint | Pricing | Profit Realization | Valuation Pressure | Policy Risk | Read-Through |
|---|---:|---:|---:|---:|---:|---:|---|

## Score Summary
| Dimension | Score | Evidence | Confidence | Comment |
|---|---:|---|---|---|

## Red Flags
[Demand, supply, pricing, policy, data-quality, valuation, or profit-pool risks that cannot be offset by the total score.]

## Policy, Technology, And Regional Checks
[Policy, regulation, localization, export controls, subsidies, technology shifts.]

## Peer Map And Listed-Company Read-Through
[Defined peer set, leaders/beneficiaries/laggards, exposure and valuation caveats.]

## Research-To-Trade Map
[Long-term research areas, tactical watch areas, watch-only areas, catalyst windows, stop-error signals.]

## Decision Impact
[How industry phase, profit pool, best expression, catalyst window, stop-error, and portfolio overlap affect the research label.]

## Monitoring Variables And Thesis Breakers
[3-5 data triggers that would upgrade, soften, or invalidate the view.]

## What Would Change The View
[Concrete demand, supply, pricing, policy, revision, valuation, or company evidence that changes the view.]

## Confidence And Limits
[Confidence level, missing data, stale data, conflicts, unsupported claims avoided.]

## Data Check
| Metric | Original Wording | Value | Unit | Period | Publisher | Link | Cross-check | Freshness | Treatment |
|---|---|---:|---|---|---|---|---|---|---|---|

## Data Freshness
| Data | Value | As of | Published | Retrieved | Source | Freshness |
|---|---:|---|---|---|---|---|

## Evidence Sources
| Source | Date | Type | Supports |
|---|---|---|---|

## Disclaimer
This is public-market research for reference only and does not constitute investment advice.
```
