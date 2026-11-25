---
name: Cosmic Speedster - Sylvie
faction: Transcendence
class: Warrior
role: Shield tank / taunt / team shields (based on skill text)
patch: in-game skill text, captured 2026-11-24
last_updated: 2026-11-24
sources: in-game screenshots (personal)
---

# Cosmic Speedster - Sylvie

## Summary
A Transcendence Warrior tank built around **Shields** and **Taunt - Confrontation**. Her active skill shields the whole team 5 times and can taunt the enemy back line. Each time she gains a shield she stacks **Assault Impetus**. When her shield breaks, she spends those stacks on damage to all enemies based on their Max HP. **Protector's Oath** lets her counterattack whenever a protected ally is hit.

> Game rule: you can't put more than one Transcendence hero with the same name in a lineup.

## Reference stats (Hero Document)
Stats shown in the in-game Hero Document at max level and tier, captured 2026-11-24. Compare against your own copy in the [roster](../../account/roster.md).

| Level | Tier | Power | HP | Attack | Armor | Speed |
|---|---|---|---|---|---|---|
| 250/250 | 6 | 205K | 911,680 | 52,136 | 1,554 | 1,284 |

## Skills
Skill text copied from the game. The tier at which each skill unlocks is in brackets.

### Active: Swift Fury Onslaught
Deals (100% of Attack) damage to back-line enemies 5 times. Each attack grants all allies a **Shield** equal to 200% of Attack. Afterward, there is a 40% chance to inflict **Taunt - Confrontation** on back-line enemies for 3 rounds. Each time **Taunt - Confrontation** is successfully inflicted on 1 enemy, additionally increases self All-damage Reduction by 4% and Holy Damage by 4% for 3 rounds.

- **Taunt - Confrontation:** Control effect. Active skills and basic attacks of heroes inflicted with Taunt - Confrontation will compulsively target the Taunt caster and this control effect also reduces affected heroes' All Damage Dealt by 33%.
- **Shield:** Skill effect. Offsets the Direct Damage and Damage Over Time received. It will disappear when the strength of the shield is 0. The shield strength caps at 100% of self HP.

### Passive: Radiant Light Piercing (Tier 2 unlock)
Changes the basic attack to: Deals (400% of Attack) damage to front-line enemies and inflicts extra damage equal to 8% of self Shield value (caps at 1500% of self Attack), with a 50% chance to inflict **Taunt - Confrontation** on the targets respectively for 2 rounds. Afterward, self gains a **Shield** equal to 200% of Attack.

### Passive: Potent Drive (Tier 4 unlock)
Each time self gains a **Shield** (only 1 Shield is counted if multiple Shields are gained from the same skill), grants self 2 layers of **Assault Impetus**. When the **Shield** on self is ineffective, for every 1 layer of **Assault Impetus** owned by self, deals damage to all enemies by 2% of their Max. HP (caps at 1500% of self Attack) and additionally inflicts (100% of Attack) **Divine Retribution** on them. Afterward, removes all **Assault Impetus** from self.

- **Assault Impetus:** Skill effect. Each layer of Assault Impetus increases self Attack by 3% and Damage Reduction by 3%, stackable up to 6 layers.
- **Divine Retribution:** Skill effect. This effect does not land a Crit, and its damage is fixed which cannot be reduced or increased by attributes or skill effects. *(Not defined in Sylvie's popup. Copied from [Sun Wukong's](sun-wukong.md) skill text.)*

### Passive: Starlight Support (Tier 6 unlock)
At the end of each round, if self has no **Shield**, increases self Damage Reduction by 10% and Control Immunity by 10% for 1 round. Afterward, self gains a **Shield** equal to 400% of Attack; if self has **Shield**, increases self Attack by 10% for 1 round and grants a **Shield** equal to 400% of Attack and **Protector's Oath** on 1 random ally without **Protector's Oath**. When the **Shield** on the ally is ineffective, **Protector's Oath** becomes ineffective as well.

- **Protector's Oath:** Skill effect. Not stackable. When the target is under a basic attack or takes damage from an active skill, Cosmic Speedster - Sylvie has a 100% chance to deal (300% of Attack) damage to back-line enemies and increase Damage Reduction by 6% for all the targets with **Protector's Oath**, caps at 18%; the effect will end as **Protector's Oath** becomes ineffective.

## How she works (analysis, unverified in play)
- **She tanks by taunting.** Her active skill (40% chance, back line) and basic attack (50% chance, front line) both apply Taunt - Confrontation, which forces enemies to target her and cuts their damage dealt by 33%.
- **She cycles shields.** She gains shields from her basic attack, her active skill, and her Tier 6 skill every round. Each new shield gives 2 Assault Impetus stacks (max 6, up to +18% Attack and Damage Reduction). When a shield breaks, she deals damage to all enemies based on their Max HP: up to 12% per enemy at 6 stacks, capped at 1500% of her Attack.
- **She shields the whole team.** Her active skill gives all allies five 200%-Attack shields, capped at 100% of each ally's HP. That stacks well with Madeleine, whose Frantic Gluttony needs allies' shields to reach 30/40/50% of Max HP.
- **Protector's Oath** lets her hit the enemy back line every time a protected ally is attacked, and it stacks Damage Reduction on protected allies up to 18%.

## Best game modes
| Mode | Rating | Notes |
|---|---|---|
| PvP | TODO | |
| Boss fights | TODO | Taunt may not work on bosses |
| PvE waves | TODO | |

## Build
- **Artifact:** TODO
- **Gear / stones:** TODO
- **Your copy's level, tier and stats:** see the [roster](../../account/roster.md) (compare with the reference stats above)

## Synergies & counters
- **Pairs well with:** TODO, likely Madeleine (her shield thresholds) and other shield-givers, which feed Potent Drive
- **Countered by:** TODO, possibly shield-breaking or control-immune heroes
- **Counters:** TODO

## Investment priority
TODO
