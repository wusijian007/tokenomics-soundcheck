"""
Structured dataset of landmark token collapses + two overview charts.

Numbers are ORDER-OF-MAGNITUDE estimates (peak market cap / value-at-risk and
drawdown), compiled from the companion case file. They are meant to convey
*relative scale and clustering by mechanism*, not to be precise accounting.
Always reconcile against live CoinGecko / on-chain data before reuse.

Outputs:
  - case_dataset.csv                  (the structured table)
  - ../simulations/charts/data_value_destroyed_by_mechanism.png
  - ../simulations/charts/data_timeline_scatter.png

Run:  python case_dataset.py
"""
import csv
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent.parent / "simulations"))
from viz import plt, save, C  # noqa: E402

# Mechanism codes (match the analysis docs):
# A algo-stable | B (3,3)/rebase | C GameFi inflation | D ponzi | E CeFi/L1
# F ICO-vapor | G celeb/meme/rug | H high-FDV unlock
MECH_LABEL = {
    "A": "Algo-stable spiral",
    "B": "(3,3) / rebase",
    "C": "GameFi inflation",
    "D": "Ponzi / HYIP",
    "E": "CeFi / exchange",
    "F": "ICO vapor / fraud",
    "G": "Celeb / meme / rug",
    "H": "High-FDV unlock",
}
MECH_COLOR = {
    "A": C["red"], "B": C["purple"], "C": C["amber"], "D": C["gray"],
    "E": C["ink"], "F": C["teal"], "G": C["green"], "H": C["blue"],
}

# name, ticker, year, mech, peak_mcap_bn (value-at-risk, USD bn), drawdown_pct, skill
CASES = [
    ("Terra/LUNA-UST", "LUNA", 2022, "A", 45.0, 99.99, "S6 absorbing barrier"),
    ("Iron Finance", "TITAN", 2021, "A", 2.0, 100.0, "S6 absorbing barrier"),
    ("Basis Cash", "BAC", 2021, "A", 0.2, 99.0, "S6 absorbing barrier"),
    ("Empty Set Dollar", "ESD", 2020, "A", 0.5, 99.9, "S6 absorbing barrier"),
    ("OlympusDAO", "OHM", 2021, "B", 4.0, 99.0, "S4 (3,3) fragility"),
    ("Wonderland", "TIME", 2022, "B", 1.5, 99.9, "S4 (3,3) fragility"),
    ("Klima DAO", "KLIMA", 2021, "B", 0.6, 99.9, "S4 (3,3) fragility"),
    ("Axie Infinity", "AXS/SLP", 2021, "C", 10.0, 99.5, "S3 uncapped faucet"),
    ("STEPN", "GMT/GST", 2022, "C", 3.0, 99.9, "S3 uncapped faucet"),
    ("DeFi Kingdoms", "JEWEL", 2021, "C", 1.0, 99.8, "S3 uncapped faucet"),
    ("Gala Games", "GALA", 2021, "C", 5.0, 98.0, "S3 uncapped faucet"),
    ("The Sandbox", "SAND", 2021, "H", 8.0, 97.0, "S7 high-FDV unlock"),
    ("Decentraland", "MANA", 2021, "H", 5.0, 95.0, "S7 high-FDV unlock"),
    ("OneCoin", "-", 2016, "D", 4.3, 100.0, "S9 narrative-only"),
    ("BitConnect", "BCC", 2017, "D", 3.5, 99.9, "S9 narrative-only"),
    ("PlusToken", "-", 2019, "D", 3.0, 100.0, "S9 narrative-only"),
    ("WoToken", "-", 2019, "D", 1.0, 100.0, "S9 narrative-only"),
    ("Forsage", "-", 2020, "D", 0.34, 100.0, "S9 narrative-only"),
    ("FTX", "FTT", 2022, "E", 9.0, 98.0, "S5 bank run + S1"),
    ("Celsius", "CEL", 2022, "E", 4.7, 99.0, "S5 bank run"),
    ("Voyager", "VGX", 2022, "E", 1.0, 99.0, "S5 bank run"),
    ("Serum", "SRM", 2022, "E", 1.5, 99.8, "S10 contagion"),
    ("EOS", "EOS", 2018, "F", 15.0, 98.0, "S7 high-FDV unlock"),
    ("Centra Tech", "CTR", 2017, "F", 0.1, 100.0, "S9 narrative-only"),
    ("Bancor", "BNT", 2017, "F", 1.0, 98.0, "S7 high-FDV unlock"),
    ("Squid Game", "SQUID", 2021, "G", 0.005, 100.0, "S9 narrative-only"),
    ("SafeMoon", "SFM", 2021, "G", 6.0, 99.9, "S9 narrative-only"),
    ("HEX", "HEX", 2019, "G", 5.0, 99.0, "S2 subsidized demand"),
    ("LIBRA (Milei)", "LIBRA", 2025, "G", 4.5, 98.5, "S9 narrative-only"),
    ("TRUMP", "TRUMP", 2025, "G", 15.0, 99.0, "S9 narrative-only"),
    ("MELANIA", "MELANIA", 2025, "G", 2.0, 99.0, "S9 narrative-only"),
    ("HAWK", "HAWK", 2024, "G", 0.49, 95.0, "S9 narrative-only"),
    ("Internet Computer", "ICP", 2021, "H", 45.0, 99.0, "S7 high-FDV unlock"),
    ("Filecoin", "FIL", 2021, "H", 9.0, 99.0, "S7 high-FDV unlock"),
    ("ApeCoin", "APE", 2022, "H", 4.0, 98.0, "S7 high-FDV unlock"),
    ("Worldcoin", "WLD", 2023, "H", 2.5, 90.0, "S7 high-FDV unlock"),
    ("Anchor Protocol", "ANC", 2022, "B", 1.0, 99.0, "S2 subsidized demand"),
    ("Mirror Protocol", "MIR", 2022, "A", 0.5, 99.0, "S10 contagion"),
]

