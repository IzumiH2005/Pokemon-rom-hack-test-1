"""Règle mécanique de contour (partie D).

Usage : python3 contour.py in.txt out.txt [CALQUE [CONTRE]] [--trait=O]
- sans CALQUE : tout pixel plein qui touche le vide (4 voisins) devient le trait ;
- avec CALQUE : seules ces lettres, si elles touchent le vide ou une lettre de CONTRE.
"""
import sys

args = [a for a in sys.argv[1:] if not a.startswith('--')]
trait = next((a.split('=')[1] for a in sys.argv[1:] if a.startswith('--trait=')), 'O')
src, dst = args[0], args[1]
calque = args[2] if len(args) > 2 else None
contre = args[3] if len(args) > 3 else ''

G = [list(l.rstrip('\n')) for l in open(src) if l.strip()]
H, W = len(G), len(G[0])
out = [r[:] for r in G]
for y in range(H):
    for x in range(W):
        c = G[y][x]
        if c == '.' or (calque and c not in calque):
            continue
        for dx, dy in ((1, 0), (-1, 0), (0, 1), (0, -1)):
            nx, ny = x + dx, y + dy
            v = G[ny][nx] if 0 <= nx < W and 0 <= ny < H else '.'
            if v == '.' or v in contre:
                out[y][x] = trait
                break
open(dst, 'w').write('\n'.join(''.join(r) for r in out) + '\n')
