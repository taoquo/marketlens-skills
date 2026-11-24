# Review And Calibration

Use this file to review a draft before publication and to review whether prior MarketLens
scorecards and research labels worked as intended.

## Purpose

Review turns a research framework into a learning loop. It should identify whether the original conclusion was right for the right reason, right for the wrong reason, early, late, or wrong.

This process is for research calibration only. It does not create a mechanical trading system.

## Separation Of Duties

The review gate is only independent if the role that judges is not the role that wrote the
draft. Run the following as distinct passes, even when one model performs all of them.

| Pass | May do | Must not do | Output |
|---|---|---|---|
| Author | Build the analysis, select the label, write the draft | Approve its own draft | Draft with source-pool IDs |
| Reviewer | Apply the six dimensions and the red-team pass | Rewrite, add facts, or change the label | `PASS` or `REVISE`, with blocking items |
| Reviser | Fix blocking items, apply the label the reviewer requires, and add cited evidence | Change the thesis or relabel on its own authority, or introduce unsourced facts | Revised draft plus a response to every item |
| Publisher | Format, check links, units, periods, block order, and the disclaimer | Change content or conclusions | Final output |

Rules:

- The reviewer receives the draft, the rubric, the source pool, and the required blocks. It
  does not receive the author's rationale or defence. If the host supports subagents, run the
  reviewer in a fresh context.
- A `PASS` still states the strongest remaining objection and the residual risk.
- The reviser answers every blocking item as fixed or not fixed with a reason. It applies a
  required downgrade or cap, but does not relabel on its own authority. An unresolved item is
  capped and recorded under `## Confidence And Limits` or `## What Would Change The View`.
- The publisher does not repair a substantive defect by editing prose. A content defect goes
  back to the reviewer and reviser.
- Do not merge review and revision into one step. The separation is what stops a draft from
  passing because its author can explain it.

## Pre-Publication Review

Run this gate before a research output is presented as complete. It checks content, not
structure; `scripts/validate_skills.py` already checks frontmatter, routing, output blocks,
versions, and example coverage.

Review the draft against six dimensions:

| Dimension | Required check |
|---|---|
| Source sufficiency | Every decisive claim has at least one Tier 1 or Tier 2 source, or is explicitly labelled as an estimate or opinion |
| Factual accuracy | The core figure check was run; number, unit, period, currency, and accounting basis agree with the source |
| Balance | The main counter-case, alternative explanation, and failure boundary are stated; a label stronger than `hold/watch` has passed the red-team pass below |
| Depth | The conclusion rests on a mechanism, dated evidence, and a falsifiable condition; `## What Would Change The View` uses measurable triggers |
| Structure | The output uses the relevant layer of the decision chain and does not let a downstream read outrun its inputs |
| Format | The six required output blocks, three timestamps, freshness grades, and exact disclaimer are present |

Return one of two verdicts:

- `PASS`: no blocking issue. Non-blocking suggestions may be listed separately.
- `REVISE`: at least one blocking issue. Each item names the location, the defect, and the
  required fix.

Blocking conditions are limited to:

- A decisive claim has no Tier 1 or Tier 2 source and is not labelled as an estimate or opinion.
- The core figure check is missing, or a unit, period, currency, or accounting basis conflicts
  with the source.
- A conclusion gate or chain constraint failed, but the label was not capped.
- The label conflicts with `scoring-standard.md`, including an averaged or ungrounded
  `hold/watch`.
- The exact disclaimer is missing or rewritten.
- A label stronger than `hold/watch` does not name the strongest opposing case, or that case
  defeats the binding constraint but the label was not changed.
- `## What Would Change The View` has no measurable trigger, or no trigger tests the binding
  constraint.

Allow at most one revision round for a single-skill output and two for a multi-skill report.
If blocking issues remain after the limit, publish only with the conclusion capped at
`monitor closely` or `evidence-gap` when a research label is used; otherwise mark the
conclusion provisional and name the missing evidence. Record the residual issues under
`## Confidence And Limits` or `## What Would Change The View`. Do not add a new mandatory
output block for this gate.

