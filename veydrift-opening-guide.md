# Veydrift Phase 1: The Four-Planet Opening

A build guide for the first four planets, from first colony through Cruiser capability.
Derived from the Veydrift contract source (`VeydriftCatalog.sol`, `VeydriftGame.sol`,
`VeydriftCombatModule.sol`). Contract-confirmed numbers are stated plainly; constructed
heuristics are marked **(heuristic)**.

---

## Why four planets first

`maxPlanets = 1 + Astrophysics level`, and Astrophysics costs scale at 1.75x per level.
The first three levels are nearly free next to everything that follows:

| Astro level | Unlocks planet | Marginal cost (M / C / D) | Running total (all resources) |
|:-----------:|:--------------:|:-------------------------:|:-----------------------------:|
| 1 | 2 | 4,000 / 8,000 / 4,000 | 16,000 |
| 2 | 3 | 7,000 / 14,000 / 7,000 | 44,000 |
| 3 | 4 | 12,200 / 24,500 / 12,200 | 92,900 |
| 4 | 5 | 21,400 / 42,900 / 21,400 | 178,600 |

Astro is not the real cost in this phase. Each colony's overhead (ship 40k, fuel,
bootstrap ferry, defense package) runs 70-90k, roughly matching each Astro step.
Expand as fast as that overhead allows.

**Crystal note:** Astrophysics costs 2x crystal at every level, and the Cruiser
tech chain is crystal-heavy. Crystal is the binding resource of this entire phase.

---

## Site selection

Temperature is permanent; everything else can be rebuilt.

- Deuterium is the only temperature-dependent resource:
  `multiplier = max(0, 12,800 - 20 x max temp) / 10,000`
- Solar Satellite output: `clamp((max temp + 140) / 6, 1, 65)` energy each
- Metal and crystal are temperature-blind

Observed correlation **(n=3, inference)**: high positions (12-15) run cold,
low positions (1-3) run hot. Aim accordingly.

| Want | Target position | Why |
|------|:---------------:|-----|
| Deut colony | 12-15 (frozen) | 1.36x+ deut multiplier at -40C and below |
| Future energy world | 1-3 (scorching) | Satellite cap of 65 energy at 250C+ |
| Crystal / metal world | anywhere nearby | Temp-blind; minimize ferry distance |

---

## The defense doctrine: two Heavy Lasers per planet

Every planet gets **2 Heavy Lasers (12,000 metal / 4,000 crystal total) on landing day**,
before mines, before anything.

The contract math: damage at or below shield does nothing, and damage must exceed
30% of hull to trigger destruction rolls.

- Heavy Laser: shield 100, hull 800
- Light Fighter attack 50: bounces off the shield entirely. Zero damage at any fleet size.
- Heavy Fighter attack 150: 50 through shield = 6.25% of hull. Can never kill one.
- Two HLs alone hold against ~13 concentrated Light Fighters (5 shots each = 18.75%, under threshold)

A drawn battle pays no loot (`loot settles only on BattleOutcome.AttackerWin`).
Two Heavy Lasers make a planet structurally immune to the entire fighter tier.
The wall breaks at Cruisers (attack 400), which is a Phase 2 problem.

**(heuristic)** No planet sits more than one day without its pair.

---

## Planet 1: Home capital

Temperate world. Role: research seat, fleet yard, metal base.

| Line | Target | Notes |
|------|:------:|-------|
| Metal Mine | 14 | Leads early, then yields priority to crystal |
| Crystal Mine | 13 | Priority line from mid-phase on |
| Deut Synth | 9 | Stop here; the ice colony takes over deut |
| Solar Plant | match demand | Synth demand is 2x a mine's per level |
| Robotics | 4 | Build speed for everything below |
| Shipyard | 5 | Cruiser gate |
| Research Lab | 4+ | The only lab in the empire until IRN |

**Research order:** Computer 2-3 first, then Impulse 4, Ion 1-2, finish Shipyard 5.

Fleet slots are `1 + Computer level`. Every transport, colonize, and attack
occupies a slot simultaneously. Computer, not shipyards, is what strangles a
multi-planet empire first.

