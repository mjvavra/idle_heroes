---
name: process-screenshots
description: Process Idle Heroes screenshots in screenshots/inbox/ into the knowledge base. Reads every image, writes skill text to hero pages and account data to the roster and profile, archives the images, and publishes the wiki. Use when the user says "process my screenshots", "check the inbox", or adds screenshots of heroes, skills or account screens.
---

# Process screenshots

Turn screenshots in `screenshots/inbox/` into knowledge-base pages, then archive the images and publish the wiki.

## Steps

1. **Load the inbox.** List `screenshots/inbox/` (ignore `.gitkeep`) and read **every** image. If it's empty, say so and stop.
2. **Sort and group the images.** First decide where each screenshot comes from. If you can't tell, ask.
   - **Hero Document (in-game encyclopedia):** shows game reference data, i.e. skill text plus stats at max level and tier. This goes on **hero pages only**, never in the roster.
   - **The player's own hero list / hero screens:** shows *their* copy's level, tier, stats and gear. This goes in the **roster** (step 5).
   - **Other account screens** (profile, inventory, progress): go to step 5.

   Group screenshots by hero, using the title at the top left (e.g. "Priestess of the Beyond - Lethia"). Usually there's one screenshot per skill popup, plus the info page.
3. **Write or update each hero page** at `heroes/<faction>/<hero-name>.md`, following the [hero page rules](#hero-page-rules). If the page exists, merge new information into it. Never drop text that's already there unless a screenshot shows it changed (and if it did, say so).
4. **Update the hero index** in `heroes/README.md` (one row per hero, sorted by name).
5. **Update account files** following the [account data rules](#account-data-rules).
6. **Archive the images:** move them to `screenshots/archive/YYYY-MM-DD/` (today's date). Screenshots are git-ignored and never pushed.
7. **Check the build:** run `python scripts/assemble_docs.py` then `mkdocs build --strict` (set `NO_MKDOCS_2_WARNING=1`). If MkDocs isn't installed, create a venv in the scratchpad and `pip install -r requirements-site.txt`. Fix any warnings.
8. **Commit and push to `main`.** The user has approved this for screenshot processing. Pushing publishes the public wiki, so first check that nothing private is in the changes (see the [privacy rules](#privacy-rules)).
9. **Report back:**
   - which heroes or pages you added or updated;
   - anything unreadable, cut off or ambiguous, listed rather than guessed;
   - which screenshots would fill the gaps.

## Hero page rules

- Start from `heroes/_TEMPLATE.md`. File name: hero's short name, lowercase and hyphenated (e.g. `lethia.md`). Folder: faction in lowercase (`shadow`, `fortress`, `abyss`, `forest`, `dark`, `light`, `transcendence`).
- Use the hero's full in-game title as the page name and the `name` field.
- **Hero pages hold game information only:** faction, class, skills, mechanics and the Hero Document's **reference stats** (level, tier, power, HP, Attack, Armor, Speed) in the "Reference stats (Hero Document)" table. The player's own copy goes in `account/roster.md`.
- **Copy skill text word for word.** Fix only obvious line-break or OCR spacing problems (e.g. "Poisonsthem" → "Poisons them"). Bold the keyword effects (the orange text in the game).
- For each skill, record:
  - its type (Active / Passive);
  - the skill name;
  - its unlock requirement (e.g. "Tier 2 unlock", shown in red at the bottom of the popup);
  - each effect definition listed under it (e.g. **Poison:**, **Shield:**).
- If the same effect definition (e.g. Poison) appears under several skills, write it out once under the first skill that uses it.
- Put analysis in a separate section titled "How they work (analysis, unverified in play)". Never mix it into the copied skill text.
- Never make up numbers. Use `TODO` for anything the screenshots don't show.
- Set `patch: in-game skill text, captured YYYY-MM-DD`, `sources: in-game screenshots (personal)` and `last_updated`.

## Account data rules

- **Roster** (`account/roster.md`): only from the player's own hero screens, **never from the Hero Document**. One row per hero, linking to the hero page. Record level, tier or stars, power, HP, Attack, Armor, Speed and gear when they're visible. Note the date.
- **Gaps vs. reference:** after updating the roster, compare each hero with the reference stats on their hero page. Note the gap in the roster's "Gaps vs. reference" section, e.g. "Tier 4/6: Tier 6 skill locked; power 150K vs 220K". Mention the biggest gaps in the report.
- **Profile** (`account/profile.md`): resources shown in the top bar (gold, etc.) with "(as of YYYY-MM-DD)". Update `last_updated`.
- Only record values you can actually read. If a popup covers part of the page (e.g. the tier bar), mark it `TODO` and mention it in the report.

## Privacy rules

The wiki is public. Never write player names, player IDs, guild member names, chat text, or server-identifying details into any published file. Leave them out even if they appear in a screenshot.

## Learned rules

Add a dated bullet here whenever the user corrects how screenshots are handled, or a new kind of screenshot or edge case comes up. Then follow it from then on.

- 2026-11-24: Skill popups often cover the hero's tier bar and stats panel. Read the stats from whichever screenshot shows them unobstructed, and ask for a popup-free info-page screenshot if none does.
- 2026-11-24: Transcendence heroes show the note "You cannot assign multiple Transcendence heroes with the same name in one lineup." Record it once on the hero page as a game rule.
- 2026-11-24: The green resource shown next to gold on the hero screen is probably spirit (unverified). Label it that way until it's confirmed.
- 2026-11-24: Long skill popups can run past the bottom of the screen (e.g. Madeleine's "Time to Feast!" stops mid-list). Check that each popup ends with a complete sentence and a "Tier X Unlock" line, or is clearly an Active skill. If not, mark the gap with a TODO and ask for a screenshot of the rest.
- 2026-11-24: The class label (MAGE, PRIEST, ...) on the info panel is often partly covered by the popup. If it's only partly readable, record the most likely class with a "confirm" comment in the frontmatter.
- 2026-11-24: The user scrolls long popups and takes several overlapping screenshots of one skill. Stitch them together where the text overlaps, and keep each sentence only once.
- 2026-11-24: Tier = the number of lit purple gems in the info page's Tier row (6 lit = Tier 6). Skill popups dim the gems so they look unlit, so read tier only from a popup-free info page.
- 2026-11-24: If a skill uses an effect its own popup doesn't define (e.g. Sylvie's Divine Retribution), copy the definition from another hero's popup and note where it came from.
- 2026-11-24: **Correction from the user:** all screenshots up to this date came from the in-game **Hero Document**, not the user's own heroes. Their stats are reference values (max level/tier) and belong on hero pages, not the roster. The user will send their own roster separately so the two can be compared.
- 2026-11-24: The user is documenting hero base skills first. Focus on getting skill text complete and accurate before analysis.
