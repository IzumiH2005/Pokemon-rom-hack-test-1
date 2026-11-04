# Conversion brute illustration -> brouillon 128x128 (point de départ, pas le résultat).
# 1) fond clair retiré par remplissage depuis les bords ; 2) chaque pixel -> couleur la plus proche
#    de la palette choisie à la main (distance pondérée sur la luminance).
# Usage : python3 convertir.py reduit128.png brouillon.txt
import sys, json
from PIL import Image
pal = json.load(open('palette.json'))
P = {k: tuple(int(v[i:i+2], 16) for i in (1, 3, 5)) for k, v in pal.items()}
im = Image.open(sys.argv[1]).convert('RGB'); W, H = im.size
px = im.load()
lum = lambda c: 0.3*c[0] + 0.59*c[1] + 0.11*c[2]
fond = set(); pile = [(x, y) for x in range(W) for y in (0, H-1)] + [(x, y) for y in range(H) for x in (0, W-1)]
while pile:
    x, y = pile.pop()
    if (x, y) in fond or not (0 <= x < W and 0 <= y < H): continue
    c = px[x, y]
    if lum(c) < 200 or max(c) - min(c) > 60: continue
    fond.add((x, y)); pile += [(x+1, y), (x-1, y), (x, y+1), (x, y-1)]
def proche(c):
    best = None
    for k, p in P.items():
        d = 3*(lum(c) - lum(p))**2 + sum((c[i] - p[i])**2 for i in range(3))
        if best is None or d < best[0]: best = (d, k)
    return best[1]
G = [''.join('.' if (x, y) in fond else proche(px[x, y]) for x in range(W)) for y in range(H)]
open(sys.argv[2], 'w').write('\n'.join(G) + '\n')