**Defense:** existing launcher/laser chaff plus the 2 Heavy Lasers.

---

## Planet 2: Ice colony (deut specialist)

Frozen world, high position. Role: fund the fuel and deut lines of every future bill.

| Line | Target | Notes |
|------|:------:|-------|
| Deut Synth | 10-11 | ~380-500/h at 1.36x, triple a temperate planet |
| Solar Plant | = Synth level | A matched pair is exactly self-powering |
| Metal Mine | Synth - 1 | Self-funding support **(heuristic)** |
| Crystal Mine | Synth - 3 | Self-funding support **(heuristic)** |
| Robotics | 2 | |
| Shipyard | 1 | Repair capability only; no production here |

No lab. No fusion reactor, ever, on a deut world (upkeep eats the product).
Defense: the Heavy Laser pair, nothing else.

---

## Planet 3: Crystal world

Sited for fields and proximity to home, not temperature. Role: feed the crystal
appetite of Astro, Ion, Impulse, and every capital ship after.

| Line | Target | Notes |
|------|:------:|-------|
| Crystal Mine | 12-13 | The priority line |
| Metal Mine | 10 | Funds crystal upgrades (they cost 2:1 metal) |
| Solar Plant | match demand | |
| Deut Synth | 0-3 | Token levels at most |
| Robotics | 2 | |

Bootstrap ferry: ~25-30k covers Robotics, first mine tiers, and the Heavy Lasers.
One Small Cargo convoy plus the Colony Ship's own hold.

Why crystal gets the dedicated planet: home leans metal, and every gate ahead
(Astro at 2x crystal, Battlecruiser at 40k, Destroyer at 50k) is crystal-bound.

---

## Planet 4: Hot world (future energy site)

Scorching world, low position. Colonize when planet 3 is self-funding and
empire output is roughly 100k/day **(heuristic)**.

The point of taking it now is locking the site. Temperature is permanent and
250C+ worlds hit the 65-energy satellite cap, which is the eventual path to
Graviton's 300,000 produced-energy requirement. In Phase 1 it just runs
temp-blind mines like any colony.

| Line | Target | Notes |
|------|:------:|-------|
| Metal Mine | 12 | |
| Crystal Mine | 10 | |
| Solar Plant | match demand | |
| Deut Synth | 2-3 max | 0.78x multiplier or worse; not worth feeding |
| Robotics | 2 | |

**No satellites yet.** Every mobile ship has rapidfire 5 against satellites,
and each one adds 40 points of score. The satellite farm waits for a real
defense line in a later phase.

---

## Logistics standing orders

- 4+ Small Cargos (2,000/2,000 each) running a ferry loop before planet 3 lands
- Ferry direction: metal and crystal flow toward whichever planet is paying the
  next Astro or tech bill; deut flows from the ice colony to wherever fleets launch
- Fleet slots budget **(heuristic)**: planets minus 1, minimum, kept free for
  logistics; raise Computer before the loop deadlocks

---

## Phase exit test

Do not buy Astrophysics 4 until all of these hold:

- [ ] One Cruiser per day off home's yard without starving the queue (29k/day surplus)
- [ ] Computer 3 or higher
- [ ] All four planets wearing their Heavy Laser pairs
- [ ] Ferry loop runs on schedule, not on attention
- [ ] Empire raw output at or above ~150k/day

The Cruiser line doubles as the raid economy. Cruisers take zero losses against
fighter-tier defense (max incoming hit is 7.4% of hull, under the 30% threshold),
so every successful raid is pure profit after fuel, and raiding funds Phase 2's
gates faster than mines alone.

## What Phase 1 deliberately does not build

Standing fleet beyond the cargo loop and the first Cruisers. Ships cost score
(4-28 points each) and sit as loot exposure; mines and mid-level buildings are
score-cheap production. The opening wants you economically deep and militarily
quiet until the Ion Cannon wall goes up in Phase 2.

---

*Sources: veydrift.com/docs.md and the Veydrift contract repository
(github.com/Borodutch/veydrift), read August 2026. Combat thresholds, costs,
score weights, and the maxPlanets formula are from contract source. Mine-spacing
ratios, pacing rules, and the exit test are constructed heuristics.*
