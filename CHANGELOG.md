# Changelog

## v1.2.0 — 2026-10-27

- Three new cards: **streak** (uptime-style contribution streaks: longest
  run with date span, current run, active-day coverage, runs bar),
  **ledger** (one year's contributions audited by type: commits, PRs,
  issues, reviews, restricted), and **reach** (stargazer signal: total
  stars, top repos, dark-matter count). Sixteen cards total.
- New **dracula** theme — the classic #bd93f9 purple on dark — joining
  phosphor, amber, paper and nord. `docs/themes/ubuntu-dracula.svg` and
  `docs/themes/streak-dracula.svg` preview it.
- README: card grid shows the three new cards; themes table gains a
  dracula column. Test suite grown to 34.

## v1.1.0 — 2026-10-19

- New **nord** theme (frost-blue accent on polar-night panels), joining
  phosphor, amber and paper. `docs/themes/ubuntu-nord.svg` previews it.
- `python -m cards.render --list` prints available themes and cards.
- CONTRIBUTING.md: invariants, and how to add cards, themes and stats.
- README: themes section now shows all four palettes.

## v1.0.0 — 2026-10-18

- Initial public release: thirteen SVG stat cards for any GitHub user,
  one GraphQL round trip, standard library only, 29 tests.
- Three themes (phosphor, amber, paper), snapshot archive with drift
  tracking, profile-README stats table between markers.
- OpenClaw skill manifest (`SKILL.md`), self-updating workflow template
  (`examples/self-updating.yml`), nightly dogfood CI.
