# Crypto / Web3 Token Collapse Analysis (2009–2026)

> 🌐 **English** | [中文](加密项目代币崩溃分析_2009-2026.md)
>
> Theme: tokens that, since Bitcoin's birth (2009), fell **≥ 95% from their issue / listing price** and entered a **tokenomics collapse loop (death spiral)** — a total-count estimate plus an assessment of the 50 most notable cases.
> Data as of June 2026. Prices are approximate and move with the market; always reconcile against live CoinGecko / CoinMarketCap data.
> This is a research-oriented survey, **not investment advice**; some projects are still under litigation or investigation.

---

## 1. Defining the criteria (the numbers only mean something once the standard is clear)

The user's two conditions actually point at **two different things** that must be separated:

**1) "Down 95%+ from issue price" — which baseline price?**
- A frequently confused trap: **"down 99% from all-time high (ATH)" ≠ "down 95% from issue price."**
- Many projects that "crashed 99%" had very low IEO / private-sale / first-listing prices, so even after the crash they remain **above issue price**. The classic example is **Axie's AXS**: Binance IEO price $0.10, ATH ~$165, now ~$1 — down ~99.4% from ATH, but still **up** relative to its issue price.
- Therefore, when noting a drawdown for each project, this document **prefers the "issue / first-listing price" as the baseline**; where that figure is unavailable it falls back to ATH and labels it explicitly.

**2) "Tokenomics collapse loop (death spiral)" — a specific mechanism, not a synonym for "crashed."**
- A true "death spiral" is a **self-reinforcing negative feedback triggered by a price drop**: drop → the mechanism is forced to mint / dump / liquidate → further drop.
- It differs in nature from a **pure Ponzi / rug pull**: the latter is **fraud**, not an endogenous collapse of the token-economic model. But the two converge in outcome (→ 0), and the user groups them together, so this document **includes both while labeling each by its failure mode**.

---

## 2. Total-count estimate: how many are there really?

**No institution has precisely counted the intersection of "down 95% from issue price + death spiral,"** so we can only give evidence-based ranges in layers.

### Macro base (CoinGecko official research)
- As of end-2025, **~53.2% of cryptocurrencies on GeckoTerminal are "dead"** (sustained volume < $1,000 / price down 99%+ from ATH / team gone dark).
- Cumulative **dead coins ≈ 13.4M+**, of which **~11.6M died in 2025 alone (86.3% of all history)**, and ~1.38M in 2024.
- Historical distribution: just 2,584 in 2021 → 213K in 2022 → 245K in 2023 → 1.38M in 2024 → an explosion in 2025.
- The inflection point was the **2024 launch of pump.fun**: zero-code token issuance flooded the market with meme coins, and the overwhelming majority of dead coins are this batch of "low-quality, fast-rotting" tokens. The single-day **$19B leverage liquidation cascade on October 10, 2025** accelerated another wave of meme-sector collapses.

### Layered estimate for "serious projects" (what this document actually cares about)
The vast majority of those 13.4M dead coins are **meme coins / honeypots that went to zero within hours to days**; their "issue price" is essentially zero, so "down 95%" is meaningless. Narrowing to **projects that had a real issuance, listed on major exchanges, and reached a meaningful market cap**:

| Layer | Rough scope | Estimate meeting "down ≥95% + effectively dead" |
|---|---|---|
| Projects that ever ranked top-2000 on CMC/CG | a few thousand | **more than half** (at the scale of thousands, most alts fall 90%+ in a bear market) |
| Down ≥95% from **issue / listing price** AND with a clear **death-spiral / fraud-collapse mechanism** | the stricter intersection | **hundreds** (conservatively 300–800; including the half-dead long tail, possibly over a thousand) |
| "Landmark collapses" that drew industry-wide attention | widely covered by media | **~50–80** (the focus of this document) |

**One-line conclusion**: under a loose definition, "dead + crashed" projects number in the **millions**; but **famous projects with a real issuance, a 95% break below issue price, and a textbook tokenomics collapse number in the hundreds**, of which ~50–80 are truly well known. Those 50 follow.

---

## 3. Collapse-mechanism taxonomy (the 50 projects are grouped by this)

