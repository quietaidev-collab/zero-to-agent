# Krenholm 1857 — Game Design Document
**Version:** 1.0 | **Genre:** 2D Construction Management Simulation | **Platform:** PC (Steam)
**Developer:** Solo Indie | **Engine Recommendation:** Godot 4 (free, lightweight, excellent 2D support)

---

## 1. Elevator Pitch

> *"Build Estonia's industrial future under the shadow of Imperial Russia."*

Krenholm 1857 is a 2D top-down construction management game in which the player oversees the real-life construction of the Krenholm Manufacturing Company — one of the largest textile factories in the Russian Empire — on Kreenholmi Island in the Narva River. Balancing ruthless Imperial production quotas, the dignity of Estonian and Ingrian workers, supply chain logistics, and financial survival, the player must transform a forested river island into a thriving industrial complex — or watch it collapse under debt and revolt.

---

## 2. Historical Context

| Fact | Detail |
|---|---|
| **Location** | Kreenholmi Island, Narva River — border of Estonia and Russia |
| **Founded** | 1857 by Ludwig Knoop (German broker) & Moscow merchants |
| **Peak workforce** | ~6,000 workers by 1872 |
| **Political context** | Governorate of Estonia under Tsar Alexander II |
| **Key tension** | Russian imperial capital interests vs. local Estonian/Ingrian labor |
| **Real events** | The 1872 Krenholm Strike — one of the first major industrial strikes in the Russian Empire |

The game's timeline spans **1857–1872**, culminating in the choice to suppress or side with the workers in the historic strike.

---

## 3. Core Design Pillars

1. **Historical authenticity** — Every building type, technology, and event is rooted in real 1850s–1870s industrial history.
2. **Moral tension over optimization** — The "best" economic decision is rarely the most humane one. The game never lets the player forget this.
3. **Readable complexity** — Inspired by Prison Architect's visual clarity: a non-gamer should be able to read the factory at a glance.
4. **Purposeful constraint** — The fixed island map, the river power dependency, and Imperial deadlines are all creative constraints, not limitations.

---

## 4. Core Gameplay Loop

```
Plan → Build → Hire → Produce → Satisfy Quota → Survive Imperial Review → Repeat
                                      ↕
               [Worker Morale / Unrest / Event Cards fire at any phase]
```

Each **in-game month** (roughly 2–3 real minutes) the player must:
1. **Assign workers** to operational buildings
2. **Manage supply** of raw cotton, coal, and machine oil
3. **Meet a soft production target** (cloth bolts)
4. **Respond to one random Event Card**
5. **Pay wages, loans, and Imperial tax** at month-end

Every **in-game year**, the Imperial Governor dispatches an **Inspector Visit** — a hard deadline review that can trigger penalties, forced upgrades, or factory seizure.

---

## 5. The Map

- **Fixed map:** Kreenholmi Island, hand-crafted, ~60×40 tile grid
- **Narva River** runs along both sides — water wheels and later turbines draw power from it
- **Bridge connections** to Estonian (west) and Russian (east) banks affect supply chain costs and worker commute
- **Buildable zones** are constrained by the island's real geography — no terraforming
- **Seasonal flooding** in spring reduces riverside tile availability

### Map Zones
| Zone | Use |
|---|---|
| River Edge | Water wheels, waste outflow, fishing (worker food bonus) |
| Central Island | Spinning halls, weaving halls, warehouses |
| North Settlement | Worker barracks, canteen, infirmary, church |
| South Administrative | Manager's office, Imperial telegraph, gatehouse |

---

## 6. Buildings

### Production
| Building | Function | Workers Required |
|---|---|---|
| **Spinning Hall** | Converts raw cotton → yarn | 8–24 |
| **Weaving Hall** | Converts yarn → cloth bolts | 8–20 |
| **Bleaching House** | Upgrades cloth value (+30%) | 4 |
| **Machine Workshop** | Repairs & maintains equipment | 2–4 |
| **Coal Store** | Buffers coal supply | 0 (passive) |
| **Cotton Warehouse** | Buffers raw cotton | 0 (passive) |
| **Water Wheel Station** | Generates power from river | 1 (overseer) |

### Worker Welfare
| Building | Effect |
|---|---|
| **Worker Barracks** | Houses 20 workers; overcrowding tanks morale |
| **Canteen** | Morale +10/month if stocked |
| **Infirmary** | Reduces injury-related absenteeism |
| **Church (Lutheran)** | Morale +5; required for Estonian worker retention |
| **School** | Unlocks skilled worker tier over time |

