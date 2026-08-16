# MarketLens Skills

[中文文档](README.zh-CN.md)

MarketLens Skills is a publishable skill repository for AI-assisted public-market research.

Repository: https://github.com/taoquo/marketlens-skills

It provides six production-oriented skills:

| Skill | Purpose |
|---|---|
| `equity-research` | Equity research for US, Hong Kong, and A-share listed companies, covering quality scoring, earnings, fundamentals, valuation, moat, regional disclosures, red flags, and data freshness. |
| `market-regime-monitor` | Market regime monitoring across liquidity, sentiment, positioning, valuation crowding, scoring confidence, risk-budget impact, and cross-market risk transmission. |
| `sector-industry-research` | Sector and industry research across cycle stage, supply-demand, value chains, policy/technology shifts, peer structure, trade expression, and listed-company read-through. |
| `catalyst-event-monitor` | Event-driven research for upcoming catalysts, expectation gaps, market pricing, trade setup, scenario paths, pre-event watch data, and post-event thesis updates. |
| `portfolio-risk-monitor` | Portfolio and watchlist risk review across concentration, quantitative risk snapshots, exposures, priority ranking, drawdown scenarios, and rebalance watch signals. |
| `trade-plan-risk-manager` | Converts market, sector, stock, catalyst, and portfolio research into non-personalized conditional trade plans with setup quality, risk triggers, execution checks, and post-trade review. |

## Installation

Install from the open-source repository:

```bash
npx skills add https://github.com/taoquo/marketlens-skills --all
```

Or clone and link/copy the skill directories into a Codex project. Every skill loads
shared rules through `../references/...`, so the top-level `references/` directory must sit
next to the skill directories:

```bash
git clone https://github.com/taoquo/marketlens-skills.git
cd marketlens-skills

mkdir -p your-project/.codex/skills

# Option A: symlink for local development
for skill in */SKILL.md; do
  ln -s "$PWD/${skill%/SKILL.md}" "your-project/.codex/skills/${skill%/SKILL.md}"
done
ln -s "$PWD/references" your-project/.codex/skills/references

# Option B: copy for a standalone project
for skill in */SKILL.md; do
  cp -R "${skill%/SKILL.md}" your-project/.codex/skills/
done
cp -R references your-project/.codex/skills/
```

Build distributable `.skill` packages from a clone:

```bash
bash scripts/build-skills.sh
ls dist/*.skill
```

## Usage

Example prompts:

```text
Use $equity-research to analyze NVIDIA's latest annual results and valuation.
Use $equity-research to review Tencent's long-term quality and key risks.
Use $market-regime-monitor to assess whether the US equity market is crowded.
Use $market-regime-monitor to assess how current liquidity affects Hong Kong and A-share markets.
Use $sector-industry-research to analyze an industry cycle and key listed-company beneficiaries.
Use $sector-industry-research to compare an export manufacturing value chain across China and global peers.
Use $catalyst-event-monitor to map the next 12 weeks of events that could change a company's thesis.
Use $catalyst-event-monitor to review whether a product launch strengthened or weakened the thesis.
Use $portfolio-risk-monitor to review a watchlist for concentration, shared risk drivers, and priority names.
Use $portfolio-risk-monitor to identify which holdings belong in add-candidate, trim-review, or exit-review buckets.
Use $trade-plan-risk-manager to convert a stock thesis into a conditional trade plan with entry, invalidation, risk unit, and review triggers.
Use $trade-plan-risk-manager to review whether a completed trade was a thesis error, timing error, risk framing error, or execution error.
```

## Data Discipline

`references/data-discipline.md` holds the rules every skill inherits. Each `SKILL.md`
adds only what is specific to its domain:

- official and primary sources first, under one shared three-tier evidence model;
- `as_of`, `published_at`, and `retrieved_at` recorded separately, never collapsed;
- a closed set of freshness grades: `Fresh`, `Lagged`, `Stale`, `Undated`, `Unavailable`;
- a core figure check with original wording, unit, period, cross-check, and one of four treatments;
- unit, currency, accounting-standard, and fiscal-calendar labelling before any cross-market comparison;
- user input classified as plan parameter, fact claim, or preference, with consistency checks before use;
- missing data marked unavailable and treated as a confidence limit, never as a directional signal.

Every skill also carries a degradation table mapping each missing or stale input to the
required handling, so a data gap changes the output in a defined way instead of being
noted and ignored.

A skill has no memory between sessions, so `references/review-and-calibration.md` defines
a `research-log/` append-only record. A call is written there when it is made, which is what
lets the 1-week, 1-month, and 3-month review cadence actually close. The directory is
gitignored and never created without asking first.

## Decision Chain

Each skill owns one layer of the research process. `references/skill-routing.md` holds
the ownership table, and `references/scoring-standard.md` holds the shared scoring and
research-label rules, the mapping from each layer to the nine shared labels, and the
binding chain constraints. When multiple skills apply, use the full chain:

```text
Market Regime -> Sector / Industry Setup -> Company Quality And Valuation -> Catalyst / Timing -> Portfolio Role And Risk -> Research Label -> Conditional Trade Plan And Risk Review
```

Release-by-release changes are tracked in [CHANGELOG.md](CHANGELOG.md).

## Examples

The `examples/` folder contains six Folio-typeset validation cases. Each case ships as
`.png` (previewed below), `.html`, and `.pdf`:

`equity-research` · NVIDIA long-term quality, valuation discipline, and research label separation.

![Equity research case](examples/marketlens-v03-equity-research-nvda.png)

`market-regime-monitor` · US technology-stock regime, liquidity/sentiment axes, and risk-budget impact.

![Market regime case](examples/marketlens-v03-market-regime-tech.png)

`sector-industry-research` · AI server supply chain, profit pools, subsector scorecard, and trade expression.

![Sector industry case](examples/marketlens-v03-sector-ai-server.png)

`catalyst-event-monitor` · Apple WWDC26 event watch, expectation gap, and trade setup discipline.

![Catalyst event case](examples/marketlens-v03-catalyst-apple-wwdc.png)

`portfolio-risk-monitor` · Equal-weight AI watchlist, concentration, factor overlap, and stress-correlation risk.

![Portfolio risk case](examples/marketlens-v03-portfolio-ai-watchlist.png)

`trade-plan-risk-manager` · NVIDIA conditional trade plan, setup quality, risk-unit framing, execution checks, and post-trade review.

![Trade plan risk case](examples/marketlens-v03-trade-plan-nvda.png)

These samples demonstrate the mandatory `Red Flags`, `Decision Impact`, `What Would Change
The View`, `Data Freshness`, `Evidence Sources`, and `Disclaimer` blocks. Scored outputs add
a `Score Summary` table; `trade-plan-risk-manager` uses `Setup Quality` instead, as allowed by
`references/scoring-standard.md`. They are output-format previews and do not constitute
investment advice.

## Validation

```bash
# structure, frontmatter, reference routing, and required output blocks
bash scripts/validate-skills.sh

# rebuild packages, then require dist/*.skill to match the working tree byte for byte
bash scripts/build-skills.sh
REQUIRE_DIST=1 bash scripts/validate-skills.sh
```

Skills are discovered from the directory layout, so a new skill needs no script or CI
edit. GitHub Actions runs the same three commands on every push and pull request.

## Disclaimer

These skills are for research and educational use only. They do not provide personalized investment, legal, tax, or financial advice. Public-market investing involves risk, including loss of principal.
