# UNTITLED — Inverted-Arc Strategy Game
## Game Design Document

**Status conventions.** Unmarked text is decided. **[OPEN]** marks a genuine unresolved question. **[PROPOSAL]** marks a suggestion raised but not adopted. **[DEFERRED]** marks something intentionally out of first-version scope. Sourced claims are separated from design interpretation wherever both appear.

---

## 1. Premise

A multiplayer strategy game that runs the genre's standard arc backwards.

The conventional arc in this lineage — Solar Realms Elite through OGame through Veydrift — is: start small and blind, expand, research upward, acquire information, meet other players late, fight at the top of the curve. Growth is the verb; the endgame is peak capability.

This game inverts it.

| | Conventional | This game |
|---|---|---|
| Opening state | Empty map, no tech, weak forces | Populated world, complete tech tree, strong armies |
| Economy | Self-sufficient, trade optional | Globally integrated, every player imports from every other |
| Information | Fog at start, cleared by scouting | Full visibility at start, fog *appears* as the world breaks |
| Tech trajectory | Monotonic ascent | Full → collapse → divergent recovery |
| Alliances | Form early, for growth | Form late, for reconstruction |
| Arc shape | Build up to a war | Fall apart, then rebuild |

**The thesis, in one line:** armies require supply chain, and this game is about the breaking down of the supply chain.

### 1.1 The four acts

1. **Integration.** Full tech, full visibility, dense mutual dependency. Competition is over fuel access, not territory.
2. **Squeeze.** Climate change raises food's fuel cost. Fuel scarcity makes seizure cheaper than supply, at different moments for different players. First defections.
3. **Collapse.** Supply chains break, fuel production goes offline, mechanization fails, fog spreads. Players fall back down the tier ladder.
4. **Reconstruction.** Blocs form around restored networks. Rejoin or stay sovereign. No formal victory is declared.

---

## 2. The core rule

**Capability equals satisfied inputs.**

Every technology, unit, and building has named input dependencies produced by specific nodes elsewhere in the world. A player's available capabilities at any moment are a readout of which inputs are currently reaching them. Nothing is ever removed by fiat — only starved.

This single rule generates the acts rather than scripting them:

- **Degradation** is unmet dependencies: automatic, reversible, and local. Two players with intact bilateral trade keep their tech while the rest of the world goes dark.
- **Fog of war** is the same rule applied to sensing and communications, which have inputs like anything else. There is no separate fog subsystem.
- **Alliances** are surviving subgraphs — observed, not declared.
- **Reconstruction** is reconnection, measurable directly off the graph.

Nearly every mechanic in this document is a consequence of this rule applied to a specific case. Where a mechanic is *not* derivable from it, that is called out explicitly.

---

## 3. Fuel, food, and the squeeze

### 3.1 Fuel sits underneath the dependency graph

Fuel is not one commodity among many. It powers transport and production, making it the precondition for the graph functioning at all. A fuel shortage degrades the network's throughput rather than adding another unmet line item.

This placement is deliberate. If fuel were simply another traded good, the dependency graph would flatten into a single commodity price and the structural asymmetry between positions — the thing that makes named, located dependencies interesting — would be lost.

Fuel is the sole tracked bottleneck resource. Higher tiers need rare earths, uranium, and similar inputs, but mining, refining, and transporting those is itself fuel-dependent, so they are treated as fuel-derived rather than independently scarce. This preserves one rule generating everything rather than a second scarcity axis competing with the first.

### 3.2 Fuel is located at specific nodes

Not a global pool. Fuel exists at identifiable places on the map that can be held, traded from, or taken. Consequences, all falling out of node-location rather than being separately designed:

- **Scarcity has an address.** When the squeeze arrives, the map already tells every player where to go. Positional asymmetry at world generation does real strategic work.
- **Two strategic identities emerge unprompted.** A player sitting on fuel nodes but light on industry is a supplier with leverage. A heavy industrial player with no fuel is powerful and precarious. They need each other in Act 1 and are natural enemies in Act 3. Neither role is authored.
- **Second-order failure.** Losing a fuel node does not only cost fuel; it degrades the ability to move everything else. Cascading failure is what distinguishes collapse from a stat declining.
- **[PROPOSAL] Price is not a market.** With fuel at nodes, price is what the holder demands, negotiated bilaterally, varying by counterparty and distance. Less clean than an exchange, but it makes Act 1's play negotiation rather than trading.

