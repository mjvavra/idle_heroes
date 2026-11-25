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

## Maintaining the repo

- When the player shares new information (new hero pulled, star-up, event results), update `account/roster.md`, and add a dated entry to `logs/decisions.md` if a resource decision was made.
- New heroes: copy `heroes/_TEMPLATE.md` to `heroes/<faction>/<hero-name>.md` (lowercase, hyphenated).
- New strategies: copy `strategies/_TEMPLATE.md`.
- New game modes: copy `game-modes/_TEMPLATE.md`.
- Keep the index tables in each folder's `README.md` up to date.
- Use dates in `YYYY-MM-DD` format.
