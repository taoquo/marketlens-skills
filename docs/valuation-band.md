# Valuation Band Guide

[中文](valuation-band.zh-CN.md)

A historical valuation band answers one question: **where does the current multiple sit in the
company's own trailing history?** It is a context exhibit and a cross-check on the valuation
layer. It is not a forecast, a target price, a probability of reversion, or a buy/sell signal.

The method is defined in
[`equity-research/references/valuation-framework.md`](../equity-research/references/valuation-framework.md).
This guide covers the data contract, the dependency-free chart utility in this repository, and
how to read the result. The NVIDIA worked case is
[`examples/marketlens-v010-valuation-band-nvda.html`](../examples/marketlens-v010-valuation-band-nvda.html).

## 1. When to use it

Use a PE(TTM) band when all of the following hold:

- TTM net profit attributable to parent is positive and comparable across the window.
- The company has at least three years of trading history; prefer five years or one full cycle.
- The business mix, accounting policy, and share count have not structurally changed inside the
  window. If they have, use only the post-break period and say so.
- You have a dated price or market-cap series and can state the TTM denominator convention.

Do not use a PE band for pre-profit companies, negative earnings, banks and insurers (use P/B
versus ROE, or P/EV), cyclicals at a peak without normalized earnings, or a company whose
denominator is not comparable across the window. Route to the appropriate method instead of
forcing a band.

A band is also not a standalone label. It can support `undemanding`, `reasonable`, or
`demanding` as a cross-check. It cannot produce `priced for perfection` or `not solvable`
without the implied-variable solve and the earnings-quality screens, and it cannot support
`add-candidate watch`, `trim-review`, or any action label on its own.

## 2. Data contract

### 2.1 CSV formats

The utility accepts either a ready-made PE series:

```csv
date,pe
2026-11-20,13.37
2026-11-23,17.73
2026-11-24,16.67
```

or market cap and TTM net profit, from which it computes `PE = market_cap / ttm_net_profit`:

```csv
date,market_cap,ttm_net_profit
2026-11-20,2990000000000,224000000000
2026-11-23,3966000000000,224000000000
2026-11-24,3740000000000,224000000000
```

Rules:

- `PE(TTM) = total market capitalisation / TTM net profit attributable to parent`.
- Use **total** market cap and total shares, not free float. For A+H or B-share structures,
  include all share classes.
- Build TTM as `current-year cumulative + prior full year - prior-year same cumulative`.
  Switch the denominator on the **announcement date**, not the period end. For a backtest, use
  the figures as originally reported at that date, not later restatements.
- Label reported versus adjusted earnings. For A-shares, compute a second series on
  扣非归母净利 and report the gap.
- Do not mix reported and adjusted PE in one band.
- A vendor PE series is Tier 3 evidence. Reconcile the denominator to filings when possible;
  otherwise cap confidence at Medium.
- Record `as_of`, `published_at`, and `retrieved_at` separately.

The dates may be ISO `YYYY-MM-DD`, `YYYY/MM/DD`, or `YYYYMMDD`. Rows with missing, non-numeric,
zero, or negative PE are skipped and counted on stderr.

## 3. Quick start

The utility is Python 3.9+ standard library only. From the repository root:

```bash
python3 scripts/pe_band_chart.py \
  --input examples/data/nvda-pe-ttm-illustrative.csv \
  --output nvda-pe-band.svg \
  --table-output nvda-pe-band.csv \
  --summary-json nvda-pe-band.json
```

It writes:

- `nvda-pe-band.svg` — self-contained chart with the PE line, rolling band, annotations, and
  footer.
- `nvda-pe-band.csv` — optional `date,pe,lower,middle,upper,percentile` table; this is also the
  table fallback when a host cannot render SVG.
- `nvda-pe-band.json` — optional latest-observation summary, including the current PE, band,
  percentile, slope, window, and observation count.

The command also prints a one-line summary:

```text
Latest: 2026-11-24 PE 16.67 | lower 32.496 | mid 49.14 | upper 64.882 | percentile 0.53 | slope falling | window 750 | observations 1410
```

Open the SVG in a browser, or embed it in an HTML or PDF deliverable. The Figure Contract in
`valuation-framework.md` describes the required chart elements.

