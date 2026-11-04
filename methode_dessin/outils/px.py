"""Rend une grille texte en PNG : ×1 (nom.png) et agrandie avec grille (nom_vue.png).

Usage : python3 px.py etape_XX.txt ECHELLE palette.json
palette.json : {"O": "#2a1a2e", ...} ; '.' = transparent.
"""
import json
import sys
from PIL import Image, ImageDraw


def charger(txt, pal):
    G = [l.rstrip('\n') for l in open(txt) if l.strip()]
    H, W = len(G), len(G[0])
    im = Image.new('RGBA', (W, H), (0, 0, 0, 0))
    for y, r in enumerate(G):
        for x, c in enumerate(r):
            if c != '.':
                if c not in pal:
                    raise SystemExit(f'couleur inconnue {c!r} en {x},{y}')
                h = pal[c].lstrip('#')
                im.putpixel((x, y), (int(h[0:2], 16), int(h[2:4], 16), int(h[4:6], 16), 255))
    return im


if __name__ == '__main__':
    txt, k, palf = sys.argv[1], int(sys.argv[2]), sys.argv[3]
    pal = json.load(open(palf))
    im = charger(txt, pal)
    base = txt.rsplit('.', 1)[0]
    im.save(base + '.png')
    W, H = im.size
    fond = Image.new('RGBA', (W * k, H * k), (236, 234, 228, 255))
    fond.alpha_composite(im.resize((W * k, H * k), Image.NEAREST))
    d = ImageDraw.Draw(fond)
    for x in range(0, W * k, k):
        d.line([(x, 0), (x, H * k)], fill=(0, 0, 0, 28) if (x // k) % 8 else (0, 0, 0, 70))
    for y in range(0, H * k, k):
        d.line([(0, y), (W * k, y)], fill=(0, 0, 0, 28) if (y // k) % 8 else (0, 0, 0, 70))
    fond.convert('RGB').save(base + '_vue.png')
