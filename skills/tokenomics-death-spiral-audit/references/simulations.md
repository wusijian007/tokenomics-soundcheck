# Runnable Simulations

Four calibrated, dependency-light models that *demonstrate* the phase transition
behind each game model. Use them to (a) build intuition, (b) fit a critical
parameter to a specific design, or (c) generate charts for a report.

## Setup
```bash
cd simulations
python -m pip install -r requirements.txt   # numpy + matplotlib
python run_all.py                            # regenerate every chart into charts/
```
Each script is standalone and self-documenting: `python sim1_algo_stable_absorbing_barrier.py`.

## What each shows

| Script | Game model | Calibrated to | Headline result |
|---|---|---|---|
| `sim1_algo_stable_absorbing_barrier.py` | M3 Absorbing barrier | Terra (R₀≈2.2, UST $18B, LUNA $40B) | A 2.2× reserve tolerates only a ~14% run; the buffer is reflexive, not real. Phase diagram of the `R=1` absorbing barrier. |
| `sim2_olympus_33_unraveling.py` | M2 (3,3) | OHM (premium ≈13.8×, APY ~7000%) | Premium collapses to **backing, not zero** (−92%). Bifurcation: premium needs perpetual new money > dilution. |
| `sim3_p2e_faucet_sink.py` | M4 Inflation glut | Axie SLP (mint ≈4× burn) | Boom→saturation→bust; uncapped → ~0, capped (mint≤burn) survives the same demand shock. |
| `sim4_bank_run_diamond_dybvig.py` | M1 Bank run | FTX/Celsius | Sequential service: ~51% of scenarios self-fulfill a run; pro-rata: ~17% (only extreme panic). |

## How to adapt to your design
- **Stablecoin**: set `sim1.simulate(R0=...)` to your reserve/liability ratio and
  `liq_frac` to your reserve token's real market depth; read off the critical run %.
- **Staking/(3,3)**: set `sim2` `dilution` to your rebase rate; the bifurcation's
  critical inflow = your dilution rate is the minimum sustainable new-money growth.
- **GameFi**: set `sim3` `sell_frac`, `buy_per_new`, `capacity` to your economy;
  toggle `capped=True` to test an emission-bound-to-sink policy.
- **Lending/exchange**: set `sim4` liquidity coverage `L`; compare sequential vs
  pro-rata to quantify how much a redemption-queue design shrinks your run basin.

## Modeling notes (honesty)
These are **minimal didactic models**, not forecasting tools. They reproduce the
*qualitative* phase transition and the *direction* of each critical condition;
absolute numbers depend on calibration. The point is structural: each model shows
that the failure is a property of the mechanism (`λ>1`), reachable from
realistic parameters, not an exogenous accident.

Charts are written to `simulations/charts/` and embedded in the analysis docs.
Chart text is in English to avoid CJK font issues across machines.
