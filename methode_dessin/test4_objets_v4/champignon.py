# Champignon 64x64 (objet posé au sol, vue un peu de dessus, comme le coffre du test 3).
# Largeur impaire centrée sur x = 32. Lumière en haut à gauche.
# Rapports décidés : chapeau = 51 px de large (≈ 4/5 de la case) ; pied = 15 px (≈ 0,3 x chapeau) ;
# hauteur du chapeau ≈ 0,55 x sa largeur ; anneau au tiers haut du pied.
from outils import *

PAL = {
    'O': (44, 12, 38), 'x': (104, 26, 52),                  # contour du chapeau (x = côté lumière)
    'a': (76, 16, 48), 'b': (132, 24, 52), 'c': (188, 40, 54), 'd': (228, 86, 64), 'e': (250, 152, 108),  # rouge
    'f': (196, 138, 136), 'h': (222, 188, 168), 'i': (252, 242, 216),                                     # taches
    'U': (62, 38, 58), 'k': (118, 90, 100), 'l': (168, 140, 134), 'm': (214, 196, 172), 'n': (244, 234, 208),  # pied
    '1': (22, 54, 52), '2': (44, 98, 60), '3': (100, 150, 64), '4': (170, 198, 92),                       # herbe
    'S': (24, 18, 44, 120),                                                                                 # ombre au sol
}

def dans_ell(x, y, cx, cy, rx, ry):
    return ((x - cx) / rx) ** 2 + ((y - cy) / ry) ** 2 <= 1

# ---------- étape 2 : volumes (données) ----------
CHAPEAU_DOME = (32, 31, 25.5, 22.6)     # demi-ellipse du haut
CHAPEAU_BORD = (32, 31, 25.5, 5.6)     # ellipse du bord (vue un peu de dessus)
PIED = [(y, 24 + (1 if 40 <= y <= 46 else 0), 40 - (1 if 40 <= y <= 46 else 0)) for y in range(33, 52)]  # légère taille
ANNEAU = [(38, 22, 42), (39, 21, 43), (40, 21, 43), (41, 22, 42)]   # jupe qui pend
BULBE = (32, 51, 10.5, 4.6)
OMBRE = (35, 55, 23, 4.2)
BEBE_CHAPEAU = (51, 47.5, 6.5, 5.4)      # petit champignon : raconte (il pousse à côté)
BEBE_BORD = (51, 47.5, 6.5, 1.6)
BEBE_PIED = [(y, 49, 53) for y in range(48, 55)]

def masques():
    M = {k: set() for k in ('ombre', 'pied', 'anneau', 'bebe', 'chapeau')}
    for y in range(64):
        for x in range(64):
            if dans_ell(x, y, *OMBRE): M['ombre'].add((x, y))
            if (y <= CHAPEAU_DOME[1] and dans_ell(x, y, *CHAPEAU_DOME)) or dans_ell(x, y, *CHAPEAU_BORD):
                M['chapeau'].add((x, y))
            if dans_ell(x, y, *BULBE): M['pied'].add((x, y))
            if (y <= BEBE_CHAPEAU[1] and dans_ell(x, y, *BEBE_CHAPEAU)) or dans_ell(x, y, *BEBE_BORD):
                M['bebe'].add((x, y))
    for y, x0, x1 in PIED:
        for x in range(x0, x1 + 1): M['pied'].add((x, y))
    for y, x0, x1 in ANNEAU:
        for x in range(x0, x1 + 1): M['anneau'].add((x, y))
    for y, x0, x1 in BEBE_PIED:
        for x in range(x0, x1 + 1): M['bebe'].add((x, y))
    return M

# ---------- étape 8 : zones de lumière (formes décidées en données) ----------
# Chapeau : éclat, lumière, demi-teinte (1 ton de transition : volume rond), ombre.
CH_ECLAT = (20, 15, 5.2, 2.5)
CH_LUM = (25, 19, 16.5, 12.5)
CH_DEMI = (28, 22, 22.5, 17)
# Taches : (cx, cy, rx, ry), plus petites et aplaties vers les bords (elles suivent le dôme).
TACHES = [(20, 18, 3.4, 2.4), (34, 13, 2.6, 1.7), (43, 21, 3.2, 2.6), (29, 25, 2.2, 1.6),
          (12, 28, 1.6, 2.2), (51, 30, 1.4, 2.0), (39, 31, 2.0, 1.2)]
