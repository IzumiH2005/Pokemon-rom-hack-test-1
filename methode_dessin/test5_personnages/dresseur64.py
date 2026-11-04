# Lina en 64 px de haut (≈ 3,2 têtes, tête cheveux compris ≈ 32 %).
# Étapes : zones (demi-carte en symétrie) → contour extérieur + lignes intérieures en ton sombre
# (selout) → ombrage de cylindre par zone, lumière à gauche → retouches à la main (visage,
# mèches, reflets). Yeux 5x4 avec blanc, iris sombre en haut et clair en bas, reflet à gauche.
from base import *

W, H, CX = 64, 64, 31.5
PAL64 = dict(PAL, w=(208, 220, 234))        # blanc de l'œil bleuté (jamais blanc pur)
RAMPE = {'H': 'abc', 'S': '123', 'J': 'rqp', 'A': 'rqp', 'N': 'nnm', 'L': '123', 'R': 'rqp',
         'Y': 'YYY', 'C': 'WWW', 'K': '123', 'B': 'YYY', 'X': 'WWW'}

def spans():
    """(rangée, zone, d0, d1) : d = distance au centre (0 = les deux colonnes centrales)."""
    s = []
    dome = {2: 5, 3: 7, 4: 8, 5: 9, 6: 10}
    for y in range(2, 22): s.append((y, 'H', 0, dome.get(y, 11)))
    s += [(22, 'H', 8, 11)]
    for y in (7, 8): s.append((y, 'Y', 0, 11))
    face = {10: 6, 11: 7, 12: 7, 13: 7, 14: 7, 15: 7, 16: 7, 17: 7, 18: 7, 19: 6, 20: 5, 21: 3}
    for y, d in face.items(): s.append((y, 'S', 0, d))
    s += [(22, 'S', 0, 3)]
    # torse : épaules arrondies, poitrine, taille marquée, hanches (pas de rectangle)
    tronc = {23: 6, 24: 8, 25: 9, 26: 9, 27: 9, 28: 9, 29: 9, 30: 8, 31: 8, 32: 7, 33: 7, 34: 7,
             35: 7, 36: 8, 37: 8, 38: 8}
    for y, d in tronc.items(): s.append((y, 'J', 0, d))
    # bras : haut du bras rond, coude, avant-bras qui s'écarte un peu, poignet plus fin
    bras = {24: (9, 11), 25: (10, 12), 26: (10, 13), 27: (10, 13), 28: (10, 13), 29: (10, 13),
            30: (10, 13), 31: (10, 13), 32: (10, 13), 33: (10, 13), 34: (11, 13), 35: (11, 14),
            36: (11, 14), 37: (11, 14), 38: (12, 14)}
    for y, (a, b) in bras.items(): s.append((y, 'A', a, b))
    main = {39: (12, 14), 40: (11, 15), 41: (11, 15), 42: (12, 15), 43: (12, 14)}
    for y, (a, b) in main.items(): s.append((y, 'K', a, b))
    for y, d in {23: 3, 24: 2, 25: 1, 26: 0}.items(): s.append((y, 'C', 0, d))
    s.append((38, 'B', 0, 8))
    for y in range(39, 47): s.append((y, 'N', 0 if y < 45 else 2, 9 if y < 44 else 8))
    jambe = {47: (2, 7), 48: (2, 7), 49: (2, 7), 50: (2, 6), 51: (2, 6), 52: (2, 7), 53: (2, 7),
             54: (2, 6), 55: (3, 5)}
    for y, (a, b) in jambe.items(): s.append((y, 'L', a, b))
    for y in (56, 57): s.append((y, 'X', 3, 6))
    for y, (a, b) in {58: (2, 6), 59: (1, 7), 60: (1, 7), 61: (1, 7)}.items(): s.append((y, 'R', a, b))
    return s

def zones():
    Z = [['.'] * W for _ in range(H)]
    for y, z, a, b in spans():
        for d in range(a, b + 1):
            Z[y][31 - d] = z; Z[y][32 + d] = z
    # frange en pointes (au-dessus du visage, asymétrique)
    bas = [11, 10, 11, 10, 10, 10, 9, 10]          # rangée la plus basse de la mèche, par d
    for d, yb in enumerate(bas):
        for y in range(9, yb + 1):
            Z[y][31 - d] = 'H'
        for y in range(9, [10, 11, 10, 10, 10, 9, 10, 10][d] + 1):
            Z[y][32 + d] = 'H'
    return Z

