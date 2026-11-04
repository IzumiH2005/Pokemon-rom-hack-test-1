# Lina, portrait anime de 3/4, construit en courbes puis passé en pixels (méthode C11).
import numpy as np
from vec import *
from tete import Tete

# 15 couleurs + transparent (GBA). Rampes avec décalage de teinte : ombres vers le violet,
# lumières vers le jaune ; le contour est un violet-marine, pas du noir.
PAL = {
 'O': (30, 26, 56),                                                   # contour, pupille
 'A': (196, 240, 222), 'B': (98, 188, 188), 'C': (54, 128, 158), 'D': (36, 72, 116),   # cheveux
 '1': (255, 236, 218), '2': (250, 204, 178), '3': (230, 146, 146), '4': (150, 66, 96),  # peau ; 4 = trait chaud
 'k': (244, 120, 128),                                                # joues
 'j': (222, 116, 56), 'Y': (252, 204, 92),                            # iris (et bandeau)
 'W': (234, 242, 248),                                                # blanc bleuté
 'r': (250, 142, 82), 'q': (212, 76, 66),                             # veste ; ombre = 4
}
TETE = (52, 37, 27)       # sphère qui sert à la lumière des cheveux (unités)
LOOMIS = Tete(51, 39, 20, lacet=28, tangage=5, roulis=-5)   # la tête construite (C12)

def construire(S):
    k = S / 100
    lab = np.full((S, S), '.', dtype='<U8'); val = np.zeros((S, S))
    ys, xs = np.mgrid[0:S, 0:S]; X = (xs + .5) / k; Y = (ys + .5) / k
    cx, cy, R = TETE
    nx, ny = (X - cx) / R, (Y - cy) / R
    lumiere = -.55 * nx - .75 * ny                     # lumière en haut à gauche, sur la sphère
    def poser(M, nom, v):
        lab[M] = nom; val[M] = v[M] if isinstance(v, np.ndarray) else v

    dos = chemin((21, 42), ((21, 14), (46, 5), (68, 9)), ((88, 15), (90, 40), (86, 60)),
                 (88, 72), (80, 67), (72, 66), (32, 66), (24, 70), (20, 62), ((19, 55), (20, 48), (21, 42)))
    poser(masque(dos, S), 'dos', lumiere - .5)
    veste = chemin((4, 100), ((7, 86), (20, 77), (36, 74)), (50, 77), (63, 71), ((76, 73), (90, 80), (96, 100)))
    poser(masque(veste, S), 'veste', 1.1 - np.hypot(X - 20, (Y - 80) * 1.3) / 34)
    poser(masque(LOOMIS.cou(77), S), 'cou', 0)
    col = chemin((39, 74), (51, 90), (65, 69), (60, 68), (51, 82), (45, 73))
    poser(masque(col, S), 'col', 0)
    poser(masque(LOOMIS.oreille(1), S), 'oreille', 0)
    visage = masque(LOOMIS.contour(), S)
    poser(visage, 'peau', 0)
    poser(visage & masque(LOOMIS.plan_cote(1), S), 'peau', 1)    # val 1 = plan de côté
    calotte = ((X - cx) / 26.5) ** 2 + ((Y - 35) / 25) ** 2 <= 1
    poser(calotte & (Y < 33), 'cal', lumiere)
    meches = [   # (racine, ctrl, ctrl, pointe, largeur) : côtés puis frange, de l'arrière vers l'avant
        ((31, 32), (23, 46), (25, 60), (33, 71), 10), ((73, 30), (83, 44), (85, 58), (82, 71), 9),
        ((69, 32), (77, 47), (75, 62), (66, 72), 11),
        ((47, 21), (39, 23), (31, 30), (27, 41), 9), ((70, 22), (74, 32), (74, 40), (71, 47), 8),
        ((64, 20), (67, 30), (66, 38), (63, 43), 8), ((55, 20), (48, 26), (40, 33), (33, 42), 10),
        ((59, 20), (58, 30), (56, 38), (52, 45), 8), ((53, 21), (50, 31), (47, 40), (45, 51), 7),
        ((56, 14), (57, 5), (65, 2), (68, 8), 3),
        ((50, 23), (44, 34), (41, 44), (40, 53), 2.6),          # mèche fine qui traverse le visage
    ]
    if S < 96: meches = meches[:-1]                    # la mèche fine ne se lit qu'en grand
    for i, (a, b, c, d, w) in enumerate(meches):
        M, T, Sd = meche(a, b, c, d, w, S)
        poser(M, 'm%d' % i, lumiere + .45 * Sd - .1 * T + .4)
        if w >= 9:                                     # grande mèche : un pli sombre la partage
            pli = M & (np.abs(Sd + .15) < .5 / (w * k * .5) + .08) & (T > .15) & (T < .85)
            lab[pli] = 'pli'
    bande, Tb, Sb = meche((25, 33), (35, 15), (62, 9), (78, 25), 3.6, S, forme=0)
    poser(bande, 'band', Sb)
    return lab, val, X, Y, nx, ny

