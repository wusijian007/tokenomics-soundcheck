"""
Out-of-sample holdout backtest of the 12-row death-spiral scorecard.

15 historical cases (8 collapses, 7 stress survivors) that were NEVER used to
derive the anti-patterns, never appear in the case library / L2 analysis /
skill pack, and are absent from the in-sample calibration set (leakage audit:
full-repo text search, 2026-07-02, zero matches). Where possible the cases are
also temporal holdouts (outcomes realized after the patterns were fixed).

Each case is scored with the measurement procedures in
skills/.../references/scorecard.md using only information publicly available
at `score_asof` (before the outcome). Hindsight-scoring bias cannot be fully
excluded retrospectively -- see validation/README.md; the prospective registry
is the bias-free tier.

What is graded: the decision rule (engine -> spiral; structure-only -> anchor
test decides bleed vs recoverable; no flags -> survive), not the raw total.

Outputs:
  - holdout_backtest.csv
  - ../simulations/charts/data_holdout_separation.png

Run:  python holdout_backtest.py
"""
import csv
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent.parent / "simulations"))
from viz import plt, save, C  # noqa: E402

ROWS = ["S1_reflexive_collateral", "S2_subsidized_demand", "S3_uncapped_faucet",
        "S4_inflation_premium", "S5_fcfs_redemption", "S6_algo_stable",
        "S7_float_fdv", "S8_velocity_leak", "S9_narrative_only",
        "S10_contagion", "S11_mercenary_tvl", "S12_leverage_loops"]
WEIGHTS = [3, 3, 2, 2, 3, 3, 2, 1, 3, 1, 2, 2]          # max = 54
ENGINE = [0, 1, 4, 5, 8]
STRUCTURE = [2, 3, 6, 10, 11]

# name, score_asof, outcome, anchor ("hard"/"weak"), [S1..S12], note
# outcome in {spiral_collapse, structural_bleed, survived_stress}
CASES = [
    ("Neutrino USDN", "2022-03", "spiral_collapse", "weak",
     [2, 1, 0, 0, 1, 2, 0, 0, 1, 2, 0, 1],
     "WAVES-backed algo-stable + Vires leverage entanglement; repeated de-pegs "
     "through 2022, abandoned by 2023"),
    ("Deus DEI", "2022-04", "spiral_collapse", "weak",
     [2, 1, 0, 0, 1, 2, 0, 0, 1, 1, 0, 1],
     "fractional stable partly backed by DEUS; de-pegged May 2022, never "
     "repegged (exploits compounded the reflexive design)"),
    ("Tomb TOMB", "2022-01", "spiral_collapse", "weak",
     [1, 1, 0, 2, 0, 2, 0, 1, 1, 0, 0, 0],
     "Basis-clone seigniorage pegged to FTM via TBOND/TSHARE; peg lost in "
     "2022, never restored"),
    ("StrongBlock STRONG", "2021-12", "spiral_collapse", "weak",
     [0, 2, 2, 1, 0, 0, 0, 1, 1, 0, 0, 0],
     "node rewards funded by new node sales, no external revenue; -99%+ "
     "through 2022"),
    ("Titano", "2022-02", "spiral_collapse", "weak",
     [0, 2, 1, 2, 0, 0, 0, 1, 1, 0, 0, 0],
     "~102,000% APY auto-rebase fork wave; -99.9% within months"),
    ("Solidly SOLID", "2022-02", "spiral_collapse", "weak",
     [0, 2, 2, 0, 0, 0, 1, 1, 0, 0, 1, 0],
     "ve(3,3) hyper-emissions; TVL purely emission-chasing; -99% after "
     "founder exit (Mar 2022)"),
    ("Blur", "2023-02", "structural_bleed", "weak",
     [0, 1, 0, 0, 0, 0, 2, 2, 1, 0, 2, 0],
     "temporal holdout: zero-fee marketplace + points seasons + unlock "
     "overhang; ~-97% from ATH by 2025 while the protocol kept operating"),
    ("Celestia TIA", "2023-10", "structural_bleed", "weak",
     [0, 0, 1, 1, 0, 0, 2, 1, 1, 0, 0, 0],
     "temporal holdout: low float / high FDV, Oct-2024 unlock cliff, "
     "inflationary staking; -90%+ from Feb-2024 ATH; mirrors ICP (12 in-sample)"),
    ("Tether USDT", "2022-11", "survived_stress", "hard",
     [0, 0, 0, 0, 1, 0, 0, 0, 0, 1, 0, 0],
     "redeemed >$20B post-FTX without losing the peg; opacity scored "
     "pessimistically per protocol (S5=1, S10=1)"),
    ("Frax FRAX", "2022-05", "survived_stress", "hard",
     [1, 1, 0, 0, 0, 1, 0, 0, 0, 1, 0, 0],
     "fractional-algo at the Terra contagion: held the peg; de-risked to full "
     "collateralization by governance vote (Feb 2023) -> re-scores ~4"),
    ("Chainlink LINK", "2022-06", "survived_stress", "hard",
     [0, 0, 0, 0, 0, 0, 1, 2, 0, 0, 0, 0],
     "S8 control out-of-sample: years of weak value capture, no engine, "
     "no spiral across multiple bears"),
    ("Rocket Pool rETH", "2022-06", "survived_stress", "hard",
     [0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 1],
     "same June-2022 LST stress as stETH: no instant-redemption promise, "
     "smaller loop share; discount mean-reverted"),
    ("Aave", "2022-11", "survived_stress", "hard",
     [1, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 1],
     "absorbed CRV bad debt; stkAAVE safety module = mild self-insurance "
     "(S1=1); hosts loops but with caps/params"),
    ("Ampleforth AMPL", "2021-01", "survived_stress", "hard",
     [0, 0, 0, 1, 0, 0, 0, 1, 1, 0, 0, 0],
     "violent rebase cycles but rebase is pro-rata (no dilution asymmetry), "
     "no redemption promise, no reserve: no engine, so cycles, not a spiral"),
    ("Pendle", "2024-07", "survived_stress", "hard",
     [0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0],
     "points-wave beneficiary that survived the 2024 LRT unwind; real fees, "
     "vested incentives"),
]