### 3.3 Extraction and refining are capabilities, not guarantees

Fuel nodes cannot be destroyed, but the ability to extract or refine at a node can be lost. Extraction and refining are themselves capabilities with named input requirements — equipment, skilled labor, a maintained tech chain — governed by the same core rule as everything else. A node with no satisfied extraction inputs produces nothing regardless of how much fuel remains underground.

This decouples territorial possession from functional capability. Conquering a node does not automatically restore its output; the occupier still has to satisfy the node's own extraction dependencies, which may be harder for an occupier than for the previous holder.

### 3.4 Food is fuel-dependent

Food production is a capability like any other, and one of its named inputs is fuel. Mechanized farming runs on it directly, and synthetic nitrogen fertilizer — the input that lets a hectare feed more people than pre-industrial yields allow — is manufactured from a fuel feedstock, since ammonia synthesis draws its hydrogen from methane via steam reforming.

**What the data shows.** Estimates converge on roughly half the global population being sustained by food grown with synthetic nitrogen fertilizer, a dependency that did not exist before 1910. This is contested on pace and inevitability, not magnitude: a documented counter-argument holds that population-collapse framing overstates immediacy, since adaptation, extensification, dietary shift, and reduced waste would blunt a fertilizer shock before it became a literal die-off. Both positions are sourced; neither is fringe.

**Interpretation.** Naming food as the specific fuel-dependent capability makes this design's causal chain match the mechanism in the historical literature (3.6), not just its shape.

### 3.5 The core allocation loop

**The starting point has no slack.** At Tier 6, under full cooperation, exactly enough Tier 6 fuel is produced to meet total Tier 6 demand — food and tech combined. Not a comfortable surplus, an exact balance. The system starts already fragile: any negative perturbation creates an immediate deficit rather than being absorbed.

**Climate change acts on food, not on tech.** As conditions degrade, food production requires more fuel for the same output. Since fuel is the sole bottleneck and food and tech draw on the same pool, this is not two shortages, it is one resource pulled harder in one direction. Every unit of fuel that food's rising cost consumes is a unit unavailable to maintain tech at its current tier.

**This makes the player's recurring decision a budget.** How much of the shared pool feeds the population versus maintains the military at its current tier — and which specific army stats absorb the difference. That is the game's central repeated choice.

**Conflict threatens the equilibrium independently of climate.** "Everyone getting along" is a condition of the starting balance, not color. The exact-balance calculation assumes efficient cooperative distribution, so conflict breaking that cooperation is a second, independent source of shortfall. This produces a reinforcing loop parallel to the one at 4.1: fuel shortage causes conflict, conflict degrades the cooperative efficiency the equilibrium depended on, which worsens the shortage, which deepens the conflict.

### 3.6 Historical grounding *(sourced, not a design decision)*

**What the data shows.** Zhang et al., studying China over the last millennium and later extending to continental scale (1400–1900), found war frequency and population decline tracked temperature cycles: cooling reduced agricultural output, producing price inflation, then war outbreak, then famine, then population decline, in that sequence. A later causality analysis by the same group concluded climate-driven economic downturn was the direct cause of crisis, and found that regions with high land-carrying capacity or trade-based economies were buffered, not suffering the same food-supply shrinkage during the same cooling period.

Separately, Turchin and Nefedov's structural-demographic theory finds that population growth outpacing productivity produces price inflation and falling real wages on its own, causing elite overproduction — too many aspirants for too few elite positions — with intra-elite competition for the shrinking surplus producing instability, typically expressed as internal breakdown rather than external war.

**Interpretation.** The design's dichotomy — take fuel by force, or face revolution at home — maps onto two distinct documented pathways rather than one. Zhang's chain supports the "take by force" branch. Turchin's SDT supports "revolution" as a mechanism in its own right rather than a lesser fallback. The buffering finding supports the design's claim that the squeeze should not hit every player simultaneously: geographic and economic position determined exposure historically, and fuel-node proximity plays that role here.

### 3.7 Conflict trigger

As supply diminishes, cost rises. Every player faces the same choice on a different timetable: **take fuel by force, or face revolution at home.**