def ombrer(Z):
    G = [['.'] * W for _ in range(H)]
    dans = lambda x, y: 0 <= x < W and 0 <= y < H and Z[y][x] != '.'
    for y in range(H):
        x = 0
        while x < W:
            z = Z[y][x]
            if z == '.': x += 1; continue
            x1 = x
            while x1 + 1 < W and Z[y][x1 + 1] == z: x1 += 1
            n = x1 - x + 1
            for i in range(n):
                t = (i + .5) / n
                lim = (.55, .85) if z in 'SK' else (.28, .75)
                if z in 'AK' and x > 32: lim = (.0, .5)          # bras du côté ombre : plus sombre
                k = 0 if t < lim[0] else (1 if t < lim[1] else 2)
                G[y][x + i] = RAMPE[z][k]
            x = x1 + 1
    # ombres portées : sous la frange (1 rangée), sous le menton, sous les bras
    for y in range(H):
        for x in range(W):
            z = Z[y][x]
            if z == 'S' and y > 0 and Z[y - 1][x] == 'H': G[y][x] = '2'
            if z == 'S' and y == 22: G[y][x] = '3'
            if z == 'J' and y in (23,) : G[y][x] = 'q' if G[y][x] == 'r' else G[y][x]
            if z == 'J' and x + 1 < W and Z[y][x + 1] == 'A' or z == 'J' and Z[y][x - 1] == 'A': G[y][x] = 'p'
            if z == 'N' and Z[y - 1][x] in 'BJ': G[y][x] = 'm'
            if z == 'L' and Z[y - 1][x] == 'N': G[y][x] = '3'
    # contour extérieur
    for y in range(H):
        for x in range(W):
            if Z[y][x] == '.' and any(dans(x + dx, y + dy) for dx, dy in ((1, 0), (-1, 0), (0, 1), (0, -1))):
                G[y][x] = 'O'
    # lignes intérieures : cheveux contre peau → ombre des cheveux ; jambes entre elles → contour
    for y in range(H):
        for x in range(W):
            z = Z[y][x]
            if z == 'H' and any(Z[y + dy][x + dx] == 'S' for dx, dy in ((1, 0), (-1, 0))) and y > 11: G[y][x] = 'c'  # seulement les côtés
            if z == 'A' and any(Z[y + dy][x + dx] == 'J' for dx, dy in ((1, 0), (-1, 0))): G[y][x] = 'p' if x > 31 else 'q'
            if z == 'K' and Z[y - 1][x] == 'A': G[y][x] = '3'
            if z == 'H' and Z[y + 1][x] == 'Y': G[y][x] = 'c'
    return G

def retouches(G):
    def put(x, y, s):
        for i, c in enumerate(s): G[y][x + i] = c
    # yeux 5x4 (colonnes 25-29 et 34-38), cil au coin extérieur
    for x0, cil in ((25, 24), (34, 39)):
        put(x0, 13, 'OOOOO'); put(x0, 14, 'wWccw'); put(x0, 15, 'wbEbw'); put(x0, 16, '1aaa1')
        put(x0 + 1, 17, '222'); G[13][cil] = 'O'; G[14][cil] = 'O'
    G[18][32] = '2'; G[19][32] = '3'                      # nez en plan d'ombre
    put(31, 20, '3p')                                     # bouche
    # mèches et reflet cassé sur la calotte
    for x, y in ((24, 4), (25, 4), (26, 4), (27, 3), (28, 3), (22, 5), (23, 5), (30, 5), (31, 5), (32, 4), (33, 4)):
        if G[y][x] in 'bc': G[y][x] = 'a'
    for x, y in ((29, 4), (29, 5), (29, 6), (36, 3), (36, 4), (36, 5), (36, 6), (40, 9), (23, 10)):
        G[y][x] = 'c'
    put(30, 23, 'WWWW')
    for d in (12,):                                         # pli du pouce
        for y in (41, 42): G[y][31 - d] = '3'; G[y][32 + d] = '3'
    return G

def dessiner(etape=99):
    Z = zones()
    if etape == 1: return chaine([[c if c == '.' else '#' for c in r] for r in Z])
    if etape == 2:
        g = [['.' if c == '.' else {'H': 'b', 'S': '2', 'J': 'q', 'A': 'q', 'N': 'n', 'L': '2', 'R': 'q', 'Y': 'Y', 'C': 'W', 'K': '2', 'B': 'Y', 'X': 'W'}[c] for c in r] for r in Z]
        return chaine(g)
    G = ombrer(Z)
    if etape == 3: return chaine(G)
    return chaine(retouches(G))

G = dessiner()
