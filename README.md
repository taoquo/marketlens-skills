# MarketLens Skills

[中文文档](README.zh-CN.md)

MarketLens Skills is a publishable skill repository for AI-assisted public-market research.

Repository: https://github.com/taoquo/marketlens-skills

It provides four production-oriented skills:

| Skill | Purpose |
|---|---|
| `equity-research` | Equity research for US, Hong Kong, and A-share listed companies, covering earnings, fundamentals, valuation, moat, regional disclosures, red flags, and data freshness. |
| `market-regime-monitor` | Market regime monitoring across liquidity, sentiment, positioning, valuation crowding, scoring confidence, and cross-market risk transmission. |
| `sector-industry-research` | Sector and industry research across cycle stage, supply-demand, value chains, policy/technology shifts, peer structure, and listed-company read-through. |
| `catalyst-event-monitor` | Event-driven research for upcoming catalysts, expectation gaps, scenario paths, pre-event watch data, and post-event thesis updates. |

## Installation

Install from the open-source repository:

```bash
npx skills add https://github.com/taoquo/marketlens-skills --all
```

Or clone and link/copy the skill directories into a Codex project:

```bash
git clone https://github.com/taoquo/marketlens-skills.git
cd marketlens-skills

# Option A: symlink for local development
mkdir -p your-project/.codex/skills
ln -s "$PWD/equity-research" your-project/.codex/skills/equity-research
ln -s "$PWD/market-regime-monitor" your-project/.codex/skills/market-regime-monitor
ln -s "$PWD/sector-industry-research" your-project/.codex/skills/sector-industry-research
ln -s "$PWD/catalyst-event-monitor" your-project/.codex/skills/catalyst-event-monitor

# Option B: copy for a standalone project
cp -R equity-research your-project/.codex/skills/
cp -R market-regime-monitor your-project/.codex/skills/
cp -R sector-industry-research your-project/.codex/skills/
cp -R catalyst-event-monitor your-project/.codex/skills/
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
```

## Data Freshness

All skills require:

- official and primary sources first;
- `as_of`, `published_at`, and `retrieved_at` timestamps when available;
- TTL-based freshness checks;
- cross-checking price-sensitive or regime-sensitive conclusions;
- marking missing data as unavailable instead of turning it into a directional signal.

## v0.2 Research Discipline

This release adds stricter conclusion gates:

- equity research must downgrade conclusions when price, filings, valuation inputs, or primary sources are missing;
- sector research must downgrade conclusions when industry scope, dated demand/supply evidence, peer set, or primary sources are missing;
- catalyst research must downgrade conclusions when event timing, source quality, expectation baseline, or post-event review criteria are missing;
- valuation work now includes sector-specific methods for financials, REITs, cyclicals, platforms, exporters, and pre-profit biotech;
- market regime calls now use indicator scoring, confidence levels, conflict handling, causal channels, and explicit view-change triggers.

## Examples

The `examples/` folder contains a Folio-typeset NVIDIA equity research preview generated with `$equity-research`:

![NVIDIA equity research sample](examples/nvidia-nvda-equity-report.png)

The sample demonstrates source dating, data freshness tables, conclusion downgrades when price-sensitive gates are incomplete, and a research-only disclaimer. It is an output-format preview and does not constitute investment advice.

## Validation

```bash
bash scripts/validate-skills.sh
```

## Disclaimer

These skills are for research and educational use only. They do not provide personalized investment, legal, tax, or financial advice. Public-market investing involves risk, including loss of principal.
