"""Coins de coffre (v2, remplacent les bossettes). Pièce 16×16.

Le coin haut-gauche est dessiné à la main en ÉTIQUETTES de surface :
  O trait · T biseau tourné vers le haut · L vers la gauche · R vers la droite ·
  B vers le bas · F face plate · . vide
Les trois autres coins = miroir de la géométrie ; la lumière reste en haut-gauche,
donc un miroir horizontal échange L↔R et un miroir vertical échange T↔B (règle décidée,
pas une ombre calculée). Ensuite : étiquette → couleur, puis on pose à la main le dôme,
les gorges gravées et l'ombre portée du dôme, coin par coin.
"""
import sys

# bras du haut, colonnes 10..15, rangées 0..7 (dessiné à la main) : lobe arrondi au bout
BRAS = [
    "OOOO..",
    "TTTTO.",
    "FFFFRO",
    "FFFFRO",
    "FFFFRO",
    "FFFBRO",
    "BBBBO.",
    "OOOO..",
]
# carré du coin 10×10 (assise du dôme) : chanfrein extérieur, coin intérieur arrondi
CARRE = [
    "..OOOOOOOO",
    ".OTTTTTTTT",
    "OLFFFFFFFF",
    "OLFFFFFFFF",
    "OLFFFFFFFF",
    "OLFFFFFFFF",
    "OLFFFFFFFF",
    "OLFFFFFFFR",
    "OLFFFFFFBO",
    "OLFFFFFBO.",
]
TRANS = {'T': 'L', 'L': 'T', 'R': 'B', 'B': 'R'}   # bras gauche = bras du haut transposé


def coin_hg():
    G = [['.'] * 16 for _ in range(16)]
    for y in range(10):
        for x in range(10):
            G[y][x] = CARRE[y][x]
    for y in range(8):
        for x in range(6):
            G[y][x + 10] = BRAS[y][x]
            G[x + 10][y] = TRANS.get(BRAS[y][x], BRAS[y][x])
    return G


def miroir(G, h, v):
    swap = {}
    if h: swap.update({'L': 'R', 'R': 'L'})
    if v: swap.update({'T': 'B', 'B': 'T'})
    H = [r[::-1] if h else r[:] for r in G]
    if v: H = H[::-1]
    return [[swap.get(c, c) for c in r] for r in H]


COUL = {'T': 'y', 'L': 'y', 'F': 'j', 'R': 'i', 'B': 'h'}

# dôme 7×7, éclairé en haut-gauche (dessiné à la main, identique aux 4 coins)
DOME = [
    "..OOO..",
    ".OzyyO.",
    "OzzyyjO",
    "OyyyjiO",
    "OyjjiiO",
    ".OiihO.",
    "..OOO..",
]

# par coin : (miroir h, miroir v, position du dôme, gorges, ombre portée du dôme)
# gorge = trait sombre h + arête claire y du côté qui regarde la lumière (à droite / dessous)
COINS = {
    'hg': (False, False, (2, 2),
           [('h', 11, 2, 11, 5), ('y', 12, 2, 12, 5), ('h', 2, 11, 5, 11), ('y', 2, 12, 5, 12)],
           [(9, 4), (9, 5), (9, 6), (4, 9), (5, 9), (6, 9)]),
    'hd': (True, False, (7, 2),
           [('h', 3, 2, 3, 5), ('y', 4, 2, 4, 5), ('h', 10, 11, 13, 11), ('y', 10, 12, 13, 12)],
           [(9, 9), (10, 9), (11, 9)]),
    'bg': (False, True, (2, 7),
           [('h', 11, 10, 11, 13), ('y', 12, 10, 12, 13), ('h', 2, 3, 5, 3), ('y', 2, 4, 5, 4)],
           [(9, 9), (9, 10), (9, 11)]),
    'bd': (True, True, (7, 7),
           [('h', 3, 10, 3, 13), ('y', 4, 10, 4, 13), ('h', 10, 3, 13, 3), ('y', 10, 4, 13, 4)],
           []),
}

for nom, (h, v, (dx, dy), gorges, ombre) in COINS.items():
    G = [[COUL.get(c, c) for c in r] for r in miroir(coin_hg(), h, v)]
    for c, x1, y1, x2, y2 in gorges:
        for y in range(y1, y2 + 1):
            for x in range(x1, x2 + 1):
                G[y][x] = c
    for x, y in ombre:
        G[y][x] = 'i'
    for y, r in enumerate(DOME):
        for x, c in enumerate(r):
            if c != '.': G[dy + y][dx + x] = c
    open(f'pieces/coin_{nom}.txt', 'w').write('\n'.join(''.join(r) for r in G) + '\n')
    print(nom); print('\n'.join(''.join(r) for r in G))