| Code | Mechanism | Core |
|---|---|---|
| **A** | Algorithmic-stablecoin death spiral | dual-token mint/burn reflexivity; de-peg → unlimited minting → 0 |
| **B** | Reflexive (3,3) / rebase / treasury model | high-APY Ponzi-style incentives; confidence breaks → bank run |
| **C** | GameFi / Move-to-Earn inflation spiral | reward token minted without limit; collapses when new users stop growing |
| **D** | Ponzi / HYIP / money game | referral-based pyramid; fraud at its core |
| **E** | CeFi / exchange / L1 insolvency | platform blows up, platform token goes to zero with it |
| **F** | ICO-era vaporware / fraud | raised on a whitepaper, then no delivery or absconded |
| **G** | Celebrity / meme / rug pull | hype-pump then pull liquidity and dump |
| **H** | High FDV / low float / high-price listing dump | absurd listing price, persistent bleed from unlock pressure |

---

## 4. The 50 most notable collapses (assessed by mechanism group)

### A. Algorithmic-stablecoin death spirals (textbook-grade)

| # | Project (token) | Year | Peak → trough | Drawdown | Assessment |
|---|---|---|---|---|---|
| 1 | **Terra / Luna + UST** | 2022.5 | LUNA $119 → $0.0001; UST de-pegs | **-99.99%** | The most classic death spiral in history. Anchor's 19.5% subsidized yield was unsustainable; after UST de-pegged, the UST↔LUNA arbitrage mechanism minted LUNA without limit, evaporating ~$40–60B in a week and triggering an industry-wide chain reaction (3AC, Celsius, Voyager, FTX). Founder Do Kwon was indicted. **The Class-A prototype.** |
| 2 | **Iron Finance (TITAN)** | 2021.6 | TITAN ~$65 → ~$0 | **-100%** | "The world's first large-scale DeFi bank run." A de-peg of the partially-algorithmic stablecoin IRON triggered unlimited TITAN minting. Mark Cuban was publicly burned and went on to call for regulation. |
| 3 | **Basis Cash (BAC)** | 2021 | long below $0.05 after de-peg | **-99%+** | A three-token algo-stable cloning Basis; never re-established the peg and slowly went to zero. Do Kwon anonymously participated in its development — seen as a "rehearsal" for Terra. |
| 4 | **Empty Set Dollar (ESD)** | 2020–21 | ~$23 → ~$0 | **-99.9%** | Elastic-supply (rebase) algo-stable; the expansion/contraction cycle broke down and fell into a death spiral. |

### B. Reflexive (3,3) / rebase / treasury models

| # | Project (token) | Year | Peak → trough | Drawdown | Assessment |
|---|---|---|---|---|---|
| 5 | **Olympus DAO (OHM)** | 2021–22 | ~$1,415 → ~$10–15 | **-99%** | The "(3,3)" high-APY (briefly thousands % to millions %) game-theory model, fundamentally sustained by new capital at a high premium; the moment expectations reversed it became a bank run. Spawned dozens of forks, nearly all of which went to zero. |
| 6 | **Wonderland (TIME)** | 2022.1 | ~$10,000 → ~$5 | **-99.9%** | The largest OHM fork. Its treasury manager "Sifu" was exposed as a co-founder of the already-collapsed exchange QuadrigaCX (with a criminal record); the collapse of trust triggered a stampede. |
| 7 | **Klima DAO (KLIMA)** | 2021–22 | ~$3,800 → below ~$1 | **-99.9%** | A "carbon credits + (3,3)" narrative, the same reflexive treasury model; went to zero once the narrative faded. |
| 8 | **Yam Finance (YAM)** | 2020.8 | collapsed within 36 hours of launch | **-99%+** | A bug in the rebase contract caused runaway minting; **collapsed a day and a half after launch** — the famous wreck of the DeFi-summer reflexivity experiments. |

### C. GameFi / Move-to-Earn inflation spirals