The repository's worked case is typeset through Folio rather than this utility. Its HTML holds a
`<figure data-folio-diagram-slot="pe-band">` slot, and Folio's `embed-drawing` fills it from the
tracked `line-chart` fixture `examples/data/nvda-pe-band-folio.json`. That path adds the visible
accessible data table, the host-fit record, and the final-size text check. The dependency-free
utility remains the standalone fallback and the source of the daily band table.

## 4. Options

| Option | Default | Meaning |
|---|---|---|
| `--input` | required | CSV path |
| `--output` | `pe-band.svg` | SVG output path |
| `--table-output` | none | Optional CSV with the band at every date |
| `--summary-json` | none | Optional JSON summary of the latest observation |
| `--date-col` | `date` | Date column name |
| `--pe-col` | `pe` | PE column name |
| `--market-cap-col` | `market_cap` | Market-cap column, used when `pe` is absent |
| `--profit-col` | `ttm_net_profit` | TTM profit column, used when `pe` is absent |
| `--window` | `750` | Trailing observations in the rolling band |
| `--min-obs` | `250` | Minimum observations before the band is drawn |
| `--method` | `percentile` | `percentile` or `mean` |
| `--lower` / `--upper` | `20` / `80` | Percentiles for the percentile method; P20/P80 is a 60% central band |
| `--k` | `1.0` | Standard-deviation multiplier for the mean method |
| `--slope-window` | `250` | Observations in each half of the slope comparison |
| `--width` / `--height` | `960` / `520` | SVG viewBox dimensions; both have minimums |
| `--title` | `PE(TTM) Band` | Chart title |
| `--subtitle` | empty | Ticker, window, data date, denominator convention |
| `--source` | empty | Source line in the footer |
| `--note` | rolling band caveat | Second footer line |

Use P16/P84 for a 68% central band, or state the realized coverage explicitly. P20/P80 is not a
68% band. For the mean method, remember that raw PE is right-skewed; state `k` and the empirical
coverage, and treat the raw μ ± kσ band as a visual cross-check only. A log-PE band is the
preferred cross-check.

These flags apply to `scripts/pe_band_chart.py`. A Folio `line-chart` fixture fixes the canvas
width at 960 and accepts a height of 400–720 in steps of 4; it also caps categories at 12 and
series at 3. Section 8 explains how the case fits the band into that budget.

## 5. How the band is computed

For each date `t`, with a trailing window `W`:

1. Take the observations in `[t-W, t]` only. No future data enters the calculation.
2. Sort the sample.
3. Percentile method: lower = P20, middle = P50, upper = P80. The current percentile is the
   share of the sample at or below the current PE.
4. Mean method: middle = mean, lower = `max(0, mean - k * stdev)`, upper = `mean + k * stdev`.
5. Slope: compare the median of the last `slope-window` observations with the median of the
   preceding `slope-window`; call the result `rising`, `falling`, or `flat` at a 2% threshold.

The band starts after `min-obs` observations. During the warm-up it uses the observations
available since the start of the file; after `window` observations it is a true trailing window.
The footer says `window ≤ N obs` for that reason. If you need a full-window band from the first
drawn point, set `--min-obs` equal to `--window`.

A full-sample band drawn across the whole history uses future information. It may be shown as
an all-history descriptive reference, clearly labelled, but it cannot be used for the percentile
or as a signal.

## 6. How to read it

Report five reads, not one:

| Read | What to report | Why it matters |
|---|---|---|
| Position | Current PE versus the current lower, middle, and upper band | Where the price sits, but not whether the centre is stable |
| Percentile | Share of the window at or below the current PE | Distribution-free, but still window-dependent |
| Slope | Direction and size of the rolling median over the last 1–2 years | A falling centre can make the same absolute multiple look cheaper than it is |
| Regime | Earnings trend, rates/ERP, and any structural break | A low multiple on falling earnings, or in a higher-rate regime, is not automatically cheap |
| Decomposition | Split the price move into the EPS(TTM) and multiple contributions | A rising price on flat EPS is a re-rating; a falling multiple on rising EPS is a de-rating |