OMBRE_SOUS_CHAPEAU = (34, 33.5, 25.5, 5.6)   # le bord du chapeau, décalé en bas à droite
BEBE_LUM = (49, 45, 4.5, 2.6)
BEBE_TACHES = [(49, 45, 1.2, 0.8), (54, 46, 0.9, 0.7)]

def bord_interieur(S, devant=frozenset()):
    """Pixels de S qui touchent (par un côté) le vide ou une partie située derrière.
    Contre une partie située devant, rien : c'est elle qui pose son propre contour."""
    res = set()
    for (x, y) in S:
        for dx, dy in ((1, 0), (-1, 0), (0, 1), (0, -1)):
            p = (x + dx, y + dy)
            if p not in S and p not in devant: res.add((x, y)); break
    # retrait des angles en L : le pixel d'angle sort du contour ; s'il touche le vide,
    # il sort aussi de la forme (sinon il resterait un pixel de remplissage hors du contour).
    efface = set()
    for (x, y) in sorted(res):
        for dx, dy in ((1, 1), (1, -1), (-1, 1), (-1, -1)):
            if (x + dx, y) in res and (x, y + dy) in res and (x - dx, y) not in res and (x, y - dy) not in res \
               and (x + dx, y + dy) not in res:
                res.discard((x, y))
                if (x - dx, y) not in S or (x, y - dy) not in S: efface.add((x, y))
                break
    S -= efface
    return res

# Touffes d'herbe dessinées pixel par pixel. Chaque brin : liste de (x, y) du pied vers la pointe.
# Brins de longueurs différentes, par groupes de 3, qui penchent vers l'extérieur.
TOUFFES = [
    [(20, 56), (19, 55), (19, 54), (18, 53), (18, 52), (17, 51), (16, 50)],
    [(21, 56), (21, 55), (21, 54), (21, 53), (22, 52), (22, 51)],
    [(22, 56), (23, 55), (24, 54), (24, 53)],
    [(19, 56), (18, 56), (17, 55), (16, 55), (15, 54)],
    [(43, 56), (43, 55), (44, 54), (44, 53), (45, 52), (45, 51)],
    [(42, 56), (42, 55), (41, 54), (41, 53)],
    [(44, 56), (45, 55), (46, 55), (47, 54)],
    [(56, 56), (57, 55), (57, 54), (58, 53), (58, 52)],
    [(55, 56), (55, 55), (54, 54)],
]
EPAISSEUR = [(20, 55), (21, 52), (19, 53), (43, 54), (42, 54), (57, 56)]  # bas des brins un peu plus épais

