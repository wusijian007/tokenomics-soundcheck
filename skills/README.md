# Skill Pack — Tokenomics Death-Spiral Audit

An open-source skill distilled from forensic analysis of 50+ landmark token
collapses. It helps you **audit a token economic design for death-spiral risk**
and **design resilient tokenomics**.

## Contents
```
tokenomics-death-spiral-audit/
  SKILL.md                      # entry point: the core idea, workflow, quick-reference, red lines
  references/
    anti-patterns.md            # the 10 failure Skills + 10 design axioms
    game-models.md              # the 4 game-theoretic models + critical conditions
    scorecard.md                # weighted risk scorecard + 2 worked examples (Terra; resilient)
    simulations.md              # how to run/adapt the 4 calibrated simulations
```

## Using it as a Claude Code / Agent skill
Drop `tokenomics-death-spiral-audit/` into your skills directory (e.g.
`~/.claude/skills/` or a plugin's `skills/`). It triggers when you ask about token
model design, sustainability, stablecoin/staking/GameFi mechanics, unlock
schedules, or due diligence on a token.

## Using it as a human design reference
Read `SKILL.md` → `game-models.md` (classify) → `anti-patterns.md` (check) →
`scorecard.md` (score) → run `../simulations/` to stress-test. The deep analysis
with full derivations is in the repo root: `death-spiral-deep-analysis.md`
(Chinese: `代币经济学死亡螺旋_深度分析与失败Skills.md`).

## License
CC BY 4.0. Research / design reference, **not investment advice**. Fraud cases
(S9) are detection targets, not engineering lessons. Reconcile all figures against
live data; some named cases are in ongoing litigation.
