# Skill Contract

Shared, non-negotiable rules for every lens skill. Each `SKILL.md` loads this
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

## Research State Card

When a request spans more than one skill, keep one compact state card and pass it forward.
It is the only shared context between layers; do not rely on a downstream skill remembering
an upstream answer.

| Field | Content |
|---|---|
| `question` | The user's question in one sentence, including the decision horizon |
| `as_of` | The market date the answer is anchored to |
| `mode` | The research desk mode from `skill-routing.md`: `quick`, `full`, `event`, or `portfolio` |
| `regime` | Market-regime read, date, and confidence |
| `sector` | Sector or industry read, date, and confidence |
| `company` | Company quality and valuation read, including the band or implied-expectations result |
| `catalyst` | Dated catalyst, pricing read, and scenario |
| `portfolio` | Role, concentration, and correlated-risk read |
| `label` | One shared research label, with the binding constraint named |
| `freshness` | Missing, stale, or unavailable inputs and their caps |
| `source_pool` | Source IDs from `data-discipline.md`, not a second bibliography |
| `open_questions` | Evidence that would change the view, and the next review date |

Rules:

- Create the card before the first layer and update it after each layer. A field that was
  not researched stays `Unavailable`; do not fill it by assumption.
- The card is a working artifact, not a required output block. Carry what matters into the
  final output; do not paste the whole card unless the user asks for it.
- Downstream layers read the card and may tighten a label, never loosen one. If a layer is
  missing, follow the degradation rule in `skill-routing.md`.
- Keep the source pool IDs stable. A downstream layer that adds evidence appends to the
  pool rather than renumbering it.

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

Before presenting the output as complete, run the `Pre-Publication Review` in
`review-and-calibration.md`, including the `Red-Team Pass` when the label is stronger than
`hold/watch` or depends on one dated catalyst. A `REVISE` verdict blocks publication until
the blocking item is fixed or the conclusion is capped and the residual issue recorded.

## Data Freshness

Record `as_of`, `published_at`, and `retrieved_at` separately for every data point.
Use only the five grades `Fresh`, `Lagged`, `Stale`, `Undated`, `Unavailable`. Missing
data is a confidence limit, never a directional signal. Run the core figure check and the
silent-failure checks in `data-discipline.md` before any claim that carries a conclusion.

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

`## Evidence Sources` lists the source-pool IDs and locators that carry the conclusion. It
is not a padded bibliography; an entry that does not support a stated claim is omitted.

`## What Would Change The View` uses the falsifiable trigger format in
`scoring-standard.md`: 2-4 measurable triggers, at least one testing the binding constraint.
A label stronger than `hold/watch` must name the strongest opposing case and why it fails.
The red-team pass is recorded under `## Red Flags` or `## What Would Change The View`; it is
not a new output block.

The disclaimer block must use this exact sentence:

```text
This is public-market research for reference only and does not constitute investment advice.
```

Skills may place domain-specific blocks before `## Red Flags`, and may add domain
blocks between `## What Would Change The View` and `## Data Freshness`. The six
required blocks keep their relative order.
