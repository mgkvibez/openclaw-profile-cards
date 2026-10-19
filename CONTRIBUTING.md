# Contributing to openclaw-profile-cards

Thanks for wanting to build on the deck. This project has three
invariants and a short list of conventions; everything else is
yours.

## Invariants

1. **Standard library only.** No pip installs, no web fonts, no
   network beyond the single GraphQL call in `github_data.py`.
   The cards must render in a bare `python3` checkout.
2. **SVGs must render inside GitHub READMEs.** GitHub proxies images
   through camo and blocks external fetches: no `<script>`, no
   external stylesheets, no web fonts. System font stacks only (see
   `theme.MONO`).
3. **Every card is pure.** A card takes the normalized profile dict
   (and, for archive-aware cards, the snapshot history) and returns
   an SVG string. Library code raises `ValueError`; I/O lives in the
   CLI and `render.py`.

## Adding a card

Cards live in `cards/card_*.py` and expose `render(profile, history=None)`.

1. Write the card against `testdata/profile.json` (offline fixture,
   no token needed).
2. Register it in `CARDS` inside `cards/render.py` with its output
   filename.
3. Add tests in `cards/test_cards.py` — build a small profile dict
   inline, render, and assert on the strings that matter (titles,
   bar widths, color hexes). Look at an existing card's tests first;
   the suite runs green in under a second.
4. Run `python -m unittest cards.test_cards` — all tests must pass.

## Adding a theme

Themes are flat palettes in `cards/theme.py` (`THEMES`). Copy an
existing entry, keep the eleven semantic slots (BG, PANEL, BORDER, FG,
DIM, GREEN, AMBER, CYAN, RED, PHOSPHOR, SCOPE_BG), and give the accent
(`GREEN`) enough contrast against BG for text. `theme.apply(name)`
mutates the module globals, so cards keep reading `theme.GREEN` —
never copy colors at import time. `python -m cards.render --list`
should show your theme, and `--theme <name>` should re-render every
card.

## Adding a stat to the data layer

`cards/github_data.py` owns the single GraphQL query and normalization.
Add the field to the query, normalize it in `_normalize`, extend the
fixture, and bump the snapshot version comment if archive shape changes
(older snapshots must keep loading — `history.py` tolerates missing
fields gracefully).

## Repo layout

- `cards/` — the generator (cards, data, history, table, themes)
- `testdata/` — offline fixture used by tests and smoke rendering
- `docs/demo/` — rendered examples, refreshed nightly by CI
- `examples/` — the self-updating workflow users copy into their
  profile repos

## Skill packaging

`SKILL.md` is the agent-facing manifest. Keep its frontmatter `name`
and `description` accurate when you change behavior — the Agensi and
ClawHub listings point at them.