def ombrer(lab, val, X, Y, nx, ny, S):
    k = S / 100
    G = np.full((S, S), '.', dtype='<U1')
    est_ch = np.char.startswith(lab, 'm') | (lab == 'cal') | (lab == 'dos') | (lab == 'pli')
    # cheveux : 3 tons par la forme, puis reflet en anneau cassé
    G[est_ch] = np.where(val[est_ch] > .45, 'B', np.where(val[est_ch] > -.42, 'C', 'D'))
    r = np.hypot(nx, ny)
    anneau = est_ch & (lab != 'dos') & (lab != 'pli') & (r > .62) & (r < .62 + 1.6 / (TETE[2] * k) + .03) & (ny < -.1) & (nx < .3) & (val > .3)
    G[anneau] = 'A'
    G[lab == 'band'] = np.where(val[lab == 'band'] < .45, 'Y', 'j')
    G[lab == 'pli'] = 'D'
    peau = lab == 'peau'
    G[peau] = '1'
    G[lab == 'cou'] = '2'
    G[lab == 'col'] = 'W'
    v = lab == 'veste'
    G[v] = np.where(val[v] > .55, 'r', np.where(val[v] > -.45, 'q', '4'))
    # ombres portées (lumière en haut à gauche → l'ombre tombe en bas à droite)
    def voisin(dx, dy):
        Z = np.full_like(lab, '.'); 
        Z[max(dy,0):S+min(dy,0), max(dx,0):S+min(dx,0)] = lab[max(-dy,0):S+min(-dy,0), max(-dx,0):S+min(-dx,0)]
        return Z
    sous = np.zeros((S, S), bool)
    for d in range(1, max(2, round(2.2 * k)) + 1):
        Z = voisin(round(d * .5), d); sous |= np.char.startswith(Z, 'm') | (Z == 'band')
    G[peau & sous] = '2'
    G[peau & (val > .5)] = '2'                               # plan de côté (Loomis) à l'ombre
    G[lab == 'oreille'] = '2'
    menton = np.zeros((S, S), bool)
    for d in range(1, round(4 * k) + 1): menton |= voisin(0, d) == 'peau'
    G[(lab == 'cou') & menton] = '3'
    G[(lab == 'veste') & (voisin(0, -1) != 'veste') & (voisin(0, -1) != '.')] = '4'   # ombre du col
    # traits intérieurs : bord d'une mèche sur ce qui est derrière (côté ombre et sur la peau)
    for dx, dy in ((1, 0), (0, 1), (-1, 0), (0, -1)):
        Z = voisin(-dx, -dy)            # ce qu'il y a à côté
        bord = np.char.startswith(lab, 'm') & (Z != lab) & (Z != '.') & (Z != 'band')
        cote_ombre = (dx > 0) | ((dy > 0) & (S >= 96))     # petit format : moins de traits
        G[bord & (cote_ombre | (Z == 'peau'))] = 'D'
        bp = peau & (Z != 'peau') & (Z != '.') & ~np.char.startswith(Z, 'm') & (Z != 'cal')
        G[bp & (Z != 'band')] = '4'                  # menton et joue sur le cou ou les cheveux
    # contour extérieur, plus clair côté lumière (selout)
    plein = lab != '.'
    for dx, dy in ((1, 0), (-1, 0), (0, 1), (0, -1)):
        Z = voisin(dx, dy); bord = plein & (Z == '.')
        G[bord] = 'O'
    clair = plein & (G == 'O') & (nx < -.2) & (ny < -.3)
    G[clair] = 'D'
    return G