This resolves the Act 1 equilibrium problem without the designer selecting a victim. Under universal mutual dependency nobody rationally defects first, but a rising price means there is a point where seizing costs less than buying, and that point arrives at different times for different players depending on reserves, military strength, and distance to nodes. The first defection is a calculation, not a story beat.

**[PROPOSAL] Revolution should be a gradient, not a fail state.** If revolution is elimination, every player defects at the same threshold and the arc becomes deterministic. If it is a gradient — unrest reduces output, then reduces held-node yield, then flips territory to neutral — some players can rationally absorb unrest for a period, and that staggering is what produces a collapse arc rather than one simultaneous scramble. Structural-demographic theory models instability as exactly this kind of graded process, which is supporting evidence for the proposal rather than a reason it is adopted.

**[OPEN] Cliff or slope.** Whether food output falls off a cliff when fuel access is cut, or declines on a slope that gives populations time to adapt. Climate change as described in 3.5 is a continuous process, which leans toward slope, but this is an inference from the framing rather than a decision. The same question applies to revolution above; both should be decided together.

---

## 4. The tier ladder

Seven tiers, floor to ceiling. Tiers 0–5 are grounded in real technological history and sequenced accordingly. Tier 6 is explicitly speculative.

**Tier 0 — Flavor floor.** Muscle power. No industrial fuel use of any kind, fire only for warmth and cooking. Texture and absolute narrative floor, not a tier sustained play is expected to reach.

**Tier 1 — Unrefined fuels.** Wood and coal burned directly for heat, no engines. Forges and kilns, blacksmithing, black-powder chemistry. The technological ceiling achievable without converting heat into motion.

**Tier 2 — Preindustrial mechanized (practical floor).** Steam and water power. Coal, timber, animal power, mechanical and hydraulic engineering — none drawn from the game's fuel resource. Steam engines and locomotives, water-driven mills, telegraph, breech-loading firearms, horse cavalry, horse-drawn artillery.

**Tier 3 — Early combustion.** The first tier that consumes the fuel resource. Internal combustion, early oil refining, basic electrification. This is where collapse first bites: everything at Tier 3 and above goes dark without fuel; Tiers 0–2 do not.

**Tier 4 — Full industrial mechanization.** Mass production, mechanized militaries, and synthetic nitrogen fertilizer — the specific link between fuel and food. Losing this tier is what makes the food shock real rather than notional.

**Tier 5 — Late industrial / information age.** Roughly the setting's technological present. Full fuel dependency plus electronics, computing, nuclear power.

**Tier 6 — One tier past today (speculative ceiling).** Hypersonic drones, autonomous robotic infantry, AI-coordinated command and control. Every player starts here.

**"The primitive tier"** means Tiers 0–2 collectively: everything below the fuel-dependency threshold. Tier 2 is the practical floor; Tiers 0–1 exist for extreme cases and texture.

### 4.1 Collapse is tier-by-tier, and it feeds itself

Because each tier depends on a larger, more specific bundle of satisfied inputs than the tier below, a fuel shortage does not drop a player straight from Tier 6 to the floor. It peels tiers from the top down as each dependency chain breaks, giving the collapse texture and giving players a sequence of decisions rather than one.

Fuel powers the network; the network produces fuel-production technology. A break in either propagates into the other, so collapse depth is determined by player behavior rather than a curve the designer drew. It is possible for the world to reach a state where fuel cannot be produced at all.

### 4.2 The primitive tier is parallel, not degraded

The defining property of Tiers 0–2 is not that they are weaker but that **they require no fuel imports.** Slow, low-throughput, sovereign with respect to the resource the collapse is actually about. Coal, timber, and other non-fuel inputs can still be traded locally without contradicting this.

Collapse therefore does not strip a player down; it converts them from a high-throughput dependent node into a low-throughput independent one. That is a lateral transformation with genuine upside, which is what makes collapse survivable to play through rather than a reason to quit.

### 4.3 The primitive tier's advantage is payable upkeep

The primitive tier does not win by doing something mechanized forces cannot do. It wins because **its upkeep can still be paid.**

The relevant comparison during collapse is not horse versus tank; it is horse versus a tank that does not run. A mechanized army without fuel is not weaker, it is stationary. Primitive units have upkeep the local, import-free economy can actually meet, making them the only forces that remain operable once the network fails. This is the core rule applied to upkeep rather than production.

*An earlier proposal giving primitive units terrain independence was considered and rejected: it would have required a traversability layer for an advantage the upkeep rule already provides.*

