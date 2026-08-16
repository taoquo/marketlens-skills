# Review And Calibration

Use this file to review whether prior MarketLens scorecards and research labels worked as intended.

## Purpose

Review turns a research framework into a learning loop. It should identify whether the original conclusion was right for the right reason, right for the wrong reason, early, late, or wrong.

This process is for research calibration only. It does not create a mechanical trading system.

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
| Key evidence | Sources and dates that drove the conclusion |
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

## Error Attribution

Separate these error types:

- Fundamental error: revenue, margin, cash flow, balance sheet, or competitive thesis was wrong.
- Valuation error: business view was right, but expected multiple or margin of safety was wrong.
- Timing error: direction was right, but catalyst or market window was too early or too late.
- Market-regime error: liquidity, rates, FX, volatility, or positioning dominated the thesis.
- Data-quality error: source was stale, incomplete, secondary, or misread.
- Event-pricing error: the event mattered but was already priced, crowded, or had poor implied-move setup.
- Portfolio-correlation error: names were more correlated in stress than the research assumed.

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
