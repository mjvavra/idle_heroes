---
name: Priestess of the Beyond - Lethia
faction: Transcendence
class: Priest
role: Debuffer / poison DoT damage / ally buffer (based on skill text)
patch: in-game skill text, captured 2026-11-24
last_updated: 2026-11-24
sources: in-game screenshots (personal)
---

# Priestess of the Beyond - Lethia

## Summary
A Transcendence Priest who marks key enemies with **Wailing Soul Mark**: they take more damage, receive less healing, and set off extra damage whenever they take damage over time. She also gives allies **Crimson Soul Pact**, which raises their Attack and hits all marked enemies whenever that ally takes damage. Most of her damage is poison and procs that bounce between marked enemies.

> Game rule: you can't put more than one Transcendence hero with the same name in a lineup.

## Skills
Skill text copied from the game. The tier at which each skill unlocks is in brackets.

### Active: Dream's End · Soul Requiem
Deals (2000% of Attack) damage to back-line enemies. If the target has **Wailing Soul Mark**, it also **Poisons** them, dealing damage equal to 15% of their Max HP (capped at 1500% of her own Attack) for 2 rounds. Then it has a 50% chance to inflict **Soul Bewitchment** on them for 2 rounds.

- **Soul Bewitchment:** Skill effect, not stackable. Changes the owner's Active Skill to: deals (2000% of the owner's Attack) damage to the owner's ally with the lowest HP. Doesn't work on Bosses.
- **Poison:** DoT. Deals damage once when inflicted, then again at the end of each round while it lasts.

### Passive: Spirit Butterfly's Bloom (Tier 2 unlock)
Changes her basic attack to: deals (600% of Attack) damage to 1 random enemy, plus (1500% of Attack) damage to targets with **Wailing Soul Mark**. Then she restores HP equal to 20% of her lost HP.

### Passive: Lament of the Sunken Abyss (Tier 4 unlock)
At the start of each round, inflicts **Wailing Soul Mark** for 2 rounds on the enemy with the highest Attack, the enemy with the highest Speed, and the enemy with the lowest HP. When an ally with **Crimson Soul Pact** takes damage, deals damage equal to 65% of the damage taken to all enemies with **Wailing Soul Mark**, then **Poisons** them, dealing (600% of the target's Attack) damage for 2 rounds.

- **Wailing Soul Mark:** Skill effect, not stackable. Reduces the target's Damage Reduction by 20% and the effect of healing they receive by 30%. Whenever the owner takes DoT, there's a 60% chance to deal (1200% of the owner's Attack) damage to 2 random enemies with Wailing Soul Mark. When a marked target dies, inflicts Wailing Soul Mark on 2 random unmarked enemies for 2 rounds.

### Passive: Embrace of the Beyond (Tier 6 unlock)
At the start of each battle, she gains **Crimson Soul Pact** until the battle ends. At the start of each round, she picks 1 random ally without Crimson Soul Pact:
- If that ally's HP is at least 70%: takes 10% of their Max HP, gives them a **Shield** equal to 10% of their Max HP, and gives them Crimson Soul Pact for 2 rounds.
- If that ally's HP is below 70% and her own HP is at least 50%: takes 10% of her own Max HP to give the ally Crimson Soul Pact for 2 rounds.

- **Crimson Soul Pact:** Skill effect. Raises the target's Attack by 20% and the effect of healing they receive by 30%. When a target with Crimson Soul Pact dies, gives Crimson Soul Pact to 1 random ally without it for 2 rounds.
- **Shield:** Skill effect. Absorbs direct damage and damage over time, and disappears when it reaches 0. Shield strength is capped at 100% of the owner's HP.

## How she works (analysis, unverified in play)
- **Marks drive everything.** Her basic attack, her active skill's poison, and the Pact reflection all target marked enemies. The marks go on the enemy with the highest Attack, the highest Speed and the lowest HP, which usually means their main damage dealer, their fastest hero and a near-dead target.
- **Wailing Soul Mark** cuts the target's Damage Reduction by 20% and their healing received by 30%, so it helps your whole team and works against healing-heavy teams.
- **She sets off her own procs.** Her poisons are DoT, so marked enemies she poisons have a 60% chance to set off the 1200%-Attack bounce. Other DoT heroes (poison, bleed, burn) should set off even more.
- **Crimson Soul Pact rewards taking hits.** Allies with the Pact hit back at marked enemies whenever they're damaged, so durable front-liners with the Pact turn incoming damage into damage on the enemy.
- **Risks:** Embrace of the Beyond costs HP (10% of an ally's, or of hers). Soul Bewitchment (50% chance) only affects enemies, so it can make an enemy's active skill hit their own lowest-HP ally. It does nothing against bosses.

## Best game modes
| Mode | Rating | Notes |
|---|---|---|
| PvP (Arena etc.) | TODO | Anti-heal and Soul Bewitchment look strong here |
| Guild Boss / boss fights | TODO | Soul Bewitchment doesn't work on bosses, and the poison is capped at 1500% of her Attack |
| PvE waves | TODO | |

## Build
- **Artifact:** TODO
- **Gear / stones:** TODO
- **Your copy's level, tier and stats:** see the [roster](../../account/roster.md)

## Synergies & counters
- **Pairs well with:** heroes that apply DoT (to set off Wailing Soul Mark procs) and durable front-liners (to make the most of Crimson Soul Pact). TODO: name specific heroes once the roster is filled in.
- **Countered by:** TODO, possibly cleanse/dispel or very fast burst damage
- **Counters:** heal-reliant teams (the mark cuts healing received by 30%)

## Investment priority
TODO
