# Red Flags

Use red flags to reduce confidence, require more evidence, or define kill conditions. A red flag is not automatically bearish; state whether it is confirmed, suspected, or only a watch item.

## Financial Quality

Every item below has a computed screen with a threshold in
`../../references/earnings-quality-screens.md`. Measure it there rather than judging
it by eye, then bring the result back here to classify. A described concern and a
quantified breach are not the same evidence.

- Revenue grows faster than cash collection for multiple periods.
- Receivables, contract assets, or inventory rise materially faster than sales.
- Free cash flow persistently trails accounting profit without a clear reinvestment reason.
- Large capitalized development costs, supplier financing, factoring, or off-balance-sheet obligations.
- Frequent one-off gains, subsidy income, fair-value gains, or asset disposals support profit.
- Gross margin or segment margin changes without volume, price, mix, or cost explanation.

## Governance And Ownership

- Related-party transactions, asset injections, connected acquisitions, or loans to affiliates.
- Auditor resignation, qualified opinion, delayed filing, internal-control weakness, or restatement.
- Heavy insider selling, pledged shares, forced-sale risk, or controlling-shareholder liquidity stress.
- Management incentives tied to vanity revenue or adjusted earnings while share count rises.

## Capital Allocation And Dilution

Every item below has a computed screen with a threshold in
`../../references/capital-allocation-record.md`. Build the sources-and-uses ledger
first, then measure the item there rather than judging strategic fit by eye. An
acquisition with an unclear rationale and one with a measured post-deal ROIC decline
are not the same evidence.

- Buybacks that only offset SBC or repeated share issuance.
- Hong Kong placements, rights issues, convertible bonds, or warrants at large discounts.
- A-share private placements, incentive plans, or unlock schedules that may pressure supply.
- M&A with unclear strategic fit, high goodwill, or aggressive synergy assumptions.
- Reinvestment continuing at scale while the incremental return on it sits below the cost of capital.
- Repeated failure to meet stated guidance, project timelines, or disclosed commitments.

## Market-Specific Checks

- Hong Kong: HKEXnews announcements, Disclosure of Interests changes, AH premium/discount, VIE/control structures, short-selling turnover, southbound concentration, and buyback cancellation rate.
- A-share: exchange inquiry letters and replies, CNINFO announcements, major shareholder pledges, restricted-share unlocks, government subsidies, non-recurring gains/losses, northbound flows, margin financing, and industry valuation percentile.
- US: SEC 8-Ks, S-3/S-8 issuance, Form 4 insider activity, short interest, SBC dilution, non-GAAP reconciliation, and guidance changes.

## Response Handling

- If a red flag affects the thesis, move it into kill conditions or monitoring triggers.
- If a red flag cannot be verified from primary sources, label it unverified and do not use it as a decisive claim.
- If several moderate red flags point in the same direction, lower confidence even if each item is individually explainable.

## Confirmation Status

Lowering confidence is the right response to a suspected red flag. It is the wrong
response to a confirmed one, because a confirmed flag is information about the
company rather than about the analysis. Classify each flag before deciding what it
does to the output.

| Status | Definition | Required response |
|---|---|---|
| Confirmed | Stated in a primary filing, auditor report, regulator action, or company disclosure | Becomes a kill condition or a stated negative thesis, not merely a confidence deduction |
| Suspected | Derived from a computed screen breach, a pattern across periods, or a credible secondary report | Becomes a named verification task with the specific document that would settle it |
| Watch | Structurally plausible but not yet visible in the data | Becomes a monitoring trigger with the release that would show it first |

For financial-quality flags, the aggregate read table in
`../../references/earnings-quality-screens.md` sets the status: two to three screen
breaches is `Watch`, four to six is `Suspected`, and seven or more is treated as a
quality failure until disproven. Do not assign a status to a financial-quality flag
without the breach count and its direction over time.

For capital-allocation flags, the aggregate read table in
`../../references/capital-allocation-record.md` sets the status the same way:
`adequate` is `Watch`, `value-leaking` is `Suspected`, and `destructive` is
treated as an allocation failure until disproven. Two exceptions are `Confirmed`
without further work, because the company states them itself: an unfulfilled
commitment in the A-share performance-of-undertakings section, and a funded project
disclosed as below its committed benefit.

A confirmed flag that keeps a name at `avoid` with no further work discards the
most useful output of the analysis. Route it as follows.

| Confirmed flag | Where it goes next |
|---|---|
| Accounting quality or disclosure failure | An accounting short thesis in `../../references/short-and-relative-value.md`, or `avoid only` if feasibility is unverified. Cite the screen breaches rather than the narrative |
| Refinancing, covenant, or runway limit | A funding read using `../../references/credit-and-cross-asset.md`, plus a dated maturity or covenant test |
| Structural demand loss or substitution | A structural-decline read, and a check of whether a peer is the other side of the same shift |
| Governance or capital-allocation leakage | A permanent quality discount in valuation sized by the allocation read in `../../references/capital-allocation-record.md`, and a governance short thesis only if it has a dated catalyst |
| Dilution or supply overhang | A dated supply event with a size estimate, feeding the trade-plan event-gap check |

Boundaries: a confirmed flag never becomes short-side language before the
feasibility checks in `../../references/short-and-relative-value.md` are run and
sourced. If borrow, float, or crowding data is unavailable, the read is `avoid
only`. Never present a short thesis as lower risk because the accounting evidence
is strong; timing risk and carry are independent of thesis quality.