### 4.4 Stranded assets: hold or cannibalize

Collapse makes higher-tier units inoperable rather than destroyed. Per unit, a player chooses:

- **Hold.** The unit sits dormant, unchanged, doing nothing. If fuel is later restored it returns to full function. A real bet: a held unit produces nothing and can be captured while it waits.
- **Cannibalize.** The unit is broken down and its high-value component mounted on primitive motive power, producing an immediate, permanent, fuel-free hybrid. A tank becomes horse-drawn artillery: the gun survives, the engine and chassis do not.

**Cannibalization is irreversible.** Hold and cannibalize are genuinely opposed choices, not two speeds of the same path. Hold trades current capability for a chance at full restoration; cannibalize trades away that chance for a permanent, lesser asset. Nothing recovers the original unit.

**Cannibalization is also a proactive budget decision, not only a reaction to a stranded unit.** Facing food's rising claim on the shared pool (3.5), a player can choose to take units down a tier *before* they strand, freeing fuel for food and reducing revolution risk.

**In combat**, a cannibalized unit is favored to beat a native unit built at its own lower tier, reflecting the genuine higher-tier component it carries. But there is a small chance of total rout — a catastrophic outcome distinct from ordinary loss — and a unit that routs this way permanently loses its cannibalized bonus: the salvaged component is destroyed or abandoned, and the unit reverts to ordinary tier-matched performance even if crew and unit survive. This is a second irreversibility on top of the first. **[OPEN]** Exact win and rout odds.

**Consequences.** Collapse does not level players onto a common baseline — a formerly rich, heavily mechanized power collapses into a far more dangerous scavenger than a power that was always poor. Prior strength persists, changing currency from throughput to scavenged firepower. And the world carries a permanent capability floor: every cannibalized unit is permanently removed from what full reconnection can ever restore. Reconstruction has a ceiling as well as a process.

### 4.5 Banked reentry

Any node can produce fuel one tier above its own current tier directly, at a very slow rate, with no special infrastructure. Output banks over time; once enough is stockpiled it can be spent to field one unit of that higher tier. Capped at exactly one tier above native — a Tier 0 node can reach for Tier 1, never directly for Tier 6, regardless of patience.

**Trading partners boost the rate.** A node with active trade relationships banks faster than an isolated one. This gives a primitive-tier civilization a concrete mechanical reason to maintain trade and alliance ties: cooperation does not just satisfy ordinary inputs, it accelerates the comeback path specifically.

This is a third path into higher-tier capability. Hold and cannibalize both require having already possessed the unit; banked reentry requires neither, so a civilization that lost or cannibalized everything can still claw back higher-tier units from nothing. Because it is a standing rate rather than a one-time contingency, it is repeatable: a long-horizon strategy available to any patient civilization.

Spent fuel is consumed, not returned, so each subsequent unit requires banking from scratch.

**[OPEN]** Banking threshold and production rate, plain and trade-boosted. Whether a fielded unit's ongoing upkeep requires that higher fuel grade or whether the one-time cost covers it outright.

### 4.6 [PROPOSAL] Below the fuel line

Every collapse mechanic above runs on fuel scarcity, but Tier 2 consumes no fuel. Once a civilization is at Tier 2, the mechanic that got it there has nothing left to push against.

**Proposed mechanism: war damage to the industrial base, not a second depletion curve.** Tier 2 still needs real inputs — skilled labor with the engineering and machining knowledge to maintain steam power, a supply of coal or timber, tooling capacity for precision parts. None of these deplete the way fuel does; they get destroyed, by the war fuel scarcity already caused. The war does not end when fuel stops being the constraint, it starts consuming a different set of inputs.

This would give two structurally different collapse mechanisms stacked on each other: economic scarcity above the fuel line, destruction below it. No new resource ladder — skilled labor and coal/timber are ordinary capability inputs subject to war damage, not a parallel tracked scarcity.

A civilization reaching Tier 1 or 0 is plausibly a losing side in an ongoing war, which makes those tiers a natural signal of approaching elimination rather than mere economic squeeze.

---

## 5. Tiers 0–3 are scavenged, not reenacted

Tiers 4–6 are clean, functioning technology because they represent an intact civilization. Tiers 0–3 are not that rebuilt from scratch — they are what is left of a civilization that had Tier 6 and lost it, and that difference should read in every description.

