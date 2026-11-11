"""Empile des grilles texte en une planche PNG indexée 16 couleurs (index 0 = transparent).
Usage : indexe.py pal.json out.png f0.txt f1.txt ..."""
import sys, json
from PIL import Image
pal = json.load(open(sys.argv[1])); out = sys.argv[2]; fs = sys.argv[3:]
cles = list(pal)
G = [[l.rstrip('\n') for l in open(f) if l.strip()] for f in fs]
im = Image.new('P', (64, 64 * len(fs)), 0)
p = [255, 0, 255]
for c in cles:
    h = pal[c].lstrip('#'); p += [int(h[i:i + 2], 16) for i in (0, 2, 4)]
p += [0, 0, 0] * (16 - len(p) // 3)
im.putpalette(p)
for n, g in enumerate(G):
    for y, r in enumerate(g):
        for x, c in enumerate(r):
            if c != '.': im.putpixel((x, 64 * n + y), cles.index(c) + 1)
im.save(out)
