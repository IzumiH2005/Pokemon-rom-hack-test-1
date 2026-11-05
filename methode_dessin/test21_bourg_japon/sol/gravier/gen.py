"""Gravier ratisse : chaque etape ecrit sa grille ; toutes les valeurs sont mes decisions (R3).
c01 forme : marge 3 sans onde (bordure droite = jardin taille), coins rayon 3.5
c02 aplats : bande de 3 px de pierres m contre l'herbe, gravier f
c03 lumiere : sillons de rateau horizontaux periode 4 (j creux, e crete) ; pierres : f en haut, l en bas
c04 contour : joints de pierres n tous les 4 px le long du bord, rang exterieur n
c05 details : quelques grains l dans le gravier (hors coutures)
"""
import math
MARGE, R = 3, 3.5
ONDE16 = [0] * 16   # R5 : l'onde en marches faisait des planches -> sillons droits
def forme(n, x, y, interieur):
    if interieur:
        return (x + .5 - 16) ** 2 + (y + .5 - 16) ** 2 > R ** 2
    cx = x < 8 or x >= 40; cy = y < 8 or y >= 40
    if cx and cy:
        ox = 8 if x < 8 else 40; oy = 8 if y < 8 else 40
        return (x + .5 - ox) ** 2 + (y + .5 - oy) ** 2 <= (8 - MARGE) ** 2 + .3
    return min(x, y, 47 - x, 47 - y) >= MARGE
def dist(G):
    H, W = len(G), len(G[0]); D = [[99] * W for _ in range(H)]
    fr = [(x, y) for y in range(H) for x in range(W) if G[y][x] == '.']
    for x, y in fr: D[y][x] = 0
    while fr:
        nf = []
        for x, y in fr:
            for dx, dy in ((1,0),(-1,0),(0,1),(0,-1)):
                a, b = x + dx, y + dy
                if 0 <= a < W and 0 <= b < H and D[b][a] > D[y][x] + 1:
                    D[b][a] = D[y][x] + 1; nf.append((a, b))
        fr = nf
    return D
def save(G, p): open(p, 'w').write('\n'.join(''.join(r) for r in G) + '\n')
for nom, n, intr in (('', 48, False), ('i', 32, True)):
    G = [['1' if forme(n, x, y, intr) else '.' for x in range(n)] for y in range(n)]; save(G, f'gravier/e01{nom}.txt')
    D = dist(G)
    G = [['.' if c == '.' else ('m' if D[y][x] <= 4 else 'f') for x, c in enumerate(r)] for y, r in enumerate(G)]
    save(G, f'gravier/e02{nom}.txt')
    for y in range(n):
        for x in range(n):
            if G[y][x] == 'f':
                w = ONDE16[x % 16]  # R5 : sillons droits = tole ondulee
                G[y][x] = 'j' if (y + w) % 4 == 0 else 'e' if (y + w) % 4 == 1 else 'f'
            elif G[y][x] == 'm':
                # face de la pierre : dessus eclaire (rang le plus proche du haut de la pierre)
                up = y > 0 and G[y-1][x] in '.'; dn = y < n - 1 and (G[y+1][x] in '.efj' or D[y][x] == 3)
                if D[y][x] == 1 and not dn: pass
                G[y][x] = {1: 'f', 2: 'm', 3: 'm', 4: 'l'}[D[y][x]]
    save(G, f'gravier/e03{nom}.txt')
    for y in range(n):
        for x in range(n):
            if G[y][x] in 'fml' and D[y][x] <= 4:
                vert = (x < 8 or x >= n - 8) and not (y < 8 or y >= n - 8)
                pos = y if vert else x
                if intr: pos = x + y
                # R5 : pierres de 4 px = corde pointillee -> pierres de 8 px, coins arrondis
                p = pos % 8
                if p == 0: G[y][x] = {1: '.', 2: 'n', 3: 'n', 4: 'j'}[D[y][x]]
                elif p in (1, 7) and D[y][x] in (1, 4): G[y][x] = 'n' if D[y][x] == 1 else 'l'
    save(G, f'gravier/e04{nom}.txt')
    grains = [(20, 18), (27, 22), (18, 26), (29, 29), (22, 13), (12, 21), (36, 27), (21, 37)] if not intr else [(5, 22), (22, 5), (26, 26)]
    for x, y in grains:
        if G[y][x] in 'ef': G[y][x] = 'l'
    save(G, f'gravier/gravier{nom}.txt' if nom == '' else 'gravier/gravier_int.txt')