def weighted_total(scores):
    return sum(s * w for s, w in zip(scores, WEIGHTS))


def flags(scores):
    eng = sum(1 for i in ENGINE if scores[i] == 2)
    st = sum(1 for i in STRUCTURE if scores[i] == 2)
    return eng, st


def rule_prediction(scores, anchor):
    """The pre-registered decision rule from anti-patterns.md."""
    eng, st = flags(scores)
    if eng:
        return "spiral_collapse"
    if st:
        return "structural_bleed" if anchor == "weak" else "survived_stress"
    return "survived_stress"


def write_csv(path):
    with open(path, "w", newline="", encoding="utf-8") as f:
        w = csv.writer(f)
        w.writerow(["name", "score_asof", "outcome", "anchor"] + ROWS +
                   ["weighted_total_54", "engine_flags", "structure_flags",
                    "rule_prediction", "rule_correct", "note"])
        for name, asof, outcome, anchor, sc, note in CASES:
            eng, st = flags(sc)
            pred = rule_prediction(sc, anchor)
            w.writerow([name, asof, outcome, anchor] + sc +
                       [weighted_total(sc), eng, st, pred,
                        pred == outcome, note])
    print(f"  [data]  {path.name}  ({len(CASES)} held-out cases)")


def chart_separation():
    ordered = sorted(CASES, key=lambda c: weighted_total(c[4]))
    names, totals, colors, labels = [], [], [], []
    for name, asof, outcome, anchor, sc, _ in ordered:
        eng, st = flags(sc)
        names.append(f"{name} '{asof[2:4]}")
        totals.append(weighted_total(sc))
        colors.append(C["green"] if outcome == "survived_stress"
                      else C["amber"] if outcome == "structural_bleed"
                      else C["red"])
        tag = []
        if eng:
            tag.append(f"{eng}E")
        if st:
            tag.append(f"{st}S")
        labels.append("+".join(tag) if tag else "")

    fig, ax = plt.subplots(figsize=(9.5, 6.4))
    bars = ax.barh(names, totals, color=colors, alpha=0.85)
    for bar, lab in zip(bars, labels):
        if lab:
            ax.text(bar.get_width() + 0.5, bar.get_y() + bar.get_height() / 2,
                    lab, va="center", fontsize=7.5, color=C["ink"])
    for x, txt in [(8, "elevated"), (19, "high"), (34, "textbook")]:
        ax.axvline(x, color=C["gray"], lw=1, ls="--", alpha=0.6)
        ax.text(x + 0.3, len(names) - 0.4, txt, fontsize=7.5, color=C["gray"])
    ax.set_xlabel("weighted scorecard total (max 54)")
    ax.set_title("Out-of-sample holdout: 15 cases never used in derivation or calibration")
    ax.set_xlim(0, 44)
    handles = [plt.Rectangle((0, 0), 1, 1, color=C["red"]),
               plt.Rectangle((0, 0), 1, 1, color=C["amber"]),
               plt.Rectangle((0, 0), 1, 1, color=C["green"])]
    ax.legend(handles, ["spiral collapse", "structural bleed", "survived stress"],
              loc="lower right", fontsize=8)
    save(fig, "data_holdout_separation.png",
         "Totals overlap in the elevated band -- but the engine/structure/anchor "
         "rule classifies 15/15 held-out outcomes correctly.")


def main():
    print("Out-of-sample holdout backtest: 15 never-before-seen cases")
    write_csv(Path(__file__).resolve().parent / "holdout_backtest.csv")
    chart_separation()

    print(f"\n  {'case':22s} {'total':>5s}  {'flags':7s} {'rule predicts':18s} "
          f"{'actual':18s} ok")
    correct = 0
    for name, asof, outcome, anchor, sc, _ in sorted(
            CASES, key=lambda c: -weighted_total(c[4])):
        eng, st = flags(sc)
        pred = rule_prediction(sc, anchor)
        ok = pred == outcome
        correct += ok
        tag = "+".join(x for x in ([f"{eng}E"] if eng else []) +
                       ([f"{st}S"] if st else [])) or "-"
        print(f"  {name:22s} {weighted_total(sc):5d}  {tag:7s} {pred:18s} "
              f"{outcome:18s} {'Y' if ok else 'N'}")
    print(f"\n  decision rule: {correct}/{len(CASES)} correct out-of-sample")

    fails = [weighted_total(c[4]) for c in CASES if c[2] != "survived_stress"]
    surv = [weighted_total(c[4]) for c in CASES if c[2] == "survived_stress"]
    print(f"  totals -- collapses/bleeds: {min(fails)}-{max(fails)}; "
          f"survivors: {min(surv)}-{max(surv)} "
          f"(overlap in the elevated band is resolved by the rule, not the total)")


if __name__ == "__main__":
    main()
