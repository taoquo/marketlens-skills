# Risk And Execution

Use this file to frame trade risk without giving personalized allocation or order instructions.

## Risk Unit

Risk unit language can be used only as a framework:

- Define one unit of planned risk as the distance from reference price to invalidation point, or the expected loss under the base adverse scenario.
- Express scenarios in R terms when possible: `+2R upside`, `-1R invalidation`, `gap risk could exceed planned R`.
- If the user has not provided risk tolerance, portfolio size, constraints, or liquidity needs, do not calculate personal position size.

## Risk Checks

| Risk | What to check |
|---|---|
| Volatility | ATR, realized volatility, implied volatility, or recent gap behavior if sourced |
| Liquidity | Average value traded, bid-ask spread, market cap, free float, suspension/limit risk |
| Event gap | Earnings, FDA/regulatory decision, policy decision, litigation, lockup, index change |
| Borrow / short | Borrow availability, borrow cost, short-sale rules, squeeze risk |
| Options | Implied move, IV rank/context, liquidity, spread, expiry fit, assignment risk |
| FX / rates | Currency mismatch, rates sensitivity, funding cost, carry unwind |
| Portfolio overlap | Existing same-factor, same-sector, same-catalyst, or same-currency exposure |

## Execution Checklist

Before calling a setup tradable, verify:

- The instrument is identifiable and liquid enough for the horizon.
- Current/reference price is dated.
- Event windows are known or marked unknown.
- Stop-error is based on thesis evidence, not only discomfort.
- Gap risk is not larger than the planned risk framework unless explicitly accepted as a research risk.
- Market regime does not directly invalidate the setup.
- Portfolio overlap is known or clearly unavailable.

## Language Boundary

Say:

- "Risk should be framed around the thesis invalidation level."
- "This belongs in conditional setup until liquidity and event timing are verified."
- "Gap risk may exceed the planned risk unit."

Do not say:

- "Buy now."
- "Sell at this stop."
- "Use 10% of your portfolio."
- "Use 3x leverage."
- "Open this exact option spread."
