# Skill Contract

Shared, non-negotiable rules for every MarketLens skill. Each `SKILL.md` loads this
file and states only its domain-specific additions. The definitions referenced here
live in `data-discipline.md` and `scoring-standard.md`.

## Core Rule

Provide public-market research, not personalized investment advice. Match the user's
language. State dates for all market, industry, company, event, and portfolio data.
Separate facts from estimates and opinions. Cite sources. Show confidence and limits.
End with the exact disclaimer in `Output Contract`.

Translate buy/sell/add/trim/exit, hedge, or allocation questions into research labels,
conditional triggers, and review language. Never prescribe a personal transaction,
target weight, exact position size, or allocation.

## Reference Routing

Every `SKILL.md` must route these four shared files:

- `../references/scoring-standard.md`
- `../references/data-discipline.md`
- `../references/skill-routing.md`
- `../references/review-and-calibration.md`

Route the six cross-cutting files by trigger, as defined in `skill-routing.md`.

## Evidence Tiers

Tier definitions, evidence weighting, and the rule that a decisive claim needs at
least one Tier 1 or Tier 2 source live in `data-discipline.md`. A skill's own
`Evidence Standard` section names only the concrete sources that fill each tier for
its domain.

## Conclusion Gates

Map every domain read to one of the nine shared research labels using `Label Layering`
in `scoring-standard.md`. Apply `Chain Constraints` as binding caps. Do not present
personalized buy/sell advice, exact allocation instructions, or transaction orders.

If any gate in the skill's own `Conclusion Gates` fails, downgrade to a watchlist-style
conclusion, state the missing data, and name the evidence that would strengthen the view.

## Data Freshness

Record `as_of`, `published_at`, and `retrieved_at` separately for every data point.
Use only the five grades `Fresh`, `Lagged`, `Stale`, `Undated`, `Unavailable`. Missing
data is a confidence limit, never a directional signal. Run the core figure check in
`data-discipline.md` before any claim that carries a conclusion.

## Output Contract

Every output must end with these blocks, in this order:

1. `## Red Flags`
2. `## Decision Impact`
3. `## What Would Change The View`
4. `## Data Freshness`
5. `## Evidence Sources`
6. `## Disclaimer`

Include `## Score Summary` before `## Red Flags` when the output uses a 0 to 3
scorecard. A skill that judges quality without a numeric scorecard may substitute a
named read table, such as `## Setup Quality`, for `## Score Summary`.

The disclaimer block must use this exact sentence:

```text
This is public-market research for reference only and does not constitute investment advice.
```

Skills may place domain-specific blocks before `## Red Flags`, and may add domain
blocks between `## What Would Change The View` and `## Data Freshness`. The six
required blocks keep their relative order.