### Administrative
| Building | Effect |
|---|---|
| **Manager's Office** | Required to hire foremen; increases oversight |
| **Imperial Telegraph** | Receive quota updates early; costs monthly upkeep |
| **Gatehouse** | Controls worker movement; needed for lockout events |

---

## 7. Workers

Workers are the heart of the game. They are **not anonymous units** — each has a nationality, a skill tier, a morale value, and a small biography blurb.

### Worker Nationalities (historically accurate)
- **Estonian** — Local, lower wage expectation, high cultural pride, reactive to Lutheran church presence
- **Ingrian Finnish** — Recruited from across the Russian border, adaptable, homesick modifier
- **Russian** — Preferred by Imperial inspectors, higher wages demanded, creates friction with Estonian workers

### Worker Tiers
| Tier | Unlocked By | Productivity | Wage |
|---|---|---|---|
| Unskilled | Default | 1× | Low |
| Trained | 6 months on-site | 1.4× | Medium |
| Skilled | School building | 2× | High |

### Morale System
- Morale (0–100) affects productivity, absenteeism, and unrest risk
- Drops from: overcrowding, unpaid wages, injuries, harsh Imperial orders
- Rises from: canteen, church, fair treatment events, wage increases
- **Below 30:** Slowdowns begin. **Below 15:** Strike risk activates.

---

## 8. Resource Supply Chain

All resources arrive via supply route — no on-island extraction.

| Resource | Source | Route |
|---|---|---|
| **Raw Cotton** | Baltic sea trade (via Narva port) | West bridge → warehouse |
| **Coal** | Russian interior mines | East bridge → coal store |
| **Machine Parts** | St. Petersburg suppliers | East bridge; long lead time |
| **Machine Oil** | Trade merchant (event-based) | Either bridge |
| **Food** | Local Estonian farms + fishing | West bridge + river tiles |

**Supply disruptions** (bridge damage, trade embargoes, Imperial re-routing) are a key source of crisis events.

---

## 9. Imperial Pressure System

The Tsar's government has a **stake in Krenholm's output** — it supplies cheap cotton to the European market and demonstrates Russian industrial power. This creates the game's central antagonist force.

### The Quota Meter
- Each quarter, the player receives a **cloth bolt production quota**
- Meeting it: +Imperial Favour, access to cheap loans
- Exceeding it: Bonus favour, possible expansion grants
- Missing it: -Imperial Favour, fines, and eventually Inspector intervention

### Imperial Favour (0–100)
| Favour Level | Effect |
|---|---|
| 80–100 | Loan access, cheap coal contracts, workforce conscription |
| 50–79 | Neutral — standard operations |
| 30–49 | Increased inspector frequency, tax audits |
| 10–29 | Forced Russian manager installed (overrides some player decisions) |
| 0–9 | Factory seizure — GAME OVER |

### Inspector Visits
Inspectors arrive **once per year** and evaluate:
- Production output vs. quota
- Building safety (infirmary presence, exit routes)
- Worker housing capacity
- Presence of "subversive materials" (triggered by high unrest)

The player is given **2 weeks advance notice** to prepare — a tense scramble period.

---

## 10. Event Card System

Every month, **one Event Card** fires. Cards are drawn from a weighted deck influenced by the current game state.

### Sample Event Cards

| Card | Trigger Condition | Choice A | Choice B |
|---|---|---|---|
| **"The Governor Writes"** | Year 1 | Accept quota increase (+favour, -morale) | Negotiate delay (-favour, morale neutral) |
| **"Broken Loom"** | Machine Workshop absent | Lose 1 week production | Pay emergency repair fee |
| **"Fever in the Barracks"** | Overcrowded housing | Close barracks (homeless workers leave) | Operate through it (injury risk rises) |
| **"Lutheran Pastor Visits"** | Church built | Morale +15, no cost | Deny visit (-15 morale, +2 Imperial favour) |
| **"Estonian Foreman's Petition"** | 50+ Estonian workers | Grant foreman status (unlock tier) | Dismiss petition (unrest +20) |
| **"St. Petersburg Orders Silk"** | High Imperial favour | Pivot production (big reward, disruption) | Decline (favour -10) |
| **"Child Found in Spinning Hall"** | Unskilled workers high | Implement age checks (productivity -5%) | Look away (morale -10, unrest +15) |

The final act has a locked **"The Workers Assemble" card** that fires in 1872 regardless of state — the player must decide how to face the historic strike.

---

## 11. Financial System

