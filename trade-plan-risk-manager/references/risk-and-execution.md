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

## Tradability Thresholds

"Liquid enough" is not a check. Without a threshold, a thin name passes the
execution checklist on a qualitative nod, and thin liquidity is the single most
reliable way for a good thesis to produce a bad outcome. Judge liquidity against
the intended horizon, and state the measured values.

| Band | Characteristics | Highest allowed label |
|---|---|---|
| Deep | Wide institutional participation, tight spread, options and borrow readily available, no venue constraint | `tradable setup` if all other gates pass |
| Adequate | Consistent daily turnover, spread that is small relative to the planned stop distance, occasional gap behaviour | `tradable setup`, with slippage and gap risk stated explicitly |
| Thin | Turnover concentrated in short bursts, spread material relative to the stop distance, limited or expensive borrow, block-dependent | `conditional setup` at best, and no precise trigger levels |
| Impaired | Frequent limit moves or halts, suspension risk, restricted access channel, no borrow, or delisting and going-private risk | `risk too high`, regardless of thesis quality |

Read these against the horizon:

| Check | How to judge it |
|---|---|
| Turnover versus horizon | Compare average daily value traded with the size the horizon implies. A multi-day exit requirement is a thin-band signal |
| Spread versus stop distance | If the round-trip spread is a meaningful fraction of the distance to invalidation, the stop is not implementable as stated |
| Free float versus reported market cap | State-owned, founder-held, strategic, and locked-up shares reduce tradable float. Judge on float, not market cap |
| Gap behaviour | Frequency of overnight gaps larger than the planned risk unit over recent history |
| Venue constraints | A-share limit moves and suspensions, Hong Kong tick and lot rules, Stock Connect eligibility, ADR liquidity versus the local line |
| Borrow, for any short-side leg | Availability, cost, and recall risk per `../../references/short-and-relative-value.md` |

Rules:

- If any liquidity input is unavailable, state it as unmeasured and cap the setup at `conditional setup`. An unmeasured liquidity profile is not an adequate one.
- Thresholds are relative to the horizon and the venue, so state the measured values rather than only the band.
- When the same view is available through two lines, such as an ADR and its local listing, name the liquidity difference without recommending a venue.

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
| Credit and funding inputs for a levered name | Latest filing, plus the latest issuance or rating action | Treat the funding path as unstated and cap at `conditional setup`, per `../../references/credit-and-cross-asset.md` |
| Portfolio overlap | User-provided as of the plan date | State overlap as unknown; do not assume the trade is additive |

Record the provenance of every research input: a prior MarketLens output with its
date, a user-provided view, or an assumption made in this run. An assumed input
cannot support a `tradable setup` label.

## Execution Checklist

Before calling a setup tradable, verify:

- The instrument is identifiable and its liquidity band is measured, per `Tradability Thresholds`.
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
- "The short leg carries borrow cost and recall risk that the long leg does not."
- "This expression removes sector beta but adds correlation-breakdown risk."

Do not say:

- "Buy now."
- "Sell at this stop."
- "Use 10% of your portfolio."
- "Use 3x leverage."
- "Open this exact option spread."
