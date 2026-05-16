# MarketLens Skills

[English](README.md)

MarketLens Skills 是一个可发布的金融投研 Skill 仓库，用于 AI 辅助公开市场研究。

仓库地址：https://github.com/taoquo/marketlens-skills

当前包含五个面向生产使用的 Skill：

| Skill | 用途 |
|---|---|
| `equity-research` | 覆盖美股、港股、A股的个股研究，包含质量评分、财报、基本面、估值、护城河、区域披露规则、风险信号和数据实效性。 |
| `market-regime-monitor` | 市场环境判断，覆盖流动性、情绪、仓位、估值拥挤度、置信度评分、风险预算影响和跨市场风险传导。 |
| `sector-industry-research` | 行业与产业链研究，覆盖周期位置、供需、库存、价格、产能、利润池、政策/技术变化、交易表达、同业比较和上市公司映射。 |
| `catalyst-event-monitor` | 事件驱动研究，覆盖未来催化、预期差、市场定价、交易设定、情景路径、事件前观察数据和事件后 thesis 更新。 |
| `portfolio-risk-monitor` | 组合与观察池风险体检，覆盖集中度、轻量量化风险快照、风险暴露、优先级排序、回撤情景和再平衡观察信号。 |

## 安装

从开源仓库安装：

```bash
npx skills add https://github.com/taoquo/marketlens-skills --all
```

或者克隆仓库后，把 skill 软链接/复制到 Codex 项目：

```bash
git clone https://github.com/taoquo/marketlens-skills.git
cd marketlens-skills

# 方式 A：本地开发时使用软链接
mkdir -p your-project/.codex/skills
ln -s "$PWD/equity-research" your-project/.codex/skills/equity-research
ln -s "$PWD/market-regime-monitor" your-project/.codex/skills/market-regime-monitor
ln -s "$PWD/sector-industry-research" your-project/.codex/skills/sector-industry-research
ln -s "$PWD/catalyst-event-monitor" your-project/.codex/skills/catalyst-event-monitor
ln -s "$PWD/portfolio-risk-monitor" your-project/.codex/skills/portfolio-risk-monitor

# 方式 B：复制到独立项目
cp -R equity-research your-project/.codex/skills/
cp -R market-regime-monitor your-project/.codex/skills/
cp -R sector-industry-research your-project/.codex/skills/
cp -R catalyst-event-monitor your-project/.codex/skills/
cp -R portfolio-risk-monitor your-project/.codex/skills/
```

从克隆仓库构建可分发 `.skill` 包：

```bash
bash scripts/build-skills.sh
ls dist/*.skill
```

## 使用示例

```text
Use $equity-research 分析英伟达最新年度财报和估值。
Use $equity-research 分析腾讯控股的长期质量和关键风险。
Use $market-regime-monitor 现在美股市场是不是太拥挤。
Use $market-regime-monitor 当前流动性对港股/A股影响如何。
Use $sector-industry-research 分析某个行业周期和关键上市公司受益方向。
Use $sector-industry-research 比较中国和全球出口制造产业链的利润池变化。
Use $catalyst-event-monitor 梳理某家公司未来 12 周可能改变 thesis 的事件。
Use $catalyst-event-monitor 复盘一次产品发布是否强化或削弱了原 thesis。
Use $portfolio-risk-monitor 检查观察池的集中度、共同风险因子和优先级。
Use $portfolio-risk-monitor 判断哪些持仓应进入加仓候选、减仓复核或退出复核观察桶。
```

## 数据实效性

所有 Skill 都要求：

- 优先使用官方源和一手来源；
- 尽量记录 `as_of`、`published_at`、`retrieved_at`；
- 按 TTL 判断数据是否过期；
- 对价格敏感或市场状态敏感的结论做交叉验证；
- 缺失数据只能标记为 unavailable，不得硬转成看多或看空信号。

## v0.2 研究纪律

本版本加入更严格的结论门槛：

- 个股研究在价格、财报、估值输入或一手来源不足时，必须降级结论；
- 行业研究在行业边界、供需证据、同业集合或一手来源不足时，必须降级结论；
- 事件研究在事件时间、来源质量、预期基线或事件后复盘标准不足时，必须降级结论；
- 组合研究在持仓、权重/假设、价格日期或风险驱动证据不足时，必须降级结论；
- 估值框架扩展到金融、REIT、周期股、平台互联网、出口制造和 pre-profit biotech 等行业；
- 市场环境判断加入指标打分、置信度、冲突处理、传导机制和反证触发条件。

## v0.3 评分与交易纪律

本版本统一所有 skill 的评分和研究标签体系：

- 统一 0-3 评分方向、置信度、数据质量、红线覆盖项和可使用的研究标签；
- 市场环境分数保留为独立的环境压力分，只用于调整风险预算语言，不机械加减个股或组合总分；
- 事件研究新增交易设定层，区分事件重要性和是否值得交易，覆盖 consensus view、variant view、市场隐含预期、implied move、赔率判断、失效证据和事件后复盘窗口；
- 组合研究新增轻量量化风险快照，覆盖单名集中度、Top 3/Top 5 暴露、行业/主题/因子重叠、流动性、压力期相关性和回撤贡献；
- 所有带评分的输出统一包含 `Score Summary`、`Red Flags`、`Decision Impact` 和 `What Would Change The View`；
- 研究结论纳入复盘校准循环，记录原始评分、证据、1周/1月/3月结果、错误归因和规则调整。

多个 skill 同时适用时，按完整决策链处理：

```text
市场环境 -> 行业/产业设置 -> 公司质量与估值 -> 催化剂/时机 -> 组合角色与风险 -> 研究标签
```

## 示例

`examples/` 目录包含 5 个使用 Folio 排版的 v0.3 验证案例，每个 Skill 一个独立案例：

`equity-research` · NVIDIA 长期质量、估值纪律和研究标签分离。

![个股研究案例](examples/marketlens-v03-equity-research-nvda.png)

`market-regime-monitor` · 美股科技股市场环境、流动性/情绪双轴和风险预算影响。

![市场环境案例](examples/marketlens-v03-market-regime-tech.png)

`sector-industry-research` · AI 服务器产业链、利润池、子行业评分和交易表达。

![行业研究案例](examples/marketlens-v03-sector-ai-server.png)

`catalyst-event-monitor` · Apple WWDC26 事件观察、预期差和交易设定纪律。

![事件催化案例](examples/marketlens-v03-catalyst-apple-wwdc.png)

`portfolio-risk-monitor` · 等权 AI 观察池、集中度、因子重叠和压力期相关性风险。

![组合风险案例](examples/marketlens-v03-portfolio-ai-watchlist.png)

这些案例展示统一的 `Score Summary`、`Red Flags`、`Decision Impact`、`What Would Change The View`，以及事件交易设定和组合量化风险快照。它们只用于展示输出预览，不构成投资建议。

## 校验

```bash
bash scripts/validate-skills.sh
```

## 免责声明

本仓库 Skill 仅用于研究和教育参考，不提供个性化投资、法律、税务或财务建议。公开市场投资存在风险，可能损失本金。
