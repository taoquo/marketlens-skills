# Valuation Framework

Use valuation to bound the research view, not to create false precision. Prefer original reporting currency, label trailing versus forward inputs, and state the valuation date.

Start from what the price implies, not from what the company is worth. The
procedures for reverse DCF, growth value share, multiples read as implied
statements, and the restated margin of safety are in
`../../references/implied-expectations.md`. Load it before any valuation that
carries a conclusion. Forward valuation below is a cross-check on that reverse
read, not a substitute for it.

Valuation also assumes the earnings base is real. Before applying any multiple to
reported profit, run the cash-conversion and accrual screens in
`../../references/earnings-quality-screens.md`. A multiple on overstated earnings
is precise and wrong.

## Method Selection

| Company type | Primary methods | Cross-checks |
|---|---|---|
| Stable compounder | DCF, normalized P/E, FCF yield | ROIC spread, reinvestment runway, dividend/buyback yield |
| Growth or platform internet | Scenario DCF, EV/sales to margin bridge, SOTP | Unit economics, user/GMV/ad load take-rate evidence |
| Cyclical industrial or commodity | Mid-cycle earnings, EV/EBITDA, replacement cost | Inventory cycle, capacity additions, cost curve position |
| Bank or broker | P/B versus sustainable ROE/COE | CET1 or capital ratio, NIM, credit cost, asset quality |
| Insurer | P/EV, new business value, solvency | Investment yield, duration mismatch, policyholder mix |
| REIT or property | NAV, cap-rate spread, AFFO/FFO yield | Debt maturity wall, occupancy, rent reversion, refinancing cost |
| Utility or infrastructure | Regulated asset base, dividend yield, DCF | Allowed return, tariff reset, leverage and capex cycle |
| Pre-profit biotech | Cash runway, probability-adjusted pipeline value | Trial catalysts, dilution risk, partner validation |

## DCF Discipline

- Use explicit assumptions for revenue growth, margin, reinvestment, tax, WACC, terminal growth, and share count.
- Sensitize at least one growth input and one discount-rate or terminal-value input.
- Do not use DCF for precision if free cash flow is structurally negative, cyclically distorted, or dependent on a binary catalyst; use scenarios instead.
- If WACC or terminal growth is guessed, label the range as illustrative.
- Report the share of enterprise value that sits beyond the explicit forecast period. When it exceeds roughly 70 percent, the terminal assumption is the valuation, and the forward DCF should not be the primary method.
- State the reinvestment needed for the growth assumed. Growth without reinvestment, or growth at an incremental ROIC above the company own history, is an arithmetic error rather than an optimistic view.
- A forward DCF and a reverse DCF using the same inputs must reconcile. If they do not, the forward version contains an assumption that was never stated.

## Relative Valuation

- Translate every multiple into the assumption it implies before comparing it, using the multiples table in `../../references/implied-expectations.md`. A peer trading at half the multiple may imply the same growth at a lower ROIC.
- Compare against local-market peers when listing venue materially affects multiples.
- Do not mix GAAP, adjusted, trailing, and forward multiples without labels.
- For China and Hong Kong names, check whether discount reflects governance, liquidity, policy, or shareholder-return differences before calling it cheap.
- For ADR/H-share/A-share structures, consider share class, liquidity, FX, convertibility, and AH premium or discount.

## Historical Valuation Band

A historical valuation band answers one question: where does the current multiple sit in the company's own history? It does not forecast the multiple, produce a target price, or replace the implied-expectations read. Treat it as a cross-check on the valuation layer, not as a standalone signal.

Use it when the company has positive, comparable TTM earnings and at least three years of trading history. Prefer five years or one full business cycle. Do not use it for pre-profit companies, negative earnings, banks and insurers (use P/B versus ROE, or P/EV), cyclicals without normalized earnings, or a company whose business, accounting, or share count has structurally changed inside the window. If the user asks for a band in one of those cases, say why the multiple is not comparable and route to the appropriate method.

### Data Contract