| # | Project (token) | Year | Peak → trough | Drawdown | Assessment |
|---|---|---|---|---|---|
| 9 | **Axie Infinity (SLP / the economy)** | 2021–22 | SLP ~$0.40 → ~$0.001 | **SLP -99.5%** | The P2E pioneer. The reward token SLP had no emission cap; once new players stopped growing, old players "farm-and-dumped" → SLP hyperinflation collapse, with DAU falling from 2.7M to the ~50K range. **Note: the governance token AXS is still up vs its IEO price** — what collapsed was the reward token and the economy. The Class-C prototype. |
| 10 | **STEPN (GMT / GST)** | 2022 | GST ~$9 → ~$0.01 | **GST -99.9%** | "Move-to-Earn." GST had the same disease as SLP: unlimited emission, demand dependent on new shoe-buyers; it collapsed mid-2022 (compounded by exiting the China market). GMT is down ~99% from its high. |
| 11 | **DeFi Kingdoms (JEWEL)** | 2021–22 | ~$22 → ~$0.05 | **-99.8%** | GameFi + DeFi; killed by the double whammy of liquidity incentives and reward-token inflation. |
| 12 | **Gala Games (GALA)** | 2021–22+ | ~$0.82 → ~$0.01–0.02 | **-98%** | A gaming-platform token, compounded by a 2021 co-founder feud / mutual lawsuits alleging token misappropriation. |
| 13 | **The Sandbox (SAND)** | 2021– | ~$8.4 → ~$0.2–0.3 | **-97%** | A peak-bubble metaverse-real-estate narrative; long bleed from unlock pressure + narrative fade. |
| 14 | **Decentraland (MANA)** | 2021– | ~$5.9 → ~$0.2–0.3 | **-95%+** | Same as above, the other half of the metaverse duo; chronically low active users and thin value support. |

### D. Ponzi / money games (fraud at the core, → 0 in outcome)

| # | Project (token) | Year | Scale | Assessment |
|---|---|---|---|---|
| 15 | **OneCoin** | 2014–17 | €4B+ | Led by "Cryptoqueen" Ruja Ignatova; **there was no real blockchain at all** — a pure referral money game and one of the largest crypto scams ever; the main culprit remains a fugitive. |
| 16 | **BitConnect (BCC)** | 2016–18 | ~$3.5B | ATH ~$463 → near zero (-99.9%). A lending Ponzi promising daily interest from a "trading bot"; crashed instantly under regulatory pressure in Jan 2018, marking the top of the ICO bubble. |
| 17 | **PlusToken** | 2018–19 | ~$2–3B+ | A China/Korea-centered wallet money game that absconded with hundreds of thousands of BTC/ETH; its dumping was at one point blamed for suppressing the 2019 market; the ringleaders were sentenced in China. |
| 18 | **WoToken** | 2019–20 | ~$1B | A Chinese "WoToken" money game with personnel overlap with PlusToken; ringleaders sentenced. |
| 19 | **Forsage** | 2020–22 | ~$0.34B | A pure smart-contract Ponzi (matrix referrals); sued by the SEC in 2022 — proof that "on-chain transparency" can't save a Ponzi at its core. |
| 20 | **Pincoin / iFan (Modern Tech)** | 2018 | ~$0.66B | Vietnam's largest ICO scam, promising 40% monthly interest; the team vanished. |

### E. CeFi / exchange / L1 insolvency (platform token collapses with it)

| # | Project (token) | Year | Peak → trough | Drawdown | Assessment |
|---|---|---|---|---|---|
| 21 | **FTX (FTT)** | 2022.11 | ~$84 → ~$1–2 | **-98%** | FTT, a "self-printed banknote," was used by Alameda as collateral; a CoinDesk balance-sheet exposé + a Binance sell-off triggered a run; collapsed in three days; SBF sentenced to 25 years. The Class-E prototype. |
| 22 | **Celsius (CEL)** | 2022 | ~$8 → ~$0.1 | **-99%** | A lending platform that blew up and went bankrupt; CEO Mashinsky convicted; CEL was alleged to have been price-manipulated. |
| 23 | **Voyager (VGX)** | 2022 | bankruptcy | **-99%+** | Dragged into bankruptcy by the 3AC default; platform token VGX collapsed with it. |
| 24 | **Serum (SRM)** | 2022.11 | ~$13 → ~$0.02 | **-99.8%** | The FTX/Alameda-affiliated DEX token; lost support after FTX blew up, and the community even forked a new chain. |

### F. ICO-era vaporware / fraud / post-listing bleed

