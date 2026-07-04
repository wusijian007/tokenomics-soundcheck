# Tokenomics Audit Protocol

A standardized, evidence-based procedure for auditing a live or proposed token
design. Two tiers: a **15-minute quick screen** (triage) and a **full audit**
(due-diligence grade). Both produce a written verdict in the report format at
the end.

Principles:
- **Evidence over vibes.** Every scored row cites a source and a confidence level.
- **Distance, not just direction.** Don't stop at "flag present" — compute how
  far the system sits from each critical threshold and what closes the gap.
- **Opacity is data.** Anything the team makes hard to verify gets scored
  pessimistically and flagged (Axiom 10).

---

## Tier 0 — Quick screen (~15 minutes)

Answer eight questions from public docs + one supply tracker. Any ❌ on Q1–Q4 =
red-line: stop or escalate to a full audit before any further engagement.

| # | Question | Pass looks like | Fail maps to |
|---|---|---|---|
| Q1 | **Zero-price test**: if the token's price were zero, would anyone still need it? | demand from fees/utility/collateral that exists anyway | S9 |
| Q2 | What actually backs any peg/claim? | exogenous, liquid, verifiable reserves | S1, S6 |
| Q3 | Where does the yield come from? Name the payer. | real fees from identifiable users | S2 |
| Q4 | Can redemptions/withdrawals be met if 30% leave in a week? | coverage ≥ 1, or queue/pro-rata | S5 |
| Q5 | Is emission capped or bound to a sink? | mint ≤ burn, or hard cap | S3 |
| Q6 | Float at TGE and unlocks over the next 12 months? | float >20%; unlocks <25% of float | S7 |
| Q7 | Who holds it? Team locked? Contract clean? | dispersed, locked, no backdoors | S9 |
| Q8 | Is TVL/growth rented (points), looped (leverage), or organic? | organic majority; caps on loops | S11, S12 |

Verdict: `PASS` (proceed normally) / `CONCERNS` (full audit before commitment) /
`RED LINE` (walk away or redesign; cite the question numbers).

---

## Tier 1 — Full audit

### Step 1 — Collect inputs

Checklist (attach each to the evidence table):

- [ ] Whitepaper / docs / tokenomics page (archive a copy — they change)
- [ ] Token distribution table + vesting/unlock schedule
- [ ] Token + core protocol contracts (or audit reports); admin-key powers
- [ ] Treasury / reserve addresses and attestations
- [ ] Revenue, fees, incentives/emissions history
- [ ] TVL history annotated with incentive-program announcement dates
- [ ] Holder distribution; large lending positions against the token
- [ ] Market data: float, FDV, DEX/CEX depth (2% slippage), MM arrangements if known

Typical sources (verify, don't trust screenshots): **DefiLlama** (TVL, fees,
revenue, emissions, treasuries), **unlock trackers** (tokenomist etc.),
**block explorers** (holders, contracts, reserves), **Dune** (mint/burn, loop
positions, cohort behavior), **CoinGecko/CMC** (supply, FDV), **Bubblemaps**
(holder clustering), governance forums (the honest numbers usually surface
there first).

### Step 2 — Draw the mechanism map

One diagram: nodes = actors (users, stakers, treasury, LPs, insiders) and
mechanisms (mint, burn, redeem, subsidy, unlock); edges = value flows. Then mark
every edge whose magnitude depends on the token's own price. **Each
price-dependent edge is a candidate λ>1 loop.** If you can't draw the map from
the docs, that finding goes in the report.

### Step 3 — Classify the game structure

Match against the 4 models in `game-models.md` (a design can hit several).
This tells you the expected failure *shape* (run / unravel-to-backing /
absorbing barrier / bleed) and which simulation to parameterize later.

### Step 4 — Score the 12 rows

Use the measurement procedures in `scorecard.md`. Fill the evidence table as
you go:

| Row | Metric value | Score | Confidence | Source/link | Note |
|---|---|---|---|---|---|
| e.g. 2 | payout 19.5% vs revenue ≈5–6%; runway ≈45 days | 2 | verified | (link) | subsidy top-ups accelerating |

