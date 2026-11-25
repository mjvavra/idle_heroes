---
name: Great Sage - Sun Wukong
faction: Transcendence
class: Warrior
role: Two-mode fighter: team shields (Immortal Soul) or fixed damage (Universe Imitation) (based on skill text)
patch: in-game skill text, captured 2026-11-24
last_updated: 2026-11-24
sources: in-game screenshots (personal)
---

# Great Sage - Sun Wukong

## Summary
A Transcendence Warrior who switches between two modes depending on his HP. In **Immortal Soul** (above 50% HP after being healed), he shields and protects the team and counterattacks. In **Universe Imitation** (at or below 50% HP after taking damage), he buffs Holy Damage and deals **Divine Retribution**, which is fixed damage that can't be reduced. He applies **Fragile**, which adds damage equal to 10% of the target's Max HP and gives him Energy.

> Game rule: you can't put more than one Transcendence hero with the same name in a lineup.

## Skills
Skill text copied from the game. The tier at which each skill unlocks is in brackets.

### Active: Havoc in Lingxiao Palace
Deals (600% of Attack) damage to all enemies, reducing back-line enemies' Armor by 10% and Damage Reduction by 10% for 2 rounds. Afterward, deals (1000% of Attack) damage (Crit is guaranteed) to back-line enemies, this damage cannot be dodged or blocked; then deals (1000% of Attack) Armor-ignoring damage to the enemy with the highest Attack. If self has more than 70% HP when releasing the active skill, deducts HP by 50% of current HP from self and generates a **Shield** equal to 70% of the lost HP. When self is under **Immortal Soul** status, additionally grants all allies a **Shield** equal to 1200% of Attack and increases their Damage Reduction by 10% for 3 rounds. When self is under **Universe Imitation** status, additionally inflicts (800% of Attack) **Divine Retribution** to the enemy with the highest Attack and restores 20% of self lost HP.

- **Shield:** Skill effect. Offsets the Direct Damage and Damage Over Time received. It will disappear when the strength of the shield is 0. The shield strength caps at 100% of self HP.
- **Divine Retribution:** Skill effect. This effect does not land a Crit, and its damage is fixed which cannot be reduced or increased by attributes or skill effects.

### Passive: Great Sage's Rage (Tier 2 unlock)
Changes the basic attack to: Deals (400% of Attack) damage to 3 random enemies, with a 60% chance to inflict **Fragile** on them. When self is under **Immortal Soul** status, additionally grants self a **Shield** equal to 800% of Attack and increases all allies' Damage Reduction by 6% for 2 rounds. When self is under **Universe Imitation** status, deals extra (400% of Attack) damage to back-line enemies, inflicts (250% of Attack) **Divine Retribution** on them, and reduces the targets' Damage Reduction by 6% for 2 rounds.

### Passive: Invulnerable Body (Tier 4 unlock)
If self has more than 50% HP after being Healed, enters **Immortal Soul** status for 5 rounds. If self has 50% or less HP after taking damage, enters **Universe Imitation** status for 5 rounds. Allies and enemies will be affected by different effects according to the status Great Sage - Sun Wukong enters.

**Immortal Soul:**
Increases self Damage Reduction by 6% and Control Immunity by 6%, up to 3 layers can be stacked.
-To All Allies: Increases Damage Reduction by 10% for 2 rounds. Grants a **Shield** equal to 800% of Attack and additionally increases Damage Reduction by 6% for 2 rounds, can be triggered up to 1 time each round.

**Universe Imitation:**
Increases self Attack by 10% and Holy Damage by 10%, up to 3 layers can be stacked.
-To All Allies: Increases Holy Damage by 10% for 2 rounds.
-To All Enemies: Inflicts (300% of Attack) **Divine Retribution**, with a 60% chance to inflict **Fragile**, and a 60% chance to inflict **Stun** for 1 round; can be triggered up to 1 time each round.

When a battle starts or when self is in the battle as a substitute, if self has 100 or more Energy, deducts 50% of the current HP to gain a **Shield** equal to 70% of the lost HP; if self has less than 100 Energy, enters **Immortal Soul** status for 5 rounds.

- **Stun:** Control effect. Stunned heroes are unable to release their active skills, basic attacks, extra attacks, or counterattacks.

### Passive: Immortal Spell of Universe (Tier 6 unlock)
When self is under **Immortal Soul** status:
Immune to Petrify. Counterattacks when taking basic attack damage or active skill damage, dealing (800% of Attack) Armor-ignoring damage to 3 random enemies (prioritizes enemies with **Fragile**). When enemies' **Fragile** is triggered, grants all allies a **Shield** equal to 600% of Attack.
When self is under **Universe Imitation** status:
Immune to Shapeshifting. Chases and attacks 2 random enemies when allies release basic attacks or active skills, inflicting (400% of Attack) **Divine Retribution** to them (prioritizes enemies with **Fragile**). When enemies' **Fragile** is triggered, increases all allies' Holy Damage by 6% for 2 rounds.

- **Fragile:** Skill effect. Not stackable. When the target with **Fragile** takes basic attack damage or active skill damage, they will take extra damage equal to 10% of their Max. HP, with an 60% chance to restore 10 Energy for Great Sage - Sun Wukong. Will be removed after triggering **Fragile**. (Caps at 3000% of Great Sage - Sun Wukong's Attack)

## How he works (analysis, unverified in play)
- **His mode depends on HP.** He enters Immortal Soul when he's above 50% HP after a heal, and Universe Imitation when he's at or below 50% after taking damage. If he starts a battle with under 100 Energy, he begins in Immortal Soul.
- **He can push himself into Universe Imitation.** His active skill costs 50% of his current HP if he's above 70%. That can drop him to 50% or below and switch him to his damage mode, while giving him a shield worth 70% of the HP he lost.
- **Immortal Soul is a support mode:** team shields (1200% Attack from his active skill, 800% from Invulnerable Body, 600% whenever an enemy's Fragile triggers), stacking Damage Reduction, and 800%-Attack counterattacks that ignore Armor.
- **Universe Imitation is a damage mode:** a lot of Divine Retribution, which is fixed damage that ignores the target's damage reduction. That includes follow-up attacks every time an ally acts (like Ignacia's Red Vine Connection), plus Holy Damage buffs for the whole team.
- **Fragile works in both modes.** It adds damage equal to 10% of the target's Max HP (capped at 3000% of his Attack) and has a 60% chance to give him 10 Energy.
- **He shares Divine Retribution with Sylvie.** Sylvie's Potent Drive also applies it, and both raise Holy Damage.

## Best game modes
| Mode | Rating | Notes |
|---|---|---|
| PvP | TODO | |
| Boss fights | TODO | Divine Retribution ignores damage reduction |
| PvE waves | TODO | |

## Build
- **Artifact:** TODO
- **Gear / stones:** TODO
- **Your copy's level, tier and stats:** see the [roster](../../account/roster.md)

## Synergies & counters
- **Pairs well with:** TODO, likely healers (to trigger Immortal Soul), heroes who act often (for Universe Imitation follow-ups), and Sylvie (Holy Damage and Divine Retribution)
- **Countered by:** TODO
- **Counters:** TODO, likely tanky teams that rely on damage reduction (Divine Retribution damage is fixed)

## Investment priority
TODO
