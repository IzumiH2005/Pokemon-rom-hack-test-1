"""Regle de berge decidee (lumiere haut-gauche, chemin en creux) :
pixel plein touchant l'herbe '.' au N ou a l'O -> OMBRE ; au S ou a l'E -> CLAIR ;
pixel plein dont le voisin N est OMBRE (2e rangee) -> DEMI.
usage: berge.py in.txt out.txt OMBRE CLAIR DEMI [calque]"""
import sys
src, dst, O, C, D = sys.argv[1:6]
cal = sys.argv[6] if len(sys.argv) > 6 else None
G = [list(l.rstrip('\n')) for l in open(src) if l.strip()]
H, W = len(G), len(G[0])
def v(x, y): return G[y][x] if 0 <= x < W and 0 <= y < H else 'X'
out = [r[:] for r in G]
for y in range(H):
    for x in range(W):
        c = G[y][x]
        if c == '.' or (cal and c not in cal): continue
        if v(x, y - 1) == '.' or v(x - 1, y) == '.': out[y][x] = O
        elif v(x, y + 1) == '.' or v(x + 1, y) == '.': out[y][x] = C
for y in range(1, H):
    for x in range(W):
        if out[y][x] not in '.'+O+C and (cal is None or G[y][x] in cal) and out[y-1][x] == O: out[y][x] = D
open(dst, 'w').write('\n'.join(''.join(r) for r in out) + '\n')
