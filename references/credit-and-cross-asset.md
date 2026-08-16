# Credit And Cross-Asset

Equity is the junior claim. Credit reprices first, and it reprices on the same
facts. Use this file when a conclusion depends on funding, refinancing, leverage,
or market-wide risk appetite. Grade every input with the freshness rules in
`data-discipline.md`.

## Why This Is Not Optional

- A company can be operationally fine and still fail if the maturity wall lands before the thesis plays out.
- An index-level equity view without a credit-spread read is a view on half the risk appetite.
- Credit markets set both the discount rate and the survival constraint for the equity claim.

## Market-Level Credit Indicators

| Indicator | Definition | Interpretation boundary |
|---|---|---|
| IG spread | Investment-grade OAS over Treasuries | Widening from a low base matters more than the absolute level; a steady grind tighter is risk-appetite support |
| HY spread | High-yield OAS, plus CCC minus BB | HY leads equity drawdowns more reliably than VIX; CCC-BB widening signals dispersion, not only direction |
| Term premium | Long-yield decomposition, or 10s2s and 10s30s curve shape | A bear-steepener driven by term premium pressures long-duration equity even when growth data is fine |
| Real yield | 10-year TIPS yield or local real-rate proxy | Rising real yields compress long-duration multiples independently of earnings |
| Breakeven inflation | Nominal minus real yield at 5y, 10y, and 5y5y | Separates a nominal-rate move into growth, inflation, and premium components |
| Cross-currency basis | USD funding basis versus EUR, JPY, and CNH | Negative basis widening is offshore dollar scarcity, and it transmits to Hong Kong and EM equity |
| Bank credit conditions | Loan officer surveys, credit impulse, aggregate financing | Tightening lending standards lead capex and small-cap earnings by quarters |
| Issuance window | IG and HY primary issuance, China onshore and offshore issuance | A closed primary market is a hard constraint on levered business models |

Do not call risk appetite supportive when equity is strong and HY spreads are
widening. Name the divergence and cap confidence at Medium.

## Single-Name Credit Checks

Run these when leverage, capex intensity, or refinancing is part of the story.

| Check | What to read |
|---|---|
| Maturity ladder | Amount and date of each maturity for the next three years, and whether any lands before the thesis can play out |
| Cost of new debt | Coupon on the most recent issue or bank facility versus the weighted average cost of existing debt |
| Bond yield and spread | Secondary yield on bonds issued by the company; a bond at a distressed yield contradicts an equity re-rating thesis |
| Covenants | Leverage, interest-coverage, and asset-value tests, plus current headroom against each |
| Liquidity sources | Cash, undrawn revolver, committed facilities, expected FCF, and disposal proceeds |
| Rating trajectory | Rating, outlook, and watch status per agency; the outlook change usually precedes the action |
| Structural seniority | Where equity sits versus secured debt, opco and holdco structure, minority interests, perpetuals, preferred |
| Contingent claims | Guarantees, puts on JV stakes, earn-outs, pension deficits, lease liabilities |

## Credit-Equity Divergence

| Pattern | Read |
|---|---|
| Bonds sell off, equity holds | Credit sees a solvency or refinancing risk the equity story is ignoring. Treat as a red flag |
| Bonds rally, equity weak | Likely an equity-only issue: dilution, governance, competitive position, or index and flow pressure |
| Both weak, bonds worse | Balance-sheet led stress. Equity upside requires the funding path to be repaired first |
| Both weak, equity worse | An earnings or multiple problem rather than a survival problem |

State which market is more liquid before drawing a conclusion. For small issuers
with thin bond trading, treat a single bond print as Tier 3 evidence.

## Sector Sensitivity

| Sector type | Credit is a primary input because |
|---|---|
| Property, REIT, infrastructure | Asset values, LTV tests, and refinancing windows drive equity value more than current earnings |
| Banks, insurers, brokers | Funding cost, asset quality, and capital ratios are the business, not a constraint on it |
| Utilities, telecom, shipping, airlines | Capital intensity means cost of debt sets returns on new capacity |
| Biotech and pre-profit growth | Cash runway plus the equity issuance window decide survival and dilution |
| Highly levered cyclicals | Covenant headroom decides whether the cycle turn can be waited out |

For these sectors, an equity conclusion without a credit read is incomplete, not
merely less precise. Cap it at `monitor closely` until the funding path is stated.

## Handling And Boundaries

- If credit data is unavailable, say so and cap the label rather than assuming the balance sheet is fine.
- Never quote a CDS, bond yield, or spread level without a date and a venue.
- Credit work here supports an equity conclusion. This is not credit research, bond selection, or relative-value advice on debt instruments.
