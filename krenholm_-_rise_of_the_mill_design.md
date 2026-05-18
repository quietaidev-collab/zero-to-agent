# 🏭 Krenholm: Rise of the Mill
### Game Design Document v1.0

---

## Concept
A 2D side-view construction management game set in 1857 Estonia under Tsar Nikolai's Imperial Russia. The player takes the role of a **site foreman** overseeing the real-life construction of Krenholm Manufacturing Company — destined to become the largest textile factory in Europe. Balancing Imperial pressure, harsh worker conditions, and scarce resources, the player must drive the construction to completion before time and budget run out.

---

## Setting & Tone
- **Location:** Narva River island, Estonia — a raw industrial site split by rushing water
- **Era:** 1850s Imperial Russia, Industrial Revolution sweeping West into the East
- **Tone:** Gritty, determined, historically grounded. The weight of Empire behind every brick.
- **Language flavor:** Russian/Estonian bilingual signage, Imperial decree notices posted on site

---

## Core Game Loops

### 🔁 Loop 1 — Daily Task Assignment (Strategy Layer)
Each in-game day, the foreman receives a **work order** from the Imperial investors. The player assigns workers to one of three active construction zones:
- **Foundation & Masonry** — laying the mill's stone base along the riverbank
- **Machinery Hall** — assembling imported industrial looms and steam engines
- **Worker Barracks** — housing must be built to keep the workforce on site

Workers have a **Stamina Bar** and a **Skill Level**. Assigning the wrong worker to the wrong task wastes a day. The player must read each worker's brief profile card and place them wisely before sunrise ends.

---

### 🔁 Loop 2 — Resource & Supply Management (Pressure Layer)
Materials arrive by barge on the Narva River on a weekly schedule. The player must:
- **Accept or defer** incoming shipments (storage space is limited)
- **Spend Imperial Rubles** to rush critical supplies when construction stalls
- **Manage shortages** — missing timber halts masonry, missing coal stops the steam crane

A **Supply Board** on the left of the screen tracks: Timber, Stone, Coal, Iron Parts, and Food Rations. If Food Rations hit zero, workers begin deserting the site.

---

### 🔁 Loop 3 — Crisis Response (Reaction Layer)
Random events fire every few in-game days, forcing quick foreman decisions:
| Event | Choice A | Choice B |
|---|---|---|
| Worker injury on scaffolding | Pay for medical care (lose Rubles) | Ignore it (lose Worker Morale) |
| Imperial inspector arrives | Stop work for inspection (lose a day) | Bribe the inspector (lose Rubles) |
| River flood warning | Reinforce the foundation now (spend resources) | Gamble and continue (risk collapse) |
| Worker strike brewing | Grant a rest day (lose progress) | Push through (morale tanks) |

Each choice feeds back into Loop 1 and Loop 2, creating a chain of consequences.

---

## Win Condition
Complete **all four construction phases** of Krenholm before the Imperial deadline expires:
1. ✅ River Foundation & Dams
2. ✅ Main Mill Building (Stone Walls + Roof)
3. ✅ Machinery Hall (Looms + Steam Engine operational)
4. ✅ Worker Barracks (minimum capacity reached)

**Final scene:** The mill fires up for the first time. Steam pours from the chimney. Workers cheer. An Imperial certificate is stamped. *Krenholm is open.*

---

## Lose Conditions
- ⛔ **Budget reaches zero** — Imperial investors pull funding
- ⛔ **Workforce drops below 5 workers** — site is abandoned
- ⛔ **Deadline expires** with less than 3 phases complete — the foreman is dismissed

---

## Art Style
- **2D flat side-view** — think hand-illustrated lithograph aesthetic, muted sepia and slate tones with amber lantern light
- **UI styled as Imperial documents** — parchment-colored panels, stamped borders, handwritten fonts
- **Workers are small distinct silhouettes** on a large construction site background — each with a visible stamina bar above their head
- **Construction progress is visible on screen** — the mill building literally grows brick by brick as phases complete
- **Weather cycles** — overcast Estonian skies shift from grey drizzle to frozen winter as the game progresses, affecting worker stamina

---

## Key Numbers (Prototype Scope)
| Parameter | Value |
|---|---|
| Game length | ~25 in-game days per run |
| Worker roster | 8–12 workers |
| Construction phases | 4 |
| Random crisis events | 10 unique events |
| Estimated playtime | 20–30 minutes per run |

---

## Historical Hook
End-of-run screen shows a **real historical fact** about Krenholm — e.g., *"By 1872, Krenholm employed over 6,000 workers and was the largest cotton mill in the world."* Grounds the fantasy in pride and real Estonian history.

---
*Design by: Senior Game Designer | Based on the historical Krenholm Manufacturing Company, Narva, Estonia, est. 1857*
