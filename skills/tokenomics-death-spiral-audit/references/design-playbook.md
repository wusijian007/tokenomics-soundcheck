# Tokenomics Design Playbook

How to design a token economy that keeps `λ < 1` — the constructive mirror of
the anti-pattern catalog. Work the steps **in order**: each step's output is the
next step's input, and the most common design failure is starting at step 4
(supply schedule) without an answer to step 1 (why does this token exist?).

Ground rules inherited from the case record:

- The 12 axioms (`anti-patterns.md`) are constraints, not suggestions. Axiom 1
  (`λ < 1`) dominates: no later step may wire fundamentals back to price.
- Every number you choose must come with the **threshold it must never cross**
  and the **monitor** that watches it (step 8). A parameter without an alarm is
  a future incident.
- Design for the bear. Any mechanism that needs growth to stay solvent is a
  death-spiral engine on a delay timer (S2, S3, S11).

---

## Step 1 — The necessity test: should this even be a token?

Answer in writing before anything else:

1. **Zero-price test (Axiom 8)**: if the token traded at zero, what breaks for
   users? If the answer is "nothing", the product doesn't need a token —
   points, equity, or a stablecoin serve better. Stop or redefine.
2. **Who pays?** Name the party that hands over money *for the service* (not
   for the token). No identifiable payer → any yield you later offer will be a
   subsidy (S2) by construction.
3. **What does the token do that a generic asset can't?** Legitimate answers
   are few: fee medium with a usage-bound sink; collateral/security bond
   (work token, slashing); metered access rights; governance over real cash
   flow. "Alignment" and "community" are not mechanisms.

Output: a one-paragraph demand thesis naming the payer, the service, and the
token's mechanical role.

## Step 2 — Demand design: build the anchor first

Rank the demand sources you can actually engineer, strongest anchor first:

| Grade | Demand source | Reflexive? | Examples |
|---|---|---|---|
| A | fees/gas burned or paid for a service used anyway | no | ETH gas, BNB fees |
| A | redemption claim on an exogenous asset | no | stETH→ETH, USDC→$ |
| B | collateral / security bond with slashing | mildly (demand scales with usage) | staking bonds |
| B | fee-share on real revenue (ve/stake) | mildly | GMX, ve-fee models |
| C | metered access / discounts | mildly | fee-discount tiers |
| D | expected airdrop / points | **yes** (S11) | farmed TVL |
| F | APY from emissions; "number go up" | **yes** (S2/S9) | the case library |

Design target: **a majority of steady-state demand from grades A–B.** D may
bootstrap (see step 6) but must be labeled as rented and given a retirement
plan. If your design's steady state is C or below, return to step 1.

## Step 3 — Value capture: pick deliberately

| Mechanism | Effect | Costs / risks | Fits when |
|---|---|---|---|
| Fee burn | supply sink ∝ usage (Axiom 4) | needs real fee volume | high-throughput protocols |
| Fee share to stakers | direct cash-flow anchor | regulatory surface; needs revenue | revenue-positive protocols |
| ve-lock (vote-escrow) | lowers velocity; aligns horizon | locked supply = future overhang; bribery markets | protocols allocating emissions/liquidity |
| Buyback (+burn/treasury) | flexible, treasury-controlled | discretionary → trust load | mature, profitable |
| Collateral utility | structural hold demand | imports liquidation risk (S12) — set caps | deep-liquidity assets only |

Rule: capture follows revenue. **Zero-revenue + strong capture = capturing
nothing** (S8 doesn't kill, but it doesn't save either — see UNI in
`survivors.md`).

## Step 4 — Supply design: schedule, float, unlocks

Benchmarks (empirical healthy ranges distilled from the S7 case set; justify
any deviation in writing):

| Parameter | Healthy range | Red line (S7) |
|---|---|---|
| Float at TGE | 15–30% of max supply | <10% |
| Insiders (team+VC) share | ≤30–35% combined | >40% |
| Cliff before insider vesting | ≥12 mo, then **linear** | cliff dumps >5% of float in a day |
| Insider full vesting | 36–48 mo | <24 mo |
| Year-1 unlocks | <25% of TGE float | >50% of float |
| Emissions budget | ≤ value of sink it funds (step 6) | uncapped (S3) |
| FDV at TGE | defensible vs comparable *revenue* multiples | no revenue + top-decile FDV |

