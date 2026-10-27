"""Star reach — the stargazer signal across deployed repos.

Stars are a signal other people send, so the card reads like one:
total stargazers across every public repo, the strongest signals
ranked, and — the honest part — how much of the fleet is dark matter,
repos nobody has starred yet. The count is kept exact, not inflated:
archived and private repos are part of the fleet even when they
contribute nothing to the signal.

No repo is named that the profile does not own, and an empty fleet
says so plainly rather than drawing a chart of zero.
"""
from . import svg, theme

W = 460
PAD = 18
TOP = 74
ROW = 24
TOP_N = 4


def render(data):
    repos = data.get("repos") or []
    starred = sorted((r for r in repos if r["stars"] > 0),
                     key=lambda r: r["stars"], reverse=True)
    total = sum(r["stars"] for r in repos)
    dark = sum(1 for r in repos if r["stars"] == 0)

    shown = starred[:TOP_N]
    h = TOP + (len(shown) + 3) * ROW + 26
    out = [svg.svg_open(W, h, "Stargazer reach: total stars across the "
                              "repo fleet, top signals ranked, dark-matter "
                              "count"),
           svg.panel(10, 10, W - 20, h - 20),
           svg.bar(10, 10, W - 20, "signal.reach"),
           svg.text(PAD, TOP - 12, "$ signal-strength --stars",
                    theme.GREEN, 13)]

    y = TOP + 16
    out.append(svg.text(PAD, y, "total stargazers", theme.DIM, 12))
    out.append(svg.text(W - PAD, y, str(total), theme.GREEN, 13,
                        anchor="end", weight="bold"))
    y += ROW

    top_count = shown[0]["stars"] if shown else 0
    for r in shown:
        y += ROW
        out.append(svg.text(PAD, y, r["name"], theme.FG, 11))
        out.append(svg.text(230, y, "\u2605 %d" % r["stars"],
                            theme.AMBER if r["stars"] < top_count
                            else theme.GREEN, 11))
        bar_w = max((W - 270 - PAD) * r["stars"] /
                    float(top_count or 1), 1.2)
        out.append(svg.rect(270, y - 9, bar_w, 10, theme.GREEN, rx=1,
                            opacity=0.85))

    y += ROW
    out.append(svg.text(PAD, y, "dark matter", theme.DIM, 11))
    out.append(svg.text(W - PAD, y,
                        "%d repos at 0 \u2605" % dark if repos
                        else "no repos",
                        theme.DIM, 11, anchor="end"))
    if not repos:
        y += ROW
        out.append(svg.text(PAD, y, "no repos in fleet", theme.DIM, 11))
    out.append(svg.svg_close())
    return "".join(out)
