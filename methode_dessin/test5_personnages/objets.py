# Objets du test 5 : baie (8 et 16 px), lanterne (16, 32, 64 px).
# Lumière en haut à gauche pour la baie ; la lanterne est sa propre source (flamme au centre).
from base import *

PAL_O = {
    'O': (36, 22, 44),
    'v': (196, 150, 240), 'u': (128, 84, 206), 't': (74, 44, 136), 's': (44, 28, 90),   # baie, ombres vers le bleu
    'W': (250, 244, 255),
    'g': (132, 206, 92), 'G': (52, 128, 72),                                           # feuille
    'k': (176, 172, 190), 'j': (104, 98, 128), 'h': (58, 52, 80),                       # fer de la lanterne
    'Y': (255, 248, 196), 'y': (255, 214, 96), 'x': (240, 140, 52), 'z': (180, 72, 44), # lueur, du cœur au bord
    'e': (120, 70, 60),                                                                 # verre sombre (reflet chaud)
}

BAIE8 = [   # 8x8 : silhouette ronde + queue ; 4 tons, 1 px de reflet
"......g.",
"...OOgGO",
"..OvuuO.",
".OvWuutO",
".OvuuutO",
".OuuuttO",
"..OtttO.",
"...OOO..",
]

BAIE16 = [  # 16x16 : sphère légèrement aplatie, fossette sous la queue, feuille à gauche
"................",
"..........OO....",
"...OOO...OGO....",
"..OggGO.OGO.....",
"..OgggGOGOOO....",
"...OGGGOOuuuOO..",
"....OOOvvuuutsO.",
"...OvvWWvuuuttO.",
"..OvvWWvuuuuttsO",
"..OvvvvuuuuutttO",
"..OuvvuuuuutttsO",
"..OuuuuuuutttssO",
"...OuuuuttttssO.",
"...OtuuttttssOO.",
"....OOtttsssO...",
"......OOOOOO....",
]

LANT16 = [  # 16x16 : anneau, chapeau, cage de verre avec flamme, socle
".......OO.......",
"......OkjO......",
"......OjhO......",
".....OOOOOO.....",
"....OkkjjjhO....",
"...OkkkjjjjhO...",
"...OjOyyyxOhO...",
"...OjOyYYyOhO...",
"...OjOyYYxOhO...",
"...OjOxyyxOhO...",
"...OjOzxxzOhO...",
"...OkjjjjjjhO...",
"....OjjjjjhO....",
"....OOOOOOOO....",
"................",
"................",
]

def lanterne(S):
    """Lanterne 32 ou 64 px : même construction, détails selon la taille (B4b)."""
    u = S / 32; c = S / 2 - .5
    Z = [['.'] * S for _ in range(S)]
    def zone(x, y):
        d = abs(x - c) / u; v = (y + .5) / u
        if 1 <= v < 5.5:                                  # anneau
            r = ((d / 3.2) ** 2 + ((v - 3.3) / 2.2) ** 2) ** .5
            return 'M' if .5 < r <= 1 else None
        if 5.5 <= v < 10:                                 # chapeau en trapèze
            return 'M' if d <= 3.5 + (v - 5.5) * 1.25 else None
        if 10 <= v < 11.5: return 'M' if d <= 10 else None   # rebord haut
        if 11.5 <= v < 24: return 'M' if 7 < d <= 9 else ('V' if d <= 7 else None)
        if 24 <= v < 26: return 'M' if d <= 10 else None     # rebord bas
        if 26 <= v < 29.5: return 'M' if d <= 8 - (v - 26) * .4 else None
        return None
    for y in range(S):
        for x in range(S):
            z = zone(x, y)
            if z: Z[y][x] = z
    G = [['.'] * S for _ in range(S)]
    fy = 18.5 * u; fx = c
    for y in range(S):
        for x in range(S):
            z = Z[y][x]
            if z == 'V':                                  # lueur radiale autour de la flamme
                r = (((x - fx) / (6.5 * u)) ** 2 + ((y - fy) / (8 * u)) ** 2) ** .5
                if S >= 64 and (x + y) % 2:              # grand format : bords de halo tramés (évite les anneaux réguliers)
                    r += .05
                G[y][x] = 'Y' if r < .22 else 'y' if r < .5 else 'x' if r < .83 else 'z' if r < 1.1 else 'e'
            elif z == 'M':
                # cylindre de métal : lumière à gauche
                xs = [i for i in range(S) if Z[y][i] == 'M']
                x0, x1 = min(xs), max(xs); t = (x - x0 + .5) / (x1 - x0 + 1)
                G[y][x] = 'k' if t < .3 else 'j' if t < .72 else 'h'
    # flamme en goutte, cœur clair
    for y in range(S):
        for x in range(S):
            if Z[y][x] != 'V': continue
            dy = (y + .5 - (fy + 2 * u)) / (5 * u); dx = (x - fx) / (2.2 * u)
            if -1 < dy < .5:
                w = (1 - (-dy)) ** .8 if dy < 0 else (1 - (dy / .5) ** 2) ** .5
                if abs(dx) < w: G[y][x] = 'W' if abs(dx) < w * (.3 if S >= 64 else .45) and dy > -.6 else 'Y'
    # métal éclairé par la flamme : bord intérieur des montants en ton chaud
    for y in range(S):
        for x in range(S):
            if Z[y][x] == 'M' and any(0 <= x + dx < S and Z[y][x + dx] == 'V' for dx in (-1, 1)):
                G[y][x] = 'x'
    # contour extérieur
    for y in range(S):
        for x in range(S):
            if Z[y][x] == '.' and any(0 <= x + dx < S and 0 <= y + dy < S and Z[y + dy][x + dx] != '.'
                                      for dx, dy in ((1, 0), (-1, 0), (0, 1), (0, -1))):
                G[y][x] = 'O'
    # lignes de séparation entre pièces (chapeau / rebord / cage / socle)
    for v in (10, 11.5, 24, 26):
        y = int(v * u)
        for x in range(S):
            if Z[y][x] == 'M' and Z[y - 1][x] == 'M': G[y - 1][x] = 'h' if G[y - 1][x] != 'O' else 'O'
    if S >= 64:
        # détails réservés au grand format : rivets, reflet sur le verre, arête du chapeau
        for v in (12.5, 22.5):
            y = int(v * u)
            for xx in (int(c - 8 * u), int(c + 8 * u) + 1):
                G[y][xx] = 'k'; G[y + 1][xx] = 'h'
        for i in range(int(5 * u)):
            x = int(c - 5.5 * u) + i // 3; y = int(13 * u) + i
            if Z[y][x] == 'V' and G[y][x] in 'ez': G[y][x] = 'x'
        for v in range(int(6 * u), int(10 * u)):
            G[v][int(c - 1)] = 'k'
    return chaine(G)

LANT32 = lanterne(32); LANT64 = lanterne(64)
