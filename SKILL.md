---
name: openclaw-profile-cards
description: Render a GitHub user's profile as 13 self-updating, terminal-themed SVG stat cards (contribution heatmap, languages, activity, collaboration, commit rhythm, years, drift, city skyline, loss-curve, oscilloscope, portscan, registry, whoami terminal) plus a stats table for their profile README. Use when the user wants to generate, refresh or re-theme GitHub profile cards or profile statistics.
---

# openclaw-profile-cards

Turn any GitHub account's live data into thirteen hand-drawn SVG stat cards
and a stats table — no third-party widget APIs, one GraphQL round trip,
committed straight to the user's profile README.

## Requirements

- Python 3.10+ (standard library only)
- A GitHub token for live data. `GITHUB_TOKEN` env var. A classic PAT with
  `repo` scope also counts private repositories; a fine-grained token with
  read-only access works for public-only cards.

## Commands

Render a user's cards from the live API:

```console
GITHUB_TOKEN=ghp_xxx python3 -m cards.render --login <username> --out assets/cards
```

Re-theme everything (phosphor | amber | paper):

```console
python3 -m cards.render --login <username> --out assets/cards --theme amber
```

Offline render from the bundled fixture (no token needed):

```console
python3 -m cards.render --fixture testdata/profile.json --out assets/cards
```

Tests:

```console
python -m unittest cards.test_cards
```

## What it produces

`assets/cards/` — 13 SVGs: `ubuntu` (whoami terminal), `heatmap`
(contribution calendar with quartile bands), `languages` (byte share by
language), `activity` (streaks + 30-day sparkline), `collab` (PRs, reviews,
issues), `rhythm` (7×24 commit heatmap), `years` (per-year monthly cells),
`drift` (language share vs a month-old snapshot), `city` (repo skyline),
`training` (contributions as a converging loss curve), `scope`
(daily waveform), `portscan` (repos as nmap services), `registry`
(repos as deployed models).

`history.jsonl` — one snapshot per render (trimmed to the last 120). The
`drift` card compares against the snapshot from ~30 days ago, so it starts
in an honest "archive started today" state and fills in after a month.

The README table: `table.build(data, history_entries)` produces a markdown
stats block meant to be maintained between `<!-- cards:table:start -->` and
`<!-- cards:table:end -->` markers in the user's profile README. Keep the
markers: that's what makes the table safely self-updating.

## Embedding

Reference the committed SVGs from the profile README:

```markdown
<img src="assets/cards/heatmap.svg" alt="Contribution heatmap" width="100%">
```

SVGs use system monospace stacks — web fonts do not render through GitHub's
camo proxy, so do not swap in web fonts.

## Self-updating profiles

Point the user at `examples/self-updating.yml` — a GitHub Action that
renders daily and commits the cards back, keeping the profile current
without any external service.
