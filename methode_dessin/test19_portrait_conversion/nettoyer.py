# Nettoyage mécanique : un pixel isolé (moins de 2 voisins identiques sur 8) prend la couleur
# majoritaire autour de lui. Ne touche pas au vide. Usage : python3 nettoyer.py in.txt out.txt [passes]
import sys
from collections import Counter
G = [list(l.rstrip('\n')) for l in open(sys.argv[1]) if l.strip()]
for _ in range(int(sys.argv[3]) if len(sys.argv) > 3 else 1):
    H = [r[:] for r in G]
    for y in range(1, 127):
        for x in range(1, 127):
            c = G[y][x]
            if c == '.': continue
            v = [G[y+j][x+i] for j in (-1, 0, 1) for i in (-1, 0, 1) if i or j]
            if v.count(c) < 2:
                m = Counter(k for k in v if k != '.').most_common(1)
                if m: H[y][x] = m[0][0]
    G = H
open(sys.argv[2], 'w').write('\n'.join(''.join(r) for r in G) + '\n')