- `PE(TTM) = total market capitalisation / TTM net profit attributable to parent`. Use total market cap and total shares, not free-float, so splits and bonus issues do not break the series. For A+H or B-share structures, include all share classes.
- Build TTM from the latest disclosed reports: current-year cumulative + prior full year - prior-year same cumulative. Switch the denominator on the announcement date, not the period end. For a backtest, use the figures as originally reported at that date, not later restatements.
- Label reported versus adjusted earnings. For A-shares, compute a second series on 扣非归母净利 and report the gap. A PE on reported profit that includes recurring subsidies, asset disposals, or investment income is not a clean denominator.
- Record `as_of`, `published_at`, and `retrieved_at`. Price and market cap are Tier 2; the TTM denominator is Tier 1 when taken from filings. A vendor PE series is Tier 3: use it as a cross-check, and cap confidence at Medium if the denominator is not reconciled to filings.

### Rolling, Point-In-Time Construction

- Choose a trailing window `W` of at least 750 trading days (about three years); prefer 1,250 days (about five years) or one full cycle. State the window and the number of observations. If a structural break falls inside the window, use only the post-break period and say so.
- At each date `t`, compute the band from observations in `[t-W, t]` only. A full-sample mean and standard deviation drawn across history uses future information and cannot be used as a signal or in a backtest. A full-sample band may be shown as a descriptive all-history reference, clearly labelled and not used for the percentile or signal.
- Primary band: percentile channel. Use P20/P80 for a 60 percent central band, or P16/P84 for a 68 percent band. State the coverage. Percentiles do not assume normality and are less distorted by a long right tail.
- Cross-check: compute the band on log-PE with the same window. Raw PE mean ± `k` standard deviations may be shown as a visual cross-check only; state `k`, the empirical coverage, and the fact that PE is right-skewed. Do not describe a raw ±1σ band as a 68 percent band unless the realised coverage is 68 percent.
- Require at least 250 observations. With fewer, mark the band `evidence-gap` or extend the window; do not draw a band from a handful of points.
- Use the same denominator convention for the current multiple and the historical series. Do not mix reported and adjusted PE in one band.

### Reading The Signal

Report five reads, not one:

| Read | What to report | Why it matters |
|---|---|---|
| Position | Current multiple versus the current lower, middle, and upper band | Shows where the price sits, but not whether the centre is stable |
| Percentile | Share of the window at or below the current multiple, with the window stated | Distribution-free, but still window-dependent |
| Slope | Direction and size of the rolling median multiple over the last 1-2 years | A falling centre can make the same absolute multiple look cheaper than it is |
| Regime | Earnings trend, rates/ERP, and any structural break | A low multiple on falling earnings, or in a higher-rate regime, is not automatically cheap |
| Decomposition | Change in price over the window split into the EPS(TTM) contribution and the multiple contribution, and which dominated | A rising price on flat or falling EPS is a re-rating, not fundamental improvement; a falling multiple on rising EPS is a de-rating despite improving earnings |

Decompose on a log basis, where the identity is exact: `log(price) = log(EPS) + log(PE)`,
so `change in log price = change in log EPS + change in log PE`. Use the same window and
denominator convention as the band. If the multiple dominates, the move is about the
discount rate, positioning, or sentiment; if EPS dominates, run the earnings-quality
screens before crediting it. Report both contributions in the output.

Map the result to the five valuation reads in `../../references/implied-expectations.md`: undemanding, reasonable, demanding, priced for perfection, or not solvable. The band can support the first three as a cross-check; it cannot produce `priced for perfection` or `not solvable` without the implied-variable solve and the earnings-quality screens. A band position alone cannot support `add-candidate watch`, `trim-review`, or any action label.

Before calling a low band position cheap, run the denominator checks:

- TTM earnings quality: OCF/NI, accrual ratio, receivables and inventory versus revenue, capitalised R&D, and recurring one-offs, per `../../references/earnings-quality-screens.md`.
- For A-shares, non-recurring gains and losses, government subsidies, asset disposals, and investment income, per the skill's `regional-market-guide.md` and `data-sources.md`.
- Cyclicals: use mid-cycle earnings, not peak TTM earnings. A low PE at a cyclical peak is a warning, not a bargain.
- Negative or zero TTM earnings: PE is undefined. Use EV/EBITDA, P/B versus ROE, or another business-model method; mark the PE band unavailable.

### Failure Boundaries

