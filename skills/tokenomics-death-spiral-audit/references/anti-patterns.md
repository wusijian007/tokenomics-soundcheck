# The 10 Failure Skills (Anti-Pattern Catalog)

Each anti-pattern is something you can detect at the **whitepaper / smart-contract
stage**, before launch. Format: core → game/math structure → quantitative red
flags → historical instances → design antidote.

> Companion analysis with full derivations: `../../../death-spiral-deep-analysis.md`
> (Chinese: `代币经济学死亡螺旋_深度分析与失败Skills.md`). Game models: `game-models.md`.

---

## S1 — Reflexive Collateral
- **Core**: the token uses itself (or an asset tightly correlated to itself) as
  reserve / collateral.
- **Structure**: collateral value and the liability it backs are positively
  correlated, so `λ > 1` — when price falls, both sides deteriorate together.
- **Red flags**: corr(reserve asset, liability) → 1; "A-coin backs the A-coin
  system"; self-printed collateral held by affiliated parties.
- **Instances**: Terra (LUNA backs UST), FTX (FTT as collateral), Iron (TITAN
  backs IRON).
- **Antidote**: exogenous, *de-correlated* collateral (USDC/ETH); >150%
  overcollateralization; reserve-adequacy circuit breaker.

## S2 — Subsidized Demand Engine
- **Core**: core demand comes from a subsidized high APY, not real willingness to pay.
- **Structure**: a subsidy is a forward-borrow against future demand (reflexive
  demand curve). When the subsidy ends or confidence flips, demand vanishes.
- **Red flags**: protocol **payout > protocol revenue**; yield-reserve runway < 12
  months; > 60% of token demand concentrated in one incentive pool.
- **Instances**: Anchor 19.5% (≈75% of UST demand sat there), OHM, most
  "liquidity-mining life-support" tokens.
- **Antidote**: real yield (= real fees); APY auto-throttles to reserve; design a
  soft-landing for when the subsidy is withdrawn.

## S3 — Uncapped Faucet
- **Core**: the reward token has no hard supply cap and its sink depends on new users.
- **Structure**: faucet (emission) is not reflexive but sink (burn/use) is — it
  only clears while the user base grows. `sink/faucet < 1` once growth stalls.
- **Red flags**: no supply ceiling; annual emission > demand growth; the sink's
  demand source is *new users*, not real consumption by the existing base.
- **Instances**: Axie SLP, STEPN GST, DeFi Kingdoms JEWEL.
- **Antidote**: bind emission to the realized sink (mint ≤ burn); hard cap; make
  the sink real utility consumed by existing users, not onboarding by new ones.

## S4 — Coordination-Fragile Staking ((3,3))
- **Core**: the model paints "everyone stakes" as optimal, but the Nash
  equilibrium is "everyone exits".
- **Structure**: a prisoner's dilemma disguised as cooperation; backward induction
  unravels it from the last buyer. Stable only while new money > dilution.
- **Red flags**: APY from inflation / new bonds; `market price / backing (RFV) > 3`;
  strong first-mover advantage to "stay" over "exit".
- **Instances**: OHM and every (3,3) fork (TIME, KLIMA, …).
- **Antidote**: pay yield from real revenue; symmetrize exit; publish backing and
  discourage premium speculation.

## S5 — Sequential-Service Redemption (Bank Run)
- **Core**: instant, full, first-come-first-served redemption + maturity/liquidity
  mismatch.
- **Structure**: Diamond–Dybvig multiple equilibria; the first-mover advantage
  makes the bad (run) equilibrium self-fulfilling on any belief shock (sunspot).
- **Red flags**: instant redemption promised against illiquid assets; liquidity
  coverage < instantly-redeemable liabilities; no queue / FCFS.
- **Instances**: FTX, Celsius, Voyager, the Anchor withdrawal wave.
- **Antidote**: redemption queues / lockups; **pro-rata haircuts instead of FCFS**
  (kills the run incentive); liquidity coverage > 100%; circuit breakers.

## S6 — Seigniorage Absorbing Barrier
- **Core**: a dual-token mint/burn stablecoin turns de-peg selling pressure into
  unlimited minting of the reserve token.