Structural rules:
- **Linear beats cliffs, always.** Cliffs create synchronized sell dates that
  the whole market front-runs (Model 4).
- **Milestone-gate what you can verify on-chain**; time-gate the rest.
- **Publish the calendar machine-readably** (Axiom 6). The lemon-market
  discount you avoid is worth more than the flexibility you give up.
- If a reward token is needed, decide **where inflation lands** and say so:
  the AXS/SLP and MKR/DAI cases show the second token is either a shock
  absorber (deliberate, honest) or a victim (players' income) — design it,
  don't let it happen.

## Step 5 — Redemption & stability infrastructure

Only for designs with any peg, deposit, or claim (skip otherwise):

- **Collateral**: exogenous, de-correlated, >100% (peg) / >150% (volatile
  collateral) — Axiom 2. Stress the tail: corr → 1, depth → 2022 levels.
- **Redemption**: pro-rata or queued under stress, never pure FCFS against
  illiquid assets (Axiom 5). Publish the coverage ratio continuously.
- **Circuit breakers, specified in advance**: the trigger metric, the
  threshold, the action, and who/what can invoke it. Example spec:
  `if reserve_ratio < 1.5 → pause expansion; < 1.2 → switch to pro-rata
  redemption; < 1.0 → freeze mint, governance recapitalization vote`.
  A breaker invented during the crisis is a tweet, not a breaker.
- **Backstop wiring**: if a second token recapitalizes the system (MKR
  pattern), verify the direction: mint-to-absorb-loss (backstop, sound) vs
  mint-to-defend-peg (engine, S6).

## Step 6 — Incentives: subsidy as priced CAC with a retirement plan

Subsidies are legitimate bootstrap tools *when accounted as customer
acquisition cost*, not "yield":

- **Budget**: total emissions value ≤ what you'd rationally pay to acquire the
  users/liquidity. Compute per-unit: emissions $ per retained user / per $ of
  fee-paying TVL. If you wouldn't pay it in cash, don't pay it in tokens.
- **Runway** (S2 line): `runway_months = incentive_reserve / net_monthly_spend`
  ≥ 12 at all times, recomputed at current token price, not launch price.
- **Decay by rule, not by vote**: emissions decay schedule published at launch;
  each extension is a governance event with a stated cost.
- **Anti-mercenary terms** (S11): rewards vest/lock past TGE; reward *flow*
  (fees paid, volume with spread, blocks validated) rather than *stock*
  (TVL parked); publish the organic-baseline dashboard — what remains if
  incentives stop today.
- **Soft landing**: model the day the subsidy ends *before it starts*. If
  projected retention at subsidy-end < the level that sustains the sink,
  the design is S2/S3 on a timer.

## Step 7 — Liquidity plan

- **Depth target**: 2%-slippage depth ≥ the largest plausible single-day net
  sell (largest unlock tranche, largest whale, largest loop unwind — whichever
  is bigger). If depth can't cover the unlock calendar, fix the calendar.
- **Owned vs rented**: protocol-owned liquidity for the base; rented (incentivized)
  liquidity is S11-class and must be counted as temporary.
- **MM terms**: cap any single/affiliated MM's share of depth; no
  loan-with-call-option structures that hand insiders synthetic dumps; disclose
  MM token allocations.
- **Loop caps** (S12): if the token or its derivative will be lendable, set LTV
  and supply caps *before* listing, sized to `unwind ≤ 2%-depth`.

## Step 8 — The monitoring dashboard: every threshold gets an alarm

Ship the dashboard with the token. Minimum panel, straight from the scorecard
rows:

| Metric | Warn | Act (pre-committed) |
|---|---|---|
| Reserve ratio R (if peg) | < 1.5 | breaker per step 5 |
| Liquidity coverage | < 1.2 | throttle expansion, publish plan |
| Incentive runway (months) | < 12 | cut emissions by rule |
| sink/faucet (30d) | < 1 | emission auto-throttle |
| Organic TVL share | < 50% | taper points program |
| Next-90d unlocks ÷ 2%-depth | > 0.5 | stagger/OTC/comms plan |
| Loop unwind ÷ 2%-depth | > 0.5 | tighten LTV/supply caps |
| Top-10 holder share | rising trend | disclosure + MM diversification |
| price ÷ backing (if treasury) | > 3 | publish backing, cool premium |

The **act** column is written *now*, while nobody is panicking (Axiom 5's
logic applied to governance).

## Step 9 — Pre-launch stress test

Run the design through the audit side of this skill before TGE:

1. Score it on the 12-row scorecard (`scorecard.md`) — target: **total ≤ 7,
   zero engine flags, zero structure flags at 2** — and the **security panel**
   (`economic-security.md`) — target: **no S13/S14 red lines.**
2. Parameterize the matching simulations (`simulations.md`): reserve ratio into
   sim1, dilution/inflow into sim2, sink/faucet into sim3, coverage into sim4,
   treasury/quorum-cost into sim6 (governance). Find the critical parameter —
   then demand the design survive **2× the worst historical shock** of its class.
3. Red-team with the audit protocol's Tier-0 questions **and** the
   cost-of-corruption ledger (can anyone buy/borrow/flash a quorum, or move the
   oracle cheaper than the credit it unlocks?), answered by someone who didn't
   design the system.

## Step 10 — Launch checklist (final gate)

- [ ] Demand thesis names a real payer; majority of steady-state demand grade A–B
- [ ] Zero-price test passes in writing
- [ ] Supply table within step-4 benchmarks; calendar published machine-readably
- [ ] Emissions capped or sink-bound; decay by rule
- [ ] Incentive runway ≥ 12 months at current prices; retirement plan written
- [ ] No native-token collateral anywhere in the reserve path
- [ ] Redemption design pro-rata/queued under stress; coverage published
- [ ] Circuit breakers specified (trigger → action → authority) and coded
- [ ] Loop/LTV caps set; MM concentration capped; depth ≥ largest unlock tranche
- [ ] **Governance (S13)**: votes locked (no flash voting) + a timelock long
      enough to exit/veto; quorum floor sized to borrowable float; treasury not
      held in the native token — corruption cost > prize at all times
- [ ] **Oracle/leverage (S14)**: if the token is lendable/settleable, LTV and
      caps derive from manipulation-cost math, not asset class; multi-venue
      manipulation-aware oracle + deviation breaker
- [ ] **Supply subsidy (S15)**, if DePIN/work-token: emissions demand-gated;
      revenue/emissions published; mint ≤ k·burn once a BME exists
- [ ] Monitoring dashboard live with the step-8 alarms
- [ ] Spiral scorecard ≤ 7 with zero engine flags **and** a clean security
      panel (no S13/S14 red lines), signed by a non-designer

---

## Worked micro-example

*A mid-size derivatives protocol wants a token. Applying the playbook:*

1. **Necessity**: payer = traders (fees exist without the token). Token role:
   fee-share staking + insurance backstop bond. Passes zero-price (protocol
   functions without it; token holders just stop earning).
2. **Demand**: grade B (fee share) + grade B (backstop bond, slashed on
   shortfall) → majority A/B ✓.
3. **Capture**: 30% of fees to stakers, 10% buyback-to-insurance-fund. No burn
   (revenue still scaling).
4. **Supply**: 1B fixed cap. TGE float 20% (airdrop 5% vested 6mo + liquidity
   10% + treasury 5%). Team 18% / investors 17%, 12-mo cliff then 36-mo
   linear → year-1 unlocks ≈ 23% of float ✓. No emissions token.
5. **Stability**: no peg; insurance fund in USDC/ETH only (never the native
   token — that's FTT wiring).
6. **Incentives**: 8% supply over 4 years, decaying 35%/yr by rule, rewarding
   *fee-paying volume* with 6-mo vesting; runway recomputed monthly.
7. **Liquidity**: POL seeded from raise; loop LTV cap 50%, supply cap sized to
   0.4× of 2%-depth.
8. **Dashboard**: runway, unlock/depth ratio, organic-volume share, insurance
   coverage — with the step-8 act column pre-committed.
9. **Stress**: scorecard = 4 (S7=1 float 20%, S2=1 vested rewards) — zero
   engine flags ✓; sim4 with coverage 1.4 → run basin only at >60% panic ✓.

Total design time: days. Total value: not being case #51.
