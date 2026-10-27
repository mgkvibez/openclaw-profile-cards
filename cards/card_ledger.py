"""Ledger — one year's contributions, audited by type.

Every contribution the account made in the window, booked to its
account: commits, pull requests, issues, reviews and restricted (the
private-repo work GitHub counts but does not itemise). Collab shows
the collaborative share; the ledger shows the full raw mix, because
the split itself is the story — a year that is mostly restricted is
a year of private craft, and a year of many PRs is a year in other
people's codebases.

Bars share one scale — the largest entry — so the shape of the year
is visible before any number is read. Restricted work is drawn in the
theme's accent colour to mark it as counted-but-not-itemised, and the
total row books the year's balance.
"""
from . import svg, theme

W = 460
PAD = 18
TOP = 74
ROW = 28
LABELS = [("commits", "commits"),
          ("prs", "pull requests"),
          ("issues", "issues"),
          ("reviews", "reviews"),
          ("restricted", "restricted (private)")]


def render(data):
    collab = data.get("collab") or {}
    entries = [(key, label, collab.get(key) or 0) for key, label in LABELS]
    largest = max((c for _, _, c in entries), default=0)
    total = sum(c for _, _, c in entries)

    h = TOP + (len(entries) + 1) * ROW + 30
    out = [svg.svg_open(W, h, "Contributions by type: the year's ledger "
                              "of commits, pull requests, issues, reviews "
                              "and restricted work"),
           svg.panel(10, 10, W - 20, h - 20),
           svg.bar(10, 10, W - 20, "ledger.contributions"),
           svg.text(PAD, TOP - 12, "$ git ledger --audit-year",
                    theme.GREEN, 13)]

    bar_left = 190
    bar_max = W - bar_left - PAD
    for i, (key, label, count) in enumerate(entries):
        y = TOP + 16 + i * ROW
        color = theme.PHOSPHOR if key == "restricted" else theme.GREEN
        out.append(svg.text(PAD, y, label, theme.DIM, 11))
        out.append(svg.text(bar_left - 10, y, str(count),
                            theme.FG if count else theme.DIM, 11,
                            anchor="end", weight="bold" if count else "normal"))
        if count and largest:
            out.append(svg.rect(bar_left, y - 9,
                                max(bar_max * count / float(largest), 1.2),
                                10, color, rx=1, opacity=0.85))

    y_total = TOP + 16 + len(entries) * ROW
    out.append(svg.line(PAD, y_total - 20, W - PAD, y_total - 20,
                        theme.BORDER))
    out.append(svg.text(PAD, y_total, "year booked", theme.DIM, 11))
    out.append(svg.text(W - PAD, y_total, str(total), theme.GREEN, 12,
                        anchor="end", weight="bold"))
    out.append(svg.svg_close())
    return "".join(out)
