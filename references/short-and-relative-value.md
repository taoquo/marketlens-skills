# Short And Relative Value

Every MarketLens framework so far reads one direction: a good thesis becomes a
watch label and a bad one becomes `avoid`. That leaves the most valuable output of
red-flag work on the floor. A confirmed accounting problem, a structural decline,
or an overearning cyclical is not merely a reason to skip a name; it is a distinct
research object with its own evidence bar. This file adds the short side and the
relative-value pair as first-class reads, and keeps both inside the existing
research-language boundary.

## Short Thesis Types

| Type | Core claim | Evidence bar | Typical failure |
|---|---|---|---|
| Accounting or disclosure | Reported numbers do not represent economics | Primary filings, restatements, auditor actions, cash versus accrual reconciliation. Media-only claims are not enough | Timeline is open-ended; the market tolerates it for years |
| Structural decline | The end market is shrinking or being substituted | Volume, share, pricing, and substitution data across several periods | Cheap valuation plus a cyclical bounce triggers a violent rerating |
| Overearning cyclical | Current margins are far above a sustainable level | Utilization, capacity additions, spread and price data, prior cycle troughs | Early by one full cycle leg |
| Balance-sheet or funding | Refinancing, covenant, or liquidity failure is likely before recovery | Maturity ladder, covenant headroom, issuance window, cost of new debt. See `credit-and-cross-asset.md` | A rescue placement, asset sale, or policy support resets the clock |
| Competitive displacement | A specific competitor or technology is taking the profit pool | Wins and losses, pricing, order or backlog shift, customer confirmation | Incumbent adapts, or the disruptor cannot fund the fight |
| Governance or capital allocation | Value leaks to insiders or into value-destroying deals | Related-party transactions, dilution history, pledges, incentive design | Governance events are slow and can be repriced by one reform |
| Valuation only | The multiple is too high | Almost never sufficient on its own | Momentum, index flow, and squeeze risk dominate |

A valuation-only short is the weakest type and must not carry a stronger label
than `short watch`. State the type explicitly; a short built on two weakly
evidenced types is not equivalent to one well-evidenced type.

## Feasibility Checks

A short thesis that cannot be held is not a thesis. Check these before any
short-side language, and mark each as sourced or unmeasured.

| Check | What to read | Why it can end the trade |
|---|---|---|
| Borrow availability | Lendable supply, utilization rate, hard-to-borrow status | No borrow means the view is only an avoid, not a short |
| Borrow cost | Annualized fee, and its trend | A high fee sets a hard deadline on the thesis |
| Recall risk | Concentration of the lending pool, index and ETF ownership | A recall forces a close at the worst moment |
| Short interest and days to cover | Short interest as a share of float, and average daily volume | Crowding converts good analysis into squeeze exposure |
| Float and liquidity | Free float, ADV, spread, limit and suspension rules | Thin float plus crowded shorts is the classic squeeze setup |
| Carry | Dividend obligation, borrow fee, financing cost | Carry is a certain cost against an uncertain gain |
| Corporate action risk | Buyback authority and pace, takeover plausibility, index inclusion, placement or rights issue | Each can produce a large adverse move independent of the thesis |
| Venue rules | Hong Kong designated securities list and tick rules, A-share securities-lending scope and limits, US locate requirements, any market-wide restriction | Local rules can make the position impossible or one-sided |
| Catalyst window | The dated evidence that would confirm the thesis | Without one, cost accrues while the thesis waits |

## Asymmetry Rules

- Loss on a short is unbounded while gain is capped at the equity value. A short needs a tighter invalidation than a long with the same conviction.
- Carry means a short thesis decays with time. State the cost of being right late.
- A short into a strong regime, a rising index, or a policy-support cycle needs name-specific evidence that is independent of market direction.
- Do not net a short read against a long read on the same driver and call the pair balanced. Both legs need their own evidence.

## Squeeze Conditions

Treat squeeze risk as a red flag when three or more of these hold: short interest
is high relative to float, days to cover is elevated, borrow is scarce or
expensive, free float is small, retail or options activity is elevated, a buyback
is active, or an index or takeover event is plausible in the horizon.

