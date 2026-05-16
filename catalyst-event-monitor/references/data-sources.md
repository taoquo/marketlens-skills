# Catalyst Event Data Sources

Use original sources first. Use secondary sources only to cross-check, fill gaps, or understand expectations, and label them as secondary.

## Company Events

- Filings and disclosures: SEC EDGAR, HKEXnews, CNINFO, SSE/SZSE/BSE announcements, annual/interim/quarterly reports.
- Company IR: earnings calendar, press releases, presentations, transcripts, investor day materials, product launch pages.
- Capital allocation: buyback authorizations, dividend announcements, equity/debt issuance filings, M&A agreements.
- Ownership and supply: prospectus lockup terms, Form 4, 13D/13G, HK disclosure of interests, exchange unlock calendars, index provider announcements.

## Regulatory, Legal, And Policy

- Regulators: FDA/NMPA/EMA, CSRC, SEC, HK SFC, antitrust regulators, telecom/energy/financial regulators where relevant.
- Courts and legal: official court dockets, settlement filings, regulator enforcement releases.
- Policy: central bank, finance ministry, industry regulator, customs/tariff authorities, official government notices.

## Market Expectations

- Company guidance and prior management language.
- Consensus estimates where provider and date are clear.
- Options-implied move, IV rank/percentile where available, short interest, borrow cost, valuation multiples, and earnings revisions.
- Pre-event price action: absolute return, sector-relative return, index-relative return, volume, and factor/peer move over 1 week, 1 month, and 3 months when useful.
- Broker or media summaries as secondary context only.

## Freshness TTL

| Data type | Freshness target | If stale |
|---|---|---|
| Event date/calendar | Latest company, exchange, or regulator update | Mark date confidence as low |
| Earnings/guidance expectations | Latest available snapshot, ideally within 7 trading days | Avoid precise surprise claims |
| Market price, options-implied move, IV rank, short interest | Latest trading day or latest official release | Mark lag and avoid intraday claims |
| Regulatory/legal status | Latest official docket, filing, or notice | Search for follow-up before concluding |
| Lockup/unlock/index event | Latest prospectus, exchange, or index provider notice | Mark as conditional if source is secondary |
| Product/customer claims | Latest company/customer announcement | Require adoption evidence before hard-catalyst label |

## Cross-Check Rules

- Confirmed event: cite primary company, exchange, regulator, court, or official calendar source.
- Expected event: cite the source and date; state that timing is expected, not confirmed.
- Rumored event: label as rumor and do not build a strong conclusion from it.
- Expectation gap: use at least one expectation source and one market-pricing or fundamentals source where possible.
- Market pricing conclusion: do not call a catalyst attractive without checking whether price, valuation, volatility, short interest, or revisions already reflect the setup.
- Post-event review: compare actual result to pre-event expectation, not to a vague narrative.