### Income
- Cloth bolt sales (priced by market fluctuation)
- Imperial bonus payments (for exceeding quotas)
- School-trained worker efficiency dividends (long-term)

### Expenses
- Worker wages (weekly)
- Supply purchases (cotton, coal, parts)
- Building construction and maintenance
- Imperial tax (monthly, % of revenue)
- Loan repayments

### Loans
- Available from: Baltic German merchants, Imperial state bank
- State bank loans: cheap interest, but tied to Imperial Favour — defaulting causes a Favour crash
- Merchant loans: higher interest, but no political strings

---

## 12. Win / Lose Conditions

### Game Over States
- Imperial Favour reaches 0 (factory seized)
- Bankruptcy with no available loans
- Full worker revolt with no Gatehouse and Imperial Favour below 40 (factory burned)

### Victory Conditions (choose your legacy)
The game ends in **1872** with the historic strike. The player's final choices shape the ending:

| Ending | Condition | Description |
|---|---|---|
| **"The Imperial Jewel"** | High favour, low morale | Krenholm becomes the Empire's model factory. Workers are forgotten. |
| **"The Compromise"** | Medium favour, medium morale | A negotiated settlement. Modest reforms. History moves slowly. |
| **"The Workers' Factory"** | Low favour, high morale | You sided with the workers. The Imperial governor is furious. The factory survives — barely — and becomes a legend. |
| **"Ashes"** | Favour < 20 AND morale < 20 | Neither side trusts you. The factory burns in the strike. |

---

## 13. Art & Audio Direction

### Visual Style
- **2D top-down**, clean and readable — Prison Architect meets 19th-century technical illustration
- Palette: desaturated industrial greys and browns, with warm amber candlelight in worker quarters and cold blue Imperial administrative buildings
- Buildings drawn in a period-accurate architectural cross-section style
- Workers are small, recognizable silhouettes with nationality-coded clothing colours

### Audio
- **Ambient soundscape:** River rushing, loom clatter, distant bells, steam hiss
- **Music:** Estonian folk themes (regilaul vocal style) that gradually incorporate industrial rhythmic elements as the factory grows — a metaphor for cultural erosion
- **Event cards:** Voiced in period-accurate Estonian, Russian, and German (subtitle translated) — a tiny but powerful authenticity detail

---

## 14. Scope & Development Roadmap

> **Estimated solo dev time: 20–30 weeks (core prototype)**
> Budget 3× total for polish, bug fixing, and release preparation ≈ **~14–22 months to 1.0**

### Phase 1 — Core Loop (Weeks 1–10)
- [ ] Grid-based building placement on fixed Narva island map
- [ ] Worker hiring, assignment, and wage system
- [ ] Basic resource supply chain (cotton → yarn → cloth)
- [ ] Water wheel power system
- [ ] Month-end financial ledger

### Phase 2 — Pressure Systems (Weeks 11–18)
- [ ] Imperial Favour meter and quota system
- [ ] Inspector visit events
- [ ] Worker morale system and unrest meter
- [ ] Core Event Card deck (30 cards minimum)

### Phase 3 — Depth & Endings (Weeks 19–26)
- [ ] Full building roster
- [ ] Worker nationality and tier system
- [ ] Loan system with two lender types
- [ ] Historical timeline events (1857–1872)
- [ ] Three ending sequences

### Phase 4 — Polish (Weeks 27–30+)
- [ ] Art pass on all buildings and UI
- [ ] Audio integration (soundscape + music)
- [ ] Balancing and playtesting
- [ ] Steam page and trailer

---

## 15. Intentionally Cut Features (Scope Management)

These were considered and **deliberately excluded** from v1.0 to keep the project shippable:

- ❌ Procedural / randomised maps (fixed map is more historically honest anyway)
- ❌ Day/night cycle (adds art cost with little gameplay gain)
- ❌ Tech tree (upgrade unlocks via Event Cards instead — simpler, more narrative)
- ❌ Multiplayer
- ❌ Mod support (can be added post-launch if community forms)

---

## 16. Why This Game Matters

Krenholm's story is nearly unknown outside Estonia, yet it is a **microcosm of the entire Industrial Revolution's moral arc** — capital vs. labour, empire vs. culture, efficiency vs. humanity. The 1872 strike preceded most European labour movements by years. By letting the player *build* the machine that eventually turns on its operators, Krenholm 1857 makes industrial history visceral, personal, and genuinely difficult.

---

*Document prepared for solo development planning. All historical details sourced from Krenholm Manufacturing Company records and Estonian industrial history archives.*
