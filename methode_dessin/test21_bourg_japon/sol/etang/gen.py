"""Etang : assemble mes pieces dans le bloc 3x3 et la planche interieure (regles decidees ci-dessous)."""
import sys; sys.path.insert(0, 'etang')
from pieces import HST, VST, COIN, PETIT, HST2, VST2
def vide(n): return [['x'] * n for _ in range(n)]
def stamp(G, P, x0, y0):
    for y, r in enumerate(P):
        for x, c in enumerate(r):
            if c != '.' and 0 <= y0 + y < len(G) and 0 <= x0 + x < len(G): G[y0 + y][x0 + x] = c
def save(G, p): open(p, 'w').write('\n'.join(''.join(r) for r in G) + '\n')
B = vide(48)
# eau : ombre y sous la rive haute (2 rangs) et a droite de la rive gauche (1 col), reflet w au-dessus de la rive basse
for x in range(48):
    B[5][x] = B[6][x] = 'y'; B[42][x] = 'w'
for y in range(48):
    B[y][5] = 'y'
for x in range(0, 48, 8):
    P = HST if x % 16 == 0 else HST2; stamp(B, P, x, 0); stamp(B, P, x, 43)
for y in range(0, 48, 8):
    P = VST if y % 16 == 0 else VST2; stamp(B, P, 0, y); stamp(B, P, 43, y)
for (x, y) in ((0, 0), (40, 0), (0, 40), (40, 40)):
    for yy in range(8):
        for xx in range(8): B[y + yy][x + xx] = 'x'
    stamp(B, COIN, x, y)
# ombre portee du galet de coin sur l'eau
for (x, y) in ((0, 0), (40, 0)):
    for xx in range(8): B[y + 8][x + xx] = 'y' if B[y + 8][x + xx] == 'x' else B[y + 8][x + xx]
# reflets de surface (tirets w) dans la case centrale et les bords, hors coutures
for (x, y, n) in ((18, 20, 3), (26, 26, 2), (21, 29, 2), (28, 18, 2), (12, 22, 2), (36, 28, 2), (20, 11, 2), (26, 37, 3)):
    for i in range(n): B[y][x + i] = 'w'
save(B, 'etang/etang.txt')
I = vide(32)
for (x, y) in ((12, 12), (16, 12), (12, 16), (16, 16)):
    stamp(I, PETIT, x, y)
for x in (12, 13, 14, 15, 16, 17, 18, 19): I[20][x] = 'y' if I[20][x] == 'x' else I[20][x]
for (x, y, n) in ((4, 6, 2), (24, 26, 2), (5, 25, 2)):
    for i in range(n): I[y][x + i] = 'w'
save(I, 'etang/etang_int.txt')
