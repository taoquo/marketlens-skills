---
name: catalyst-event-monitor
description: Use when a user asks which upcoming public-market events matter, how to rank catalysts, what expectations are priced in, how an event could move a stock/sector, what data to watch before/after earnings, guidance, approvals, policy decisions, buybacks, unlocks, litigation, M&A, investor days, or whether a completed event strengthened, delayed, impaired, broke, or left neutral an investment thesis.
license: MIT
metadata:
  version: 0.10
---

# Catalyst Event Monitor

## Core Rule

Shared operating rules are in `../references/skill-contract.md`: public-market research only, no personalized investment advice, dated and sourced evidence, confidence and limits, and the exact disclaimer. Apply them to every output.

Separate event importance from whether the event is tradable. An event can be material to the thesis and still offer no usable setup.

## Skill Boundary

Use this skill for dated catalysts, event materiality, expectation gaps, market-implied pricing, scenario paths, and post-event thesis updates. For anything outside that scope, route through `../references/skill-routing.md`.

## Mode Selection

Choose the lightest mode that answers the user:

| User intent | Mode | Minimum input | Output depth |
|---|---|---|---|
| "What events matter in the next 1-12 weeks?" | `event-calendar` | Ticker or scope, plus a stated current date | Dated event list, catalyst score, source, expected impact |
| "Which event is worth tracking?" | `catalyst-priority` | Two or more candidate events with sourced dates | Scorecard using certainty, impact, expectation gap, pricing, crowding |
| "Will this event change the thesis?" | `catalyst-analysis` | The event, its source and date, and the thesis it is tested against | Event mechanism, market pricing, expectation gap, valuation-anchor impact |
| "What are the scenarios before/after the event?" | `scenario-tree` | The event date plus one dated pricing or expectation input | Base/upside/downside paths, price reaction path, evidence to watch |
| "What changed after the event?" | `post-event-review` | The actual outcome, its source, and the pre-event expectation | Actual vs expected, thesis status, next watch items |
| Broad or ambiguous event request | Hybrid | Ticker or scope | Start with event calendar, then analyze the highest-impact events |

If no event date can be sourced, do not build a scenario tree or trade setup. Report the calendar gap and what disclosure would fill it.

## Reference Loading

Read only the references needed:

- For event categories and materiality tests, read `references/event-taxonomy.md`.
- For source priority, freshness TTL, and cross-check rules, read `references/data-sources.md`.
- For catalyst priority scoring, market pricing, pre-event price action, and crowding, read `references/market-pricing.md`.
- For consensus view, variant view, implied move, risk/reward read, invalidating evidence, and post-event trading window, read `references/trade-setup.md`.
- For expectation gaps, scenario trees, event reaction paths, and valuation-anchor impact, read `references/scenario-framework.md`.
- For post-event review and thesis status updates, read `references/post-event-review.md`.
- For industry-specific event checklists, read `references/sector-event-checklists.md`.
- For the shared operating, evidence, gate, freshness, and output contract, read `../references/skill-contract.md`.
- Required shared files: `../references/scoring-standard.md`, `../references/data-discipline.md`, `../references/skill-routing.md`, and `../references/review-and-calibration.md`.
- For the reference class behind any scenario probability, approval rate, deal-completion rate, or post-event drift claim, read `../references/base-rates.md`.
- For crowded shorts, squeeze conditions, and how an event can support a negative thesis, read `../references/short-and-relative-value.md`.
- For refinancing, covenant, placement, or rating-action events, read `../references/credit-and-cross-asset.md`.
- For whether the pre-event price already implies the outcome the event would deliver, read `../references/implied-expectations.md`.
- For earnings events where the beat or miss may be accrual-driven rather than operational, read `../references/earnings-quality-screens.md`.
- For buyback, dividend, equity-raise, or M&A events, read `../references/capital-allocation-record.md` and price the announcement against the company own allocation record rather than its headline size.

## Evidence Standard

Tier definitions and the decisive-claim rule are in `../references/data-discipline.md` and `../references/skill-contract.md`. Domain sources:

| Tier | Sources | Use |
|---|---|---|
| Tier 1 | Company filings, official announcements, exchange disclosures, regulator notices, court filings, official event pages | Confirmed event date, terms, guidance, approvals, litigation, lockups |
| Tier 2 | Company IR calendars, earnings call transcripts, official industry/regulator data, exchange calendars | Event context, watch data, historical cadence |
| Tier 3 | Financial platforms, media, broker notes, event databases, consensus datasets | Context only; never sole basis for a decisive event conclusion |

## Conclusion Gates

Map the catalyst and post-event read to a shared label using the `Label Layering` table in `../references/scoring-standard.md`, and apply the shared gate rules in `../references/skill-contract.md`. Do not present personalized buy/sell advice, exact allocation instructions, or transaction-prescriptive event trades.

Domain-specific gates. Do not give a strong event conclusion unless these are satisfied:

- Event date or expected timing is stated, or the uncertainty is explicit.
- Event source is cited and classified as confirmed, expected, rumored, or conditional.
- Pre-event expectation is separated into consensus expectation, market-implied expectation, and variant perception where data allows.
- Market pricing is checked: pre-event price action, valuation move, implied move or volatility context when available, short interest/borrow cost where relevant, and estimate revisions.
- The mechanism is explicit: revenue, margin, cash flow, valuation multiple, discount rate, balance sheet, policy access, legal liability, or sentiment.
- At least one post-event data point is defined in advance for judging whether the event strengthened, stayed neutral, delayed, impaired, broke, or triggered a crowded unwind in the thesis.

