# MarketLens Skills

[中文文档](README.zh-CN.md)

MarketLens Skills is a publishable skill repository for AI-assisted public-market research.

Repository: https://github.com/taoquo/marketlens-skills

It provides two production-oriented skills:

| Skill | Purpose |
|---|---|
| `equity-research` | Equity research for US, Hong Kong, and A-share listed companies, covering earnings, fundamentals, valuation, moat, regional disclosures, and data freshness. |
| `market-regime-monitor` | Market regime monitoring across liquidity, sentiment, positioning, valuation crowding, and cross-market risk conditions. |

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

# Option B: copy for a standalone project
cp -R equity-research your-project/.codex/skills/
cp -R market-regime-monitor your-project/.codex/skills/
```

Build distributable `.skill` packages from a clone:

```bash
bash scripts/build-skills.sh
ls dist/*.skill
```

## Usage

Example prompts:

```text
Use $equity-research to analyze Tencent's long-term value.
Use $equity-research to review Kweichow Moutai's latest earnings.
Use $market-regime-monitor to assess whether the US equity market is crowded.
Use $market-regime-monitor to assess how current liquidity affects Hong Kong and A-share markets.
```

## Data Freshness

Both skills require:

- official and primary sources first;
- `as_of`, `published_at`, and `retrieved_at` timestamps when available;
- TTL-based freshness checks;
- cross-checking price-sensitive or regime-sensitive conclusions;
- marking missing data as unavailable instead of turning it into a directional signal.

## Examples

The `examples/` folder contains a sample one-page equity research report. It is included only as an output example and does not constitute investment advice.

## Validation

```bash
bash scripts/validate-skills.sh
```

## Disclaimer

These skills are for research and educational use only. They do not provide personalized investment, legal, tax, or financial advice. Public-market investing involves risk, including loss of principal.
