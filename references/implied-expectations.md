# Implied Expectations

Forward valuation answers "what is it worth" and produces a number whose precision
far exceeds the precision of its inputs. Reverse valuation answers "what does this
price require" and produces a claim that can be checked against history. The second
question is the one a research process can actually resolve, because the market
price is the one input that is never wrong about itself.

Use this file whenever a valuation carries a conclusion. Grade every input with
`data-discipline.md`, and test every solved number against `base-rates.md`.

## Why Reverse The Question

- A forward DCF hides its conclusion inside WACC and terminal growth, where a 100bp change moves fair value more than any operating assumption. That makes it unfalsifiable.
- A reverse DCF fixes what is observable, accepts the market price, and solves for the operating assumption. The output is a statement about the world, not about the model.
- A solved assumption can be compared with the company own record and with the industry distribution. A fair value cannot.
- The same discipline works on multiples. A multiple is already an implied statement; it just has not been read out loud.

## Growth Value Share

Run this first. It needs no iteration, no forecast period, and no terminal
assumption, so it is the hardest step to manipulate.

```text
No-growth EV   = current NOPAT / WACC
Growth value   = current EV - no-growth EV
Growth share   = growth value / current EV
```

Build the EV bridge explicitly: market cap, plus net debt, plus lease liabilities,
plus minorities and preferred, less investments carried at equity and other
non-operating assets. State each line, because an EV assembled silently is the most
common source of a wrong implied number.

| Growth share of EV | What the price requires |
|---:|---|
| Below 30 percent | Most of the value is in cash flow that already exists |
| 30 to 60 percent | A normal growth company; the forecast matters but does not carry everything |
| 60 to 80 percent | The thesis is the growth path, not the current business |
| Above 80 percent | Current earnings are almost irrelevant to the price. Treat the valuation itself as a risk factor |

Report the WACC used and re-run at the ends of a defensible WACC range. A growth
share quoted without its discount rate is not a finding.

## Reverse DCF Procedure

1. Fix the observables: current revenue, current NOPAT margin, tax rate, diluted share count, and the EV bridge above.
2. Fix a WACC range rather than a point. State how the range was built and never present a single WACC as known.
3. Fix the terminal assumption to something defensible: terminal growth at or below long-run nominal GDP, or an exit multiple justified by a mature peer.
4. Solve for one variable and one only: implied revenue CAGR over the forecast period, implied steady-state operating margin, or implied ROIC on incremental capital. Solving for two at once produces a curve, not a finding.
5. Translate the solved variable into an absolute quantity: revenue in currency units in the terminal year, unit volume, subscriber count, capacity, or implied market share. Absolutes are falsifiable; percentages hide impossibility.
6. Test the absolute against `base-rates.md`: how often has this company, or any company in this industry, achieved it.

The value-driver identity keeps the solved numbers internally consistent:

```text
P/E = (1 - g / ROIC) / (r - g)
```

Two companies on the same P/E imply very different growth when their ROIC differs.
At r = 9 percent, a 30x P/E implies roughly 7.3 percent perpetual growth at 15
percent ROIC, but roughly 8.1 percent at 8 percent ROIC. A high-return business
earns its multiple with less growth, and that is a valuation argument that survives
scrutiny.

## Multiples As Implied Statements

| Multiple | Solve for | Sanity check |
|---|---|---|
| P/E | Implied perpetual growth at a stated r and ROIC | The company own multi-year growth record, and the industry distribution |
| EV/Sales | Implied steady-state EBIT margin, as EV/Sales divided by a mature EV/EBIT | The best margin any company in this industry has sustained |
| EV/EBITDA | Implied maintenance capex and reinvestment burden | Historical capex to sales, and whether EBITDA converts to FCF |
| P/B | Implied sustainable ROE, as P/B times cost of equity | The ROE range through a full cycle, and the capital constraint |
| FCF yield | Implied growth needed to match the cost of equity | Whether current FCF is depressed or inflated by working capital or capex timing |

An EV/Sales of 12x checked against a mature EV/EBIT of 15x implies an 80 percent
steady-state EBIT margin. No commentary about growth is needed once that number is
on the page. This is the fastest way to turn a relative-valuation argument into a
testable one.

## Implied Variable By Business Type

A reverse DCF is not always the right instrument. Solve for what the business model
actually prices.

| Business type | Solve for | Check against |
|---|---|---|
| Bank or broker | Implied sustainable ROE from P/B and cost of equity | Through-cycle ROE, capital requirement, credit cost normalization |
| Insurer | Implied new business value growth from P/EV | Prior NBV growth, distribution capacity, product mix shift |
| REIT or property | Implied cap rate from price versus NOI | Transaction cap rates, the spread over financing cost |
| Regulated utility | Implied premium or discount to regulated asset base | Allowed return, next tariff reset, capex funding path |
| Cyclical or commodity | Implied mid-cycle EBITDA or long-run commodity price | Prior cycle range, marginal cost of the industry, forward curve |
| Pre-profit platform | Implied steady-state margin at scale | Best-in-class peer margin, and whether the cost base is structurally different |
| Pre-revenue biotech | Implied probability of approval times peak sales | Phase-specific approval base rates, analogue launch curves |

## Margin Of Safety Restated

A margin of safety expressed as a discount to a computed fair value inherits every
weakness of that computation. Express it as the distance between the implied
assumption and the historical record instead.

| Read | Condition | Effect on the label |
|---|---|---|
| Undemanding expectations | The implied assumption sits below the company own historical rate and below the industry median | Can support `add-candidate watch` if quality and evidence gates also pass |
| Reasonable expectations | The implied assumption sits inside the historical distribution | Supports `hold/watch`; not sufficient for add-candidate language on valuation alone |
| Demanding expectations | The implied assumption requires close to the best outcome the company or industry has achieved | No `add-candidate watch` on valuation. State what must be true |
| Priced for perfection | The implied assumption exceeds any comparable precedent, or implies share above the industry ceiling | Red flag under `scoring-standard.md`, and `trim-review` on valuation |
| Not solvable | Inputs are missing, cash flow is structurally negative, or the model does not fit the business | Directional language only. Do not present a range as a valuation |

## Boundaries

- Never present the solved variable as a forecast. It is what the price requires, not what is expected.
- Never quote an implied number without its WACC or discount-rate range and its terminal assumption. Change either and the implied number changes.
- Do not output a single point target price. A reverse DCF produces a threshold for belief, not a target.
- If the implied share of an end market exceeds the plausible ceiling, say the valuation is internally inconsistent rather than adjusting the market size to fit.
- This is valuation testing for research. It is not a price target service, a position size, or a transaction instruction.

