"""
Sim 1 — Algorithmic stablecoin "absorbing barrier" (Terra / LUNA-UST archetype)
================================================================================

Models failure Skill #6 (Seigniorage Absorbing Barrier) and #1 (Reflexive
Collateral). The reserve-adequacy ratio is

        R(t) = M_luna(t) / S_ust(t)     (LUNA market cap / UST supply)

Peg defense burns UST and MINTS+SELLS LUNA. That selling crashes LUNA's price,
which lowers M_luna, which lowers R, which weakens the peg further -> a positive
feedback loop (system gain lambda > 1, see analysis doc section 1.1).

Below a critical R the system crosses an *absorbing barrier*: full redemption is
mathematically impossible without driving LUNA -> 0. Once crossed the terminal
state is unique (collapse) regardless of subsequent behaviour.

Calibration (peak, April 2022):  M_luna ~= $40B, S_ust ~= $18B  ->  R0 ~= 2.2.
That 2.2x "safety buffer" evaporated in ~72h because M_luna is itself reflexive.

Run:  python sim1_algo_stable_absorbing_barrier.py
"""
import numpy as np
from viz import plt, save, C


def peg_price(R, k=8.0):
    """UST market price as a function of reserve adequacy R.
    Holds ~$1 while R is comfortably > 1, degrades through R~1.0-1.3,
    collapses below R~1. Logistic centred at the R=1 absorbing barrier."""
    return 1.0 / (1.0 + np.exp(-k * (R - 1.0)))


def simulate(R0=2.2, shock=0.05, steps=120,
             alpha=0.9,        # redemption intensity per unit depeg
             impact=0.55,      # LUNA price impact coefficient
             liq_frac=0.12):   # absorbable LUNA depth as fraction of mcap
    """One run. Returns time-series dict and a 'survived' flag."""
    S = 18.0                   # UST supply ($B)
    M = R0 * S                 # LUNA market cap ($B)
    Pl = 1.0                   # LUNA price index (normalised)
    Ql = M / Pl                # LUNA token supply (index units)
    p = peg_price(R0)

    H = {"R": [], "p_ust": [], "Pl": [], "S": []}
    shock_ust = shock * S      # one-off exogenous redemption at t=0

    for t in range(steps):
        R = M / max(S, 1e-9)
        p = peg_price(R)
        depeg = max(0.0, 1.0 - p)

        redeem = alpha * depeg * S + (shock_ust if t == 0 else 0.0)
        redeem = min(redeem, S)

        # Burn UST -> mint LUNA worth `redeem`, then dump it into finite depth.
        Ql += redeem / max(Pl, 1e-6)
        depth = max(liq_frac * M, 1e-6)
        Pl *= max(0.02, 1.0 - impact * redeem / depth)
        S -= redeem
        M = Pl * Ql

        H["R"].append(M / max(S, 1e-9))
        H["p_ust"].append(peg_price(M / max(S, 1e-9)))
        H["Pl"].append(Pl)
        H["S"].append(S)

    # "Survived" = peg held AND the stablecoin still exists (supply not redeemed
    # to ~zero). The supply check removes the degenerate case where a total run
    # empties UST so that R = M / (~0) spuriously spikes.
    survived = H["p_ust"][-1] > 0.90 and H["R"][-1] > 1.0 and H["S"][-1] > 0.5 * 18.0
    return H, survived


def phase_diagram(ax):
    """Sweep (initial R0, exogenous shock) -> survived/collapsed. The basin
    boundary IS the absorbing barrier."""
    R0s = np.linspace(0.8, 3.0, 70)
    shocks = np.linspace(0.0, 0.30, 70)
    grid = np.zeros((len(shocks), len(R0s)))
    for i, sh in enumerate(shocks):
        for j, r0 in enumerate(R0s):
            _, ok = simulate(R0=r0, shock=sh)
            grid[i, j] = 1.0 if ok else 0.0
    ax.imshow(grid, origin="lower", aspect="auto", cmap="RdYlGn",
              extent=[R0s[0], R0s[-1], shocks[0] * 100, shocks[-1] * 100],
              vmin=0, vmax=1)
    ax.set_xlabel("Initial reserve adequacy  R0 = M_luna / S_ust")
    ax.set_ylabel("Exogenous redemption shock (% of UST)")
    ax.set_title("Basin of attraction: green=peg survives, red=death spiral")
    ax.axvline(1.0, color=C["ink"], ls="--", lw=1)
    ax.text(1.02, 27, "R=1\nabsorbing\nbarrier", color=C["ink"], fontsize=8, va="top")
    ax.scatter([2.2], [5], color="black", zorder=5, s=40)
    ax.annotate("Terra peak\n(R~2.2)", (2.2, 5), textcoords="offset points",
                xytext=(8, 8), fontsize=8)
    ax.grid(False)


def main():
    print("Sim 1: algorithmic-stablecoin absorbing barrier (Terra archetype)")
    fig = plt.figure(figsize=(12, 8))

    # --- Top row: two time-series runs from the SAME R0=2.2, different shock ---
    ax1 = fig.add_subplot(2, 2, 1)
    ax2 = fig.add_subplot(2, 2, 2)
    for ax, shock, title in [
        (ax1, 0.05, "Small shock (5%): self-corrects"),
        (ax2, 0.22, "Large shock (22%): death spiral"),
    ]:
        H, ok = simulate(R0=2.2, shock=shock)
        t = range(len(H["R"]))
        ax.plot(t, H["p_ust"], color=C["blue"], label="UST price ($)")
        axb = ax.twinx()
        axb.plot(t, H["R"], color=C["red"], label="R = M/S", lw=1.6)
        axb.axhline(1.0, color=C["gray"], ls=":", lw=1)
        ax.set_ylim(0, 1.1)
        ax.set_title(f"{title}\n{'SURVIVED' if ok else 'COLLAPSED'}")
        ax.set_xlabel("step")
        ax.set_ylabel("UST price ($)", color=C["blue"])
        axb.set_ylabel("R", color=C["red"])
        axb.spines["top"].set_visible(False)

    # --- Bottom: phase diagram (the headline) ---
    ax3 = fig.add_subplot(2, 1, 2)
    phase_diagram(ax3)

    save(fig, "sim1_absorbing_barrier.png",
         "Same R0=2.2 buffer; outcome flips on shock size -> buffer is reflexive, not real.")

    # Console summary of the critical shock at the calibrated buffer
    lo, hi = 0.0, 0.4
    for _ in range(30):
        mid = (lo + hi) / 2
        _, ok = simulate(R0=2.2, shock=mid)
        if ok:
            lo = mid
        else:
            hi = mid
    print(f"  critical shock at R0=2.2: ~{mid*100:.1f}% of UST supply triggers the spiral")
    print("  lesson: a 2.2x reserve looks safe but tolerates only a single-digit/low-double-digit")
    print("          % run, because defending the peg destroys the very reserve backing it.")


if __name__ == "__main__":
    main()