- **Structure**: reserve ratio `R = M_reserve / S_stable`. `R < 1` is an
  irreversible absorbing barrier — past it, full redemption mathematically forces
  the reserve token to 0.
- **Red flags**: no reserve-adequacy circuit breaker; unlimited mint on de-peg;
  reserve token is reflexive/same-system as the stablecoin.
- **Instances**: Terra, Iron, Basis Cash, ESD.
- **Antidote**: reserve-ratio circuit breaker + switch to partial collateral; mint
  rate-limiting is only a band-aid — the real fix is to drop "algorithmic + own
  token" entirely.

## S7 — Float–FDV Asymmetry
- **Core**: the marginal seller (insiders) has a cost basis ≈ 0, and continuous
  unlocks drag price toward the floor.
- **Structure**: lemon market (info asymmetry on the unlock calendar) + a supply
  curve that shifts right every unlock. A *continuous* spiral, not a run.
- **Red flags**: initial float < 10%; first-year unlock > 50% of float;
  `FDV / annual real revenue > 100×` (no revenue → auto-max risk).
- **Instances**: ICP, Filecoin, Worldcoin, ApeCoin.
- **Antidote**: long, linear unlocks (no cliffs); float matched to real demand
  depth; insider unlocks tied to verifiable milestones; on-chain public calendar.

## S8 — Velocity Leak
- **Core**: a pure medium-of-exchange token with no value capture; high velocity
  keeps pushing price down.
- **Structure**: `P = utility_value / (M · V)` — high V → low P; no non-reflexive
  reason to hold.
- **Red flags**: no burn / no ve-lock / no fee-share; high share of "earn-and-dump"
  users; very short median holding time.
- **Instances**: most utility/GameFi reward tokens.
- **Antidote**: fee burn, ve-locking for governance + fee share — upgrade the token
  from "medium of exchange" to "productive asset".

## S9 — Narrative-Only Demand
- **Core**: demand is 100% narrative / celebrity / meme with no cash-flow anchor.
- **Structure**: extreme reflexive demand = attention; attention can be financed
  instantly and can evaporate instantly. (Usually *fraud*, not failed engineering.)
- **Red flags**: zero revenue; extreme holder concentration; team/celebrity
  holdings **unlocked**; contract has high tax / cannot-sell / mint backdoors.
- **Instances**: LIBRA, MELANIA, TRUMP, HAWK, SQUID, SafeMoon.
- **Antidote**: none by design — the value here is *detection and avoidance*, and a
  regulatory/due-diligence red line.

## S10 — Leverage Contagion
- **Core**: protocols are interlinked at the collateral / market-making / lending
  layer, so one local spiral becomes systemic.
- **Structure**: tokens cross-collateralize; concentrated market makers; in a
  crisis correlations → 1.
- **Red flags**: tokens used as collateral for each other; few affiliated MMs
  provide most liquidity; shared upstream risk exposure.
- **Instances**: Terra → 3AC → Celsius/Voyager → FTX chain reaction.
- **Antidote**: diversify collateral + stress-test correlations; cap affiliated
  MM concentration; isolate risk exposures.

---

# The 10 Design Axioms (mirror of the anti-patterns)

1. **Decouple fundamentals from price** — ensure `λ < 1`. This is the master axiom.
2. **Exogenous, de-correlated collateral** — never the native token; stress-test
   tail correlation → 1.
3. **Yield from real cash flow** — real yield first; any subsidy needs a runway and
   a soft-landing path.
4. **Self-balancing supply/demand** — `sink ≥ faucet`; emission bound to real
   consumption, not user growth.
5. **Kill the first-mover advantage** — pro-rata payouts, redemption queues, circuit
   breakers; make "running first" non-profitable.
6. **Predictable supply + symmetric info** — linear unlocks, float matched to
   demand, public on-chain calendar.
7. **Capture value to suppress velocity** — long-term holding driven by real
   fee-share/governance, not APY bribery.
8. **Demand must pass the zero-price test** — "if price went to zero, would anyone
   still need this?" If no, redesign or don't ship.
9. **Isolate contagion** — limit cross-protocol collateral links and MM concentration.
10. **Transparency is verifiable** — treasury, collateral, unlocks, team holdings
    all on-chain readable. Opacity is the #1 sunspot fuel.
