# Skill Pack — Tokenomics Death-Spiral Audit

An open-source skill distilled from forensic analysis of 50+ landmark token
collapses and **calibrated against a control group of survivors**. It helps you
**audit a token economic design for death-spiral risk** and **design resilient
tokenomics**.

## Contents
```
tokenomics-death-spiral-audit/
  SKILL.md                      # entry point: core idea, 4 modes, quick-reference, red lines
  references/
    anti-patterns.md            # the 12 failure Skills (engine/structure/amplifier) + 12 design axioms
    game-models.md              # the 4 game-theoretic models + critical conditions
    scorecard.md                # measurable 12-row scorecard + Terra & DAI worked examples + calibration
    audit-protocol.md           # 15-min quick screen + full audit procedure + report template
    survivors.md                # control group: why DAI/USDC/stETH/BNB/ETH/GMX/UNI/CRV held
    design-playbook.md          # 10-step design process, parameter benchmarks, launch checklist
    simulations.md              # how to run/adapt the 4 calibrated simulations
```

## Using it as a Claude Code / Agent skill
Drop `tokenomics-death-spiral-audit/` into your skills directory (e.g.
`~/.claude/skills/` or a plugin's `skills/`). It triggers when you ask about token
model design, sustainability, stablecoin/staking/GameFi/points/restaking
mechanics, unlock schedules, or due diligence on a token.

## Using it as a human reference
- **Evaluating a project**: `SKILL.md` → quick screen in `audit-protocol.md` →
  full audit: `game-models.md` (classify) → `scorecard.md` (measure & score) →
  `../simulations/` (stress-test) → report template.
- **Designing a token**: `design-playbook.md` end to end, with
  `anti-patterns.md` as the constraint set and `survivors.md` as the positive
  evidence base.

The deep analysis with full derivations is in the repo root:
`death-spiral-deep-analysis.md` (Chinese: `代币经济学死亡螺旋_深度分析与失败Skills.md`).

## License
CC BY 4.0. Research / design reference, **not investment advice**. Fraud cases
(S9) are detection targets, not engineering lessons. Reconcile all figures against
live data; some named cases are in ongoing litigation.
