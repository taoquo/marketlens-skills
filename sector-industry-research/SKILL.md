---
name: sector-industry-research
description: Use when analyzing sectors, industries,产业链, peer groups, industry cycles, supply-demand, inventory, pricing, capacity, profit pools, policy or technology disruption, competitive structure, subsector scorecards, industry beta, sector rotation, trade expression, catalysts, stop-loss/stop-error triggers, or questions like which companies benefit most from an industry trend across US, Hong Kong, or A-share markets.
---

# Sector Industry Research

## Core Rule

Provide public-market sector and industry research, not personalized investment advice. Match the user's language. State dates for all market, industry, and macro data; separate facts from estimates and opinions; cite sources; show confidence and limits; and end with a short disclaimer that the analysis is for research only and does not constitute investment advice.

This skill sits between `market-regime-monitor` and `equity-research`: use it to judge the industry field, then use company-level work only for named stocks or final single-stock conclusions.

Use the cross-module chain from `../references/scoring-standard.md`: market regime -> sector / industry setup -> company quality and valuation -> catalyst / timing -> portfolio role and risk -> research label.

## Mode Selection

Choose the lightest mode that answers the user:

| User intent | Mode | Output depth |
|---|---|---|
| "How is this industry doing?" / sector quick view | `cycle-scan` | Cycle stage, key indicators, 3-5 monitoring variables |
| Industry deep dive or产业链 analysis | `industry-deepdive` | Supply-demand, pricing, capacity, value chain, policy, technology |
| Compare leaders and beneficiaries | `peer-map` | Peer set, factor exposure, winners/losers, valuation context |
| "How to express this view?" / trading read-through | `research-to-trade` | Trader view, best expression, catalysts, stop-error conditions |
| "Which stock benefits?" / sector allocation question | Hybrid | Start with industry conclusion, then list candidate types and evidence needed before single-stock calls |

If the industry has regulated, balance-sheet-driven, capital-intensive, commodity-like, digital/platform, consumer/channel, export-driven, policy-heavy, or science/technology-risk characteristics, adjust the indicators before judging and explain the adjustment.

## Evidence Standard

Use primary or official sources first. Do not fabricate citations or quote text you cannot verify.

| Tier | Sources | Use |
|---|---|---|
| Tier 1 | Government/regulator data, exchange disclosures, company filings, official industry association releases | Demand, output, capacity, policy, company segment data |
| Tier 2 | Exchange/market data, customs/trade data, rates/FX, company IR, official price indices | Flows, pricing, margins, regional transmission |
| Tier 3 | Broker notes, expert calls, media, data vendors, consensus datasets | Context only; never sole basis for a decisive conclusion |

Always include an `Evidence Sources` section with source name, date, link, and what it supports.

## Reference Loading

Read only the references needed:

- For source priority, TTL, and cross-check rules, read `references/data-sources.md`.
- For cycle stage, supply-demand, inventory, pricing, and capacity, read `references/industry-cycle-framework.md`.
- For产业链, profit pools, bargaining power, and margin transmission, read `references/value-chain-framework.md`.
- For peer-set construction, winner/loser classification, and valuation context, read `references/peer-comparison.md`.
- For policy, regulation, subsidy, localization, export control, and technology disruption, read `references/policy-and-technology.md`.
- For trader view, subsector scorecards, catalysts, stop-error conditions, and research-to-trade mapping, read `references/research-to-trade.md`.
- For shared scoring, confidence, red-flag, and label discipline, read `../references/scoring-standard.md`.
- For review of prior industry calls, read `../references/review-and-calibration.md`.

## Conclusion Gates

Use research language such as improving, resilient, cyclical recovery, late-cycle, crowded, pressured, structurally challenged, watch, or avoid. Do not present personalized buy/sell advice.

Do not give a strong sector stance, ranked beneficiaries, or precise stock-selection conclusion unless these are satisfied:

- Industry scope and geography are explicit.
- At least one demand indicator and one supply/capacity/pricing indicator are dated.
- At least one primary or official source supports the core industry claim.
- Peer comparison uses a defined peer set and explains inclusion/exclusion.
- If naming stock beneficiaries, the analysis separates industry exposure from company-specific execution and valuation.
- Core figures are checked against original wording, unit, period, and source link; quantity-scale anomalies are caveated or excluded.

If any gate fails, downgrade to a watchlist-style conclusion, state the missing data, and explain what evidence would strengthen the view.

Industry research provides expression, risk conditions, and evidence requirements. It does not replace company valuation, event risk/reward, or portfolio position review.

## Data Freshness Protocol

Do not use an industry data point unless its source date is known. Record:

- `as_of`: the period or market date the value describes.
- `published_at`: when the source published it, if available.
- `retrieved_at`: when you fetched or viewed it.

Industry data often lags. Label stale or survey-based data, reduce confidence, and never convert missing data into a bullish or bearish signal.

For core figures, keep an audit trail with original wording, value, unit, period, publisher, link, cross-check result, and treatment. Use only these treatments: `Use`, `Use with caveat`, `Proxy only`, or `Exclude`.

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
[Industry stance, cycle stage, confidence, and the main reason.]

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
[Long-term allocation areas, swing-trade areas, watch-only areas, catalyst windows, stop-error signals.]

## Decision Impact
[How industry phase, profit pool, best expression, catalyst window, stop-error, and portfolio overlap affect the research label.]

## Monitoring Variables And Thesis Breakers
[3-5 data triggers that would upgrade, soften, or invalidate the view.]

## What Would Change The View
[Concrete demand, supply, pricing, policy, revision, valuation, or company evidence that changes the view.]

## Confidence And Limits
[Confidence level, missing data, stale data, conflicts, unsupported claims avoided.]

## Data Check
| Metric | Original Wording | Value | Unit | Period | Publisher | Link | Cross-check | Treatment |
|---|---|---:|---|---|---|---|---|---|

## Evidence Sources
| Source | Date | Type | Supports |
|---|---|---|---|

## Disclaimer
This is public-market research for reference only and does not constitute investment advice.
```
