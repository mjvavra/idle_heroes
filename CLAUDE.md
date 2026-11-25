# Idle Heroes Knowledge Base

This repo stores information about the mobile game **Idle Heroes**: the player's own account, hero details, game-mode notes and strategies. Use it to give advice that fits this specific account, not generic advice.

## How to use this repo when answering questions

1. **Start with the account.** Read `account/profile.md` (level, VIP, goals, play style) and `account/roster.md` (heroes owned, stars, gear) before recommending anything. Advice must use heroes the player actually has, or clearly say "you'd need to acquire X".
2. **Look up the heroes and modes involved** in `heroes/` and `game-modes/`.
3. **Check `strategies/`** for existing team comps and plans before inventing new ones.
4. **Check `logs/decisions.md`** for past decisions and their reasons so advice stays consistent (e.g. resources already committed to a hero).

## Accuracy rules

- The game is patched often. Prefer information in this repo over general training knowledge, and note when the repo might be outdated (check `last_updated` / `patch` fields).
- If information in the repo is missing and you fill it in from general knowledge, say so and mark the claim as **unverified**.
- Never invent exact skill numbers. Leave a `TODO` instead.

## Current focus: hero base skills

The player is documenting heroes' base skills first.
- Hero pages hold game information only: faction, class, skill text copied word for word from the in-game **Hero Document** (including unlock tier and effect definitions), and the Document's reference stats at max level and tier.
- The player's own heroes (actual level, tier, stats, gear) go in `account/roster.md`. That data comes from their own hero screens, never from the Hero Document.
- When advising, compare the player's copy (roster) with the reference stats and the skills locked by tier (hero page). For example, a hero below Tier 6 doesn't have their Tier 6 skill yet.
- Keep analysis in its own section marked unverified, apart from the copied skill text.

## Processing screenshots

Use the `process-screenshots` skill (`.claude/skills/process-screenshots/SKILL.md`). It has the full process and the screenshot rules. When the user corrects how screenshots are handled, or a new edge case comes up, add a dated bullet to that skill's **Learned rules** section.

## Web research

General game info (hero skills, tier lists, mode mechanics, events) can be researched on the web. Sources disagree and go stale, so record the source and date in the file's `sources` / `patch` fields, and prefer the newest sources. See `reference/sources.md`.

## Public wiki site

Pushing to `main` publishes the markdown folders as a public, searchable site (GitHub Pages, MkDocs Material) at https://mjvavra.github.io/idle_heroes/. `scripts/assemble_docs.py` gathers the pages; templates, `CLAUDE.md` and screenshots are left out.
- Everything in the published folders is public. Don't write player IDs, emails or other private details into them.
- Screenshots are git-ignored and never pushed.
- To preview locally: `pip install -r requirements-site.txt`, `python scripts/assemble_docs.py`, `mkdocs serve`.

## Maintaining the repo

- When the player shares new information (new hero pulled, star-up, event results), update `account/roster.md`, and add a dated entry to `logs/decisions.md` if a resource decision was made.
- New heroes: copy `heroes/_TEMPLATE.md` to `heroes/<faction>/<hero-name>.md` (lowercase, hyphenated).
- New strategies: copy `strategies/_TEMPLATE.md`.
- New game modes: copy `game-modes/_TEMPLATE.md`.
- Keep the index tables in each folder's `README.md` up to date.
- Use dates in `YYYY-MM-DD` format.
