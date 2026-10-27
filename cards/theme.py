"""Palettes and typography for the profile cards.

Five themes ship out of the box:

  phosphor — the terminal-green default (GitHub-dark base, #00ff41 accent)
  amber     — retro amber CRT (#ffb000 accent on warm dark)
  paper     — light mode for light-profile users (GitHub-green accent)
  nord     — polar-night blues with a frost accent
  dracula  — the classic purple-on-dark palette (#bd93f9 accent)

All use system monospace stacks: web fonts do not load inside GitHub's
camo-proxied SVGs, so the stack is what every renderer can rely on.

``apply(name)`` swaps the active palette at runtime; every module reads
colours through this module's attributes at draw time, so a single call
re-themes all 13 cards. The module-level names below are the active
(phosphor) palette and stay importable for backward compatibility.
"""

THEMES = {
    "phosphor": {
        "BG": "#0a0e14", "PANEL": "#0d1117", "BORDER": "#1f2730",
        "FG": "#c9d1d9", "DIM": "#8b949e", "GREEN": "#00ff41",
        "AMBER": "#e3b341", "CYAN": "#58a6ff", "RED": "#f85149",
        "PHOSPHOR": "#39d353", "SCOPE_BG": "#04120a",
    },
    "amber": {
        "BG": "#120c02", "PANEL": "#161004", "BORDER": "#3a2a0a",
        "FG": "#f0dfae", "DIM": "#a08c5a", "GREEN": "#ffb000",
        "AMBER": "#ff7b00", "CYAN": "#ffd875", "RED": "#ff5a4d",
        "PHOSPHOR": "#d99a00", "SCOPE_BG": "#1d1300",
    },
    "nord": {
        "BG": "#2e3440",
        "PANEL": "#3b4252",
        "BORDER": "#4c566a",
        "FG": "#eceff4",
        "DIM": "#d8dee9",
        "GREEN": "#88c0d0",
        "AMBER": "#ebcb8b",
        "CYAN": "#81a1c1",
        "RED": "#bf616a",
        "PHOSPHOR": "#a3be8c",
        "SCOPE_BG": "#434c5e",
    },
    "paper": {
        "BG": "#f6f8fa", "PANEL": "#ffffff", "BORDER": "#d0d7de",
        "FG": "#1f2328", "DIM": "#57606a", "GREEN": "#1a7f37",
        "AMBER": "#9a6700", "CYAN": "#0969da", "RED": "#cf222e",
        "PHOSPHOR": "#2ea043", "SCOPE_BG": "#dafbe1",
    },
    "dracula": {
        "BG": "#282a36", "PANEL": "#21222c", "BORDER": "#44475a",
        "FG": "#f8f8f2", "DIM": "#6272a4", "GREEN": "#50fa7b",
        "AMBER": "#f1fa8c", "CYAN": "#8be9fd", "RED": "#ff5555",
        "PHOSPHOR": "#bd93f9", "SCOPE_BG": "#343746",
    },
}

MONO = ("ui-monospace, SFMono-Regular, 'SF Mono', Menlo, Consolas, "
        "'Liberation Mono', monospace")

# Active palette — starts as phosphor; apply() swaps it.
BG = THEMES["phosphor"]["BG"]
PANEL = THEMES["phosphor"]["PANEL"]
BORDER = THEMES["phosphor"]["BORDER"]
FG = THEMES["phosphor"]["FG"]
DIM = THEMES["phosphor"]["DIM"]
GREEN = THEMES["phosphor"]["GREEN"]
AMBER = THEMES["phosphor"]["AMBER"]
CYAN = THEMES["phosphor"]["CYAN"]
RED = THEMES["phosphor"]["RED"]
PHOSPHOR = THEMES["phosphor"]["PHOSPHOR"]
SCOPE_BG = THEMES["phosphor"]["SCOPE_BG"]


def apply(name):
    """Set the active theme. Raises KeyError on an unknown name."""
    palette = THEMES[name]
    globals().update(palette)
    return name
