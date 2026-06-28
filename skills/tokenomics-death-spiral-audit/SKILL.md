---
name: tokenomics-death-spiral-audit
description: >
  Audit a crypto/Web3 token economic design for death-spiral (reflexive collapse)
  risk, and guide the design of resilient tokenomics. Use whenever someone is
  designing, reviewing, or doing due diligence on a token model, stablecoin,
  staking/yield mechanism, GameFi/Play-to-Earn economy, points/airdrop program,
  bonding/treasury (3,3) system, or token unlock/emission schedule — or asks
  "will this tokenomics work", "is this sustainable", "what's the risk in this
  token model", or "how do I design tokenomics that won't collapse". Built from
  forensic analysis of 50+ landmark collapses (Terra, OlympusDAO, Axie, FTX, ICP…).
license: Open-source (CC BY 4.0). Research / design reference, NOT investment advice.
---

# Tokenomics Death-Spiral Audit

A death spiral is **not bad luck or bad ops — it is a built-in phase transition.**
A token model with reflexive feedback is a stable attractor above a critical
parameter and jumps to a different attractor (→ 0, or → backing) once that
threshold is crossed. This skill finds the threshold *before* it is crossed.

## The one idea that explains every collapse

Every death spiral is a **positive feedback loop** where the token's own price is
the fuel for the mechanism:

```
price ↓ → mechanism is forced to mint / sell / liquidate / redeem → supply ↑ / demand ↓ → price ↓↓
```

Formally, the system gain is `λ = (∂g/∂F)·(∂h/∂P)`, where `P` is price and `F` is
"fundamentals". Healthy projects keep `∂(fundamentals)/∂(price) ≈ 0` so `λ < 1`
(self-correcting). Death-spiral projects wire fundamentals *to* price (collateral
is the token itself, demand is an APY, rewards depend on new users) so `λ > 1`
and any downward nudge is amplified.

**The master test:** *If the token's price went to zero, would anyone still need
this token?* If the answer is "no", demand is reflexive and unanchored — redesign
or walk away.

## How to use this skill

### Mode A — Auditing an existing/proposed design
1. **Classify the mechanism.** Read `references/game-models.md` and place the
   design into one (or more) of the 4 structures: bank run, (3,3) coordination,
   seigniorage absorbing barrier, unlock/inflation supply glut.
2. **Run the anti-pattern checklist.** Go through all 10 patterns in
   `references/anti-patterns.md`. For each, check the *quantitative red flags*.
3. **Score it.** Fill in the scorecard in `references/scorecard.md` (weighted).
   Any item scoring 2 on a ×3-weight row is a red line.
4. **Locate the critical condition.** For each triggered pattern, state the
   explicit threshold (e.g. reserve ratio `R = M/S → 1`, new-money growth <
   dilution, sink/faucet < 1, liquidity coverage < redeemable liabilities).
5. **Prescribe the antidote.** Each anti-pattern ships a concrete design fix.
6. **Report**: mechanism class → triggered patterns → critical thresholds →
   score → prioritized fixes.

### Mode B — Designing resilient tokenomics from scratch
Invert the anti-patterns into the 10 design axioms at the end of
`references/anti-patterns.md`. The non-negotiable one is axiom #1: **decouple
fundamentals from price (`λ < 1`)** — every other axiom serves it.

### Mode C — Demonstrating / stress-testing a mechanism
The `simulations/` folder (see `references/simulations.md`) has runnable, calibrated
models for the 4 archetypes. Use them to *show* the phase transition, fit the
critical parameter to a specific design, or generate charts for a report.

## Quick-reference: the 10 failure Skills

| # | Anti-pattern | One-line tell | Killer threshold |
|---|---|---|---|
| S1 | Reflexive collateral | reserve = the token itself | corr(reserve, liability) → 1 |
| S2 | Subsidized demand engine | APY paid from subsidy, not revenue | payout > revenue; reserve runway < 12mo |
| S3 | Uncapped faucet | reward token has no supply cap | sink/faucet < 1, sink needs new users |
| S4 | (3,3) coordination fragility | "everyone stakes = best" | price/backing > 3; yield from inflation |
| S5 | Sequential-service redemption | instant first-come-first-served + illiquid | liquidity coverage < redeemable liabilities |
| S6 | Seigniorage absorbing barrier | mint/burn dual-token stable | reserve ratio R = M/S → 1 |
| S7 | Float–FDV asymmetry | low float, high FDV, cheap insiders | float <10%; 1yr unlock >50% of float |
| S8 | Velocity leak | pure medium-of-exchange, no capture | no burn/lock/fee-share; high velocity |
| S9 | Narrative-only demand | celeb/meme, zero cash flow | no revenue; concentrated, unlocked holders |
| S10 | Leverage contagion | tokens cross-collateralize each other | shared MM/collateral; corr→1 in stress |

Full detail, instances, and antidotes: `references/anti-patterns.md`.

## Hard red lines (auto-fail)
- Algorithmic stablecoin collateralized by its own/affiliated token, no reserve circuit-breaker. (S6+S1 → Terra, Iron)
- Yield whose source is unidentifiable or is "the next depositor". (S2 → Anchor, HEX)
- Reward emission with no cap whose only sink is user growth. (S3 → Axie, STEPN)
- Instant full redemption promised against illiquid/maturity-mismatched assets. (S5 → FTX, Celsius)
- Demand that fails the zero-price test (100% narrative/APY/celebrity). (S9 → LIBRA, SQUID)

## Scope & honesty
Research and design reference, **not investment advice**. Ponzi/rug cases (S9) are
*fraud*, not failed engineering — for those, the skill's value is detection, not
repair. Estimates in the data layer are order-of-magnitude; reconcile against live
data. Several named cases involve ongoing litigation — defer to final rulings.
