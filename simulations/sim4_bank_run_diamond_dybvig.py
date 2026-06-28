"""
Sim 4 — Bank-run coordination game (Diamond-Dybvig): FTX / Celsius archetype
================================================================================

Models failure Skill #5 (Sequential-Service Redemption). A platform promises
instant, full, first-come-first-served redemption but holds illiquid/maturity-
mismatched assets. The redemption game has TWO equilibria:

    everyone waits  (good, fragile)   vs   everyone runs (bad, self-fulfilling)

Under SEQUENTIAL SERVICE the first to withdraw get paid in full; latecomers get
a haircut once liquidity L is exhausted. So if you believe others will run, your
best response is to run first -> the bad equilibrium is self-fulfilling and a
tiny belief shock (a "sunspot": a leaked balance sheet, a tweet) tips it.

The design fix is PRO-RATA redemption (everyone shares the same haircut
regardless of order). That removes the first-mover advantage, so a patient
depositor no longer gains by running -> the run basin shrinks dramatically.

This sim sweeps (liquidity coverage L, initial panic theta0) -> final run
fraction, for sequential vs pro-rata service.

Run:  python sim4_bank_run_diamond_dybvig.py
"""
import numpy as np
from viz import plt, save, C


def run_fraction(L, theta0, prorata=False, recovery=0.4, iters=60):
    """Fixed-point of beliefs. theta = expected fraction running.
    A depositor runs if payoff(run) > payoff(wait)."""
    theta = theta0
    for _ in range(iters):
        if not prorata:
            if theta <= L:
                # Run is absorbed by liquidity, the bank survives. Patient
                # depositors are paid in full later -> no advantage to running.
                run_payoff, wait_payoff = 1.0, 1.0 + 0.02   # tiny patience premium
            else:
                # Liquidity exhausted: first-come-first-served. Runners are paid in
                # full up to L; the rest and all waiters share fire-sold assets.
                frac_full = L / theta
                run_payoff = frac_full * 1.0 + (1 - frac_full) * recovery
                wait_payoff = recovery * 0.8                 # waiters get the worst
        else:
            # Pro-rata: order does not matter -> identical payoff for run vs wait,
            # with a small patience premium (no fire-sale urgency). First-mover
            # advantage is eliminated.
            avg = min(1.0, L + (1 - L) * recovery)
            run_payoff, wait_payoff = avg, avg + 0.02
        gap = run_payoff - wait_payoff
        br = 1.0 / (1.0 + np.exp(-15.0 * gap))               # logistic best response
        theta = 0.5 * theta + 0.5 * max(theta0, br)          # inertia, seeded by panic
    return theta


def sweep(prorata):
    Ls = np.linspace(0.05, 1.0, 80)
    thetas = np.linspace(0.0, 0.6, 80)
    grid = np.zeros((len(thetas), len(Ls)))
    for i, th in enumerate(thetas):
        for j, L in enumerate(Ls):
            grid[i, j] = run_fraction(L, th, prorata=prorata)
    return Ls, thetas, grid


def main():
    print("Sim 4: Diamond-Dybvig bank-run coordination game (FTX/Celsius)")
    fig = plt.figure(figsize=(12, 5))

    for k, (prorata, title) in enumerate([
        (False, "Sequential service (first-come-first-served)"),
        (True,  "Pro-rata redemption (design fix)"),
    ]):
        Ls, thetas, grid = sweep(prorata)
        ax = fig.add_subplot(1, 2, k + 1)
        im = ax.imshow(grid, origin="lower", aspect="auto", cmap="RdYlGn_r",
                       extent=[Ls[0], Ls[-1], thetas[0], thetas[-1]], vmin=0, vmax=1)
        ax.set_xlabel("liquidity coverage L (redeemable / deposits)")
        ax.set_ylabel("initial panic theta0 (belief shock)")
        ax.set_title(title)
        ax.grid(False)
        fig.colorbar(im, ax=ax, fraction=0.046, pad=0.04, label="final run fraction")

    save(fig, "sim4_bank_run.png",
         "Sequential service: large self-fulfilling run basin. Pro-rata: basin collapses.")

    # Quantify the run basin (fraction of the (L,theta0) space that ends in a run)
    for prorata, label in [(False, "sequential"), (True, "pro-rata")]:
        _, _, g = sweep(prorata)
        basin = (g > 0.5).mean() * 100
        print(f"  {label:>10} service: {basin:5.1f}% of scenarios end in a self-fulfilling run")
    print("  lesson: maturity mismatch + first-come-first-served is the run engine;")
    print("          pro-rata haircuts remove the first-mover advantage and shrink the basin.")


if __name__ == "__main__":
    main()
