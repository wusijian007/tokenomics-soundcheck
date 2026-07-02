![tokenomics-autopsy](assets/social-preview.png)

# tokenomics-autopsy

**代币死亡螺旋的机制级"尸检" + 一套避坑设计 skill。**

[![License: CC BY 4.0](https://img.shields.io/badge/License-CC%20BY%204.0-blue.svg)](LICENSE)
[![Python 3.x](https://img.shields.io/badge/Python-3.x-3776AB?logo=python&logoColor=white)](simulations/)
[![Cases analyzed](https://img.shields.io/badge/cases-50%2B-red.svg)](加密项目代币崩溃分析_2009-2026.md)
[![Failure Skills](https://img.shields.io/badge/failure%20skills-12-purple.svg)](skills/)
![GitHub stars](https://img.shields.io/github/stars/wusijian007/tokenomics-autopsy?style=social)

> [English](README.md) | 🌐 **中文** · 许可:[CC BY 4.0](LICENSE)

> 一个开源的代币经济学**避坑知识库**:从 2009–2026 的 50+ 个标志性崩盘中,蒸馏出可复用的失败反模式、博弈论模型与可复现仿真,供未来代币项目作设计参考。
> An open-source knowledge base for tokenomics design: forensic analysis of 50+ landmark collapses distilled into reusable anti-patterns, game-theoretic models, and reproducible simulations.
>
> **研究 / 设计参考,非投资建议。** Research / design reference, **not investment advice.**

---

## 三层结构 / Three layers

| 层 | 内容 | 文件 |
|---|---|---|
| **L1 现象层** Cases | 50 个崩盘案例 + 8 类机制分类,总量估算 | [`加密项目代币崩溃分析_2009-2026.md`](加密项目代币崩溃分析_2009-2026.md) |
| **L2 机制层** Mechanisms | 统一反身性方程(λ>1)、4 个博弈模型、供需定量解剖、逐案拆解 + 仿真图 | [`代币经济学死亡螺旋_深度分析与失败Skills.md`](代币经济学死亡螺旋_深度分析与失败Skills.md) |
| **L3 知识层** Skills | 可触发的开源 skill pack:12 个失败反模式 + 可测量评分卡 + 完整审计协议 + 幸存者对照组 + 10 步设计手册 | [`skills/`](skills/) |

支撑层 / Supporting:
- [`simulations/`](simulations/) — 4 个校准过的可复现 Python 仿真,生成所有相变图表。
- [`data/`](data/) — 38 个案例的结构化数据集 + 18 案例评分卡校准(10 崩盘 vs 8 幸存者)+ 宏观总览图。
- [`validation/`](validation/README.md) — **out-of-sample 验证**:15 案例泄漏审计留出集回测 + 冻结的前瞻性预注册登记册(可证伪预测,2027/2028 复核)。

---

## 核心洞见 / The core idea

死亡螺旋**不是运气或运营失误,而是机制内生的相变**。当系统增益

```
λ = (∂fundamentals/∂price) · (∂price/∂fundamentals) > 1
```

时,代币价格本身成为机制的燃料,任何向下扰动被指数放大。健康设计保持 `λ < 1`(基本面与价格解耦)。

**一句话判据**:*如果币价归零,还有人需要这个代币吗?* 答"否" = 需求反身、无锚 → 重新设计或不做。

---

## 12 个失败 Skills(速查)/ The 12 failure Skills

分层:**引擎 engine**(制造螺旋,权重 ×3)· **结构 structure**(累积卖压,×2)· **放大器 amplifier**(放大冲击,×1)。

| # | 反模式 | 层级 | 致命阈值 |
|---|---|---|---|
| S1 | 反身性抵押 Reflexive collateral | 引擎 | corr(储备, 负债) → 1 |
| S2 | 补贴需求 Subsidized demand | 引擎 | 支出 > 收入;储备 runway < 12 月 |
| S3 | 无上限龙头 Uncapped faucet | 结构 | sink/faucet < 1 且 sink 靠新用户 |
| S4 | (3,3) 协调脆性 | 结构 | 市价/背书 > 3;收益靠增发 |
| S5 | 银行挤兑结构 Sequential redemption | 引擎 | 流动性覆盖 < 可即时赎回负债 |
| S6 | 算稳吸收壁垒 Absorbing barrier | 引擎 | 储备率 R = M/S → 1 |
| S7 | 低流通高 FDV | 结构 | 初始流通 <10%;首年解锁 >50% |
| S8 | 速度漏损 Velocity leak | 放大器 | 无价值捕获;高 velocity |
| S9 | 纯叙事需求 Narrative-only | 引擎 | 零收入;持仓集中;名人未锁 |
| S10 | 杠杆传染 Leverage contagion | 放大器 | 互为抵押;危机中相关性→1 |
| S11 | 雇佣兵积分 / 租来的 TVL | 结构 | 有机 TVL 占比 <30%;快照/TGE 悬崖 |
| S12 | 递归杠杆循环 Recursive loop | 结构 | 平仓规模 > 真实市场深度 |

详解 + 解药:[`anti-patterns.md`](skills/tokenomics-death-spiral-audit/references/anti-patterns.md) · 幸存者为何幸存(对照组):[`survivors.md`](skills/tokenomics-death-spiral-audit/references/survivors.md)

**校准(in-sample)** — 评分卡在 18 个历史案例上回测(10 个崩盘 + 8 个压力幸存者):崩盘组 12–37 分,幸存组 1–11 分,**没有任何幸存者触发引擎红线**([`data/scorecard_calibration.py`](data/scorecard_calibration.py)):

![评分卡分离度](simulations/charts/data_scorecard_separation.png)

**验证(out-of-sample)** — 另取 15 个在本库中从未出现、从未参与工具构建的案例(泄漏审计:USDN、DEI、Tomb、StrongBlock、Titano、Solidly、Blur、Celestia vs USDT、Frax、LINK、rETH、Aave、AMPL、Pendle)。原始总分在中间区间有重叠——但**引擎 → 结构 → 锚 三级判定规则 15/15 全部分类正确**,包括两个纯结构阴跌案例和一个高压幸存者([`validation/`](validation/README.md))。另有冻结的[前瞻性登记册](validation/prospective-registry.md)(Ethena、Hyperliquid、pump.fun、USDD、Jupiter + 2 个进行中案例)预注册了可证伪预测,2027/2028 复核——这是无后见之明偏差的金标准层:

![留出集分离度](simulations/charts/data_holdout_separation.png)

---

## 4 个博弈模型 / The 4 game models

| 模型 | 失败形态 | 看什么 | 仿真 |
|---|---|---|---|
| 银行挤兑 Diamond–Dybvig | 突变 | 信念冲击 | `sim4` |
| (3,3) 协调 | 塌到背书价 | 新钱增长率 | `sim2` |
| 算稳吸收壁垒 | 归零 | 储备率 R | `sim1` |
| 解锁/通胀供给 | 阴跌 | 解锁日历 | `sim3` |

详见 [`game-models.md`](skills/tokenomics-death-spiral-audit/references/game-models.md)。

---

## 快速开始 / Quick start

**15 分钟快筛**:用 [`audit-protocol.md`](skills/tokenomics-death-spiral-audit/references/audit-protocol.md) 开头的 8 问快筛 → `PASS` / `CONCERNS` / `RED LINE`。

**完整审计**(人类或 AI agent)— 按 [`audit-protocol.md`](skills/tokenomics-death-spiral-audit/references/audit-protocol.md) 走:
1. 收集输入,画机制图(每条依赖币价的流 = 候选 λ>1 回路)。
2. 用 [`game-models.md`](skills/tokenomics-death-spiral-audit/references/game-models.md) 归类博弈结构。
3. 按 [`scorecard.md`](skills/tokenomics-death-spiral-audit/references/scorecard.md) 的测量方法给 12 行打分(实例:Terra 37/54,DAI 1/54)。
4. 计算距阈值距离,用仿真压测,按模板出报告。

**设计一个代币** — 按 10 步 [`design-playbook.md`](skills/tokenomics-death-spiral-audit/references/design-playbook.md):必要性测试 → 需求锚 → 价值捕获 → 供给基准 → 熔断器 → 激励即获客成本 → 流动性方案 → 监控面板 → 发行前压测 → 上线清单。

**跑仿真 / 生成图表:**
```bash
cd simulations && python -m pip install -r requirements.txt && python run_all.py
cd ../data && python case_dataset.py && python scorecard_calibration.py
```

**作为 Claude / Agent skill 使用:** 把 `skills/tokenomics-death-spiral-audit/` 放进 skills 目录,询问代币模型设计/可持续性时会自动触发。

---

## 目录树 / Repo layout
```
cryptofail/
├── README.md                                  # 本文件
├── 加密项目代币崩溃分析_2009-2026.md            # L1 案例库
├── 代币经济学死亡螺旋_深度分析与失败Skills.md     # L2 深度分析(含仿真图)
├── skills/
│   ├── README.md
│   └── tokenomics-death-spiral-audit/
│       ├── SKILL.md                           # L3 skill 入口(4 种模式)
│       └── references/{anti-patterns,game-models,scorecard,
│                       audit-protocol,survivors,design-playbook,simulations}.md
├── simulations/
│   ├── sim1..sim4_*.py, run_all.py, viz.py, requirements.txt
│   └── charts/*.png
├── data/
│   ├── case_dataset.py / case_dataset.csv               # 38 个崩盘案例
│   └── scorecard_calibration.py / scorecard_calibration.csv  # 18 案例 in-sample 校准
└── validation/
    ├── README.md                                        # OOS 协议 + 冻结记录
    ├── holdout_backtest.py / holdout_backtest.csv       # 15 个泄漏审计留出案例
    └── prospective-registry.md / registry_scores.csv    # 冻结预测(2027/2028 复核)
```

## 许可 / License
CC BY 4.0。欢迎社区贡献新案例与新模型。数字为量级估算,请以实时数据为准;部分案例仍在诉讼中,定性以最终司法结论为准。
