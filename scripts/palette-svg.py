"""Render assets/palette.svg from colors.toml: a terminal sample over the swatches.

Usage: python3 scripts/palette-svg.py
"""
import tomllib
from pathlib import Path

root = Path(__file__).resolve().parent.parent
c = tomllib.loads((root / "colors.toml").read_text())

W, PAD = 880, 32
FONT = "ui-monospace, 'SF Mono', Menlo, Consolas, monospace"

def text(x, y, s, fill, size=14, weight=400):
    s = s.replace("&", "&amp;").replace("<", "&lt;").replace(">", "&gt;")
    return f'<text x="{x}" y="{y}" fill="{fill}" font-family="{FONT}" font-size="{size}" font-weight="{weight}" xml:space="preserve">{s}</text>'

def line(x, y, parts, size=14):
    """Draw a row of (text, colour) runs using a fixed character width."""
    out, cw = [], size * 0.6
    for s, col in parts:
        out.append(text(x, y, s, col, size))
        x += len(s) * cw
    return "".join(out)

el = []
# Window chrome
el.append(f'<rect width="{W}" height="560" rx="14" fill="{c["darker_background"]}"/>')
el.append(f'<rect x="{PAD}" y="{PAD}" width="{W-2*PAD}" height="300" rx="10" fill="{c["background"]}"/>')
el.append(f'<rect x="{PAD}" y="{PAD}" width="{W-2*PAD}" height="300" rx="10" fill="none" stroke="url(#border)" stroke-width="2"/>')
el.append(text(PAD + 20, PAD + 30, "outlaw — ~/trail", c["dark_foreground"], 12))

fg, cm = c["foreground"], c["muted"]
rows = [
    [("~/trail ", c["blue"]), ("on ", cm), (" main ", c["magenta"]), ("❯ ", c["green"]), ("cat wanted.rs", fg)],
    [("// Dead or alive, payable at the sheriff's office.", cm)],
    [("pub fn ", c["magenta"]), ("bounty", c["blue"]), ("(", fg), ("name", c["cyan"]), (": &", fg), ("str", c["yellow"]), (") -> ", fg), ("Poster", c["yellow"]), (" {", fg)],
    [("    let ", c["magenta"]), ("reward", fg), (" = ", fg), ("5_000", c["orange"]), (";", fg)],
    [("    Poster", c["yellow"]), ("::", fg), ("new", c["blue"]), ("(name, reward, ", fg), ('"Blackwater"', c["green"]), (")", fg)],
    [("}", fg)],
    [("", fg)],
    [("● ", c["green"]), ("3 riders mounted   ", fg), ("● ", c["yellow"]), ("storm on the ridge   ", fg), ("● ", c["red"]), ("bridge out", fg)],
]
y = PAD + 70
for r in rows:
    el.append(line(PAD + 20, y, r))
    y += 28
# Selection + cursor on the prompt line
el.append(f'<rect x="{PAD+20}" y="{y-20}" width="{8*8.4}" height="20" fill="{c["selection_background"]}"/>')
el.append(line(PAD + 20, y - 4, [("selected", c["selection_foreground"]), (" ", fg)]))
el.append(f'<rect x="{PAD+20+9*8.4}" y="{y-19}" width="8.4" height="18" fill="{c["bright_foreground"]}"/>')

# Swatches: two rows of eight (normal, bright)
names = ["background", "red", "green", "yellow", "blue", "magenta", "cyan", "foreground"]
bright = ["muted", "bright_red", "bright_green", "bright_yellow", "bright_blue", "bright_magenta", "bright_cyan", "bright_foreground"]
sw = (W - 2 * PAD - 7 * 8) / 8
for row, keys in enumerate([names, bright]):
    for i, k in enumerate(keys):
        x, yy = PAD + i * (sw + 8), 360 + row * 92
        el.append(f'<rect x="{x:.1f}" y="{yy}" width="{sw:.1f}" height="56" rx="8" fill="{c[k]}" stroke="{c["lighter_background"]}"/>')
        el.append(text(x + 2, yy + 74, c[k], c["dark_foreground"], 12))

svg = f'''<svg xmlns="http://www.w3.org/2000/svg" width="{W}" height="560" viewBox="0 0 {W} 560">
<defs><linearGradient id="border" x1="0" y1="0" x2="1" y2="1">
<stop offset="0" stop-color="{c["yellow"]}"/><stop offset="1" stop-color="{c["accent"]}"/></linearGradient></defs>
{"".join(el)}
</svg>
'''
(root / "assets" / "palette.svg").write_text(svg)
print("wrote assets/palette.svg")