This gate is about the baseline, not the reviewer's taste. Do not return `REVISE` for a
stylistic preference when the evidence and structure hold.

## Red-Team Pass

Run this pass as part of the pre-publication review when the draft carries a label stronger
than `hold/watch` (`add-candidate watch`, `high-priority watch`, `trim-review`,
`exit-review`, `avoid`) or when the conclusion depends on one dated catalyst. A bearish label
runs the symmetric bull case.

1. Write 3-5 numbered objections to the conclusion. Each names the mechanism, the layer it
   attacks (regime, sector, company, valuation, catalyst, or portfolio), and the source-pool
   ID or locator that supports it.
2. Rank them. Name the single strongest objection and state whether it defeats the binding
   constraint named in the label.
3. If it does, downgrade one step or use `evidence-gap`; do not keep the label because the
   rest of the evidence is supportive. If it does not, state why it fails, is already priced,
   or is covered by a named trigger.
4. Promote the strongest surviving objection into `## What Would Change The View` or
   `## Red Flags`.
5. Keep the result to a short paragraph. Do not add a new mandatory output block.

The pass is deliberately adversarial. It is not a request for a balanced summary, and it is
not satisfied by restating the existing red flags.

## Review Cadence

Use the shortest cadence that matches the thesis:

| Setup | Review window |
|---|---|
| Event catalyst | Pre-event, immediately post-event, and after the first revision window |
| Earnings or guidance | After results, after call transcript, and after estimate revisions settle |
| Market regime | Weekly or when liquidity, FX, rates, or positioning indicators move materially |
| Industry cycle | Monthly, quarterly, or after key demand/supply data |
| Portfolio risk | After major price moves, new disclosures, or regime changes |

For standardized calibration, record 1-week, 1-month, and 3-month outcomes when market data is available.

## Review Record

Use this structure:

| Field | Required content |
|---|---|
| Original date | Date of the score or label |
| Scope | Company, event, industry, regime, or portfolio |
| Original label | Research label used at the time |
| Original score | Scorecard total or axis score, if applicable |
| Key evidence | Source-pool IDs, sources, and dates that drove the conclusion |
| Key assumption | The assumption that mattered most |
| Red flags | Red flags known at the time |
| 1-week result | Price, event, data, or thesis result |
| 1-month result | Price, event, data, or thesis result |
| 3-month result | Price, event, data, or thesis result |
| Error source | Fundamental, valuation, timing, market regime, data quality, event read, or portfolio correlation |
| Calibration action | Keep, tighten, loosen, add red flag, or revise scoring language |

## Research Log

A Codex skill has no memory between sessions. The cadence and record above only
work if the original call was written to a file, so persistence is part of the
workflow rather than an optional extra.

Write each new call to an append-only log in the current working directory:

| Scope | Path |
|---|---|
| Company, stock, or trade plan | `research-log/equity/TICKER.md` |
| Sector or industry | `research-log/sector/industry-slug.md` |
| Market regime | `research-log/regime/market.md` |
| Portfolio or watchlist | `research-log/portfolio/name.md` |
| Event or catalyst | `research-log/equity/TICKER.md`, in the same entry as the thesis it tests |

Rules:

- Ask once before creating `research-log/` the first time. Never write outside the working directory.
- One entry per call. Head it with the ISO date, the skill name, and the research label, then record the fields from `Review Record`.
- Mark each entry `Status: open` until a review closes it, then `Status: reviewed`.
- The original claim lines are immutable. Later results and corrections are appended to the same entry under a `Results` heading, with their own dates.
- A correction that changes the label is a new entry that cites the original date. Do not edit the earlier label.

Entry skeleton:

```markdown
### 2026-08-16 equity-research high-priority watch
Status: open
- Scope:
- Original score:
- Key evidence:
- Key assumption:
- Red flags:
- Invalidation condition:

#### Results
- 2026-08-23 (1w):
```

