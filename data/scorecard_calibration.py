"""
Scorecard calibration: back-score 18 historical cases (10 collapses, 8 stress
survivors) on the 12-row death-spiral scorecard and show the separation.

Scores are ORDER-OF-MAGNITUDE, scored *at each case's stress point* using the
measurement procedures in skills/.../references/scorecard.md. This is in-sample
calibration (the same record the anti-patterns were distilled from), meant to
check the instrument's consistency, not out-of-sample validation.

Outputs:
  - scorecard_calibration.csv           (case x 12-row score matrix + totals)
  - ../simulations/charts/data_scorecard_separation.png

Run:  python scorecard_calibration.py
"""
import csv
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent.parent / "simulations"))
from viz import plt, save, C  # noqa: E402

# Scorecard rows (S1..S12) and weights; engine x3, structure x2, amplifier x1.
ROWS = ["S1_reflexive_collateral", "S2_subsidized_demand", "S3_uncapped_faucet",
        "S4_inflation_premium", "S5_fcfs_redemption", "S6_algo_stable",
        "S7_float_fdv", "S8_velocity_leak", "S9_narrative_only",
        "S10_contagion", "S11_mercenary_tvl", "S12_leverage_loops"]
WEIGHTS = [3, 3, 2, 2, 3, 3, 2, 1, 3, 1, 2, 2]          # max = 54
ENGINE = [0, 1, 4, 5, 8]        # indices of x3 rows (S1 S2 S5 S6 S9)
STRUCTURE = [2, 3, 6, 10, 11]   # indices of x2 rows (S3 S4 S7 S11 S12)