This follows from cannibalization rather than adding to it. A Tier 1 musket here is not an accurate 17th-century musket; it is a barrel or lock pulled from Tier 4+ wreckage and hand-fitted by a smith who can forge a stock but could not manufacture the harder metal parts from nothing. A Tier 0 raider's armor is plate scavenged from a wreck, not tanned leather. The technology looks period-appropriate and is functionally rated at that tier, but its origin is salvage, not organic invention.

**Tier 0.** Raiders and remnant bands in armor pieced from scavenged hull and vehicle plating; weapons that are sharpened scrap and rebar as often as forged metal. Siege engines built around salvaged girders and cable, since metal survives collapse better than any organization capable of smelting more.

**Tier 1.** Smiths who can forge a stock and lock but not a barrel, so functioning barrels are the scarce scavenged part rather than the smith-made part — the reverse of how the real 17th century worked, and worth keeping visible.

**Tier 2.** Where the aesthetic is already mechanically established: horse-drawn artillery *is* a cannibalized tank gun. Steam ironclads patched with welded salvage plate; cavalry in scavenged high-tier plate over period tack.

**Tier 3.** Where this becomes the genre's full visual language. Jury-rigged combustion vehicles built from multiple wrecks, engines kept alive by scavenging rather than supply chain, mismatched armor welded onto whatever chassis survived. The first tier where a wrecked engine is worth more than anything a smith can build by hand.

---

## 6. Armies

Armies are where abstract capability becomes a concrete, ownable, playable object.

**Structure.** An army has:
- **Size**, measured in people, drawn from and limited by the controlling civilization's population.
- **Five stats**, each independently set at a tier (0–6): infantry, indirect fire, sea power, air power, mechanized infantry.

**Why five independent tiers rather than one army-wide tier.** This is the playable form of tier-by-tier collapse. Each capability depends on its own bundle of satisfied inputs, so an army's air power can sit at Tier 2 while its infantry holds at Tier 5, if that is where the supply chain broke and where it did not. The stat block makes that visible and actionable rather than a background narrative claim.

**Supply chain dependency.** Each stat, at its current tier, needs that tier's fuel grade and whatever other tier-specific inputs the core rule implies. When a given stat's supply chain breaks, that stat triggers either the hold-or-cannibalize choice or proactive reallocation, independently of the other four. A player does not manage one army-wide tier number; they manage five supply chains that can fail on five separate schedules.

**[OPEN]** The numeric relationship between army size and stat capability. Whether army size draws on the same food supply competing with fuel in 3.5 — a natural extension, since soldiers eat, but an inference rather than a decision.

### 6.1 Representative units by tier

Historical examples for Tiers 0–5; Tier 6 is speculative.

| Tier | Infantry | Indirect fire | Sea power | Air power | Mechanized infantry |
|---|---|---|---|---|---|
| **0** Flavor floor | Levies with sharpened scrap and forged spearheads | Siege engines, salvage-frame catapults and ballistae | Salvage-hulled rafts and dugout canoes | Hang gliders, scavenged-fabric wings | Mounted raiders |
| **1** Unrefined fuels | Musket and pike infantry, barrels scavenged and hand-fitted | Muzzle-loading cannon and mortars | Sail-powered gun ships | Hot air balloons, wood or coal-fired, unpropelled | Dragoons, heavy cavalry |
| **2** Preindustrial mechanized | Breech-loading rifle infantry | Horse-drawn artillery, some cannibalized from higher-tier guns | Coal-fired steam ironclads, salvage-plated | Steam-powered dirigibles, observation balloons | Cavalry, scavenged plate over period tack |
| **3** Early combustion | Bolt-action rifle infantry | Truck-towed field guns, jury-rigged mounts | Early oil-fired warships, wreck-salvaged hulls | First-generation biplanes, scavenged engine parts | Motorized infantry, mismatched multi-wreck vehicles |
| **4** Full industrial | Combined-arms rifle squads | Self-propelled artillery | Fuel-powered destroyers and carriers | Piston-engine fighters and bombers | APCs, tank-escort infantry |
| **5** Late industrial / info age | Networked infantry, digital optics and comms | Precision-guided rocket and missile artillery | Gas-turbine and nuclear-powered warships | Jet fighters, guided munitions | IFVs, combined-arms mechanized units |
| **6** Speculative ceiling | AI-assisted powered infantry | Hypersonic strike systems | Autonomous naval vessels | Hypersonic drones, autonomous strike aircraft | Robot infantry, autonomous mechanized units |

