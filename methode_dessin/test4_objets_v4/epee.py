# Épée 32x32 (icône d'inventaire), sur la diagonale : pointe en haut à droite.
# Repère : a = x + y (travers de la lame), b = x - y (le long de la lame). Axe : a = 30,5.
# La lumière vient du haut à gauche, donc du côté des petits a.
# Rapports décidés : poignée + pommeau ≈ 1/4 de la longueur totale ; garde ≈ 1,6 x la poignée.
from outils import *

PAL = {
    'O': (24, 20, 38), 'o': (62, 64, 98),                          # contour (o = selout côté lumière)
    '1': (38, 46, 76), '2': (80, 96, 132), '3': (138, 158, 186),   # acier
    '4': (200, 212, 224), 'W': (246, 250, 242),
    'p': (110, 52, 34), 'q': (182, 106, 36), 'r': (232, 170, 52), 't': (252, 230, 130),  # or
    'k': (52, 26, 34), 'l': (96, 50, 42), 'm': (146, 86, 56),      # cuir
    'g': (106, 12, 44), 'h': (206, 30, 56), 'j': (255, 140, 120),  # gemme rouge (accent)
}

AXE = 30.5
# Bords de la lame (a mini, a maxi) selon b : la pointe se resserre sur 6 pas.
def bords_lame(b):
    if b < -9 or b > 24: return None
    if b <= 19: return (29, 32)
    if b <= 21: return (29, 31)
    if b <= 23: return (30, 31)
    return (30, 30)
B_GARDE = (-12, -10)            # 3 pas d'épaisseur : la garde est exagérée (forme iconique)
DEMI_GARDE = 6.5
B_POIG = (-20, -13)
POMMEAU = (4, 27)

def construire():
    """Carte des matières (sans contour), avec la position (a, b) de chaque pixel."""
    m = {}
    for y in range(32):
        for x in range(32):
            a, b = x + y, x - y
            bl = bords_lame(b)
            if bl and bl[0] <= a <= bl[1] and b >= -9: m[(x, y)] = 'lame'
            if B_GARDE[0] <= b <= B_GARDE[1] and abs(a - AXE) <= DEMI_GARDE: m[(x, y)] = 'garde'
            if B_GARDE[0] - 1 <= b <= B_GARDE[1] + 1 and 5.5 <= abs(a - AXE) <= DEMI_GARDE: m[(x, y)] = 'garde'  # bouts renflés
            if B_POIG[0] <= b <= B_POIG[1] and 30 <= a <= 31: m[(x, y)] = 'poignee'
    cx, cy = POMMEAU
    for y in range(cy - 2, cy + 3):
        for x in range(cx - 2, cx + 3):
            if (x - cx) ** 2 + (y - cy) ** 2 <= 2: m[(x, y)] = 'pommeau'
    return m

def contour(m):
    """Contour = pixels hors forme qui touchent la forme par un côté ; puis retrait des angles en L."""
    c = set()
    for (x, y) in m:
        for dx, dy in ((1, 0), (-1, 0), (0, 1), (0, -1)):
            p = (x + dx, y + dy)
            if p not in m: c.add(p)
    return c

# Zones de lumière (décidées) : lame = biseau clair | arête | face sombre | reflet du bord.
TON_LAME = {29: '3', 30: '4', 31: '1', 32: '2'}

def colorer(m):
    g = grille_vide(32, 32)
    for (x, y), v in m.items():
        a, b = x + y, x - y
        if v == 'lame': c = TON_LAME[a]
        elif v == 'garde':
            # face haute (vers la lame) un peu éclairée, face basse dans l'ombre ;
            # le bout en haut à gauche est plus proche de la lumière que l'autre bout.
            rampe = 'pqrt'
            i = {-9: 2, -10: 2, -11: 1, -12: 0, -13: 0}[b]
            if a <= 26: i += 1
            if a >= 35: i -= 1
            c = rampe[max(0, min(3, i))]
        elif v == 'poignee':
            c = ('m' if a == 30 else 'l') if (b // 2) % 2 == 0 else ('l' if a == 30 else 'k')
        else: c = 'q'
        g[y][x] = c
    for (x, y) in contour(m):
        # selout : contour plus clair sur les bords tournés vers la lumière (au-dessus/à gauche de la forme)
        g[y][x] = 'o' if ((x + 1, y) in m or (x, y + 1) in m) and m.get((x + 1, y), m.get((x, y + 1))) == 'lame' else 'O'
    RETOUCHES = {
        # éclats nets sur l'arête claire (2 tirets de longueur différente)
        (22, 8): 'W', (23, 7): 'W', (24, 6): 'W', (16, 14): 'W', (17, 13): 'W',
        # reflet de l'environnement sur la face sombre, vers la pointe
        (25, 6): '3', (26, 5): '3',
        # gemme du centre de garde (accent) : clair en haut à gauche, ombre en bas à droite
        (9, 20): 'j', (10, 20): 'h', (9, 21): 'h', (10, 21): 'g',
        # pommeau rond éclairé en haut à gauche
        (3, 26): 't', (4, 26): 'r', (3, 27): 'r', (4, 27): 'q', (5, 26): 'q',
        (9, 18): 'r', (8, 20): 'q', (10, 22): 'q', (9, 22): 'l', (8, 22): 'm',
        (3, 28): 'q', (4, 28): 'p', (5, 28): 'p', (5, 27): 'p',
    }
    for (x, y), c in RETOUCHES.items(): g[y][x] = c
    return chaine(g)

if __name__ == '__main__':
    m = construire()
    G = colorer(m)
    vue(G, PAL, 'epee_v6.png', k=14)
    print(angles_L(G, 'Oo'))
    for i, r in enumerate(G): print('%2d' % i, r)