| # | Project (token) | Year | Peak → trough | Drawdown | Assessment |
|---|---|---|---|---|---|
| 25 | **EOS** | 2018– | ATH ~$22.7 → ~$0.4–0.5 | **-98%** | One of the largest ICOs in history (~$4.1B raised over a full year). The "Ethereum killer" narrative fell through, with a hollow ecosystem and a long bleed (renamed Vaulta in 2025). |
| 26 | **Centra Tech (CTR)** | 2017 | to zero | **-100%** | A "crypto debit card" scam endorsed by Floyd Mayweather and DJ Khaled; founders jailed for fraud; a landmark SEC enforcement case. |
| 27 | **Veritaseum (VERI)** | 2017– | near-zero | **-99%+** | Led by Reggie Middleton; the SEC found it a fraudulent offering; a textbook vaporware project. |
| 28 | **Dentacoin (DCN)** | 2017– | ATH ~$0.0166 → ~$0.000000x | **-99.9%** | A "dental-industry coin" that once made the news for its absurd supply; near-zero for the long term. |
| 29 | **Bancor (BNT)** | 2017– | ATH ~$10 → ~$0.2 | **-98%** | A giant 2017 ICO (~$150M), an AMM pioneer later overtaken by Uniswap, compounded by the 2022 suspension of "impermanent-loss protection" that broke trust. |
| 30 | **Status (SNT)** | 2017– | ATH ~$0.68 → ~$0.02 | **-97%** | An encrypted-messaging narrative with slow delivery; a textbook ICO that opened high and bled. |

### G. Celebrity / meme / rug pull (hype-pump then dump)

| # | Project (token) | Year | Peak → trough | Drawdown | Assessment |
|---|---|---|---|---|---|
| 31 | **Squid Game Token (SQUID)** | 2021.11 | $0.01 → $2,861 → $0 | **-100%** | Rode the *Squid Game* hype with a honeypot "can't-sell" mechanism; went to zero in minutes — a textbook rug pull. |
| 32 | **SafeMoon (SFM)** | 2021– | ATH → near-zero | **-99%+** | A "reflection + burn" high-tax mechanism + celebrity marketing; the SEC and DOJ charged the team with misappropriation in 2023; bankrupt in 2024. |
| 33 | **HEX** | 2019– | ATH ~$0.55 → ~$0.003 | **-99%** | Richard Heart's "stake for high APY" model, widely called Ponzi-like; sued by the SEC in 2023 (later dismissed on procedural grounds). |
| 34 | **Save the Kids (KIDS)** | 2021 | pumped then instantly dumped | **-99%+** | A "charity coin" endorsed en masse by FaZe Clan influencers; the contract hid sell logic, and the scandal shook the influencer world. |
| 35 | **CryptoZoo (Logan Paul)** | 2021–22 | never delivered | **-99%+** | Influencer Logan Paul's "NFT breeding game"; the game was never delivered, sparking class-action lawsuits and a refund saga. |
| 36 | **$LIBRA (Milei)** | 2025.2 | $4.5B market cap → crash | **-98.5%** | Argentine president Milei tweeted an endorsement; insiders pulled liquidity within hours; 74,000 traders lost ~$286M; it escalated into the "Cryptogate" political scandal. The Class-G + PolitiFi exemplar. |
| 37 | **$MELANIA** | 2025.1 | ~$14 → ~$0.10 | **-99%** | Almost contemporaneous with $TRUMP; peaked at launch, then insider dumping. |
| 38 | **$TRUMP** | 2025.1 | peak → -99% from peak | **-99% (from peak)** | Market cap briefly pumped to tens of billions; massive team holdings + unlock dumping; pioneered the controversial "political meme coin" category. |
| 39 | **$HAWK (Hawk Tuah)** | 2024.12 | $490M market cap → crash | **-90%+ (in minutes)** | Influencer Haliey Welch's coin; crashed 90%+ within minutes of launch, alleged to be a rug; she went quiet afterward. |
| 40 | **MOTHER (Iggy Azalea)** | 2024 | from peak | **-99%** | A celebrity meme coin; topped out mid-2024, then bled to near-zero, leaving holders trapped. |

### H. High FDV / high-price listing / unlock dumping (the best fit for "down 95% from issue price")

| # | Project (token) | Year | Listing/peak → trough | Drawdown | Assessment |
|---|---|---|---|---|---|
| 41 | **Internet Computer (ICP)** | 2021.5 | first-day ~$700 (briefly thousands on some venues) → ~$5 | **~-99% from listing** | The most typical "down 95%+ from issue/listing price" case: it listed high under a star-studded halo (a16z et al.), then was crushed by early-investor unlock pressure into a long bleed. |
| 42 | **Filecoin (FIL)** | 2020/2021 | ICO $5 → first day ~$30 → ATH $237 → ~$2–3 | **~-99% from ATH, also below first day** | A giant ICO (~$257M raised in 2017); mining-collateral requirements + continuous unlocks created persistent sell pressure; a disaster zone for Chinese retail miners. |
| 43 | **ApeCoin (APE)** | 2022– | ATH ~$26 → ~$0.4–0.6 | **-98%** | The Yuga/BAYC ecosystem token; airdrop + unlocks; a continuous bleed after the narrative faded. |
| 44 | **Worldcoin (WLD)** | 2023– | ATH ~$11 → ~$0.7–1 | **-90%+** | The textbook "high FDV" case of very low initial float + huge future unlocks; under continuous release pressure. |

