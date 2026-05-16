# Sector Industry Data Sources

Use primary, official, or original-publisher sources first. Use secondary platforms only to cross-check or fill gaps, and label them as secondary.

## Global And US

- Government and macro: BEA, BLS, Census, EIA, USDA, Department of Commerce, Federal Reserve, FRED.
- Regulators and exchanges: SEC filings, FTC/DOJ where relevant, FDA for drugs/devices, FCC/FERC for regulated sectors.
- Industry associations: original industry association releases, trade groups, standards bodies, and dated survey publishers.
- Company evidence: 10-K/10-Q/8-K, segment disclosures, investor presentations, earnings call transcripts.
- Market data: commodity curves, rates, FX, freight indices, index constituents, ETF holdings.

## Hong Kong And China

- Official macro and policy: NBS, PBOC, NDRC, MIIT, MOF, SAMR, CSRC, ministry/regulator notices.
- Exchange and company disclosures: HKEXnews, CNINFO, SSE, SZSE, BSE, company annual/interim/quarterly reports.
- Industry data: CAAM, CPCA, CISA, NEA, NMPA, CAICT, CEA, WIND/Choice/iFinD when available and dated.
- Trade and customs: China Customs, UN Comtrade, WTO, partner-country customs data.
- Market structure: northbound/southbound flows, margin financing, short selling, sector valuation data.

## Cross-Border And Export Sectors

- Customs/trade data: import/export volume, value, ASP, destination mix, tariff changes.
- FX/rates: USD/CNH, USD/HKD, local funding rates, hedging cost.
- Geopolitics: official export-control lists, sanctions, entity lists, tariff announcements.
- Customer markets: end-market demand from downstream company filings and official statistics.

## Source Discipline

- Record source date and reporting period separately.
- Preserve the original wording, unit, period, and link for every core number.
- Prefer original units and currency; convert only when needed.
- Do not mix shipment volume, revenue, ASP, and booking/backlog without labeling.
- For survey data, state sample period and publisher.
- If exact data cannot be found, write "not found from primary sources" and use a labeled proxy or omit the metric.
- If a number has a quantity-scale anomaly versus the source, peer data, or historical range, mark it `Use with caveat` or `Exclude`; do not smooth it into the narrative.

## Data Check Table

Use this table for all core figures before making strong conclusions:

| Metric | Original Wording | Value | Unit | Period | Publisher | Link | Cross-check | Treatment |
|---|---|---:|---|---|---|---|---|---|

Allowed `Treatment` values:

- `Use`: original source, unit, period, and cross-check are consistent.
- `Use with caveat`: usable, but stale, estimated, survey-based, or partly inconsistent.
- `Proxy only`: useful for direction, not enough for strong or precise conclusions.
- `Exclude`: undated, unverifiable, wrong unit/period, or quantity-scale anomaly.

## Freshness TTL

Use these maximum ages unless the user explicitly asks for historical analysis:

| Data type | Freshness target | If stale |
|---|---|---|
| Sector price/index/ETF, rates, FX, commodities | Latest trading day | Mark non-real-time and avoid tactical timing claims |
| Monthly industry output, sales, shipments, inventory | Latest official monthly release | State release lag and next release risk |
| Quarterly company segment data | Latest reported quarter | Reduce confidence if a newer earnings cycle has started |
| Policy/regulation | Latest official notice | Search for follow-up guidance before concluding |
| Capacity/capex/project pipeline | Latest company or official disclosure | Treat announced but unfunded capacity separately |
| Consensus estimates and peer multiples | Latest available snapshot, ideally within 7 trading days | Label as estimate and avoid false precision |
| Survey/PMI/expert-call data | Latest survey period | Use as context, not sole basis for strong conclusion |

## Cross-Check Rules

- Cycle conclusion: verify at least one demand indicator and one supply/pricing/capacity indicator.
- Value-chain conclusion: use evidence from at least two adjacent segments when possible.
- Peer conclusion: define the peer set and cross-check exposure from company segment disclosures.
- Policy-heavy conclusion: cite official policy/regulator documents before relying on media summaries.
- Trading read-through: cross-check the industry view against valuation pressure, earnings revision, and catalyst evidence.
- Conflicts: state both values, prefer primary or more direct data, and name the tie-breaker to monitor.
