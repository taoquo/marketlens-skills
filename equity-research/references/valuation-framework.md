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