The three air power entries at Tiers 0–2 form a progression rather than a coincidence: Tier 0 has aerodynamics alone, Tier 1 adds heat from direct combustion for lift with no propulsion, Tier 2 adds an engine and real steering. Each tier contributes exactly one capability over the last, consistent with how the rest of the ladder is built.

### 6.2 Cannibalized Tier 6 materiel at each tier

Tiers 0–5 only; nothing above Tier 6 cannibalizes down into it. This is not the single-unit choice from 4.4 — it is what a civilization's forces look like when cannibalized Tier 6 materiel has become a normal part of its arsenal.

**The retained-function principle:** how much of a component's original capability survives is a direct function of how much Tier 6 supporting infrastructure the receiving tier still has. At Tier 0 nothing but mass and structural strength survives — an armor plate is just armor, a rotor blade is a very good knife. By Tier 5, enough computing and power infrastructure exists natively that a cannibalized system runs in a degraded but partially functional state.

| Tier | Infantry | Indirect fire | Sea power | Air power | Mechanized infantry |
|---|---|---|---|---|---|
| **0** | Salvaged Tier 6 plate as trophy protection; edged weapons from broken composite and rotor fragments | Catapults hurling drone or missile debris as heavy shot, no explosive or guidance retained | Rafts hulled with riveted composite panels, no propulsion gained | Hang gliders framed on salvaged airframe spars, still unpowered | Raiders wearing cannibalized plating, no functional systems |
| **1** | Muskets built around scavenged Tier 6 barrels, forged stocks and locks | Cannon cast from metal reclaimed by melting Tier 6 hull alloy | Sail warships reinforced with riveted salvaged plate | Balloons with envelopes sewn from fire-resistant Tier 6 airframe fabric | Dragoons in cannibalized plating over period tack |
| **2** | Rifles rebuilt around cannibalized Tier 6 barrels and actions | Horse-drawn guns firing an actual cannibalized Tier 6 barrel | Ironclads patched with salvaged Tier 6 hull plate | Dirigibles using a salvaged Tier 6 airframe as gondola, steam-driven | Cavalry in cannibalized plate, weapons improvised from wreckage |
| **3** | Rifle infantry using non-powered scavenged Tier 6 optics | Field guns firing stripped Tier 6 munitions, unguided | Warships with a salvaged Tier 6 hull section grafted on | Biplanes on a cannibalized Tier 6 airframe with a period piston engine | Trucks welded from multiple wrecks, some carrying Tier 6 plate |
| **4** | Rifle squads in salvaged Tier 6 armor, optics present but non-functional | Self-propelled guns firing stripped Tier 6 munitions as unguided shells | Destroyers with a grafted Tier 6 hull section | Fighters on a Tier 6 airframe, AI stripped, human pilot installed | APCs on gutted Tier 6 robot-infantry chassis, crewed manually |
| **5** | Infantry in actual Tier 6 armor and optics, running degraded | Rocket artillery using an actual Tier 6 guidance system at reduced accuracy | Warships integrating an actual Tier 6 hull and systems, partially functional | Jets on a Tier 6 airframe, propulsion throttled, partial capability retained | IFVs on Tier 6 chassis running degraded, semi-autonomous software |

### 6.3 Fuel and food grades by tier

A given tech tier needs fuel of its own matching tier, not just volume of something called "fuel."

**Tech and food have different onset points.** Tier 3 is the first tier consuming fuel at all; Tier 4 is where food becomes fuel-hostage via synthetic fertilizer. That one-tier lag is deliberate: historically, mechanized farm equipment preceded synthetic fertilizer's mass adoption by a real margin.

**Grade matters independently of volume.** A node can sit on abundant crude and still be capped below Tier 6, or below Tier 4, if it lacks the refining capability for that grade. Fuel scarcity and fuel *inadequacy* are two different failure modes: a civilization can be fuel-rich and still tech- or food-insecure because what it has does not match what its equipment needs.

