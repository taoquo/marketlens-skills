# Post-Trade Review

Use this file to review completed or active trades against the original plan. The goal is process calibration, not blame or hindsight storytelling.

## Required Inputs

Ask for or reconstruct only what is available:

- Original thesis and date.
- Planned entry, invalidation, review triggers, and time horizon.
- Actual entry, exit or current status, and major decision timestamps.
- Market regime, sector move, catalyst outcome, and company news during the holding window.
- User notes or stated reason for deviations, if provided.

## Error Attribution

| Error type | Meaning |
|---|---|
| Thesis error | The core research driver was wrong or unsupported |
| Timing error | The thesis may be right, but entry/review window was poor |
| Risk framing error | Gap, volatility, liquidity, or concentration risk exceeded plan assumptions |
| Execution error | Actual behavior deviated from the plan without new evidence |
| Data-quality error | The decision used stale, missing, or wrong data |
| Regime error | Market environment changed or was misread |
| Catalyst error | Event probability, timing, or expectation gap was misjudged |

## Review Output

```markdown
## Post-Trade Review
| Item | Planned | Actual | Difference | Attribution |
|---|---|---|---|---|

## Process Score
| Dimension | Score | Evidence | Rule Update |
|---|---:|---|---|

## Rule Updates
[1-3 concrete rules to improve the next plan.]
```

## Rule Update Discipline

Good rule updates are specific and testable:

- "Do not hold the same risk unit through earnings unless implied move and downside scenario are reviewed."
- "Downgrade to conditional setup when current price is stale."
- "Require a time stop for catalyst theses without a fixed date."

Avoid vague updates such as "be more careful" or "trust conviction."
