"""Uptime — contribution streaks, the calendar as an SLA.

The contribution calendar is treated as a service status feed: a day
with at least one contribution is up, an empty day is an outage. The
card reports the longest unbroken run (with its date span), the run
still standing, and how many of the window's days were up at all.

Trailing empty days are the calendar's future, not downtime — they
are ignored before the current run is measured, and a profile with no
contributions at all is reported honestly rather than as a zero-day
streak. The bulk bar at the foot shows every run as a block of green
proportional to its length, so a profile's rhythm is legible at a
glance without reading a number.
"""
from . import svg, theme

W = 460
PAD = 18
TOP = 74
ROW = 30


def _runs(days):
    """[(start_index, length), ...] of consecutive count>0 days."""
    runs, start, length = [], 0, 0
    for i, d in enumerate(days):
        if d["count"] > 0:
            if length == 0:
                start = i
            length += 1
        elif length:
            runs.append((start, length))
            length = 0
    if length:
        runs.append((start, length))
    return runs


def _current(days):
    """The run touching the last up day; trailing empty days ignored."""
    i = len(days) - 1
    while i >= 0 and days[i]["count"] == 0:
        i -= 1
    n = 0
    while i >= 0 and days[i]["count"] > 0:
        n += 1
        i -= 1
    return n


def render(data):
    days = data.get("days") or []
    runs = _runs(days)
    longest = max((r[1] for r in runs), default=0)
    current = _current(days)
    up_days = sum(1 for d in days if d["count"] > 0)
    window = len(days)

    h = TOP + 4 * ROW + 92
    out = [svg.svg_open(W, h, "Contribution streaks: longest run, current "
                              "run and active-day coverage for the year"),
           svg.panel(10, 10, W - 20, h - 20),
           svg.bar(10, 10, W - 20, "uptime.streaks"),
           svg.text(PAD, TOP - 12, "$ uptime --contributions --human",
                    theme.GREEN, 13)]

    span = ""
    best = max(runs, key=lambda r: r[1], default=None)
    if best:
        span = "%s \u2192 %s" % (days[best[0]]["date"],
                                days[best[0] + best[1] - 1]["date"])
    rows = [
        ("longest run", str(longest) + "d", span, theme.GREEN),
        ("current run", str(current) + "d" if current else "down",
         "live" if current else "", theme.GREEN if current else theme.DIM),
        ("days up", "%d / %d" % (up_days, window),
         "%.0f%% coverage" % (100.0 * up_days / window) if window else "",
         theme.FG),
        ("outages", str(window - up_days),
         "empty days in window", theme.DIM),
    ]
    for i, (label, value, note, color) in enumerate(rows):
        y = TOP + 14 + i * ROW
        out.append(svg.text(PAD, y, label, theme.DIM, 12))
        out.append(svg.text(150, y, value, color, 12, weight="bold"))
        if note:
            out.append(svg.text(W - PAD, y, note, theme.DIM, 10, anchor="end"))

    # Bulk bar: one green block per run, width proportional to length.
    bar_y = TOP + 4 * ROW + 18
    out.append(svg.text(PAD, bar_y - 6, "runs", theme.DIM, 9))
    if runs:
        scale = (W - 2 * PAD) / float(window)
        for start, length in runs:
            out.append(svg.rect(PAD + start * scale, bar_y,
                                max(length * scale, 1.2), 10,
                                theme.PHOSPHOR, rx=1))
    else:
        out.append(svg.text(PAD, bar_y + 10, "no contribution history yet",
                            theme.DIM, 11))
    out.append(svg.text(PAD, h - 16, "one year window \u00b7 up = 1+ "
                    "contribution that day \u00b7 trailing empty days are "
                    "the future", theme.DIM, 9))
    out.append(svg.svg_close())
    return "".join(out)