def oeil(G, cx, cy, w, h, ext, S):
    """Œil anime : cil épais (plus épais au coin extérieur, avec un crochet), blanc réduit,
    iris haut et ovale (sombre en haut, chaud au milieu, clair en bas), pupille, reflets."""
    x0 = round(cx - w / 2); y0 = round(cy - h / 2)
    for j in range(h):
        for i in range(w):
            xi = ((i + .5) / w * 2 - 1) * ext             # +1 = coin extérieur
            top = h * (.16 + .12 * (xi + .2) ** 2 - .06 * xi)
            bot = h * (.98 - .30 * xi ** 2 - .05 * xi)
            y = j + .5
            if not (top <= y <= bot): continue
            ic = w * (.46 if ext > 0 else .54)            # le regard part un peu vers la gauche
            dxi = (i + .5 - ic) / (w * .40); dyi = (y - h * .56) / (h * .50)
            if dxi * dxi + dyi * dyi <= 1:
                tv = (y - h * .11) / (h * .89)
                c = '4' if tv < .3 else 'j' if tv < .72 else 'Y'
                if ((i + .5 - ic) / (w * .15)) ** 2 + ((y - h * .52) / (h * .22)) ** 2 <= 1: c = 'O'
            else:
                c = 'W' if (y - top > 1 or w < 9) else '3'
            G[y0 + j][x0 + i] = c
    # cil du haut : 1 px partout, 2 px sur la moitié extérieure, crochet au coin
    for i in range(-1, w + 1):
        xi = ((i + .5) / w * 2 - 1) * ext
        top = h * (.16 + .12 * (xi + .2) ** 2 - .06 * xi)
        yt = y0 + int(np.floor(top - .01)) - (0 if top % 1 > .5 else 1)
        yt = y0 + round(top) - 1
        ep = (3 if xi > .3 and w >= 10 else 2) if w >= 7 and xi > -.6 else 1
        for e in range(ep): G[yt - e][x0 + i] = 'O'
    xo = x0 + w if ext > 0 else x0 - 1
    for e in range(1, 1 + (2 if w >= 9 else 1)):
        G[y0 + round(h * .2) + e - 1][xo + (e if ext > 0 else -e) - (1 if ext > 0 else -1)] = 'O'
    # reflets, du côté de la lumière
    ic = x0 + round(w * (.46 if ext > 0 else .54) - w * .2)
    rw = 2 if w >= 8 else 1
    for a in range(rw):
        for b in range(rw): G[y0 + round(h * .3) + b][ic + a] = 'W'
    if w >= 7: G[y0 + round(h * .74)][x0 + round(w * .62)] = 'W'
    # paupière du bas : petit trait au coin extérieur
    for i in range(w):
        xi = ((i + .5) / w * 2 - 1) * ext
        if xi > .2:
            yb = y0 + round(h * (.98 - .30 * xi ** 2 - .05 * xi))
            if G[yb][x0 + i] in '12': G[yb][x0 + i] = '3'

def sourcil(G, cx, top, w, ext, haut):
    """Sourcil fin en arc, posé PAR-DESSUS la frange (convention anime) : trait chaud sur la peau,
    cheveux sombres sur les mèches. Plus épais côté nez."""
    for i in range(-1, w + 1):
        xi = ((i + .5) / w * 2 - 1) * ext
        y = round(top - haut - 1.1 * (1 - (xi - .1) ** 2))
        x = round(cx - w / 2) + i
        for e in range(2 if (xi < -.2 and w >= 9) else 1):
            c = G[y + e][x]
            G[y + e][x] = '4' if c in '123k' else 'D' if c in 'ABC' else c

def ferme(G, cx, cy, w, h, ext):
    """Œil fermé (clin d'œil) : arc de cils vers le bas, crochet au coin extérieur."""
    x0 = round(cx - w / 2)
    for i in range(w):
        xi = ((i + .5) / w * 2 - 1)
        y = round(cy + h * .12 - h * .22 * (1 - xi * xi))
        G[y][x0 + i] = 'O'
        if abs(xi) < .6 and w >= 9: G[y - 1][x0 + i] = 'O'
    xo = x0 + w if ext > 0 else x0 - 1
    G[round(cy + h * .12) + 1][xo] = 'O'