## Short-Side Reads

These are domain reads, not the shared labels. Map them through the `Label
Layering` table in `scoring-standard.md` before stating a stance.

| Read | Meaning |
|---|---|
| Short candidate | Thesis type is evidenced, feasibility is verified and sourced, a dated catalyst exists, and invalidation is concrete |
| Short watch | Thesis is credible but feasibility, timing, or evidence is incomplete |
| Crowded short | Thesis may be right, but positioning and borrow conditions make the expression unattractive |
| Not shortable | Thesis may be right, but borrow, venue rules, liquidity, or corporate-action risk blocks the expression |
| Avoid only | Enough to stay away, not enough to take the other side |

`Avoid only` is the correct read for most negative conclusions. Reaching for
`short candidate` without feasibility evidence is the main error this section
exists to prevent.

## Relative Value And Pairs

A pair is one position on one spread, not two positions. It is legitimate only
when the two legs share a driver and the thesis is about the difference.

| Pair type | Spread thesis | What must be verified |
|---|---|---|
| Quality versus laggard in one industry | Same demand driver, different execution or balance sheet | Both legs move on the same driver; the gap is not already at a historical extreme for a structural reason |
| Winner versus displaced | Share is transferring between two named companies | Direct evidence of transfer, not two separate stories |
| Stock versus sector or index hedge | Company-specific alpha with the sector risk removed | Beta and its stability, plus the tracking gap between the name and the hedge |
| Upstream versus downstream | Margin is shifting along the value chain | Pass-through evidence from `../sector-industry-research/references/value-chain-framework.md` |
| Dual-listed share classes | The same cash flow is priced differently across venues | Whether the classes are fungible, and whether the gap reflects tax, capital controls, liquidity, or governance rather than mispricing |
| Holdco versus listed subsidiary | The discount to sum-of-parts is too wide | Whether the discount can be closed at all, given control, tax, and history |

Constraints that make a spread structurally persistent rather than mispriced:

- A and H shares are not fungible. The AH gap can persist indefinitely and reflects capital controls, investor base, dividend withholding, and liquidity.
- ADRs are usually convertible, so a persistent ADR gap is more often a fee, tax, or borrow artifact than an opportunity.
- Holdco discounts often reflect a permanent control or tax structure. Require a named catalyst before treating one as a spread trade.
- A crowded spread carries the same unwind risk as a crowded direction.

For any pair, state the beta relationship, the correlation regime it relies on,
what breaks the spread rather than each leg, and the borrow and carry cost of the
short leg.

## Expression Comparison

The same view can be expressed several ways with materially different risk. Name
the risk differences so the reader can see them; do not select an instrument for
the user, size a position, or specify a structure.

| Expression | Risk characteristic | When the difference matters |
|---|---|---|
| Cash long | Loss bounded by the position; no time cost | Baseline expression |
| Cash short | Loss unbounded; borrow and dividend carry; recall and squeeze risk | Whenever a negative view is discussed as a position rather than an avoid |
| Pair or spread | Removes shared beta; adds correlation-breakdown risk and short-leg carry | When the thesis is about relative outcome, not direction |
| Sector or index hedge overlay | Reduces market beta; adds tracking error and hedge cost | When name-level conviction is high but regime risk is elevated |
| Defined-risk options | Loss capped at premium; adds time decay and implied-volatility path dependence | When an event has a known date and a demanding implied move; see `../catalyst-event-monitor/references/market-pricing.md` |
| Leveraged or margin exposure | Amplifies both directions; introduces forced-close risk | Only as a risk warning, never as a suggestion |

## Boundaries

- This file adds a research direction, not an execution service. No position size, no leverage, no specific option structure, no order instruction.
- If borrow, short interest, or float data is unavailable, the read cannot be stronger than `short watch` or `avoid only`.
- Never state a short thesis on a company without naming what would prove it wrong, and never present a short as lower risk than a long because the analysis is stronger.
