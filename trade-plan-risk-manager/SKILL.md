---
name: trade-plan-risk-manager
description: Use when converting market regime, sector, equity, catalyst, or portfolio research into a non-personalized public-market trade plan framework, including setup quality, entry triggers, invalidation conditions, risk unit, stop/review triggers, time stop, event-risk window, liquidity checks, execution checklist, and post-trade review.
license: MIT
metadata:
  version: 0.4
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

| User intent | Mode | Output depth |
|---|---|---|
| "Turn this thesis into a plan" / "How would you structure the trade?" | `trade-plan` | Setup, triggers, risk unit, review plan, invalidation |
| "Is this setup tradable?" / "Do I have an edge?" | `setup-quality-check` | Edge test, red flags, pass/watch/avoid label |
| "What must be true before entry?" | `pre-trade-checklist` | Required evidence, timing, liquidity, event and regime checks |
| "Where is the stop or exit logic?" | `risk-trigger-map` | Stop-error, time stop, thesis stop, event stop, review triggers |
| "Review my trade after the fact" | `post-trade-review` | Plan adherence, thesis error, timing error, execution error, rule update |
| Broad or ambiguous trading request | Hybrid | Start with setup quality, then build the minimal plan |

## Reference Loading

Read only the references needed:

- For shared confidence, red-flag, and label discipline, read `../references/scoring-standard.md`.
- For deciding which skill owns a question, read `../references/skill-routing.md`.
- For setup quality, edge tests, and tradability labels, read `references/setup-quality.md`.
- For entry, stop, review, and invalidation triggers, read `references/trigger-framework.md`.
- For risk unit, liquidity, event, volatility, and execution checks, read `references/risk-and-execution.md`.
- For post-trade review and rule updates, read `references/post-trade-review.md`.
- For reviewing prior plans or labels over time, read `../references/review-and-calibration.md`.

## Evidence Standard

Use primary or official sources first where possible. Do not fabricate citations or quote text you cannot verify.

| Tier | Sources | Use |
|---|---|---|
| Tier 1 | User-provided thesis/plan, official filings, company announcements, exchange disclosures, event calendars | Thesis, event timing, company facts, plan inputs |
| Tier 2 | Exchange data, official macro/rates/FX data, company IR, options/volatility data when sourced | Price, liquidity, volatility, regime, event-risk context |
| Tier 3 | Financial platforms, media, broker notes, consensus datasets, technical summaries | Context and proxy data only |

Always include an `Evidence Sources` section when the plan uses external market data. For user-provided data, label it as user-provided and do not infer personal constraints.

## Conclusion Gates

Use research language such as tradable setup, conditional setup, monitor closely, event watch, risk too high, evidence-gap, plan violated, thesis intact, thesis impaired, thesis broken, timing error, or execution error.

Do not give a strong tradable setup label unless these are satisfied:

- The instrument, direction of thesis, time horizon, and current or reference price/date are explicit.
- The research basis is tied to at least one market, sector, company, catalyst, or portfolio input.
- Entry trigger, invalidation condition, and review window are defined.
- Event, liquidity, volatility, and market-regime risks are checked or explicitly marked unavailable.
- Risk is framed as conditional risk units or review limits, not personal allocation.

If any gate fails, downgrade to conditional setup, monitor closely, or evidence-gap and state the missing evidence.

## Data Freshness Protocol

Do not use a price, volatility, liquidity, event, or regime data point unless its source date is known. Record:

- `as_of`: the market date, event date, reporting period, or portfolio date.
- `published_at`: when the source published it, if available.
- `retrieved_at`: when you fetched or viewed it.

For price-sensitive plans, current price, key levels, volatility, and event dates must be dated. If current data is unavailable, avoid precise trigger-price language and use evidence-based conditional triggers instead.

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
