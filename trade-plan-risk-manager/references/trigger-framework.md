# Trigger Framework

Use this file to convert research into conditional triggers. Triggers are review points, not personal transaction instructions.

## Trigger Types

| Trigger | Purpose | Examples |
|---|---|---|
| Entry trigger | Defines what must become true before the setup is active | Valuation discount reaches threshold, breakout with volume, earnings revision turns positive, policy detail is confirmed |
| Confirmation evidence | Reduces false positives | Primary filing, official data, guidance, margin trend, volume confirmation, peer read-through |
| Review trigger | Forces reassessment | Price moves faster than revisions, event date changes, regime deteriorates, thesis metric misses |
| Stop-error | Defines what proves the thesis wrong | Core metric breaks, management guide-down, policy denial, balance-sheet stress, failed product adoption |
| Time stop | Prevents stale thesis drift | No evidence improvement by a specific event or reporting window |
| Event stop | Controls gap/catalyst risk | Do not keep same risk framing through earnings, approval, litigation, or policy decision without review |

## Price Triggers

Use precise price levels only when current price and valuation inputs are dated and sourced. Otherwise use conditional language:

- "review if price reaches the valuation range"
- "activate only if the market confirms the breakout with volume"
- "downgrade if the stock rerates without estimate support"

Do not present a price as a personal order level.

## Invalidation Rules

Good invalidation is observable, dated, and tied to the thesis driver:

- Fundamentals: revenue, margin, backlog, cash flow, leverage, churn, or unit economics.
- Catalyst: event delay, miss, no guidance raise, approval denial, unfavorable legal/policy result.
- Market: funding stress, volatility shock, factor unwind, liquidity gap, FX or rates break.
- Portfolio: concentration, correlation, or overlapping catalyst risk becomes dominant.

## Review Cadence

| Setup type | Default review cadence |
|---|---|
| Event-driven | Before event, immediately after release, and after first revision cycle |
| Earnings revision | Before results, after guidance, and after consensus updates |
| Valuation mean reversion | When price or multiple reaches the review band |
| Regime-sensitive | Weekly or when liquidity/sentiment indicators change |
| Long-term thesis | Each filing cycle and when a kill condition appears |