def dessiner(etape=99):
    M = masques()
    g = grille_vide(64, 64)
    pose = lambda S, c: [g[y].__setitem__(x, c) for (x, y) in S]
    # étape 5 : silhouette
    if etape == 5:
        for k in ('pied', 'anneau', 'bebe', 'chapeau'): pose(M[k], 'O')
        return chaine(g)
    pose(M['ombre'], 'S')
    # --- pied (cylindre : lumière à gauche) ---
    for (x, y) in M['pied']:
        c = 'n' if x <= 27 else 'm' if x <= 33 else 'l' if x <= 37 else 'k'
        if y >= 53: c = {'n': 'm', 'm': 'l', 'l': 'k', 'k': 'k'}[c]      # bas du bulbe tourné vers le sol
        if etape >= 8 and dans_ell(x, y, *OMBRE_SOUS_CHAPEAU): c = 'k' if x >= 30 else 'l'
        if etape >= 8 and y in (42, 43) and 23 <= x <= 41: c = 'l' if x <= 30 else 'k'  # ombre de l'anneau
        g[y][x] = c if etape >= 8 else 'm'
    for (x, y) in M['anneau']:
        c = 'm' if x <= 30 else 'l' if x <= 37 else 'k'
        if y == 41: c = 'l' if x <= 30 else 'k'
        if y == 38 and x <= 34: c = 'n'
        g[y][x] = c if etape >= 8 else 'l'
    # --- petit champignon ---
    for (x, y) in M['bebe']:
        if y <= 48:
            c = 'd' if dans_ell(x, y, *BEBE_LUM) else 'c' if x <= 53 else 'b'
            if y == 48: c = 'b'
        else:
            c = 'm' if x <= 50 else 'l'
            if y == 49: c = 'k'
        g[y][x] = c if etape >= 8 else ('c' if y <= 48 else 'm')
    # --- chapeau ---
    for (x, y) in M['chapeau']:
        if etape < 8: c = 'c'
        elif y > 31 and not dans_ell(x, y, *CHAPEAU_DOME): c = 'a' if y >= 35 else 'b'   # dessous du bord
        elif dans_ell(x, y, *CH_ECLAT): c = 'e'
        elif dans_ell(x, y, *CH_LUM): c = 'd'
        elif dans_ell(x, y, *CH_DEMI): c = 'c'
        else: c = 'b'
        g[y][x] = c
    if etape >= 9:
        for cx, cy, rx, ry in TACHES:
            for (x, y) in M['chapeau']:
                if dans_ell(x, y, cx, cy, rx, ry):
                    fond = g[y][x]
                    c = {'e': 'i', 'd': 'i', 'c': 'h', 'b': 'f', 'a': 'f'}[fond]
                    if not dans_ell(x - 1, y - 1, cx, cy, rx, ry):   # pas de pixel en haut à gauche : bord éclairé
                        pass
                    elif not dans_ell(x + 1, y + 1, cx, cy, rx, ry): # bord bas-droit : épaisseur, 1 ton plus sombre
                        c = {'i': 'h', 'h': 'f', 'f': 'f'}[c]
                    g[y][x] = c
        for cx, cy, rx, ry in BEBE_TACHES:
            for (x, y) in M['bebe']:
                if y <= 47 and dans_ell(x, y, cx, cy, rx, ry): g[y][x] = 'i' if x < 52 else 'h'
        for t in TOUFFES:
            for i, (x, y) in enumerate(t):
                g[y][x] = '1' if i == 0 else '2' if i < len(t) // 2 else '3' if i < len(t) - 1 else '4'
        for (x, y) in EPAISSEUR: g[y][x] = '2'
        # fibres du pied : petits tirets verticaux par 2 ou 3, longueurs variées, dans les tons moyens
        for (x, y) in [(26, 45), (26, 46), (29, 48), (29, 49), (29, 50), (27, 51), (27, 52)]:
            g[y][x] = 'm'
        for (x, y) in [(35, 45), (35, 46), (35, 47), (37, 50), (37, 51)]:
            g[y][x] = 'k'
    # --- étape 6 : contours (bord intérieur de chaque partie, devant en dernier) ---
    if etape >= 6:
        for (x, y) in bord_interieur(M['pied'], M['anneau'] | M['chapeau'] | M['bebe']):
            g[y][x] = 'k' if y >= 54 else 'U'                     # pas de contour noir au contact du sol
        for (x, y) in bord_interieur(M['anneau'], M['chapeau']):
            voisins = [(x + dx, y + dy) for dx, dy in ((1, 0), (-1, 0), (0, 1), (0, -1))]
            vide = [p for p in voisins if not any(p in M[k] for k in ('pied', 'anneau', 'chapeau'))]
            if vide: g[y][x] = 'U'
            elif (x, y + 1) in M['pied'] and (x, y + 1) not in M['anneau']: g[y][x] = 'k'   # ombre sous l'anneau
        for (x, y) in bord_interieur(M['bebe']):
            g[y][x] = 'O' if y <= 48 else 'U'
        for (x, y) in bord_interieur(M['chapeau']):
            g[y][x] = 'x' if (x + y < 52 and y < 30) else 'O'      # selout : plus clair en haut à gauche
    tout = set().union(*(M[k] for k in ('pied', 'anneau', 'bebe', 'chapeau', 'ombre')))
    for y in range(64):
        for x in range(64):
            if (x, y) not in tout and g[y][x] not in '1234': g[y][x] = '.'
    return chaine(g)

if __name__ == '__main__':
    import sys
    e = int(sys.argv[1]) if len(sys.argv) > 1 else 99
    vue(dessiner(e), PAL, 'champi_e%d.png' % e, k=8)
