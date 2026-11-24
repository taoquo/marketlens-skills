# 历史估值带使用教程

[English](valuation-band.md)

历史估值带只回答一个问题：**当前估值倍数处在公司自身历史的什么位置？** 它是估值层的
上下文图表和交叉校验，不是预测、目标价、均值回归概率，也不是买入/卖出信号。

方法定义在
[`equity-research/references/valuation-framework.md`](../equity-research/references/valuation-framework.md)。
本教程覆盖数据口径、仓库内的零依赖绘图脚本，以及如何读图。NVIDIA 完整案例见
[`examples/marketlens-v010-valuation-band-nvda.html`](../examples/marketlens-v010-valuation-band-nvda.html)。

## 1. 什么时候用

同时满足以下条件时，才使用 PE(TTM) 估值带：

- 归母 TTM 净利润为正，且在整个窗口内可比。
- 至少有三年交易历史；优先五年或一个完整周期。
- 窗口内业务结构、会计政策和股本没有发生结构性变化。如果发生了，只用变化后的区间，
  并在输出中说明。
- 有带日期的价格或市值序列，并能说明 TTM 分母的口径。

不要对未盈利公司、负利润公司、银行和保险（改用 P/B 对 ROE，或 P/EV）、没有正常化利润的
周期顶点、以及分母在窗口内不可比的公司使用 PE 估值带。遇到这些情况，应切换到合适的方法，
而不是硬画一条带。

估值带也不是独立标签。它可以作为交叉校验，支持 `undemanding`、`reasonable` 或
`demanding`；没有隐含变量求解和盈利质量筛子，它不能单独得出 `priced for perfection` 或
`not solvable`，也不能单独支持 `add-candidate watch`、`trim-review` 或任何行动标签。

## 2. 数据口径

### 2.1 CSV 格式

脚本接受两种输入。第一种是现成的 PE 序列：

```csv
date,pe
2026-05-13,54.80
2026-05-14,54.90
2026-05-15,55.00
```

第二种是市值和 TTM 归母净利润，脚本计算 `PE = market_cap / ttm_net_profit`：

```csv
date,market_cap,ttm_net_profit
2026-05-13,5480000000000,100000000000
2026-05-14,5490000000000,100000000000
2026-05-15,5500000000000,100000000000
```

规则：

- `PE(TTM) = 总市值 / TTM 归母净利润`。
- 用**总市值**和总股本，不用自由流通市值。A+H 或 B 股结构要包含全部股份类别。
- `TTM = 当年累计 + 上年全年 - 上年同期累计`。分母切换用**公告日**，不是报告期末。
  回测使用当时最初披露的数字，不用后来的重述。
- 标注 reported 与 adjusted；A 股另算一条扣非归母净利润序列，并报告两者差距。
- 同一条估值带里不能混用 reported 和 adjusted。
- 供应商 PE 序列属于 Tier 3 证据。能对回 filings 就对回；否则置信度封顶 Medium。
- `as_of`、`published_at`、`retrieved_at` 分开记录。

日期支持 `YYYY-MM-DD`、`YYYY/MM/DD`、`YYYYMMDD`。缺失、非数字、零或负 PE 的行会被跳过，
并在 stderr 计数。

## 3. 快速开始

脚本只依赖 Python 3.9+ 标准库。在仓库根目录运行：

```bash
python3 scripts/pe_band_chart.py \
  --input examples/data/nvda-pe-ttm-illustrative.csv \
  --output nvda-pe-band.svg \
  --table-output nvda-pe-band.csv \
  --summary-json nvda-pe-band.json
```

输出：

- `nvda-pe-band.svg`：自包含图表，含 PE 线、滚动带、当前标注和页脚。
- `nvda-pe-band.csv`：可选的 `date,pe,lower,middle,upper,percentile` 表，也是无法渲染图表时的
  表格回退。
- `nvda-pe-band.json`：可选的最新观测摘要，含当前 PE、带值、百分位、斜率、窗口和观测数。

命令还会打印一行摘要：

```text
Latest: 2026-05-15 PE 55.00 | lower 44.756 | mid 54.72 | upper 82.048 | percentile 51.33 | slope falling | window 750 | observations 1305
```

用浏览器打开 SVG，或嵌入 HTML/PDF 交付物。图表必需元素见
`valuation-framework.md` 的 Figure Contract。