# name, stress year, outcome, [S1..S12], one-line note
CASES = [
    ("Terra/LUNA-UST", 2022, "collapsed",
     [2, 2, 0, 1, 2, 2, 0, 0, 1, 2, 1, 2],
     "4 engines at once: reflexive collateral + Anchor subsidy + run vector + absorbing barrier"),
    ("Iron Finance", 2021, "collapsed",
     [2, 1, 0, 1, 2, 2, 0, 0, 1, 0, 0, 0],
     "partial-algo stable; TITAN mint on de-peg; first large DeFi bank run"),
    ("Basis Cash", 2021, "collapsed",
     [2, 0, 0, 1, 1, 2, 0, 1, 1, 0, 0, 0],
     "seigniorage clone; peg never re-established"),
    ("OlympusDAO", 2021, "collapsed",
     [1, 2, 1, 2, 1, 0, 0, 1, 1, 0, 0, 1],
     "(3,3) premium unravels to backing; APY from mint + new bonds"),
    ("Wonderland", 2022, "collapsed",
     [1, 2, 1, 2, 1, 0, 0, 1, 1, 1, 0, 0],
     "largest OHM fork + treasury-trust collapse (Sifu)"),
    ("Axie SLP", 2021, "collapsed",
     [0, 2, 2, 0, 0, 0, 1, 2, 1, 0, 1, 0],
     "uncapped faucet; sink (breeding) needs new players; scholar guilds = rented labor"),
    ("STEPN GST", 2022, "collapsed",
     [0, 2, 2, 0, 0, 0, 1, 2, 1, 0, 1, 0],
     "isomorphic to SLP: emission uncapped, sink needs new shoe buyers"),
    ("FTX FTT", 2022, "collapsed",
     [2, 0, 0, 0, 2, 0, 1, 0, 1, 2, 0, 1],
     "self-printed collateral at an affiliate + classic run"),
    ("Celsius", 2022, "collapsed",
     [1, 2, 0, 0, 2, 0, 0, 1, 1, 2, 0, 2],
     "subsidized yield + FCFS promise + levered stETH loops"),
    ("Internet Computer", 2021, "collapsed",
     [0, 0, 1, 1, 0, 0, 2, 1, 1, 0, 0, 0],
     "no engine - pure S7 structure: supply glut bleed, weak zero-price anchor"),
    ("MakerDAO DAI", 2023, "survived",
     [0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0],
     "exogenous collateral; MKR mint is a backstop, not the peg mechanism"),
    ("USDC", 2023, "survived",
     [0, 0, 0, 0, 1, 0, 0, 0, 0, 1, 0, 0],
     "SVB de-peg to ~$0.88 mean-reverted: claims on real, recoverable assets"),
    ("Lido stETH", 2022, "survived",
     [0, 0, 0, 0, 0, 0, 0, 1, 0, 1, 0, 2],
     "structure flag (loops) but hard 1:1 anchor; no redemption promise = nothing to run"),
    ("BNB", 2022, "survived",
     [1, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0],
     "cash-flow anchor (fees/gas) + usage-linked burn; partial S1 remains"),
    ("Ethereum ETH", 2022, "survived",
     [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
     "zero-price-test archetype; EIP-1559 sink proportional to usage"),
    ("GMX", 2022, "survived",
     [0, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0],
     "real yield in ETH from trading fees; payer exists at any token price"),
    ("Uniswap UNI", 2022, "survived",
     [0, 0, 0, 0, 0, 0, 1, 2, 0, 0, 0, 0],
     "S8 control: zero value capture yet no spiral - no engine, lambda<1"),
    ("Curve CRV", 2023, "survived",
     [0, 1, 1, 0, 0, 0, 1, 0, 0, 2, 0, 1],
     "stressed survivor: founder leverage near-cascade; real-usage anchor held"),
]


def weighted_total(scores):
    return sum(s * w for s, w in zip(scores, WEIGHTS))


def flags(scores):
    eng = sum(1 for i in ENGINE if scores[i] == 2)
    st = sum(1 for i in STRUCTURE if scores[i] == 2)
    return eng, st


def write_csv(path):
    with open(path, "w", newline="", encoding="utf-8") as f:
        w = csv.writer(f)
        w.writerow(["name", "stress_year", "outcome"] + ROWS +
                   ["weighted_total_54", "engine_flags", "structure_flags", "note"])
        for name, yr, outcome, sc, note in CASES:
            eng, st = flags(sc)
            w.writerow([name, yr, outcome] + sc + [weighted_total(sc), eng, st, note])
    print(f"  [data]  {path.name}  ({len(CASES)} cases)")


def chart_separation():
    ordered = sorted(CASES, key=lambda c: weighted_total(c[3]))
    names, totals, colors, labels = [], [], [], []
    for name, yr, outcome, sc, _ in ordered:
        eng, st = flags(sc)
        names.append(f"{name} '{str(yr)[2:]}")
        totals.append(weighted_total(sc))
        colors.append(C["red"] if outcome == "collapsed" else C["green"])
        tag = []
        if eng:
            tag.append(f"{eng}E")
        if st:
            tag.append(f"{st}S")
        labels.append("+".join(tag) if tag else "")

    fig, ax = plt.subplots(figsize=(9.5, 7))
    bars = ax.barh(names, totals, color=colors, alpha=0.85)
    for bar, lab in zip(bars, labels):
        if lab:
            ax.text(bar.get_width() + 0.5, bar.get_y() + bar.get_height() / 2,
                    lab, va="center", fontsize=7.5, color=C["ink"])
    for x, txt in [(8, "elevated"), (19, "high"), (34, "textbook")]:
        ax.axvline(x, color=C["gray"], lw=1, ls="--", alpha=0.6)
        ax.text(x + 0.3, len(names) - 0.4, txt, fontsize=7.5, color=C["gray"])
    ax.set_xlabel("weighted scorecard total (max 54)")
    ax.set_title("Scorecard calibration: 10 collapses (red) vs 8 stress survivors (green)")
    ax.set_xlim(0, 44)
    handles = [plt.Rectangle((0, 0), 1, 1, color=C["red"]),
               plt.Rectangle((0, 0), 1, 1, color=C["green"])]
    ax.legend(handles, ["collapsed", "survived the stress event"],
              loc="lower right", fontsize=8)
    save(fig, "data_scorecard_separation.png",
         "nE/nS = engine/structure rows at 2. No survivor has an engine flag; "
         "borderline pair ICP vs CRV is resolved by the zero-price anchor test.")


def main():
    print("Scorecard calibration: 18-case back-scoring")
    write_csv(Path(__file__).resolve().parent / "scorecard_calibration.csv")
    chart_separation()
    def median(xs):
        xs = sorted(xs)
        n = len(xs)
        return xs[n // 2] if n % 2 else (xs[n // 2 - 1] + xs[n // 2]) / 2

    fails = [weighted_total(c[3]) for c in CASES if c[2] == "collapsed"]
    surv = [weighted_total(c[3]) for c in CASES if c[2] == "survived"]
    print(f"  collapses: min {min(fails)}  max {max(fails)}  median {median(fails)}")
    print(f"  survivors: min {min(surv)}  max {max(surv)}  median {median(surv)}")
    eng_surv = [c[0] for c in CASES if c[2] == "survived" and flags(c[3])[0] > 0]
    print(f"  survivors with engine flags: {eng_surv or 'none'}")


if __name__ == "__main__":
    main()
