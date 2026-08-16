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

## Input Freshness TTL

A plan is only as fresh as its weakest input. Grade each input using the five
freshness grades in `../../references/data-discipline.md` before labelling a setup.

| Input | Freshness target | If stale |
|---|---|---|
| Reference price, key levels | Latest completed trading session | No precise trigger levels; use conditional evidence triggers |
| Realized or implied volatility | Latest trading day | No volatility-scaled stop or R arithmetic |
| Liquidity, ADV, spread, free float | Latest trading day or latest disclosure | State execution risk as unmeasured |
| Event calendar for the horizon | Checked as of the plan date | Add an event-risk caveat; no time stop past the unchecked window |
| Market regime read | Within 1 week for tactical horizons, 1 month for multi-month horizons | Treat regime as neutral, not supportive; cap at `conditional setup` |
| Company or sector research basis | Latest reporting period, or the last dated MarketLens output | Cap at `conditional setup` and name the input to refresh |
| Borrow, short interest, options liquidity | Latest official or exchange release | Mark the constraint as unmeasured, no squeeze or spread claim |
| Portfolio overlap | User-provided as of the plan date | State overlap as unknown; do not assume the trade is additive |

Record the provenance of every research input: a prior MarketLens output with its
date, a user-provided view, or an assumption made in this run. An assumed input
cannot support a `tradable setup` label.

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
