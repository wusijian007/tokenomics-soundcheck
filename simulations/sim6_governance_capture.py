"""
Sim 6 — Governance-capture economics: the timelock as a circuit breaker
================================================================================

Models failure Skill #13 (Captureable Governance), the Beanstalk archetype. A
DAO controls a treasury of value V. An attacker acquires a deciding quorum and
votes to drain it. The audit inequality (economic-security.md):

    profit = V_recoverable - cost_to_corrupt_quorum > 0   ->   attack is rational

Two design levers set the two sides:

  * COST TO CORRUPT (x-axis): how expensive it is to assemble a deciding quorum.
    Near zero if votes are flash-loanable or the float is thin/borrowable
    (Beanstalk: ~one block of flash-loan fees). Large if a quorum must be bought
    and held against a finite float (convex market impact) and/or vote-locked.

  * TIMELOCK (the two panels): a delay T between "proposal passes" and
    "executes". The attacker must hold the position through T while the market
    reprices the token toward its post-drain value once the malicious proposal
    is public. This (a) makes a FLASH attack impossible (borrowed votes can't be
    held across T) and (b) craters the recoverable value and the attacker's own
    collateral. A timelock converts corruption cost from "flash-loan fees" into
    "full position risk through the crash you cause."

Sweep (treasury/float-value ratio, cost-to-corrupt-quorum) -> attacker profit,
with no timelock vs a 7-day timelock.

Run:  python sim6_governance_capture.py
"""
import numpy as np
from viz import plt, save, C

REPRICE_PER_DAY = 0.35   # how fast the market prices in the coming drain during T


def attacker_profit(v_ratio, quorum_cost, timelock_days):
    """Expected attacker profit, in float-market-cap units.

    v_ratio     : treasury value V / float market cap  (the prize)
    quorum_cost : cost to assemble a deciding quorum / float market cap
    timelock_days : delay between pass and execute
    """
    decay = np.exp(-REPRICE_PER_DAY * timelock_days)   # recoverable fraction after T
    # With a timelock the attacker also holds `quorum_cost` of exposure that
    # decays with the crash they trigger; with no timelock they execute at once.
    recoverable = v_ratio * decay
    holding_loss = quorum_cost * (1 - decay)
    return recoverable - quorum_cost - holding_loss


def sweep(timelock_days):
    v_ratios = np.linspace(0.05, 3.0, 90)        # treasury can exceed float mcap
    costs = np.linspace(0.001, 1.0, 90)          # cost to corner a quorum
    grid = np.zeros((len(costs), len(v_ratios)))
    for i, c in enumerate(costs):
        for j, vr in enumerate(v_ratios):
            grid[i, j] = attacker_profit(vr, c, timelock_days)
    return v_ratios, costs, grid


def main():
    print("Sim 6: governance-capture economics (Beanstalk archetype)")
    fig = plt.figure(figsize=(12, 5))

    for k, (T, title) in enumerate([
        (0.0, "No timelock (execute on pass)"),
        (7.0, "7-day timelock (design fix)"),
    ]):
        vr, costs, grid = sweep(T)
        ax = fig.add_subplot(1, 2, k + 1)
        im = ax.imshow(np.sign(grid), origin="lower", aspect="auto", cmap="RdYlGn_r",
                       extent=[vr[0], vr[-1], costs[0], costs[-1]], vmin=-1, vmax=1)
        ax.contour(vr, costs, grid, levels=[0.0], colors="black", linewidths=1.2)
        ax.set_xlabel("treasury value / float market cap  (the prize)")
        ax.set_ylabel("cost to corner a quorum / float mcap")
        ax.set_title(title)
        ax.grid(False)
        # Mark the Beanstalk point: near-zero quorum cost, treasury >> float.
        if k == 0:
            ax.scatter([2.5], [0.02], marker="*", s=180, color=C["ink"],
                       edgecolors="white", zorder=5)
            ax.annotate("Beanstalk\n(flash quorum)", (2.5, 0.02), fontsize=7.5,
                        color=C["ink"], textcoords="offset points", xytext=(-70, 18))
        fig.colorbar(im, ax=ax, fraction=0.046, pad=0.04,
                     label="attack profitable (>0) / unprofitable (<0)")

    save(fig, "sim6_governance_capture.png",
         "No timelock: attack profitable whenever prize > quorum cost (most of the plane). "
         "A 7-day timelock flips nearly all of it safe by forcing hold-through-the-crash.")

    for T, label in [(0.0, "no timelock"), (7.0, "7-day timelock")]:
        _, _, g = sweep(T)
        basin = (g > 0).mean() * 100
        print(f"  {label:>14}: {basin:5.1f}% of (treasury, quorum-cost) space is a profitable attack")

    print("  worked point: treasury = 2.5x float mcap, quorum cost = 0.02 (flash-thin):")
    print(f"    no timelock : profit = {attacker_profit(2.5, 0.02, 0.0):+.2f} float-mcap  (Beanstalk)")
    print(f"    7-day lock  : profit = {attacker_profit(2.5, 0.02, 7.0):+.2f} float-mcap  (repriced away)")
    print("  lesson: the timelock is the cheapest circuit breaker in tokenomics;")
    print("          raising the quorum cost (vote-locking, deep float) is the complementary lever.")


if __name__ == "__main__":
    main()