If any gate fails, downgrade to an event-watch conclusion, state what evidence is missing, and apply the downgrade rule in `../references/skill-contract.md`.

An important event is not automatically an attractive setup. If the expectation gap is unclear, implied move is already demanding, crowding is extreme, or downside is hard to bound, use `event watch` or `monitor closely`.

## Data Freshness Protocol

Apply the timestamp, freshness, and core-figure rules in `../references/data-discipline.md` and `../references/skill-contract.md`. Domain additions:

Catalyst-specific additions:

- Classify every event date as confirmed, expected, rumored, or conditional, and keep that status next to the date.
- For every material event, record time zone and release window when available: pre-market, regular session, post-market, exact clock time, regulatory deadline, exchange effective date, or data-release time.
- An `as_of` in the future is normal for an event date and must not be graded `Stale`. Grade the freshness of the source that establishes the date, not the date itself.

Degrade conclusions as follows:

| Missing or stale item | Required handling |
|---|---|
| Event date is unconfirmed or media-only | Use `event watch`, no scenario tree with dated price paths |
| Release window or time zone is unknown | Mark it unknown, no pre-market or post-market reaction language |
| Consensus expectation is unavailable or stale | State the expectation gap as unknown, no variant-perception claim |
| Implied move, options, or volatility data is unavailable | Describe pricing qualitatively, no implied-move arithmetic |
| Crowding, short interest, or borrow data is unavailable | Do not rule out a crowded unwind; state it as unmeasured |
| Post-event data point was not defined in advance | Do not declare the thesis strengthened or broken; reopen the review |
| Event calendar coverage is incomplete | Add a pending-disclosure caveat and state the window searched |

## Workflow

1. Identify the company, ticker, sector, market, time window, user intent, and current date.
2. Build a 1-12 week event calendar with source, date confidence, time zone/window, and event type.
3. Score events for timing certainty, financial impact, expectation gap, market pricing, crowding, and total priority.
4. Classify each event as hard catalyst, soft catalyst, narrative catalyst, or noise.
5. Identify the expectation gap: consensus expectation, market-implied expectation, and variant perception.
6. Analyze market pricing and pre-event price behavior before judging risk/reward.
7. Build the trade setup when relevant: consensus view, variant view, market-implied expectation, implied move, upside, downside, risk/reward read, invalidating evidence, and review window.
8. Map the event mechanism to valuation anchor, financial metric, risk premium, or thesis variable.
9. Build a scenario tree for material events: upside, base, downside, watch data, thesis read-through, and price reaction path.
10. Define pre-event data to monitor and post-event review criteria before forming a conclusion.
11. After the event, compare actual data against pre-event expectations and classify thesis status as strengthened, neutral, delayed, impaired, broken, crowded unwind, or inconclusive.

## Output Template

```markdown
# [Company / Sector] Catalyst Event Monitor

## Conclusion
[Most important upcoming event, expected thesis impact, confidence, and why.]

## Event Calendar
| Event | Date / Window | Time Zone | Status | Type | Source | Watch Data |
|---|---|---|---|---|---|---|

## Catalyst Scorecard
| Event | Timing Certainty | Financial Impact | Expectation Gap | Market Pricing | Crowding | Score |
|---|---:|---:|---:|---:|---:|---:|

## Score Summary
| Dimension | Score | Evidence | Confidence | Comment |
|---|---:|---|---|---|

## Red Flags
[Timing uncertainty, weak financial impact, unclear expectation gap, extreme crowding, demanding implied move, or missing data that cannot be offset by total score.]

## Event Materiality
[Which events can change revenue, margin, cash flow, valuation anchor, policy access, legal liability, or sentiment.]

## Expectation Gap
[Consensus expectation, market-implied expectation, variant perception, and what would surprise the market.]

## Market Pricing
[Pre-event relative performance, valuation move, implied move/volatility context if available, short interest/borrow cost where relevant, and estimate revisions.]

## Trade Setup
| Item | Read |
|---|---|
| Consensus View |  |
| Variant View |  |
| Market-Implied Expectation |  |
| Implied Move / Volatility |  |
| Upside Scenario |  |
| Downside Scenario |  |
| Risk/Reward Read |  |
| Invalidating Evidence |  |
| Post-Event Review Window |  |

## Scenario Tree
| Scenario | What Happens | Evidence To Watch | Thesis Read-Through | Price Reaction Path | Post-Event Decision Framework |
|---|---|---|---|---|---|

## Event Reaction Framework
[Beat and raise, beat but no raise, miss but guide up, sell-the-news, squeeze, de-risking, or no real thesis change.]

## Pre-Event Watch Data
[3-5 indicators to monitor before the event.]

## Post-Event Review Plan
[How to classify the result as strengthened, neutral, delayed, impaired, broken, crowded unwind, or inconclusive.]

## Decision Impact
[How the event score and trade setup affect the label: priority catalyst, monitor closely, event watch, evidence-gap, or thesis status.]

## What Would Change The View
[Concrete pre-event or post-event evidence that would upgrade, downgrade, or invalidate the setup.]

## Confidence And Limits
[Confidence level, missing dates, stale data, rumor risk, unsupported claims avoided.]

## Data Freshness
| Data | Value | As of | Published | Retrieved | Source | Freshness |
|---|---:|---|---|---|---|---|

## Evidence Sources
| Source | Date | Type | Supports |
|---|---|---|---|

## Disclaimer
This is public-market research for reference only and does not constitute investment advice.
```