def visage(G, S, expr='sourire'):
    """Traits posés depuis la tête 3D : yeux sur la ligne des yeux, nez et bouche sur l'axe."""
    k = S / 100; T = LOOMIS
    P = lambda p: (p[0] * k, p[1] * k)
    ew = {48: (4, 5, 5, 6), 64: (6, 7, 7, 8), 96: (9, 11, 11, 12)}[S]
    (xl, yl), fl = T.regard(-1); (xp, yp), fp = T.regard(1)
    oeil(G, xl * k, yl * k, ew[0], ew[1], -1, S)          # œil lointain, raccourci
    if expr == 'clin': ferme(G, xp * k, yp * k, ew[2], ew[3], 1)
    else: oeil(G, xp * k, yp * k, ew[2], ew[3], 1, S)
    if S >= 64:
        haut = 2 if expr == 'surprise' else 0
        sourcil(G, xl * k, yl * k - ew[1] / 2 - 1, ew[0] + 1, -1, haut + (1 if S >= 96 else 0))
        sourcil(G, (xp + .5) * k, yp * k - ew[3] / 2 - 1, ew[2] + 1, 1, haut + (1 if S >= 96 else 0))
    # joues : une bande rose sous chaque œil, sur la pommette
    for (q, rx) in ((T.p2((-.45, .62, .78)), 3.5), (T.p2((.45, .62, .78)), 5)):
        for y in range(S):
            for x in range(S):
                if abs((x + .5) / k - q[0]) / rx + abs((y + .5) / k - q[1]) / 1.4 <= 1 and G[y][x] in '12':
                    G[y][x] = 'k'
    xn, yn = [round(v) for v in P(T.point('nez'))]          # nez : un plan d'ombre, côté ombre
    G[yn][xn] = '3'
    if S >= 96: G[yn + 1][xn + 1] = '3'; G[yn - 1][xn - 1] = '1'
    xm, ym = [round(v) for v in P(T.point('bouche', .06))]  # bouche ouverte, souriante
    B = {48: ['44'], 64: ['O44', '.k'], 96: ['4OOO4', '.Okk', '..k']}[S]
    if S >= 96 and expr == 'clin': B = ['4OOOO4', '.OWkk', '..kk']
    if S >= 96 and expr == 'surprise': B = ['.44', '4OO4', '4Ok4', '.44']; ym -= 1
    for j, row in enumerate(B):
        for i, ch in enumerate(row):
            if ch != '.': G[ym + j][xm - len(B[0]) // 2 + i] = ch

def nettoyer(G, tours=2):
    """Pixel orphelin (aucun voisin direct de sa couleur) → couleur majoritaire autour.
    Le contour et le fond ne bougent pas."""
    S = len(G)
    for _ in range(tours):
        H = [r[:] for r in G]
        for y in range(1, S - 1):
            for x in range(1, S - 1):
                c = G[y][x]
                if c in '.O': continue
                v = [G[y + dy][x + dx] for dx, dy in ((1, 0), (-1, 0), (0, 1), (0, -1))]
                if c not in v:
                    cand = [n for n in v if n not in '.O']
                    if cand: H[y][x] = max(set(cand), key=cand.count)
        G = H
    return G

def portrait(S, etape=99, expr='sourire'):
    lab, val, X, Y, nx, ny = construire(S)
    if etape == 1:
        return [['O' if c != '.' else '.' for c in r] for r in lab]
    G = nettoyer(ombrer(lab, val, X, Y, nx, ny, S).tolist())
    if etape == 2: return G
    visage(G, S, expr)
    return G

if __name__ == '__main__':
    import sys
    from PIL import Image
    out = sys.argv[1] if len(sys.argv) > 1 else 'portraits.png'
    ims = [png(portrait(S), PAL, None, 1) for S in (48, 64, 96)]
    k = 5; W = sum(i.width for i in ims) * k + 40; H = 96 * k
    sheet = Image.new('RGB', (W, H), (232, 230, 222)); x = 0
    for im in ims:
        im = im.resize((im.width * k, im.height * k), Image.NEAREST)
        sheet.paste(im, (x, H - im.height), im); x += im.width + 20
    sheet.save(out)