### Supplement: Terra-ecosystem satellites & other famous cases

| # | Project (token) | Year | Drawdown | Assessment |
|---|---|---|---|---|
| 45 | **Anchor Protocol (ANC)** | 2022 | **-99%+** | The Terra-ecosystem lending protocol; its 19.5% high yield was UST's demand engine, so it died with its parent. |
| 46 | **Mirror Protocol (MIR)** | 2022 | **-99%+** | The Terra-ecosystem synthetic-assets protocol; went to zero with Terra; the SEC also classified MIR as a security. |
| 47 | **Frosties (NFT)** | 2022 | **-100%** | An NFT rug pull; the team withdrew funds and fled; founders arrested — a landmark NFT enforcement case. |
| 48 | **Evolved Apes (NFT)** | 2021 | **-100%** | A famous NFT rug where an anonymous team minted, sold, absconded with funds, and never delivered the game. |
| 49 | **Auroracoin (AUR)** | 2014 | **-99%+** | An early "Iceland national coin" airdrop; the huge pre-mine dumped after the airdrop and collapsed — an early tokenomics-failure specimen. |
| 50 | **PayCoin / GAW Miners (XPY)** | 2014–15 | **-99%+** | Promised a "$20 price floor" it couldn't honor; founder Josh Garza jailed for fraud — an early "price-backing" scam. |

---

## 5. Common-pattern summary (distilled from the 50 cases)

1. **Reflexivity is the #1 killer**: what classes A/B/C share is that **the token's price itself is the fuel for the mechanism**. When price rises the mechanism is self-consistent; the moment price reverses, the mechanism accelerates the fall (minting, dumping, liquidation). Terra, OHM, and SLP are three variants of the same disease.

2. **"Subsidized high APY" almost always ends in a bank run**: Anchor's 19.5% and OHM's thousands % were sustained by new capital or treasury subsidy — fundamentally a **forward-borrow against future demand**; they collapse once the subsidy runs out or confidence reverses.

3. **Uncapped emission + demand reliant on newcomers = GameFi death spiral**: SLP / GST have no emission ceiling; the economy only holds while users **keep growing net-positive**, and collapses the moment growth stops — a structural defect of the P2E model, not an operational issue.

4. **"High-price listing + low-float high-FDV" is a chronic death spiral**: ICP, FIL, WLD, APE don't go to zero in a single crash; they **bleed for years on continuous unlock pressure** — which is precisely the most common way "down 95% from issue price" actually plays out.

5. **Ponzi / rug and "tokenomics collapse" look alike but differ in essence**: the zeroing of OneCoin, BitConnect, SQUID, and LIBRA is **fraud realized**, not model failure. But for holders the outcome is identical, and they often disguise themselves as "innovative tokenomics."

6. **Celebrity / political endorsement = the new harvesting tool**: 2024–25's HAWK, LIBRA, MELANIA, TRUMP prove that **attention itself** can be financialized instantly; regulators have begun citing these cases to argue that "celebrity/political endorsement causes unacceptable consumer harm."

7. **Collapses are contagious**: Terra (2022) directly dragged down 3AC → Celsius → Voyager → finally FTX, showing these projects are highly interconnected at the **leverage, collateral, and market-making layers** — a single-point death spiral can escalate into a systemic event.

---

## 6. Risk notes for the reader
- All "drawdowns" and "peaks" above are approximate, and crypto prices are extremely volatile — **rely on live quotes**.
- Some projects (LUNA, HEX, SafeMoon, FTX, LIBRA) involve **ongoing litigation / criminal proceedings**; defer to final judicial conclusions for characterization.
- This document is a historical and mechanistic survey, **not investment advice**; I am not a licensed investment adviser. Generic red flags for spotting a "potential death spiral": abnormally high APY of unclear origin, uncapped reward tokens, very low initial float + huge future unlocks, price as the only support for the mechanism, opaque team/treasury.
