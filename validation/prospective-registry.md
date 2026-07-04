# Prospective Registry — Pre-Registered Scores & Falsifiable Predictions

**Freeze date: 2026-07-02.** This file is **append-only** after the freeze:
no edits to the frozen sections, only dated entries in the Amendment Log.
Timestamp of record = the git commit introducing this file (optionally
anchored via OpenTimestamps). Outcome definitions, grading rules, and
integrity rules: [`README.md`](README.md).

Scores use the measurement procedures in
`skills/tokenomics-soundcheck/references/scorecard.md` (12 rows,
max 54; engine ×3 / structure ×2 / amplifier ×1), computed from public data
available at the freeze date. Rows resting on unverifiable data are scored
pessimistically per protocol. **This is research, not investment advice** —
the registry exists to test the instrument, in both directions: a low-scored
project collapsing falsifies it exactly as much as a flagged project sailing
through.

Review dates: **2027-07-02** (12-month) and **2028-07-02** (24-month).

---

## Part A — Clean pre-registrations (outcome genuinely open at freeze)

| Project | Score /54 | Flags | Band | Row detail (nonzero) |
|---|---|---|---|---|
| Ethena USDe/ENA | 13 | 1 structure (S12=2) | elevated | S2=1 regime-dependent yield marketed high; S5=1 secondary-venue fragility (Oct-2025 Binance dislocation); S10=1 hedge-venue/custody concentration; S11=1 points-origin TVL; **S12=2 PT/sUSDe loops on lending markets** |
| Hyperliquid HYPE | 3 | none | low | S7=1 large future team/foundation unlocks; S10=1 single-venue concentration (HLP absorbed the Mar-2025 JELLY incident) |
| pump.fun PUMP | 6 | none | low | S7=1 concentrated ICO/insider share; S8=1 capture via buybacks only; S9=1 revenue real but attention-cyclical |
| USDD | 10 | none (all partials) | elevated | S1=1 affiliated/opaque reserve mix; S5=1 redemption opacity; S6=1 algorithmic lineage; S10=1 TRX-ecosystem concentration — opacity rows scored pessimistically |
| Jupiter JUP | 7 | 1 structure (S7=2) | low/elevated boundary | **S7=2 unlock overhang vs float**; S2=1 launchpad/incentive programs. Anchor: hard (real aggregator/perp fees) |

### Falsifiable predictions (Part A)

**Ethena USDe** — anchor: hard-ish (redemption claim on hedged exogenous
collateral); shape risk: deleveraging cascade (S12), not slow bleed.
- **P-USDe-1**: Absent trigger **T** (≥60 consecutive days of median negative
  perp funding across major venues while USDe supply > $5B), USDe suffers no
  secondary discount >2% sustained >72h with primary redemptions functioning,
  through 2028-07-02.
- **P-USDe-2 (conditional)**: If **T** occurs: supply contracts >30% within
  90 days and at least one discount event >1% occurs; solvency holds if and
  only if the reserve fund covers realized negative carry. Either branch
  grades the S12+S5 scoring.
- **P-USDe-3 (shape)**: any USDe stress is fast (redemption/deleveraging
  wave), not a multi-month bleed.

**Hyperliquid HYPE** — no flags; the low score is itself the falsifiable claim.
- **P-HYPE-1**: no `spiral_collapse` by 2028-07-02; any ≥70% drawdown is
  attributable to business/market factors, **not** a mechanism forced to mint,
  dump, or liquidate HYPE (falsifier: an HLP/insurance shortfall mechanically
  recapitalized by minting/dumping HYPE).
- **P-HYPE-2 (re-score trigger)**: if realized 12-month unlocks exceed 50% of
  float without matching demand, S7 re-scores to 2 by amendment — the
  prediction then shifts to bleed-shape, and this registry says so *before*
  the fact.

**pump.fun PUMP** — no flags; revenue extremely regime-dependent.
- **P-PUMP-1**: no engine spiral by 2028-07-02; if memecoin volumes collapse,
  PUMP declines proportionally (business risk) without entering a mechanical
  mint/dump loop. A reflexive-loop collapse would falsify the low score.

**USDD** — all partials, driven by opacity.
- **P-USDD-1**: holds the peg in calm regimes through 2028-07-02.
- **P-USDD-2 (conditional)**: if a TRX drawdown >60% coincides with a
  redemption wave >30% of supply within 90 days: a discount >3% follows
  unless reserves prove exogenous and liquid. If it sails through such an
  episode cleanly, our pessimistic S1/S5 scoring was too harsh — revise down
  and record it.

**Jupiter JUP** — structure flag, hard anchor.
- **P-JUP-1**: any major underperformance through 2028-07-02 is
  unlock-calendar-shaped (bleed), not a run; the protocol itself remains
  functional on its fee anchor. A run-shaped collapse would falsify the
  engine/structure distinction.

## Part B — In-flight observations (outcome partially realized at freeze; tracked for confirmation only, not clean OOS)

| Project | Score /54 | Flags | Status at freeze |
|---|---|---|---|
| EigenLayer EIGEN | 12 | 2 structure (S7=2, S11=2) | bleed largely realized through 2025 — consistent with structure-flag prediction; tracked for the *de-risking* claim below |
| Ondo ONDO | 8 | 1 structure (S7=2) | mild structure bleed underway at freeze |

- **P-EIGEN-1 / P-ONDO-1 (de-risking claim)**: while S7/S11 remain at 2, the
  bleed continues; if either project's flags genuinely clear (unlock schedule
  substantially completed + organic-majority TVL), price stabilizes within
  6 months of the flag clearing. This is the falsifiable *positive* direction
  of the instrument.

---

## Instrument-level success criteria (pre-registered)

- **C1**: No Part-A project with zero engine flags and total ≤ 7 (HYPE, PUMP)
  suffers `spiral_collapse` by 2028-07-02.
- **C2**: No registry project **without** an engine flag experiences a
  run-to-zero spiral. Bleeds do not count against C2; a true spiral in any of
  them falsifies the engine-necessity claim at the heart of the instrument.
- **C3**: If USDe survives a realized trigger-T episode with <2% sustained
  discount and functioning redemptions, the S12 weighting is over-cautious
  for hedged-collateral designs → documented downward revision.
- **C4**: At each review, publish the full confusion table (prediction vs
  outcome). **Two or more misclassifications at the 24-month review force a
  documented revision of the scorecard**, with a post-mortem of which row or
  weight failed.

## Grading log

*(append-only; add one dated section per review)*

- 2027-07-02 review: —
- 2028-07-02 review: —

## Amendment log

*(append-only; dated; never modify frozen sections above)*

- 2026-07-04 — Project/skill renamed to **Tokenomics Soundcheck** (repo, skill
  folder, and plugin id migrated from the former `tokenomics-autopsy` /
  `tokenomics-death-spiral-audit`). The only edit to this file was a mechanical
  path-reference update in the preamble (the `scorecard.md` pointer); **no
  prediction, score, flag, band, freeze date, or success criterion was
  changed.** The freeze-record hash for this file in `validation/README.md` was
  re-recorded to match; the original frozen content remains verifiable in git
  history (commit `a87e923` and earlier), which is the authoritative
  tamper-evidence.
