---
name: Weaver of Life - Ignacia
faction: Transcendence
class: Mage   # the "MAGE" label was partly covered by popups in every screenshot; confirm
role: Multi-hit damage / stacking burst (based on skill text)
patch: in-game skill text, captured 2026-11-24
last_updated: 2026-11-24
sources: in-game screenshots (personal)
---

# Weaver of Life - Ignacia

## Summary
A Transcendence Mage who builds up **Seed of Life** stacks. Her basic attack applies **Constraint** to enemies. Each time an ally attacks, she makes a follow-up attack that can apply **Shaping**. With 4 or more Seeds, her active skill detonates both effects for damage based on the target's Max HP and lost HP. It also gives her 50 Energy and +50% damage at the end of the round.

> Game rule: you can't put more than one Transcendence hero with the same name in a lineup.

## Skills
Skill text copied from the game. The tier at which each skill unlocks is in brackets.

### Active: Enlightenment · Life Weaving
Attacks 4 random enemies 4 times, each of which deals (300% of Attack) damage. If self has 4 layers of **Seed of Life** when releasing the active skill, additionally attacks targets with **Constraint**, dealing damage equal to 10% of their Max. HP (caps at 2000% of self Attack), and then removes **Constraint** owned by the targets; besides, attacks targets with **Shaping**, dealing damage equal to 10% of their lost HP (caps at 2000% of self Attack), and then removes **Shaping** owned by the targets; afterward, removes all layers of **Seed of Life** owned by self. If self is under the **Life-shaping State** status after releasing the active skill, exits the **Life-shaping State** status; if not, enters the **Life-shaping State** status. During **Life-shaping State**, there is a 50% chance to gain 1 more layer when self gains **Seed of Life**.

### Passive: Imperishable Vein (Tier 2 unlock)
Changes the basic attack to: Deals (600% of Attack) damage to 4 random enemies and inflicts **Constraint** on them, then grants self a **Shield** equal to 400% of Attack. If an attacked enemy has **Shaping**, grants self 1 layer of **Seed of Life**, up to 8 layers can be owned. If self has 4 or more layers of **Seed of Life** when gaining **Seed of Life**, additionally increases self Damage Reduction by 6% for 2 rounds.

- **Constraint:** Skill effect. Not stackable. Reduces the owner's Attack by 6%.
- **Shield:** Skill effect. Offsets the Direct Damage and Damage Over Time received. It will disappear when the strength of the shield is 0. The shield strength caps at 100% of self HP.

### Passive: Red Vine Connection (Tier 4 unlock)
When an ally releases basic attacks or active skills, self chases and attacks 2 random enemies, dealing (300% of Attack) damage, with a 45% chance to inflict **Shaping** on the targets. If a target has **Constraint** when being inflicted with **Shaping**, self gains 1 layer of **Seed of Life** (up to 8 layers can be owned) and increases self Crit Damage by 4% for 2 rounds. If self has 4 or more layers of **Seed of Life** when gaining **Seed of Life**, additionally increases self Attack by 6% for 2 rounds.

- **Shaping:** Skill effect. Not stackable. The owner takes damage equal to 6% of self Max. HP at the end of each round (caps at 2000% of the inflictor's Attack).

### Passive: Vortex of Vitality (Tier 6 unlock)
At the end of each round, if self has 4 or more layers of **Seed of Life**, grants self 50 Energy and increases self All Damage Dealt by 50%. This effect is not stackable and will be ineffective after releasing the active skill next time. If self has less than 4 layers of **Seed of Life**, each layer of **Seed of Life** grants self a **Shield** equal to 200% of Attack.

## How she works (analysis, unverified in play)
- **How she gains Seeds:** her basic attack applies Constraint to 4 enemies. Her follow-up attacks (one each time an ally attacks) have a 45% chance to apply Shaping. When Shaping lands on an enemy with Constraint, or her basic attack hits an enemy with Shaping, she gains a Seed of Life.
- **She wants allies who act often.** Red Vine Connection triggers on every ally basic attack or active skill, so a fast team that attacks a lot gives her more follow-ups and more Seeds.
- **Her payoff at 4+ Seeds:** at the end of the round she gains 50 Energy and +50% All Damage Dealt (Tier 6). Then her active skill deals extra damage based on Max HP and lost HP to every enemy with Constraint or Shaping. That damage is capped at 2000% of her Attack per hit.
- **She toggles Life-shaping State** each time she casts her active skill. While she's in it, every Seed she gains has a 50% chance to give an extra one, so every other cast should come back faster.
- **She's safer before her stacks are ready.** With fewer than 4 Seeds, she gets a 200%-Attack shield per Seed each round, on top of a 400%-Attack shield from every basic attack.
- **Shaping also does damage on its own:** 6% of the target's Max HP every round, which is damage over time. That could also set off Lethia's Wailing Soul Mark procs (60% chance each time a marked enemy takes damage over time).

## Best game modes
| Mode | Rating | Notes |
|---|---|---|
| PvP | TODO | |
| Boss fights | TODO | Damage based on Max HP and lost HP is capped at 2000% of her Attack |
| PvE waves | TODO | |

## Build
- **Artifact:** TODO
- **Gear / stones:** TODO
- **Your copy's level, tier and stats:** see the [roster](../../account/roster.md)

## Synergies & counters
- **Pairs well with:** TODO, likely fast heroes who attack often, and Lethia (Shaping is damage over time)
- **Countered by:** TODO, possibly debuff cleansing (removes Constraint and Shaping)
- **Counters:** TODO

## Investment priority
TODO
