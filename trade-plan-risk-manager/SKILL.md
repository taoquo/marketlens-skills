---
name: trade-plan-risk-manager
description: Use when converting market regime, sector, equity, catalyst, or portfolio research into a non-personalized public-market trade plan framework, including setup quality, entry triggers, invalidation conditions, risk unit, stop/review triggers, time stop, event-risk window, liquidity checks, execution checklist, and post-trade review.
license: MIT
metadata:
  version: 0.7
---

# Trade Plan Risk Manager

## Core Rule

Convert research conclusions into a structured trade plan framework, not personalized investment advice. Match the user's language. State dates for all prices, volatility, event windows, liquidity, and source data. Separate facts, assumptions, estimates, and opinions. Cite sources when using market data. End with a short disclaimer that the plan is for research only and does not constitute investment advice.

This skill does not tell the user to buy, sell, short, use leverage, use options, allocate a percentage of total assets, or place exact orders. It defines conditional triggers, risk limits, review points, and invalidation evidence.

## Skill Boundary

Use this skill for trade setup conversion, pre-trade checklist, risk unit framing, execution-risk review, and post-trade review. This skill consumes the other MarketLens skills; route research questions through `../references/skill-routing.md`.

This skill should synthesize prior skill outputs when available. It should not redo full company, industry, market, event, or portfolio research unless the missing input directly blocks the trade plan.

## Mode Selection

Choose the lightest mode that answers the user:

| User intent | Mode | Minimum input | Output depth |
|---|---|---|---|
| "Turn this thesis into a plan" / "How would you structure the trade?" | `trade-plan` | Instrument, thesis direction, horizon, and a dated reference price | Setup, triggers, risk unit, review plan, invalidation |
| "Is this setup tradable?" / "Do I have an edge?" | `setup-quality-check` | Instrument, the stated edge, and at least one sourced research input | Edge test, red flags, pass/watch/avoid label |
| "What must be true before entry?" | `pre-trade-checklist` | Instrument and thesis direction | Required evidence, timing, liquidity, event and regime checks |
| "Where is the stop or exit logic?" | `risk-trigger-map` | Instrument, thesis direction, and the invalidation condition | Stop-error, time stop, thesis stop, event stop, review triggers |
| "Review my trade after the fact" | `post-trade-review` | The original plan, the execution record, and the outcome | Plan adherence, thesis error, timing error, execution error, rule update |
| Broad or ambiguous trading request | Hybrid | Instrument and thesis direction | Start with setup quality, then build the minimal plan |

If no dated price is available, build the plan from conditional evidence triggers and state that no price level is specified.

## Reference Loading

Read only the references needed:

- For shared confidence, red-flag, and label discipline, read `../references/scoring-standard.md`.
- For timestamps, freshness grades, evidence tiers, unit and calendar rules, and user-input handling, read `../references/data-discipline.md`.
- For deciding which skill owns a question, read `../references/skill-routing.md`.
- For setup quality, edge tests, and tradability labels, read `references/setup-quality.md`.
- For entry, stop, review, and invalidation triggers, read `references/trigger-framework.md`.
- For risk unit, liquidity, event, volatility, and execution checks, read `references/risk-and-execution.md`.
- For post-trade review and rule updates, read `references/post-trade-review.md`.
- For reviewing prior plans or labels over time, and for how a plan decays when its catalyst window passes, read `../references/review-and-calibration.md`.
- For short-side feasibility, squeeze conditions, pairs, and how the same view differs by expression, read `../references/short-and-relative-value.md`.
- For maturity, covenant, or cash-runway limits inside the plan horizon, read `../references/credit-and-cross-asset.md`.
- For the reference class behind any probability in the plan, read `../references/base-rates.md`.
- For whether the upside case requires an assumption the price already contains, read `../references/implied-expectations.md`.
- For whether the thesis rests on reported earnings that have not been reconciled to cash, read `../references/earnings-quality-screens.md`.

## Evidence Standard

Use primary or official sources first where possible. Do not fabricate citations or quote text you cannot verify.

| Tier | Sources | Use |
|---|---|---|
| Tier 1 | Official filings, company announcements, exchange disclosures, regulator notices, official event calendars | Event timing, company facts, terms, legal status |
| Tier 2 | Exchange data, official macro/rates/FX data, company IR, options/volatility data when sourced, prior MarketLens outputs with their dates | Price, liquidity, volatility, regime, event-risk context |
| Tier 3 | Financial platforms, media, broker notes, consensus datasets, technical summaries | Context and proxy data only |

A user-provided thesis or plan is not evidence. It is the object being tested. Classify it using the User-Provided Input rules in `../references/data-discipline.md`:

- Plan parameters such as instrument, direction, horizon, and stated constraints are accepted as given and labelled `user-provided`.
- Fact claims inside the thesis are claims to verify. Source them at Tier 1 or Tier 2 before the plan leans on them.
- Preferences shape scope only and never become an inferred number.

A plan built entirely on unverified user claims cannot be labelled `tradable setup`. Use `conditional setup` or `evidence-gap` and name the claim that needs sourcing.

Always include an `Evidence Sources` section when the plan uses external market data. Do not infer personal constraints.