| Tier | Fuel grade | Consumes fuel resource | Food capability |
|---|---|---|---|
| **0** | None — muscle power | No | Foraging and subsistence gathering, no cultivated surplus |
| **1** | None — wood and coal burned directly | No | Animal-drawn subsistence farming, natural fertilizer only |
| **2** | None — steam and water power | No | Mechanically milled and processed food; no yield-boosting input |
| **3** | Crude oil, early refined product — kerosene, basic gasoline | Yes — first tier that does | Mechanized equipment and transport; yields still pre-fertilizer |
| **4** | Refined gasoline and diesel, natural gas as feedstock | Yes | Synthetic nitrogen fertilizer and mechanized harvest — food becomes fuel-hostage here |
| **5** | Aviation-grade refined fuel, enriched nuclear fuel | Yes | Precision agriculture; fuel-dependent cold-chain logistics |
| **6** | Exotic thermally-stable high-energy propellant | Yes | Highly automated closed-loop production at scale |

*Tier 6 has a real-world precedent: JP-7-type aviation fuel, developed for thermal stability at sustained Mach 3+ and used in both the SR-71 and the X-51 Waverider's scramjet.*

---

## 7. Cooperation and conquest

Cooperation and conquest are not different objectives. They are two routes to the same state: a player or bloc whose dependencies are satisfied.

Conquest is vertical integration — take the node, own the output. Cooperation is horizontal — leave it autonomous, pay for the output. Both converge on the same measure. They are freely mixable, conquer upstream and trade downstream, so there is no branch to balance and no victory condition to design around it.

**Conquered nodes can be released.** Seize during the crunch, release once stable, recover yield. In a persistent world this is close to a precondition for the map staying dynamic rather than trending toward one empire holding everything permanently.

**[PROPOSAL] The dominance problem.** As stated, conquest strictly dominates: seizing a node yields its output *and* removes a counterparty. Proposed correction: a conquered node produces less, because production has an input the local population supplies and an occupier cannot replicate. Conquest would then trade throughput for certainty, become self-limiting — a conquered empire under-produces an equivalent trade bloc — and give conquerors real reconstruction work rather than only cooperators. If adopted, release becomes the natural exit: seize for the yield during crisis, release once the penalty is no longer worth paying.

---

## 8. Player elimination

### 8.1 First version: elimination is final

A player who loses every controlled node is eliminated and exits. This is the simplest version and it ships first. Non-elimination is deliberately deferred rather than solved badly under time pressure.

### 8.2 [PROPOSAL] Tenacity at the last settlement

A culture reduced to its last settlement should be harder to eliminate than plain arithmetic predicts. Two non-equivalent routes:

**Emergent, no new rule.** Hold-versus-cannibalize already produces this at maximum stakes. Holding is a bet on surviving to see fuel restored; a player about to lose their last settlement has no such prospect, so full cannibalization is rational — converting every remaining asset into permanent, upkeep-free local firepower in one place. No new mechanic required.

**Declared, if the emergent version is insufficient.** A player already at primitive tier, or worn down by attrition rather than a single strike, has nothing left to cannibalize. This case would need a defense bonus added outright — the first mechanic in this document not derived from the core rule, worth naming honestly. If adopted, the recommended form is removal of distribution overhead rather than a flat multiplier: a settlement defending alone has no other node's upkeep or garrison split to sustain, so all local output converts to defense.

Banked reentry (4.5) partially addresses the second case, but over a much longer horizon than a single last stand.

### 8.3 [DEFERRED] Diaspora and resettlement

A fully displaced player would not exit. Their population persists without territorial control and can later reclaim a foothold in weakly controlled territory.

**The diaspora state is not a new mechanic.** A player with no controlled nodes has no trade graph connection by definition, which is already the primitive tier's condition. Removing hard elimination may only require *not deleting the player* at that state. The population becomes, structurally, an unusually large primitive-tier remnant with no address.

**Resettlement is the genuinely new piece.** It needs a rule for identifying weakly controlled territory — low garrison relative to node value, a node taken too recently to consolidate, or unclaimed territory — plus a settlement action available to landless players, since a just-eliminated population cannot out-fight an established holder.

**[OPEN]** Whether resettlement happens unilaterally or requires a patron. A diaspora population has no military weight of its own; this kind of return has historically often depended on external protection or negotiated arrangement rather than independent force. If a patron is required, that is the alliance-as-subgraph rule extended to a client relationship rather than new tooling.

