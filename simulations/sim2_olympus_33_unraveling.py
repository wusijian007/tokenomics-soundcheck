"""
Sim 2 — OlympusDAO "(3,3)" premium unraveling
================================================================================

Models failure Skill #4 (Coordination-Fragile Staking) and #2 (Subsidized
Demand). OHM trades at

        price = backing * premium

where `backing` (RFV, treasury per token) grows slowly from bond sales, and
`premium` is the reflexive, sentiment-driven multiple the market pays on top.

The (3,3) "stake-stake is best" matrix hides where the yield comes from: rebase
inflation + NEW bond capital. Staking only beats selling while new-money inflow
outruns dilution. As inflow decays, premium collapses -> but the treasury floors
it at backing. So OHM falls to ~1x backing, NOT to zero (contrast with Terra).

Calibration: Dec-2021 premium ~= 413/30 ~= 13.8x; peak staking APY ~7000-8000%.

Run:  python sim2_olympus_33_unraveling.py
"""
import numpy as np
from viz import plt, save, C


def simulate(inflow0=0.12, inflow_decay=0.03, premium0=13.8, steps=200,
             dilution=0.06,      # per-step rebase dilution (high-APY regime)
             beta=0.9,           # premium sensitivity to (inflow - dilution)
             panic=0.25,         # extra premium decay once returns turn negative
             bond_profit=0.02,   # treasury/backing growth per unit inflow
             prem_cap=1000.0):   # bubble ceiling (markets don't pay infinite premium)
    backing = 1.0
    premium = premium0
    H = {"premium": [], "price": [], "backing": [], "inflow": []}
    for t in range(steps):
        inflow = inflow0 * np.exp(-inflow_decay * t)   # new money slows over time
        # treasury (backing) grows from bond inflow, net of nothing (one-way ratchet)
        backing *= (1 + bond_profit * inflow)
        # reflexive premium: rewarded when new money > dilution, punished otherwise
        drive = beta * (inflow - dilution)
        if drive < 0:
            drive -= panic * (premium - 1.0) / max(premium, 1e-6)  # stampede out of premium
        premium *= (1 + drive)
        premium = min(max(1.0, premium), prem_cap)     # floored at backing, capped at bubble ceiling
        H["premium"].append(premium)
        H["backing"].append(backing)
        H["price"].append(backing * premium)
        H["inflow"].append(inflow)
    return H


def steady_premium(inflow_const, **kw):
    """Hold inflow constant -> read off the steady-state premium (for bifurcation)."""
    H = simulate(inflow0=inflow_const, inflow_decay=0.0, steps=400, **kw)
    return H["premium"][-1]


def main():
    print("Sim 2: OlympusDAO (3,3) premium unraveling")
    fig = plt.figure(figsize=(12, 5))

    # --- Left: trajectories under decaying new-money inflow ---
    ax1 = fig.add_subplot(1, 2, 1)
    H = simulate()
    t = range(len(H["premium"]))
    ax1.plot(t, H["price"], color=C["blue"], lw=2, label="OHM price")
    ax1.plot(t, H["backing"], color=C["green"], lw=1.6, ls="--", label="backing (RFV floor)")
    ax1.fill_between(t, H["backing"], H["price"], color=C["amber"], alpha=0.15,
                     label="reflexive premium (evaporates)")
    ax1.set_yscale("log")
    ax1.set_xlabel("step")
    ax1.set_ylabel("value (log scale)")
    ax1.set_title("Premium collapses to backing, not to zero")
    ax1.legend(fontsize=8)

    # --- Right: bifurcation — steady premium vs sustained new-money rate ---
    ax2 = fig.add_subplot(1, 2, 2)
    inflows = np.linspace(0.0, 0.20, 120)
    prem = [steady_premium(x) for x in inflows]
    ax2.plot(inflows * 100, prem, color=C["purple"], lw=2)
    ax2.set_yscale("log")
    # critical inflow ~ dilution: below it premium dies (->1x), above it sustains (->ceiling)
    ax2.axvline(6.0, color=C["red"], ls="--", lw=1)
    ax2.text(6.3, 30, "critical inflow\n= dilution rate", color=C["red"], fontsize=8)
    ax2.axhline(1.0, color=C["gray"], ls=":", lw=1)
    ax2.set_xlabel("sustained new-money inflow (% per step)")
    ax2.set_ylabel("steady-state premium (x backing)")
    ax2.set_title("Bifurcation: premium needs perpetual new money")

    save(fig, "sim2_olympus_33.png",
         "Premium is a function of new-money growth; below dilution it unravels to 1x backing.")

    drop = (H["price"][0] - H["price"][-1]) / H["price"][0] * 100
    print(f"  premium {H['premium'][0]:.1f}x -> {H['premium'][-1]:.2f}x;"
          f" price drawdown {drop:.1f}% (floored by backing, not zero)")
    print("  lesson: any staking yield paid from inflation+new bonds is a coordination game;")
    print("          it is stable ONLY while new money outpaces dilution -> structurally finite.")


if __name__ == "__main__":
    main()
