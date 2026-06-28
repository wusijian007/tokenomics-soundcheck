# Death-Spiral Risk Scorecard

Score each row 0 (absent) / 1 (partial) / 2 (clearly present). Multiply by the
weight. Sum. Any **×3 row scoring 2 is a red line** — fix it before anything else.

| # | Red flag | Skill | Weight | 0/1/2 | Weighted |
|---|---|---|---|---|---|
| 1 | Collateral/reserve correlated with the native token | S1, S6 | ×3 | | |
| 2 | Core demand from subsidized APY, not real revenue | S2 | ×3 | | |
| 3 | Reward token has no supply cap; sink needs new users | S3 | ×2 | | |
| 4 | High APY from inflation; price ≫ backing | S4 | ×2 | | |
| 5 | Instant FCFS redemption against illiquid assets | S5 | ×3 | | |
| 6 | Algo-stablecoin self-collateralized, no circuit breaker | S6 | ×3 | | |
| 7 | Initial float <10% or first-year unlock >50% of float | S7 | ×2 | | |
| 8 | No value capture; high velocity | S8 | ×1 | | |
| 9 | Pure narrative/celebrity demand, zero cash flow, concentrated | S9 | ×3 | | |
| 10 | Deeply interlinked collateral/MM with other protocols | S10 | ×1 | | |

**Max weighted score = 46.**

| Score | Verdict |
|---|---|
| 0–6 | Low *structural* death-spiral risk (market risk still applies). |
| 7–15 | Reflexive design present; require explicit critical conditions + circuit breakers. |
| 16–28 | High risk; one or two `λ>1` engines — hidden in a bull market, exposed in a bear. |
| ≥29 | Textbook death-spiral model; historical peers almost all went to ~0. |

Usage: for every row scored 2, jump to that anti-pattern's **antidote** in
`anti-patterns.md` and redesign. Prioritize the ×3 rows.

---

## Worked example — Terra (LUNA/UST), early 2022

| # | Red flag | Score | Weighted | Note |
|---|---|---|---|---|
| 1 | Collateral correlated with native token | 2 | 6 | UST "backed" by LUNA — perfectly reflexive |
| 2 | Subsidized APY demand | 2 | 6 | Anchor 19.5%, reserve depleting, ≈75% of UST |
| 3 | Uncapped reward faucet | 0 | 0 | n/a |
| 4 | (3,3) inflation premium | 1 | 2 | Anchor-driven, indirect |
| 5 | Instant FCFS redemption | 2 | 6 | Anchor instant withdrawals were the run vector |
| 6 | Self-collateralized algo-stable, no breaker | 2 | 6 | the core mechanism; no reserve-ratio breaker |
| 7 | Float/FDV asymmetry | 0 | 0 | n/a |
| 8 | Velocity leak | 0 | 0 | n/a |
| 9 | Narrative-only demand | 1 | 3 | "stablecoin of the future" narrative amplified it |
| 10 | Leverage contagion | 2 | 2 | 3AC/Celsius/Voyager/FTX exposure |
| | **Total** | | **31 / 46** | **≥29 → textbook death-spiral** |

Three ×3 red lines (rows 1, 5, 6) fired simultaneously — the worst possible
combination: reflexive collateral + a bank-run vector + a seigniorage absorbing
barrier with no circuit breaker.

---

## Worked example — a resilient design (target profile)

A well-designed protocol should score **0–6**: exogenous overcollateralization
(row 1 = 0), real-yield (row 2 = 0), capped/sink-bound emissions (row 3 = 0),
queued or pro-rata redemption with >100% liquidity coverage (row 5 = 0), no
self-collateralized stablecoin (row 6 = 0), linear milestone-gated unlocks with
healthy float (row 7 = 0), fee-share/ve value capture (row 8 = 0), real cash-flow
demand that passes the zero-price test (row 9 = 0), isolated collateral (row 10 = 0).
