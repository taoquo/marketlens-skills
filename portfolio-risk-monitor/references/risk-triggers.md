# Risk Triggers

Use this file to identify drawdown scenarios and monitoring variables. Apply `../../references/scoring-standard.md` for red-flag and confidence discipline.

## Risk Driver Types

| Risk Driver | Typical Evidence |
|---|---|
| Valuation | Multiple expansion, low earnings yield, rate sensitivity, high expectations |
| Earnings | Margin pressure, guidance cuts, negative revisions, customer weakness |
| Policy | Regulation, export control, antitrust, reimbursement, subsidy rollback |
| FX / rates | USD strength, CNH pressure, funding cost, duration sensitivity |
| Liquidity | Market regime stress, widening spreads, low float, forced selling |
| Crowding | High ownership overlap, momentum unwind, short squeeze risk, retail chase |
| Balance sheet | Refinancing wall, leverage, working capital stress, dilution |
| Governance | Related-party issues, pledges, insider selling, disclosure quality |
| Correlation | Same customer, supplier, commodity, geography, or factor exposure |
| Stress correlation | Funding, policy, or risk-off shocks that make normally separate holdings move together |

## Drawdown Scenario Table

Use this structure:

| Scenario | Affected Names | Transmission Channel | Leading Indicator | Severity | Confidence |
|---|---|---|---|---|---|

Severity is qualitative: low, medium, high. Confidence depends on data quality and freshness.

Add expected correlation behavior when stress could make hidden overlap dominate stock-specific drivers.

## Trigger Examples

- Valuation: multiple expands while revisions flatten.
- Earnings: revenue beats but margins or cash conversion deteriorate.
- Policy: official rule changes eligible market, pricing, or compliance cost.
- FX/rates: currency move pressures revenue translation or funding cost.
- Liquidity: risk regime shifts from supportive to fragile.
- Crowding: high-beta names fall together despite company-specific news being unchanged.
- Balance sheet: refinancing terms worsen or dilution risk rises.

## Kill Conditions

A portfolio-level risk thesis is strengthened when:

- Multiple holdings fail on the same driver.
- A shared macro or policy variable moves against the cluster.
- Correlations rise during stress.
- Liquidity falls when downside risk rises.

It is weakened when:

- Exposure is smaller than assumed.
- Names have different drivers after deeper review.
- Offsetting catalysts or hedges exist and are evidenced.