仓库里的案例走 Folio 排版路径，而不是这张脚本图。案例 HTML 里放
`<figure data-folio-diagram-slot="pe-band">` 槽位，Folio 的 `embed-drawing` 用仓库跟踪的
`line-chart` fixture `examples/data/nvda-pe-band-folio.json` 填入。该路径会生成可见的无障碍
数据表、宿主适配记录和最终字号检查。无依赖脚本仍是独立图表的回退方案，并负责逐日带值表。

## 4. 参数

| 参数 | 默认值 | 含义 |
|---|---|---|
| `--input` | 必填 | CSV 路径 |
| `--output` | `pe-band.svg` | SVG 输出路径 |
| `--table-output` | 无 | 可选的逐日带值 CSV |
| `--summary-json` | 无 | 可选的最新观测 JSON 摘要 |
| `--date-col` | `date` | 日期列名 |
| `--pe-col` | `pe` | PE 列名 |
| `--market-cap-col` | `market_cap` | 没有 `pe` 时使用的市值列 |
| `--profit-col` | `ttm_net_profit` | 没有 `pe` 时使用的 TTM 利润列 |
| `--window` | `750` | 滚动窗口的观测数 |
| `--min-obs` | `250` | 开始画带所需的最小观测数 |
| `--method` | `percentile` | `percentile` 或 `mean` |
| `--lower` / `--upper` | `20` / `80` | 百分位法的上下轨；P20/P80 是 60% 中枢区间 |
| `--k` | `1.0` | 均值法的标准差倍数 |
| `--slope-window` | `250` | 斜率比较两半各自的观测数 |
| `--width` / `--height` | `960` / `520` | SVG viewBox 尺寸，均有下限 |
| `--title` | `PE(TTM) Band` | 图表标题 |
| `--subtitle` | 空 | 代码、窗口、数据日期、分母口径 |
| `--source` | 空 | 页脚来源 |
| `--note` | 滚动带声明 | 页脚第二行 |

68% 中枢区间用 P16/P84，并明确报告实际覆盖率。P20/P80 不是 68% 区间。均值法要注意原始 PE
右偏；必须说明 `k` 和经验覆盖率，原始 μ ± kσ 只能作为视觉交叉校验，优先用 log-PE 复核。

这些参数只适用于 `scripts/pe_band_chart.py`。Folio `line-chart` fixture 的画布宽度固定 960，
高度 400–720（步长 4），类别上限 12、序列上限 3。案例如何在预算内装下带，见第 8 节。

## 5. 带的计算方式

对每个日期 `t` 和滚动窗口 `W`：

1. 只取 `[t-W, t]` 内的观测，未来数据不进入计算。
2. 对样本排序。
3. 百分位法：下轨 = P20，中轨 = P50，上轨 = P80。当前百分位是样本中小于等于当前 PE 的比例。
4. 均值法：中轨 = 均值，下轨 = `max(0, 均值 - k * 标准差)`，上轨 = `均值 + k * 标准差`。
5. 斜率：比较最近 `slope-window` 个观测的中位数与前一段同长度观测的中位数；以 2% 为阈值，
   输出 `rising`、`falling` 或 `flat`。

观测数达到 `min-obs` 后开始画带。预热期使用文件开始以来已有的观测；达到 `window` 后才是
完整的滚动窗口。因此页脚写的是 `window ≤ N obs`。如果希望从第一个带点开始就是完整窗口，
把 `--min-obs` 设为与 `--window` 相同。

用全样本均值和标准差横跨整段历史，会引入未来信息。它可以作为 `all-history descriptive`
参考，但必须单独标注，不能用于百分位或信号。

## 6. 怎么读

至少报告五个读数，而不是一个：

| 读法 | 报告什么 | 为什么重要 |
|---|---|---|
| 位置 | 当前 PE 对当前下轨、中轨、上轨 | 说明价格在带内的位置，但不说明中轨是否稳定 |
| 百分位 | 窗口内小于等于当前 PE 的比例 | 不假设正态，但仍依赖窗口选择 |
| 斜率 | 最近 1–2 年滚动中位数的方向和幅度 | 中轨下移会让同一个绝对倍数看起来更便宜 |
| 环境 | 盈利趋势、利率/ERP、结构性变化 | 盈利下行的低倍数、或高利率环境下的低倍数，不等于便宜 |
| 分解 | 把价格变动拆成 EPS(TTM) 贡献和倍数贡献 | EPS 持平而价格上涨是重估；EPS 上升而倍数下降是杀估值 |

