# As Instructed
**Prototype Game Design Document**

Platform: Web · Status: Prototype feeding into a larger game · Version 0.1

---

## Logline

You run an evil lair by giving your henchmen plain English orders, and they follow them exactly, forever. That's the joke and the whole game.

## Core Fantasy

You're second-in-command at a cartoonishly evil lair. Your only tool is language. You never move a henchman directly, you tell them what to do once, and that becomes their standing order, not a suggestion, a fixed behavior they'll carry out with total mechanical honesty until you countermand it. The fun isn't commanding well. It's discovering, live, exactly how far "watch the door" was from what you actually meant.

## Core Loop

1. Player is shown the lair and a short scenario (a heist, a raid, a hero incoming)
2. Player types instructions to one or more henchmen, in plain English
3. Each instruction is compiled once into a fixed behavior and starts running immediately
4. The scenario plays out in real time or short ticks, henchmen executing their standing instructions with no further input
5. Player watches the gap between instruction and intention cause a small, specific, legible disaster
6. Player can issue new instructions at any time to patch the situation, which themselves get taken exactly as literally
7. Scenario ends in a short, contained failure or success, either way, funny

## The Mechanic

### Standing instructions, not commands

This is the one rule the whole game hangs on: an instruction is not a one-time action, it's a persistent behavior. "Guard the door" doesn't mean walk to the door once, it means become a thing that guards the door, indefinitely, under every future circumstance, including ones the player didn't anticipate when they said it.

### The compile step

When the player submits an instruction, one AI call translates it into a small, fixed grammar the game engine actually runs; something like:

```
WATCH(target: Door)
ON_APPROACH(actor):
  IF actor != Player THEN BLOCK(actor)
  ELSE ALLOW(actor)
```

That's it for the AI's involvement. Once compiled, the behavior runs as ordinary deterministic game logic, no further model calls, no re-reading of text, no judgment calls during play.

### Why compile-once, not live

Two failure modes this deliberately avoids, both surfaced hard in earlier prototyping:

- **Latency.** Calling a model on every tick during a live scenario would make the game feel laggy exactly when it needs to feel snappy. Compiling once means the AI's cost is paid at instruction time, not during play.
- **Manipulation.** A henchman that kept reading text during execution could in principle be talked out of its orders by anything in the world, an NPC, a note, another player. Compiling once removes that surface entirely: there's nothing left for anything to persuade, because nothing is reading language anymore once the behavior is running.

The tradeoff, made deliberately: henchmen can't be talked out of a standing order mid-scenario, only replaced by a new instruction from the player. That's a feature here, not a limitation, it's what keeps the failures the player's own fault, not something sprung on them.

## World Model

Objects in the lair are entities with properties, not special cases. A door is `Guardable`. A cauldron is `Fillable` and `Overflowable`. A hero is `Detectable` and `Capturable`. Compiled henchman behaviors act on whatever properties are actually present, the same way fire spreading to anything flammable doesn't need to know what kind of object it's burning.

This is what makes the comedy systemic instead of scripted: nobody hand-authors "what happens if you tell a henchman to fill the cauldron and never tell them to stop." It falls out of `Fillable` interacting with `Overflowable` interacting with whatever's standing nearby when it overflows.

## Prototype Scope

**In scope:**
- One lair, three to five rooms
- Three to four henchman archetypes
- A small object property set: guardable, fillable, flammable, breakable, detectable
- Two or three short scenarios, each finishable in a few minutes
- Single player, no persistence between sessions

**Explicitly out of scope for this prototype:**
- Any world state that continues running when the player isn't there
- Multiple players, or henchmen belonging to more than one lair
- Live re-prompting of a henchman's behavior mid-scenario based on things it senses in the world (this is the adversarial, "trick the other player's minion" version discussed as a future direction, and it directly reopens the manipulation risk the compile-once model exists to avoid)
- Any scoring, difficulty curve, or progression system

## Tone

Failure is the content, not a punishment for failure. When an instruction goes wrong, it should read as a specific, traceable, slightly delightful consequence of exactly what was typed, never as an arbitrary or unfair result. The player should always be able to look at the outcome and immediately see their own sentence in it.

## Technical Architecture

- **Target:** browser, single page, no install
- **World simulation:** Entity-Component-System. Given the prototype's small entity counts, an ergonomics-first library (Miniplex or Koota) over a raw-performance one (bitECS), the scale here never needs typed-array-level throughput
- **The one AI call:** instruction text in, small fixed-grammar behavior out, called once per player instruction, never during simulation ticks
- **State:** in-memory only for this prototype, nothing persisted server-side

## What This Prototype Needs to Prove

- Does the compile step reliably turn a vague English sentence into a sensible bounded behavior, without the player needing to think like a programmer to get something reasonable
- Does an underspecified instruction actually produce a legible, funny failure, rather than a confusing or arbitrary one
- Does watching a compiled behavior run feel like enough agency, given the player never directly controls anything after the instruction is given

## Open Questions for the Larger Game

- Persistence: should a lair's state survive between sessions, and what does that cost
- Multiplayer: the adversarial version, where another player's henchman can encounter and react to text left in the world, deliberately deferred here
- How many properties and behaviors before the compile step starts producing inconsistent results, this prototype is the way to find that ceiling