COLS = ["name", "ticker", "year", "mechanism", "mechanism_label",
        "peak_value_at_risk_usd_bn", "drawdown_pct", "primary_failure_skill"]


def write_csv(path):
    with open(path, "w", newline="", encoding="utf-8") as f:
        w = csv.writer(f)
        w.writerow(COLS)
        for name, tk, yr, m, mcap, dd, sk in CASES:
            w.writerow([name, tk, yr, m, MECH_LABEL[m], mcap, dd, sk])
    print(f"  [data]  {path.relative_to(path.parent.parent)}  ({len(CASES)} cases)")


def chart_by_mechanism():
    totals, counts = {}, {}
    for *_, m, mcap, _, _ in [(c[0], c[1], c[2], c[3], c[4], c[5], c[6]) for c in CASES]:
        totals[m] = totals.get(m, 0) + mcap
        counts[m] = counts.get(m, 0) + 1
    order = sorted(totals, key=lambda k: totals[k], reverse=True)
    fig, ax = plt.subplots(figsize=(10, 5))
    labels = [f"{MECH_LABEL[m]}\n(n={counts[m]})" for m in order]
    ax.bar(labels, [totals[m] for m in order],
           color=[MECH_COLOR[m] for m in order])
    ax.set_ylabel("aggregate peak value-at-risk (USD bn, est.)")
    ax.set_title("Where the money died: value-at-risk by failure mechanism")
    ax.tick_params(axis="x", labelsize=8)
    save(fig, "data_value_destroyed_by_mechanism.png",
         "Algo-stable + high-FDV unlock + CeFi concentrate the largest capital destruction.")


def chart_timeline():
    fig, ax = plt.subplots(figsize=(11, 5.5))
    for m in MECH_LABEL:
        pts = [(c[2], c[4], c[0]) for c in CASES if c[3] == m]
        if not pts:
            continue
        xs = [p[0] for p in pts]
        ys = [p[1] for p in pts]
        ax.scatter(xs, ys, s=[max(20, v * 12) for v in ys],
                   color=MECH_COLOR[m], alpha=0.65, label=MECH_LABEL[m],
                   edgecolors="white", linewidths=0.6)
    # annotate the giants
    for c in CASES:
        if c[4] >= 9.0:
            ax.annotate(c[0], (c[2], c[4]), fontsize=7,
                        textcoords="offset points", xytext=(4, 4))
    ax.set_yscale("log")
    ax.set_xlabel("year")
    ax.set_ylabel("peak value-at-risk (USD bn, est., log)")
    ax.set_title("Token collapses 2016-2025: bubble size = capital at risk")
    ax.legend(fontsize=7, ncol=2, loc="lower center")
    save(fig, "data_timeline_scatter.png",
         "Collapses cluster in bull-market tops (2021-22) and the 2024-25 PolitiFi/meme wave.")


def main():
    print("Building structured case dataset + overview charts")
    out = Path(__file__).resolve().parent / "case_dataset.csv"
    write_csv(out)
    chart_by_mechanism()
    chart_timeline()


if __name__ == "__main__":
    main()
