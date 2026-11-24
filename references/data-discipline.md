# Data Discipline

Shared data rules for MarketLens skills. Load this file before scoring,
labelling, or writing a `Data Freshness` table. Each skill keeps only the rules
that are specific to its domain and inherits everything here.

## Timestamps

Record three timestamps for every data point. Never collapse them into one date.

| Field | Meaning |
|---|---|
| `as_of` | The period, market date, event date, or portfolio date the value describes |
| `published_at` | When the source published it, if available |
| `retrieved_at` | When you fetched or viewed it |

A data point with no `as_of` is undated. Do not score it.

## Freshness Grades

The `Freshness` column of every `Data Freshness` table must use one of these
five values. Do not invent alternative wording.

| Grade | Meaning | Required handling |
|---|---|---|
| `Fresh` | Within the TTL the skill defines for that data type | Full weight |
| `Lagged` | Published on schedule but delayed by design, such as a weekly survey, monthly release, quarterly filing, or prime-broker report | Usable; state the lag; never present it as current positioning |
| `Stale` | Past the TTL, and a newer value should already exist | Half weight; cap confidence at Medium; avoid precise level language |
| `Undated` | No `as_of` can be established | Do not score; list as unavailable |
| `Unavailable` | Searched and not found, paywalled, or not disclosed | Do not score; state the confidence impact |

Missing data is never bullish or bearish. It is a confidence limit.

TTLs are per skill. Most skills define them in `references/data-sources.md`;
`portfolio-risk-monitor` uses `references/data-inputs.md`, and
`trade-plan-risk-manager` uses `references/risk-and-execution.md`. When a skill
defines no TTL for a data type, use the shortest defensible one for that class of
data and state it in the output.

## Evidence Tiers

All skills use the same three tiers. A skill's own `Evidence Standard` section
only names which concrete sources fill each tier for its domain.

| Tier | Definition | Use |
|---|---|---|
| Tier 1 | The original record from the issuer, exchange, regulator, court, or official publisher | Core facts, dated events, financials, terms, legal status |
| Tier 2 | Official market, macro, rates, FX, or index data, plus issuer IR material | Prices, flows, market structure, context |
| Tier 3 | Financial platforms, media, broker notes, consensus datasets, vendor estimates | Context and proxy only |

A decisive claim needs at least one Tier 1 or Tier 2 source. Tier 3 alone caps
confidence at Medium and cannot support a strong action-style label.

Do not fabricate citations or quote text you cannot verify.

## Source Pool And Claim Citation

Build a source pool before the first conclusion and reuse it across every layer of the
same research run. The pool is the audit trail from a claim back to a dated record; it is
not a bibliography padded to a target count.

| Field | Required content |
|---|---|
| ID | Stable short id, such as `S1` |
| Tier | `Tier 1`, `Tier 2`, or `Tier 3` |
| Publisher | Issuer, exchange, regulator, data vendor, or publication |
| Title | Document, page, or dataset title |
| `as_of` | Period, market date, or event date the source describes |
| `published_at` | Publication date, if available |
| `retrieved_at` | Date the source was viewed or fetched |
| Locator | URL, filing number, accession number, or other stable locator |
| Used in | The layer, table, or output block that uses it |

Rules:

- Every decisive claim maps to at least one pool ID. A claim without a pool entry is an
  estimate or an opinion, and must be labelled as one.
- Entries that describe the same underlying record are one source. The same filing
  republished by three vendors is not three independent sources.
- Judge independence by origin and incentive, not by count. A Tier 3 article quoting the
  same Tier 1 filing adds no independent support.
- A source that cannot be located does not enter the pool. List it as `Unavailable` in
  `Data Freshness` and state the confidence impact.
- Carry the pool forward across skills in the research state card defined in
  `skill-contract.md`. Do not rebuild it at each layer.
- Report only the entries that carry a conclusion. Do not pad the pool to reach a source
  count.

### Claim Citation

- Separate fact, estimate, and opinion in the sentence itself. Use wording such as
  `the filing reports`, `the model estimates`, and `the view argues`.
- Put the source next to the claim it supports, not only in a closing list. A reader must
  be able to tell which source supports which number.
- Quote only text that was opened and can be located. Do not reconstruct a quotation, a
  date, or a figure from memory.
- When two sources conflict, cite both, state the conflict, and name the source the
  analysis uses and why. Do not silently choose the convenient one.
- A source's tier and its `as_of` date travel with the claim. A precise number from an
  undated page is still undated.

## Core Figure Check

Run every figure that carries a conclusion through this table before making a
strong claim. Use it for financials, industry data, event terms, prices, and
portfolio weights alike.

| Metric | Original Wording | Value | Unit | Period | Publisher | Link | Cross-check | Treatment |
|---|---|---:|---|---|---|---|---|---|

Allowed `Treatment` values:

- `Use`: source, unit, period, and cross-check are consistent.
- `Use with caveat`: usable, but stale, estimated, survey-based, or partly inconsistent.
- `Proxy only`: good for direction, not enough for a precise or strong conclusion.
- `Exclude`: undated, unverifiable, wrong unit or period, or a quantity-scale anomaly.

A quantity-scale anomaly is a figure that is off by roughly a factor of 10 or
more versus the source, peer data, or the historical range. Mark it
`Use with caveat` or `Exclude`; never smooth it into the narrative.

## Units, Currency, And Calendar

- Print the unit and currency next to every number. A bare number is not a data point.
- Do not convert currency or scale silently. State the rate, its date, and the direction of the conversion.
- Chinese-language filings often report in units of 100 million; US filings in thousands or millions. Restate the figure in the unit you print, and keep the original wording in the core figure check.
- Label the accounting standard when comparing across markets: US GAAP, IFRS, HKFRS, or China ASBE. Do not compare adjusted figures across standards without saying so.
- Label the calendar. `FY2025` is the issuer's fiscal year; `CY2025` is the calendar year. State the fiscal year-end whenever it is not December.
- Do not mix trailing, forward, reported, and adjusted metrics in the same comparison without labels.

## User-Provided Input

Classify user input before using it. User input is not automatically Tier 1.

| Input type | Example | Handling |
|---|---|---|
| Plan parameter | Holdings, weights, horizon, cost basis, thesis tag, stated constraint | Accept as given, label it `user-provided`, and do not infer anything beyond it |
| Fact claim | Revenue grew 40 percent, approval is on March 3, a quoted price or multiple | Treat as a claim to verify, not as evidence. Source it before building a conclusion on it |
| Preference | Risk tolerance, style, target return, horizon preference | Use to shape scope only. Never infer a value the user did not state |

Run these consistency checks and report any failure before the analysis:

- Weights do not sum to the stated total, or exceed 100 percent.
- A date is in the future, inconsistent with the stated period, or precedes a prerequisite event.
- A price, market cap, or metric sits far outside the range the sources support.
- A cited source cannot be located.
- Two user statements conflict, or a user figure conflicts with the primary source.

When a check fails, state the conflict, use the sourced value for the analysis,
and mark the user value as unverified. Do not silently overwrite user input,
and do not build a conclusion on an unverified user figure.