*Design note: this mechanic was developed with reference to a specific modern historical case. Displacement followed by resettlement in weakly held territory is a recurring structural pattern rather than unique to any one instance, and shipped documentation should describe the general pattern rather than naming a contested case.*

---

## 9. World and session structure

**Persistent world, no round boundary.** Sandbox in character, with no formal end state to design toward. No victory is declared and no wipe occurs.

**No winning.** The point of play is not to win. Recovery can be individual, collective, or partial and overlapping without resolving into a declared winner. Each player or bloc chooses independently in Act 4: rejoin and regain throughput at the cost of vulnerability, or stay sovereign, poor, and unstarvable. Different players can rationally land on different answers, and the world can hold several valid outcomes side by side.

**Static map.** A fixed set of nodes that does not regenerate or reshape.

**Asynchronous action, not turns.** Players act whenever they choose, gated by a rate limit or resource cost rather than a shared turn order. This is close to required by the persistent-world decision rather than a preference: synchronized turns need a fixed, known player set resolving at a shared moment, which a persistent world with an open player set does not have. "Turn" is the wrong term for this model; "action" is more accurate.

**Offline defense will exist.** Asynchronous action means attacks land while defenders are absent, so resolution cannot depend on both parties being present. **[OPEN]** The mechanism. One candidate is standing doctrine — a defender pre-commits a defense posture applied automatically when attacked offline.

**[OPEN] Long-run world state.** Fuel depletion is permanent and the cannibalization capability floor is permanent. In an endless world, both point toward eventually reaching a fixed, fully-scavenged, fuel-exhausted state that simply holds. Whether that is acceptable long-run character or needs a countervailing renewal mechanic — new deposits, slow regeneration, new civilizations spawning in — is unresolved.

**[OPEN] Remaining structural questions.** Player count. Node adjacency structure and whether adjacency constrains the trade graph. Whether nodes are players or territory. Combat resolution. Server model and whether new players can join an aged world.

---

## 10. What is novel

Assessed against the lineage this design draws from — Veydrift, OGame, Planetarion, Barren Realms Elite, Earth 2025, Utopia, TradeWars 2002 — and against general genre knowledge. "Novel" here means *no precedent known to this document*, which is weaker than *no precedent exists*.

1. **Fog of war as emergent loss rather than purchased gain.** Every game in this lineage treats information as something you spend to acquire. Here it is a capability you begin with and lose structurally. This claim rests on recollection rather than a completed survey and is the one most worth verifying before building around it.

2. **Tech degradation as a network readout.** Tech loss elsewhere appears as damage, decay, or scripted event. Deriving it entirely from unmet supply dependencies — nothing removed by rule, only starved — makes collapse legible and reversible rather than punitive.

3. **A primitive tier defined by payable upkeep, with a cannibalized upper tier.** The low end is fallback technology whose running costs the collapsed economy can meet. The high end is not independently invented but built from wreckage — a tank's gun on a horse team rather than a hand-cast cannon. Collapse does not equalize players onto a common baseline; prior strength persists as scavenged capability.

4. **Self-reinforcing collapse via fuel.** Fuel powers the network that produces fuel technology, so collapse depth is player-determined and can bottom out at a genuinely pre-industrial floor.

5. **Full mutual dependency at t=0.** Standard 4X opens with players isolated and offers trade as an option. Opening with a saturated dependency graph inverts the pressure: entanglement is the default and isolation is the achievement.

6. **Alliance as an observed graph property.** Blocs are not declared; whoever remains connected is an alliance whether they intended it or not. Sidesteps conventional diplomacy UI.

7. **Parsimony.** Fog, degradation, alliance formation, and recovery are consequences of a single dependency-satisfaction rule rather than four subsystems.

---

## 11. Status

The world's shape, arc, and philosophy are settled. There is no remaining critical conceptual gap.

What is open is mechanical, and falls into three groups:

**Blocks combat design.** The offline defense mechanism (9). Combat resolution itself.

**Numeric tuning, conceptually settled.** Climate change's rate of increase on food's fuel cost. Banking threshold and rate for reentry. Cannibalized-unit win and rout odds. Army size-to-capability relationship.

**Structural, decidable independently.** Player count, node identity, map adjacency, server model. Whether below-the-fuel-line collapse (4.6) is adopted. Whether the conquered-node yield penalty (7) is adopted. Whether revolution is a gradient and whether food falls on a cliff or a slope (3.7) — these two should be decided together.