Confidence levels: `verified` (computed from on-chain/primary data) /
`reported` (team-published, not independently checked) / `estimated`
(inferred; state the assumption). A row resting on `estimated` data cannot
lower a score below 1 if the pessimistic reading would give 2.

### Step 5 — Distance-to-threshold

For every row scored ≥1, compute how far the system is from its critical
condition and what direction it is trending:

| Trigger | Distance metric | Example |
|---|---|---|
| S1/S6 | reserve ratio R vs 1; % of reserve that is reflexive | R = 2.2 sounds safe; reflexive reserve → critical run size only ~14% (sim1) |
| S2 | runway months = reserve ÷ net subsidy burn; trend | 45 days and shrinking |
| S3 | sink/faucet ratio, 3-month trend | 0.25 and falling |
| S4 | premium ÷ 3× threshold; new-money inflow vs dilution | inflow needs to double monthly |
| S5 | liquidity coverage vs 1; largest plausible outflow week | coverage 0.4 → a 15% outflow breaks it |
| S7 | next 4 unlock dates + size ÷ average daily volume | June cliff = 38 days of volume |
| S11 | organic TVL share; days to next snapshot | 22% organic, snapshot in 6 weeks |
| S12 | unwind size ÷ 2% DEX depth | 5.3× depth → cascade on any 3% de-peg |

### Step 6 — Security panel (cost-of-corruption ledger)

Score the attack axis with `economic-security.md`. For each **control
surface**, compute `cost to corrupt` vs `value extractable` under adversarial
financing (flash loans, borrowed stake, rented votes, custodial shares):

| Surface | Skill | The inequality to compute | Red line |
|---|---|---|---|
| Governance | S13 | cost(deciding quorum) vs treasury + NPV(mint/emissions control) | quorum flash-loanable/borrowable/rentable below value at stake, or no timelock |
| Oracle / leverage | S14 | cost(move oracle X% over its window) vs borrowable at the inflated mark | manipulation cost < borrowable value on any live venue |
| Supply subsidy | S15 | service revenue ÷ emissions value (trailing) | ≪ 0.1 persistently, emissions insensitive to utilization |
| Consensus (L1/L2) | — | security spend vs value secured (Budish); stake rentability; validator/LST concentration | attack cost < bridged/secured value, or a >⅓ liveness veto |

Mandatory whenever the design has governance over value, a price oracle used
for credit, or a DePIN/work-token supply side. Report the panel **beside** the
spiral score, never summed into it.

### Step 7 — Stress-test

Parameterize the matching simulation(s) with the audited numbers
(`simulations.md` has the mapping table). Report the critical parameter — the
run size / inflow growth / coverage / quorum cost at which the design flips
regime — and how plausible that shock is against historical episodes
(2022-grade drawdown, single-whale exit, negative-funding quarter, a
flash-loan-scale vote). For governance, `sim6_governance_capture.py` shows the
timelock/vote-lock phase boundary.

### Step 8 — Control-surface & contagion map

Combine two maps:
- **Control surfaces** (from step 6): governance, oracle, sequencer/consensus,
  liquidity — who can move each, at what cost, controlling what value.
- **Contagion**: where the token is accepted as collateral; top lenders/MMs;
  known large loans against the token (incl. founder/key-person); what upstream
  failure would hit reserves. Score S10, and name the single most plausible
  contagion path.

### Step 9 — Valuation context (not a price target)

The spiral score answers "will it *survive*?"; a full audit also frames "is it
*priced* for that survival?" — without issuing a price target (not investment
advice). First classify the **regime**, because it decides the method:

- **Currency-regime token** (reward/medium-of-exchange, gas, dual-token soft
  currency): governed by MV=PQ and inflation. Value ~ real transactional
  demand ÷ (velocity × supply); death mode is Cagan-style hyperinflation
  (reuse S3/S8). Ask: what non-speculative flow *must* hold it?
- **Equity-regime token** (fee-share, ve, buyback, governance over cash flow):
  governed by discounted claims. Triangulate:
  - revenue/fee multiple vs comparable protocols (fully-diluted and float);
  - staking-yield DDM: sustainable real yield ÷ (discount − growth);
  - dilution-adjusted forward supply (reuse the S7 unlock numbers) → the
    per-token claim after the next 12–24 months of emissions.