分解在对数口径下是恒等式：`log(价格) = log(EPS) + log(PE)`。用与估值带相同的窗口报告
哪一项主导。若倍数主导，变动来自折现率、仓位或情绪；若 EPS 主导，先跑盈利质量筛子，
再把它算作基本面改善。

把结果映射到五种估值读数之一：`undemanding`、`reasonable`、`demanding`、
`priced for perfection`、`not solvable`。估值带可以作为前三者的交叉校验；后两者必须依赖
隐含变量求解和盈利质量筛子。

在把低带位称为便宜之前，先跑分母检查：

- TTM 盈利质量：OCF/NI、应计比率、应收和存货对收入、研发资本化、经常性一次性项目。
- A 股：非经常性损益、政府补贴、资产处置、投资收益。
- 周期品：用中周期利润，不用峰值 TTM。周期顶部的低 PE 是警告，不是便宜。
- TTM 利润为零或为负：PE 没有定义，切换方法并把 PE 带标为 unavailable。

还要把估值带与盈利趋势、10 年期收益率或股权风险溢价配对。PE 带不是利率调整后的估值。

## 7. 在 skill 里怎么用

可以直接问 equity-research skill：

```text
Use $equity-research 给我看英伟达的 PE(TTM) 估值带，55x 在它自己的历史里处在什么位置。
Use $equity-research 把微软当前倍数放进一个五年滚动百分位带里。
```

skill 会进入 `valuation-band` 模式，输出：

- 倍数和分母口径。
- 窗口、观测数、是否覆盖完整周期。
- 带的算法和覆盖率（P20/P80、P16/P84，或 log-PE μ ± kσ）。
- 当前位置、百分位、斜率。
- 价格变动中的 EPS(TTM) 贡献和倍数贡献。
- 失败检查，以及哪些检查不可用。
- 估值读数和置信度封顶。

如果继续问“那该怎么做”，skill 会进入 `decision-framework`；估值带本身不产生行动标签。
如果宿主无法渲染图表，skill 应输出紧凑表格回退，而不是描述一张没有生成的图。

## 8. Figure Contract

`Valuation Band` 图必须包含：

- 标题：`[Company] PE(TTM) Band`。
- 副标题：代码、窗口、观测数、最后更新日期、reported 或 adjusted 口径。
- x 轴：日期；y 轴：PE(TTM)，并标出当前值。
- 一条线：point-in-time PE 序列。
- 三条线或阴影带：每个日期只用当时滚动窗口算出的下轨、中轨、上轨。Folio `line-chart` 最多
  三个序列；当 PE 线和上下轨已经占满三个序列时，把中轨放进表格和图注，而不是丢掉一条边界。
- 标注：当前 PE、当前百分位、斜率方向、当前上下轨。Folio 折线图最多三个标注，其余读数可以
  放在指标条和带读数表里。
- 页脚：来源、TTM 公式、带算法、覆盖率，以及 `descriptive, not a signal`。

规则：

- 日期 `t` 的带只能使用 `t` 及之前的观测。
- 线与带使用同一分母口径。
- 不要为了显得极端而截断 y 轴；从零开始，或在图注中说明截断。
- 宿主无法画图时，输出同字段的表格回退。
- 不能把图说成买入/卖出信号、目标价或均值回归概率。

脚本为独立 SVG 实现了这些元素。NVIDIA 案例改用 Folio 的 `line-chart`：画布 960×440，通过
`data-folio-diagram-slot` 宿主槽位嵌入；图上是从逐日序列抽出的 8 个季度样本，三条序列
（PE、P20、P80），以及当前中轨的参考线。y 轴从 20x 起，因此图注明确说明截断。
`embed-drawing` 会生成可见的 8 行数据表、宿主适配记录和最终字号检查；
`scripts/pe_band_chart.py` 仍是独立图表的回退方案，并输出逐日的
`date,pe,lower,middle,upper,percentile` 表。

## 9. NVIDIA 示例

案例数据是示例数据，不是实时行情。使用 750 个观测的滚动窗口和 P20/P80：

