# Simulations — death-spiral phase transitions

Four minimal, calibrated models that *demonstrate* the mechanism behind each
collapse archetype. No heavy dependencies (numpy + matplotlib only).

```bash
python -m pip install -r requirements.txt
python run_all.py          # regenerate all charts into ./charts/
# or run one:
python sim1_algo_stable_absorbing_barrier.py
```

| Script | Archetype | Chart |
|---|---|---|
| `sim1_algo_stable_absorbing_barrier.py` | Algo-stable (Terra) | `charts/sim1_absorbing_barrier.png` |
| `sim2_olympus_33_unraveling.py` | (3,3) (OlympusDAO) | `charts/sim2_olympus_33.png` |
| `sim3_p2e_faucet_sink.py` | Play-to-Earn (Axie/STEPN) | `charts/sim3_p2e_faucet_sink.png` |
| `sim4_bank_run_diamond_dybvig.py` | Bank run (FTX/Celsius) | `charts/sim4_bank_run.png` |

`viz.py` holds the shared chart style. See
`../skills/tokenomics-death-spiral-audit/references/simulations.md` for how to
adapt each model to your own token design.

> These are didactic models: they reproduce the *qualitative* phase transition and
> the direction of each critical condition, not precise forecasts.