Output a **risk × valuation quadrant** placement, in words:

| | Low spiral risk | High spiral / attack flag |
|---|---|---|
| **Cheap vs fundamentals** | resilient & unloved (best risk/reward context) | value trap: cheap because the engine is priced in |
| **Rich vs fundamentals** | priced for perfection (execution risk) | reflexive bubble (the case-library zone) |

State the inputs and their confidence; this contextualizes the audit, it does
not recommend a trade.

### Step 10 — Write the report

```markdown
# Tokenomics Audit — <project> (<date>)

## Verdict
<one paragraph: spiral score X/54, N engine + M structure flags, band;
 security panel result (any S13/S14/S15 red lines); the single most dangerous
 loop or surface in plain words; the one-line action.>

## Mechanism map & game classification
<diagram or description; which of the 4 models, expected failure shape>

## Scorecard (spiral axis)
<the 12-row evidence table, with confidence labels>

## Security panel (attack axis)
<S13/S14/S15 cost-of-corruption table; control surfaces and their prices>

## Critical thresholds & distance
<the Step-5 table: each triggered row, current value, threshold, trend, ETA>

## Stress test
<simulation parameters used, critical values found, plausibility assessment>

## Control surfaces & contagion
<who can move governance/oracle/consensus/liquidity, at what cost; most
 plausible contagion path>

## Valuation context (not a price target)
<regime classification; the quadrant placement with its inputs and confidence>

## Prescriptions (prioritized)
1. <engine fixes + any attack-surface red lines first — cite antidotes>
2. <structure fixes — supply schedule, caps, vesting>
3. <monitoring: which metrics to watch, alert thresholds, review date>

## Limitations & blind spots
<data gaps, estimated rows, what would change the verdict, and which
 blind-spot categories below apply>
```

### The blind-spot register (state these in every report)

The instrument sees *structural economic* failure. It is deliberately blind to
several real ways a token dies — say so, so the verdict is not over-read:

| Blind spot | Why it's out of scope | Where to look instead |
|---|---|---|
| **Smart-contract exploits** | code bugs, not mechanism design (reentrancy, math errors) | contract audits, formal verification |
| **Regulatory / legal kill** | enforcement, sanctions, delistings | counsel, jurisdiction analysis |
| **Key-person / operational** | founder fraud, lost keys, team implosion | governance, custody, key-person risk |
| **Chain-level failure** | the underlying L1/L2 halts or is exploited | the security panel's consensus row, but only partially |
| **Pure market beta** | the whole market draws down; no mechanism fault | position sizing, macro |
| **Off-chain fraud beyond S9's tells** | fake reserves, cooked books an audit can't see | attestations, proof-of-reserves, forensic accounting |
| **Narrative/timing** | *when* a sound-or-doomed design turns is not predicted | the instrument gives structure, never timing |

Stating the blind spots is not boilerplate: a design can score 0/54 with no
attack flags and still go to zero via any row above. The instrument bounds
*one* failure family well; it does not bound the others.

---

## Pitfalls (read before signing a verdict)

- **Bull-market masking.** Every λ>1 design looks self-correcting while inflows
  grow. Score the mechanism, not the chart.
- **"Audited" ≠ solvent.** Contract audits test code safety, not economic
  design. Terra's contracts worked exactly as written.
- **Survivorship anchoring.** "Project X did the same and is fine" — check
  `survivors.md`; survivors differ on engines and anchors, not on luck.
- **Renounce theater.** Renounced ownership / burned LP is compatible with S9;
  it constrains the contract, not the tokenomics.
- **TVL is a liability.** Rented TVL (S11) measures future sell pressure, not
  adoption.
- **The team's spreadsheet is a scenario, not a forecast.** Re-derive runway
  and emissions from on-chain flows.
- **Code audit ≠ economic audit.** Beanstalk and Mango passed their code
  audits and were drained via the *mechanism* (step 6). The security panel and
  the contract audit are complementary, not substitutes.
- **Not investment advice.** The instrument detects structural collapse and
  attack risk and frames valuation *context* (step 9); it never issues a price
  target, and it does not predict *timing* — a doomed design can run for years.
