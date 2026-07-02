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

### Step 6 — Stress-test

Parameterize the matching simulation(s) with the audited numbers
(`simulations.md` has the mapping table). Report the critical parameter — the
run size / inflow growth / coverage at which the design flips regime — and how
plausible that shock is against historical episodes (2022-grade drawdown,
single-whale exit, negative-funding quarter).

### Step 7 — Contagion map

List: where the token is accepted as collateral; who the top lenders/MMs are;
known large loans against the token; what upstream failure would hit reserves.
Score S10 from this, and name the single most plausible contagion path.

### Step 8 — Write the report

```markdown
# Tokenomics Audit — <project> (<date>)

## Verdict
<one paragraph: score X/54, N engine flags, M structure flags, band,
 the single most dangerous loop in plain words, and the one-line action.>

## Mechanism map & game classification
<diagram or description; which of the 4 models, expected failure shape>

## Scorecard
<the 12-row evidence table, with confidence labels>

## Critical thresholds & distance
<the Step-5 table: each triggered row, current value, threshold, trend, ETA>

## Stress test
<simulation parameters used, critical values found, plausibility assessment>

## Contagion
<links, concentrations, most plausible contagion path>

## Prescriptions (prioritized)
1. <engine fixes first — cite the antidote from anti-patterns.md>
2. <structure fixes — supply schedule, caps, vesting>
3. <monitoring: which metrics to watch, alert thresholds, review date>

## Limitations
<data gaps, estimated rows, what would change the verdict>
```

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
- **Not investment advice.** The instrument detects structural collapse risk;
  it says nothing about upside, timing, or fair value.