| Assumption | What breaks it | Required handling |
|---|---|---|
| Mean reversion | Structural change in growth, profitability, regulation, or business mix | Use a post-break window; report the rolling centre; do not extrapolate the old band |
| Denominator comparability | Profit collapse, profit peak, accounting-policy change, merger, or divestiture | Normalise earnings; use a clean series; mark the band `evidence-gap` if the series is not comparable |
| Clean earnings | Asset disposals, subsidies, investment income, or other one-offs | Compute the 扣非 series; compare reported and recurring PE |
| Positive earnings | TTM net profit at or below zero | PE is unavailable; switch method |
| Stable share count | Large issuance, buyback, or conversion | Use total market cap and the share count on each date; restate the series if needed |
| Stable discount rate | A material change in the risk-free rate or equity risk premium | Pair the band with the 10-year yield or ERP; a PE band is not rate-adjusted |

### Output

When a historical band is used, state:

- The multiple and denominator convention: PE TTM, reported or 扣非, total market cap, and the TTM formula.
- The window, number of observations, and whether it covers a full cycle.
- The band method and coverage: P20/P80, P16/P84, or log-PE μ ± kσ, with `k` and realised coverage.
- The current position, percentile, and slope.
- The EPS(TTM) and multiple contribution to the price move over the same window.
- The failure checks and any that are unavailable.
- The resulting valuation read and the confidence cap. If the denominator is not reconciled to filings, cap confidence at Medium; if the history is shorter than 750 days, use `evidence-gap` rather than a strong read.

A worked arithmetic check:

```text
TTM = current cumulative + prior full year - prior-year same cumulative
    = 644.67 + 823.20 - 646.27
    = 821.60
PE  = total market cap / TTM
```

The numbers above are an arithmetic illustration, not a live data point. Verify the share count, market cap, and announcement dates before using them.

### Figure Contract

When the user asks for a visual, or when the band is the main deliverable, produce a `Valuation Band` figure, not only a table. The figure must use the same point-in-time series as the calculation.

Required elements:

- Title: `[Company] PE(TTM) Band`.
- Subtitle: ticker, window, number of observations, last update, and whether the denominator is reported or 扣非.
- x-axis: date. y-axis: PE(TTM), with the current value marked.
- One line: the point-in-time PE series.
- Three lines or a shaded band: lower, middle, and upper values from the rolling window used at each date.
- Annotations: current PE, current percentile, slope direction, and the current lower and upper band values.
- Footer: source, TTM formula, band method (P20/P80, P16/P84, or log-PE μ ± kσ), coverage, and `descriptive, not a signal`.

Rules:

- The band at date `t` must use only observations up to `t`. Do not draw a full-sample band over the historical line and call it a signal. If an all-history band is shown, label it `all-history descriptive` and keep it visually separate from the rolling band.
- Use the same denominator convention for the line and the band. Do not mix reported and 扣非.
- Do not truncate the y-axis to make the current value look extreme; show zero or state the truncation in the caption.
- If the host cannot render a chart, output a compact table with the same fields (date, PE, lower, middle, upper, percentile) and a text summary. Do not describe a chart that was not produced.
- The figure is a valuation context exhibit. It must not be presented as a buy/sell signal, a target price, or a probability of reversion.

## Margin Of Safety

Give precise action-price ranges only when current price, share count, valuation inputs, and primary filings are dated and cross-checked. Otherwise use directional ranges such as materially below fair value, near fair value, or above fair value.

Express the margin of safety as the distance between the implied assumption and
the historical record, not as a discount to a computed fair value. A 40 percent
discount to a fair value built on a guessed WACC is not a margin of safety. Use the
five reads in `../../references/implied-expectations.md`: undemanding, reasonable,
demanding, priced for perfection, or not solvable. Map the read to a shared label
through the `Label Layering` table in `../../references/scoring-standard.md`.

Required in any output that states a valuation conclusion:

- The solved implied variable, its WACC range, and its terminal assumption.
- The absolute quantity it translates to, such as terminal-year revenue, volume, or implied market share.
- The company own historical rate for that variable, and the industry distribution where available.
- The earnings quality read, because a multiple is only as good as the earnings under it.
