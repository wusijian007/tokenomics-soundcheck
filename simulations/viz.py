"""Shared plotting style + helpers for the death-spiral simulations.

Chart text is intentionally in English (universal for an open-source repo and
avoids CJK font-rendering issues across machines). The Chinese analysis lives in
the markdown docs and the skill pack.
"""
import matplotlib
matplotlib.use("Agg")  # headless: write PNGs, never open a window
import matplotlib.pyplot as plt
from pathlib import Path

CHARTS = Path(__file__).parent / "charts"
CHARTS.mkdir(exist_ok=True)

plt.rcParams.update({
    "figure.dpi": 130,
    "savefig.dpi": 130,
    "font.size": 10,
    "axes.titlesize": 11,
    "axes.titleweight": "bold",
    "axes.grid": True,
    "grid.alpha": 0.22,
    "axes.spines.top": False,
    "axes.spines.right": False,
    "figure.facecolor": "white",
    "axes.facecolor": "white",
    "legend.frameon": False,
})

# Consistent palette across all charts
C = {
    "blue":   "#2563eb",
    "red":    "#dc2626",
    "green":  "#16a34a",
    "amber":  "#d97706",
    "gray":   "#6b7280",
    "purple": "#7c3aed",
    "teal":   "#0d9488",
    "ink":    "#111827",
}


def save(fig, name, caption=None):
    """Tight-layout, save into charts/, close, and report the path."""
    fig.tight_layout()
    path = CHARTS / name
    fig.savefig(path, bbox_inches="tight")
    plt.close(fig)
    print(f"  [chart] {path.relative_to(CHARTS.parent.parent)}")
    if caption:
        print(f"          {caption}")
    return path