```bash
python3 scripts/pe_band_chart.py \
  --input examples/data/nvda-pe-ttm-illustrative.csv \
  --output nvda-pe-band.svg \
  --window 750 --min-obs 250 \
  --method percentile --lower 20 --upper 80 \
  --title "NVIDIA PE(TTM) Band" \
  --subtitle "NVDA · 1,305 observations · rolling 750-observation window · illustrative reported-basis TTM · through 2026-05-15" \
  --source "Source: illustrative dataset, not live market data" \
  --note "Point-in-time rolling band. Descriptive, not a signal, forecast, or target price."
```

结果：当前 PE 55.0x，下轨 44.8x，中轨 54.7x，上轨 82.0x，百分位 51，斜率 falling。
读数落在带中部，作为交叉校验是 `reasonable`；但中轨在下移，同一个绝对倍数比两年前更不苛刻。
2023-Q3 至 2026-Q2 的变动由 EPS 主导：价格 +452%，EPS(TTM) +875%，倍数 -43%。倍数在压缩，
盈利基础在扩张，所以价格上升不是重估。EPS 路径是示例数据，未与财报勾稽。隐含预期读数仍要求
22.5% 的十年 NOPAT CAGR，所以标签仍是 hold/watch。估值带支持估值层，但不决定标签。

案例本身走 Folio 路径。`examples/data/nvda-pe-band-folio.json` 是仓库跟踪的 `line-chart`
fixture：从逐日序列抽 8 个季度样本，三条序列（PE、P20 下轨、P80 上轨），当前中轨的参考线，
以及当前点的标注。DSL 上限是 12 个类别、3 条序列，所以案例按季度抽样而不是画 1,305 个逐日点，
中轨放在表格和图注里。填入宿主槽位：

```bash
python3.12 ~/.claude/skills/folio/scripts/folio.py embed-drawing \
  examples/data/nvda-pe-band-folio.json \
  --host-contract a4-portrait \
  --host-file path/to/host-with-pe-band-slot.html \
  --output-host path/to/filled.html \
  --artifact-dir examples/assets/folio \
  --slot pe-band \
  --caption "Illustrative reported-basis TTM; 8 quarterly samples from 1,305 daily observations; the y-axis starts at 20x. Descriptive, not a signal." \
  --profile embed
```

命令会写出图、可见的无障碍数据表和宿主适配记录。渲染前运行
`python3.12 .../folio.py verify-drawing-host path/to/filled.html`。仓库里的案例已经填好；
重建案例或把 fixture 换到别的宿主时，再走这条命令。

## 10. 表格回退

无法渲染图表时，使用 `--table-output` 的 CSV，或下面这张紧凑表：

| 日期 | PE | 下轨 | 中轨 | 上轨 | 百分位 |
|---|---:|---:|---:|---:|---:|
| 2026-05-15 | 55.00 | 44.76 | 54.72 | 82.05 | 51.33 |

再加一句文字摘要：`PE 55.0x，P20/P80 带 44.8x–82.0x，中轨 54.7x，百分位 51，斜率 falling，
750 观测窗口，共 1,305 个观测。` 不要描述没有生成的图。

Folio `embed-drawing` 路径会根据 fixture 的序列自动生成可见表格，因此图和回退表不会在绘图值上
不一致。脚本的 `--table-output` CSV 则给出每个日期的中轨和百分位；宿主需要完整逐日序列而不是
图中季度样本时，用它。

## 11. 发布前检查

- [ ] 整个窗口的 TTM 利润为正且可比。
- [ ] 至少 750 个交易日；优先 1,250 个或一个完整周期。
- [ ] 带内至少有 250 个观测。
- [ ] TTM 分母对回 filings，或把置信度封顶在 Medium。
- [ ] 明确 reported 与 adjusted 口径，且不混用。
- [ ] 使用总市值和全部股份类别；处理股本变化。
- [ ] 滚动、point-in-time；不用全样本带做信号。
- [ ] 写清窗口、观测数、算法和覆盖率。
- [ ] 报告位置、百分位、斜率、环境，以及 EPS/PE 分解。
- [ ] 跑失败检查；缺失项标为 unavailable。
- [ ] 生成图或表格回退；不虚构图表。
- [ ] Folio 折线图不超过 12 个类别、3 条序列；中轨在表格和图注里；y 轴截断已说明。
- [ ] 图注写明 `descriptive, not a signal`。