## Conclusion Gates

Use research language such as tradable setup, conditional setup, monitor closely, event watch, risk too high, evidence-gap, plan violated, thesis intact, thesis impaired, thesis broken, timing error, or execution error. The `Label Layering` and `Chain Constraints` tables in `../references/scoring-standard.md` govern which upstream label allows a `tradable setup`.

Do not give a strong tradable setup label unless these are satisfied:

- The instrument, direction of thesis, time horizon, and current or reference price/date are explicit.
- The research basis is tied to at least one market, sector, company, catalyst, or portfolio input.
- Entry trigger, invalidation condition, and review window are defined.
- Event, liquidity, volatility, and market-regime risks are checked or explicitly marked unavailable.
- Risk is framed as conditional risk units or review limits, not personal allocation.

If any gate fails, downgrade to conditional setup, monitor closely, or evidence-gap and state the missing evidence.

## Data Freshness Protocol

Timestamps, freshness grades, evidence tiers, unit and calendar rules, and user-input checks are defined in `../references/data-discipline.md`. Load that file before writing the `Data Freshness` table and use its five freshness grades verbatim.

Plan-specific additions:

- Price, key levels, volatility, and event dates must be dated before any precise trigger language.
- Every upstream research input needs provenance: a prior MarketLens output with its date, a user-provided view, or an assumption made in this run. An assumed input cannot support a `tradable setup` label.
- Re-check the freshness of the research basis, not only the price. A plan resting on a three-month-old regime read is stale even with a live quote.

Degrade conclusions as follows:

| Missing or stale item | Required handling |
|---|---|
| Current price is stale or undated | No precise trigger levels; use conditional evidence triggers |
| Volatility or implied-move data is unavailable | No volatility-scaled stop or sizing arithmetic |
| Liquidity data such as ADV or spread is unavailable | State execution risk as unmeasured and avoid size-dependent claims |
| Event calendar for the horizon is unchecked | Add an event-risk caveat and no time stop shorter than the unchecked window |
| Market regime input is missing or older than its TTL | Treat regime as neutral, not supportive, and cap at `conditional setup` |
| The research basis is a user claim with no source | Cap at `conditional setup` or `evidence-gap` and name the claim to verify |
| Execution record is incomplete in a post-trade review | Separate what is known from what is inferred; do not assign an error type by guess |

## Workflow

1. Identify instrument, ticker, market, thesis direction, time horizon, current date, and whether the user provided portfolio constraints.
2. Summarize the research basis without redoing full research: regime, sector, company, catalyst, portfolio role, and evidence gaps.
3. Classify setup quality using edge, asymmetry, timing, liquidity, regime alignment, event risk, and invalidation clarity.
4. Define the plan only as conditional triggers: entry trigger, confirmation evidence, invalidation evidence, review triggers, time stop, and post-event review window.
5. Frame risk using risk units, scenario loss, volatility, liquidity, and event gap risk. Do not set personalized position size unless the user supplies constraints and asks for a general framework.
6. Build the pre-trade checklist: evidence, price/volume/liquidity, catalyst calendar, earnings blackout, regime, sector, portfolio overlap, and data freshness.
7. Define what would upgrade, downgrade, pause, or retire the setup.
8. For post-trade review, compare plan vs execution and separate thesis error, timing error, sizing/risk error, execution error, and data-quality error.

## Output Template

```markdown
# [Instrument / Thesis] Trade Plan Risk Manager

## Conclusion
[Tradable setup / conditional setup / monitor closely / evidence-gap / risk too high, confidence, and main reason.]

## Research Basis
[Market regime, sector, company, catalyst, and portfolio inputs used. State missing inputs.]

## Setup Quality
| Dimension | Read | Evidence | Confidence | Comment |
|---|---|---|---|---|

## Trade Plan Framework
| Component | Conditional Plan |
|---|---|
| Thesis |  |
| Time Horizon |  |
| Entry Trigger |  |
| Confirmation Evidence |  |
| Review Trigger |  |
| Invalidation / Stop-Error |  |
| Time Stop |  |
| Event-Risk Window |  |
| Post-Event Review |  |

## Risk Unit And Execution Checks
[Risk unit framing, volatility/liquidity/event gap risk, slippage, borrow/options constraints if relevant, no personalized allocation.]

## Pre-Trade Checklist
| Check | Status | Required Evidence / Action |
|---|---|---|

## Red Flags
[Risks that can pause or invalidate the setup.]

## Decision Impact
[How setup quality, regime, catalyst timing, valuation, and portfolio overlap affect the plan label.]

## What Would Change The View
[Concrete data, price, event, regime, liquidity, or thesis triggers.]

## Post-Trade Review Plan
[How to judge whether the result came from thesis quality, timing, risk framing, execution, or data quality.]

## Confidence And Limits
[Confidence level, missing data, stale data, personal constraints not inferred, unsupported claims avoided.]

## Data Freshness
| Data | Value | As of | Published | Retrieved | Source | Freshness |
|---|---:|---|---|---|---|---|

## Evidence Sources
| Source | Date | Type | Supports |
|---|---|---|---|

## Disclaimer
This is public-market research for reference only and does not constitute investment advice.
```