The decomposition is exact on a log basis: `log(price) = log(EPS) + log(PE)`. Report which
contribution dominated over the same window as the band. If the multiple dominated, the move
is about the discount rate, positioning, or sentiment; if EPS dominated, run the earnings-quality
screens before crediting it.

Map the result to one of the five valuation reads: `undemanding`, `reasonable`, `demanding`,
`priced for perfection`, or `not solvable`. The band can support the first three as a
cross-check. It cannot produce the last two without the implied-variable solve and the
earnings-quality screens.

Before calling a low band position cheap, run the denominator checks:

- TTM earnings quality: OCF/NI, accrual ratio, receivables and inventory versus revenue,
  capitalised R&D, and recurring one-offs.
- A-shares: non-recurring gains and losses, government subsidies, asset disposals, and
  investment income.
- Cyclicals: use mid-cycle earnings, not peak TTM earnings. A low PE at a cyclical peak is a
  warning, not a bargain.
- Negative or zero TTM earnings: PE is undefined. Switch method and mark the PE band unavailable.

Pair the band with the earnings trend and the 10-year yield or equity risk premium. A PE band
is not rate-adjusted.

## 7. Using it through the skill

Ask the equity-research skill a question such as:

```text
Use $equity-research to show NVIDIA's PE(TTM) band and tell me where 16.7x sits in its own history.
Use $equity-research to put Microsoft's current multiple in a rolling five-year percentile band.
```

The skill enters `valuation-band` mode and returns:

- The multiple and denominator convention.
- The window, observation count, and whether it covers a full cycle.
- The band method and coverage (P20/P80, P16/P84, or log-PE μ ± kσ).
- Current position, percentile, and slope.
- The EPS(TTM) and multiple contribution to the price move.
- The failure checks and any that are unavailable.
- The valuation read and the confidence cap.

If you ask what to do next, the skill continues into `decision-framework`; the band on its own
does not produce an action label. If the host cannot render a chart, the skill outputs the
compact table fallback instead of describing a chart that was not produced.

## 8. Figure Contract

A `Valuation Band` figure must include:

- Title: `[Company] PE(TTM) Band`.
- Subtitle: ticker, window, observation count, last update, and reported versus adjusted
  denominator.
- x-axis: date. y-axis: PE(TTM), with the current value marked.
- One line: the point-in-time PE series.
- Three lines or a shaded band: lower, middle, and upper values from the rolling window at each
  date. A Folio `line-chart` is limited to three series; when the PE line and two bounds use all
  three, carry the rolling middle in the table and caption instead of dropping a bound.
- Annotations: current PE, current percentile, slope direction, and the current lower and upper
  band values. The Folio line chart accepts at most three annotations, so a case may carry the
  remaining reads in the metrics strip and the band-read table.
- Footer: source, TTM formula, band method, coverage, and `descriptive, not a signal`.

Rules:

- The band at date `t` uses only observations up to `t`.
- The line and the band use the same denominator convention.
- Do not truncate the y-axis to make the current value look extreme; show zero or state the
  truncation in the caption.
- If the host cannot render a chart, output the table fallback with the same fields.
- Never present the figure as a buy/sell signal, target price, or probability of reversion.

The utility implements these elements for a standalone SVG. The NVIDIA case instead uses Folio's
`line-chart` drawing at 960×460, embedded through a `data-folio-diagram-slot` host slot: ten
quarterly samples from the daily series, three series (PE, P20, P80), and a current-median
reference rule. The chart's y-axis starts at 0x, and the caption states that the band is
descriptive and the denominator is peak-cycle earnings. `embed-drawing` generates the visible
ten-row data table and the host-fit trace;
`scripts/pe_band_chart.py` remains the dependency-free fallback and writes the daily
`date,pe,lower,middle,upper,percentile` table.

## 9. Worked NVIDIA example

The case is illustrative, not live market data. It uses a 750-observation rolling window and a
P20/P80 band:

```bash
python3 scripts/pe_band_chart.py \
  --input examples/data/nvda-pe-ttm-illustrative.csv \
  --output nvda-pe-band.svg \
  --window 750 --min-obs 250 \
  --method percentile --lower 20 --upper 80 \
  --title "NVIDIA PE(TTM) Band" \
  --subtitle "NVDA · 1,410 observations · rolling 750-observation window · reported-basis TTM · through 2026-11-24" \
  --source "Source: quarter-end PE anchors from a vendor series, daily path interpolated; not a live feed" \
  --note "Point-in-time rolling band. Descriptive, not a signal, forecast, or target price."
```

Result: current PE 16.7x, lower 32.5x, middle 49.1x, upper 64.9x, percentile 0.5, slope
falling. The read is below the band and `undemanding` as a cross-check, but the denominator is
peak-cycle earnings: TTM EPS of $9.31 is up 143% year on year and Q3 CFO/NI is 0.74. The move
from 2023-Q4 to 2026-Q4 is EPS-led: price +213%, EPS(TTM) +1,125%, multiple -74.4%. The multiple
compressed while the earnings base expanded, so the price gain is not a re-rating. The EPS path
is anchored to quarter-end filings and interpolated between them, so the daily line is
illustrative. The implied-expectations read now requires only a 6.2% ten-year NOPAT CAGR, so the
valuation layer is undemanding; the label remains hold/watch because cash conversion and
governance, not price, are the constraint. The band supports the valuation layer; it does not
set the label.

The case itself takes the Folio path. `examples/data/nvda-pe-band-folio.json` is the tracked
`line-chart` fixture: ten quarterly samples from the daily series, three series (PE, P20 lower,
P80 upper), a reference rule at the current median, and an annotation at the current point. The
DSL cap is 12 categories and 3 series, which is why the case samples quarters rather than plotting
1,410 daily points and why the rolling middle sits in the table and caption. The host slot is
filled with:

```bash
python3.12 ~/.claude/skills/folio/scripts/folio.py embed-drawing \
  examples/data/nvda-pe-band-folio.json \
  --host-contract a4-portrait \
  --host-file path/to/host-with-pe-band-slot.html \
  --output-host path/to/filled.html \
  --artifact-dir examples/assets/folio \
  --slot pe-band \
  --caption "Reported-basis TTM; 10 quarterly samples from 1,410 daily observations; the y-axis starts at 0x. Descriptive, not a signal." \
  --profile embed
```

The command writes the artifact, the visible accessible table, and the host-fit record. Run
`python3.12 .../folio.py verify-drawing-host path/to/filled.html` before rendering. The case is
already filled; use this sequence when rebuilding it or adapting the fixture to another host.

## 10. Table fallback

If a chart cannot be rendered, use the `--table-output` CSV or this compact table:

| Date | PE | Lower | Middle | Upper | Percentile |
|---|---:|---:|---:|---:|---:|
| 2026-11-24 | 16.67 | 32.50 | 49.14 | 64.88 | 0.53 |

Add a text summary: `PE 16.7x, P20/P80 band 32.5x–64.9x, middle 49.1x, percentile 0.5, slope
falling, 750-observation window, 1,410 observations.` Do not describe a chart that was not
produced.

The Folio `embed-drawing` path emits the visible table automatically from the fixture's series,
so the chart and the fallback cannot disagree on the plotted values. The utility's
`--table-output` CSV adds the rolling middle and percentile at every date; use it when the host
needs the full daily series rather than the chart's quarterly samples.

## 11. Checklist before publishing

- [ ] Positive, comparable TTM earnings for the whole window.
- [ ] At least 750 trading days; prefer 1,250 or a full cycle.
- [ ] At least 250 observations in the band.
- [ ] TTM denominator reconciled to filings, or confidence capped at Medium.
- [ ] Reported versus adjusted convention stated and not mixed.
- [ ] Total market cap and all share classes; share count changes handled.
- [ ] Rolling, point-in-time band; no full-sample signal.
- [ ] Window, observations, method, and coverage stated.
- [ ] Position, percentile, slope, regime, and EPS/PE decomposition reported.
- [ ] Failure checks run; missing checks marked unavailable.
- [ ] Figure or table fallback produced; no invented chart.
- [ ] Folio line chart: at most 12 categories and 3 series; the rolling middle is in the table and
      caption; any y-axis truncation is stated.
- [ ] Caption says `descriptive, not a signal`.