When a review is requested and no log entry exists, say so plainly. Do not
reconstruct a prior call from memory or from the current price. Offer to record
the present call as the first entry instead, and state that calibration starts
from this date.

If the user does not want files written, ask them to paste the earlier output and
label the review as unverified history.

## Thesis Decay

A thesis has a shelf life. Confidence recorded at the original date is not
confidence today, because the evidence behind it aged while the unverified
assumptions stayed unverified. Without an explicit decay rule, a stale call keeps
its original label indefinitely, which is the most common way a research framework
quietly stops working.

Apply this at every review, and whenever an open log entry is reused as an input.

| Condition at review | Effect on the earlier label |
|---|---|
| Expected catalyst window passed with no confirming evidence | Downgrade one step and record a timing error candidate |
| Two consecutive review windows with no new primary evidence | Cap at `monitor closely` regardless of the original label |
| The key assumption is still unverified after the period in which it should have been observable | Move the assumption into `evidence-gap` and cap the label |
| Price moved materially toward the thesis while fundamental evidence did not follow | Reduce, do not raise, confidence. Price is not confirmation |
| The price now implies a more demanding assumption than at the original date | Re-solve the implied variable. A thesis that was undemanding at entry can become demanding without any news |
| A new reporting period is available and the quality screens were not re-run | Treat the earnings-quality read as expired and re-compute before reusing the label |
| Price moved materially against the thesis with no new information | Hold the label but re-check the invalidation condition; do not widen it |
| A new red flag appeared after the original date | Re-run the red-flag overrides in `scoring-standard.md` before reusing the label |
| The regime layer behind the call is more than one review window old | Treat regime as neutral rather than supportive |

Rules:

- Decay is automatic. A label that has not been reconfirmed is not intact by default.
- Never re-derive confidence from the current price. Confirmation must come from the evidence the original thesis named.
- An open log entry older than its own review window cannot serve as a Tier 1 input to a new call. Cite it as a dated prior view and refresh the inputs that matter.
- Record the decay action in the entry `Results` section so the review history shows when confidence was reduced and why.

## Error Attribution

Separate these error types:

- Fundamental error: revenue, margin, cash flow, balance sheet, or competitive thesis was wrong.
- Valuation error: business view was right, but expected multiple or margin of safety was wrong.
- Implied-expectation error: the thesis was correct but the price already contained it, so being right produced no return. See `implied-expectations.md`.
- Earnings-quality error: the reported base was overstated, so the multiple was measured against a number that did not repeat. See `earnings-quality-screens.md`.
- Capital-allocation error: the operating thesis held, but reinvestment, acquisitions, buyback timing, or issuance moved value away from shareholders. See `capital-allocation-record.md`.
- Timing error: direction was right, but catalyst or market window was too early or too late.
- Market-regime error: liquidity, rates, FX, volatility, or positioning dominated the thesis.
- Data-quality error: source was stale, incomplete, secondary, or misread.
- Event-pricing error: the event mattered but was already priced, crowded, or had poor implied-move setup.
- Portfolio-correlation error: names were more correlated in stress than the research assumed.
- Base-rate error: the reference class was wrong, too small, or overridden by case detail. See `base-rates.md`.
- Credit or funding error: the equity thesis was reasonable but a maturity, covenant, or issuance-window constraint decided the outcome.
- Decay error: the conclusion was correct at the original date but was reused after its evidence had aged.

## Calibration Rules

- Do not change a scorecard because of one noisy outcome.
- Tighten a rule when the same failure repeats across comparable cases.
- Add a red flag when a risk repeatedly overrides high total scores.
- Lower confidence standards when evidence gaps were visible at the original date.
- Keep useful false negatives visible; missed opportunities can reveal overly strict gates.

## Output Template

```markdown
## Review Summary
[Original label, result, and whether the thesis was right for the right reason.]

## Outcome Table
| Horizon | Result | Evidence | Read-Through |
|---|---|---|---|

## Error Attribution
[Primary and secondary error source.]

## Calibration Action
[Keep, tighten, loosen, add red flag, or revise scoring language.]
```
