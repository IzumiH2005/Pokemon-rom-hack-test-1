"""Formes posées à la main sur une grille 128 (aucune forme n'est décidée par l'outil).
Usage : python3 formes.py in.txt|NEW:WxH out.txt cmds.txt
Lignes de cmds.txt (coordonnées x y) :
  poly C x1 y1 x2 y2 ...        polygone plein
  ligne C L x1 y1 x2 y2 ...     ligne brisée d'épaisseur L (1 = pixel-perfect)
  px C x y [x y ...]            pixels isolés
  masque C D                    remplace D par C (ex. retirer une couleur)
Un C en majuscule '_' efface (remet '.')."""
import sys
from PIL import Image, ImageDraw
src, dst, cmds = sys.argv[1:4]
if src.startswith('NEW:'):
    W, H = map(int, src[4:].split('x')); G = [['.'] * W for _ in range(H)]
else:
    G = [list(l.rstrip('\n')) for l in open(src) if l.strip()]; H, W = len(G), len(G[0])
for l in open(cmds):
    l = l.split('#')[0].split()
    if not l: continue
    op, c = l[0], l[1]; c = '.' if c == '_' else c
    if op == 'masque':
        G = [[c if v == l[2] else v for v in r] for r in G]; continue
    if op == 'px':
        n = list(map(int, l[2:]))
        for x, y in zip(n[::2], n[1::2]): G[y][x] = c
        continue
    m = Image.new('1', (W, H), 0); d = ImageDraw.Draw(m)
    if op == 'poly':
        n = list(map(float, l[2:])); d.polygon(list(zip(n[::2], n[1::2])), fill=1)
    elif op == 'ligne':
        w = int(l[2]); n = list(map(float, l[3:])); p = list(zip(n[::2], n[1::2]))
        d.line(p, fill=1, width=w)
        if w == 1 and len(p) == 1: d.point(p, fill=1)
    px = m.load()
    for y in range(H):
        for x in range(W):
            if px[x, y]: G[y][x] = c
open(dst, 'w').write('\n'.join(''.join(r) for r in G) + '\n')
