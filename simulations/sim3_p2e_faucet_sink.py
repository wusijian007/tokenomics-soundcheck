"""
Sim 3 — Play-to-Earn faucet/sink inflation spiral (Axie SLP / STEPN GST)
================================================================================

Models failure Skill #3 (Uncapped Faucet) and #8 (Velocity Leak). A reward
token's price is set by the balance between

    faucet (emission, minted by players earning)  vs  sink (burned by breeding/use)

Crucially the SINK is reflexive (breeding pays off only while new players push
NFT prices up) but the FAUCET is not (it mints regardless). So:

    players up -> breeding/sink up -> token price up -> ROI up -> players up ...

and in reverse once growth stalls -> sink collapses, faucet keeps minting ->
hyperinflation -> price -> 0 -> ROI payback -> infinity -> player exodus.

Calibration (Axie, early 2022): ~250M SLP minted/day vs ~40M burned/day
(emission ~4x burn). Season-20 patch cut emission to ~45M/day.

This sim also runs a COUNTERFACTUAL: a capped policy (mint <= burn) on the same
demand shock, to show the design fix keeps the economy alive.

Run:  python sim3_p2e_faucet_sink.py
"""
import numpy as np
from viz import plt, save, C


def simulate(capped=False, steps=300,
             mint_per_player=1.0,     # tokens minted/player/step (faucet)
             entry_cost=8.0,          # onboarding cost (token-days to break even)
             join_gain=0.08,          # player response speed to ROI
             payback_target=150.0,    # acceptable payback horizon (steps)
             capacity=8.0e6,          # addressable market (TAM saturation)
             sell_frac=0.85,          # share of minted tokens earners dump
             buy_per_new=20.0,        # tokens a new player buys to onboard/breed
             kappa=0.10):             # price sensitivity to order-flow imbalance
    players = 5.0e5                    # start small, with room to grow into TAM
    price = 0.20                       # reward-token price ($)
    H = {"price": [], "players": [], "mint": [], "burn": [], "payback": []}

    for t in range(steps):
        # ROI payback horizon drives player flow; saturation caps the upside
        daily_usd = mint_per_player * price
        payback = entry_cost / max(daily_usd, 1e-9)
        roi_pull = (payback_target - payback) / payback_target
        saturation = 1.0 - players / capacity
        growth = join_gain * roi_pull * saturation
        new_players = players * growth                       # can go negative (exodus)
        players = max(1.0e4, players + new_players)

        # FAUCET: every earner mints; earners SELL most of it.
        mint = mint_per_player * players
        sell = sell_frac * mint
        # DEMAND: only NEW players buy the token (to onboard/breed) -> reflexive on growth.
        buy = buy_per_new * max(new_players, 0.0)
        # SINK (burn) tracks onboarding purchases that are consumed by breeding.
        burn = buy
        if capped:
            # Design fix: emission may not exceed the real sink -> sellers <= buyers.
            sell = min(sell, buy)
            mint = min(mint, burn)

        imbalance = (buy - sell) / (buy + sell + 1e-9)        # in [-1, 1]
        price *= (1 + kappa * imbalance)
        price = float(np.clip(price, 0.001, 5.0))

        H["price"].append(price)
        H["players"].append(players)
        H["mint"].append(mint)
        H["burn"].append(burn)
        H["payback"].append(min(payback, 2000))

    return H


def main():
    print("Sim 3: Play-to-Earn faucet/sink inflation spiral (Axie/STEPN)")
    fig = plt.figure(figsize=(12, 8))
    Hu = simulate(capped=False)
    Hc = simulate(capped=True)
    t = range(len(Hu["price"]))

    ax1 = fig.add_subplot(2, 2, 1)
    ax1.plot(t, Hu["price"], color=C["red"], lw=2)
    ax1.set_title("Uncapped faucet: reward-token price")
    ax1.set_xlabel("step"); ax1.set_ylabel("token price ($)")

    ax2 = fig.add_subplot(2, 2, 2)
    ax2.plot(t, Hu["mint"], color=C["amber"], lw=1.8, label="mint (faucet)")
    ax2.plot(t, Hu["burn"], color=C["teal"], lw=1.8, label="burn (sink)")
    ax2.set_yscale("log")
    ax2.set_title("Faucet keeps minting after sink collapses")
    ax2.set_xlabel("step"); ax2.set_ylabel("tokens / step (log)")
    ax2.legend(fontsize=8)

    ax3 = fig.add_subplot(2, 2, 3)
    ax3.plot(t, Hu["players"], color=C["blue"], lw=2)
    axb = ax3.twinx()
    axb.plot(t, Hu["payback"], color=C["gray"], lw=1.4, ls="--")
    axb.set_ylabel("ROI payback (steps)", color=C["gray"])
    axb.spines["top"].set_visible(False)
    ax3.set_title("Active players vs ROI payback horizon")
    ax3.set_xlabel("step"); ax3.set_ylabel("active players", color=C["blue"])

    ax4 = fig.add_subplot(2, 2, 4)
    ax4.plot(t, Hu["price"], color=C["red"], lw=2, label="uncapped (mint free)")
    ax4.plot(t, Hc["price"], color=C["green"], lw=2, label="capped (mint <= burn)")
    ax4.set_title("Design fix: cap emission to the sink")
    ax4.set_xlabel("step"); ax4.set_ylabel("token price ($)")
    ax4.legend(fontsize=8)

    save(fig, "sim3_p2e_faucet_sink.png",
         "Same demand shock: uncapped emission hyperinflates to ~0; capped emission survives.")

    pu = Hu["price"][-1] / Hu["price"][0] * 100
    pc = Hc["price"][-1] / Hc["price"][0] * 100
    print(f"  uncapped final price: {pu:.1f}% of start  |  capped final price: {pc:.1f}% of start")
    print("  lesson: an uncapped reward faucet whose sink depends on user GROWTH is a")
    print("          structural death spiral; bind emission to real burn to survive a slowdown.")


if __name__ == "__main__":
    main()
