# Lina, portrait anime de 3/4 (méthode C11 + C12). Version 3 : tête construite en 3D,
# grandes mèches propres, yeux plus grands et plus clairs, buste aux épaules tombantes.
import numpy as np
from vec import *
from tete import Tete

# 15 couleurs + transparent (GBA). Ombres vers le violet, lumières vers le jaune.
PAL = {
 'O': (30, 26, 56),                                                   # contour, pupille, cils
 'A': (196, 240, 222), 'B': (98, 188, 188), 'C': (54, 128, 158), 'D': (36, 72, 116),   # cheveux
 '1': (255, 236, 218), '2': (250, 204, 178), '3': (230, 146, 146), '4': (150, 66, 96),  # peau ; 4 = trait chaud
 'k': (244, 120, 128),                                                # joues, bouche
 'j': (222, 116, 56), 'Y': (252, 204, 92),                            # iris
 'W': (234, 242, 248),                                                # blanc bleuté
 'r': (250, 142, 82), 'q': (212, 76, 66),                             # veste ; ombre = 4
}

def sym(*pts):
    """Miroir d'une liste de points autour de x = 50 (vue de face)."""
    return [(100 - x, y) for x, y in pts]

VUES = {
 '34': dict(tete=Tete(50, 37, 22, lacet=28, tangage=5, roulis=-5),
    dos=chemin((22, 36), ((22, 14), (40, 6), (54, 7)), ((70, 8), (80, 20), (79, 38)),
                 ((79, 52), (81, 62), (83, 70)), (77, 68), (74, 72), (69, 66), (32, 66), (27, 71),
                 (24, 66), (18, 69), ((20, 58), (21, 46), (22, 36))),
    veste=chemin((2, 100), ((4, 90), (12, 85), (24, 83)), ((35, 81), (42, 77), (47, 75)), (63, 74),
                   ((68, 77), (75, 81), (84, 83)), ((92, 85), (97, 92), (99, 100))),
    col=chemin((44, 76), (55, 90), (67, 75), (62, 74), (55, 84), (49, 75)), ombre_veste=64,
    meches=[
        ((29, 28), (23, 42), (22, 56), (26, 70), 9),     # côté lointain, à l'extérieur de la joue
        ((70, 28), (75, 42), (74, 56), (68, 68), 10),    # côté proche, devant l'oreille
        ((48, 12), (38, 16), (30, 25), (27, 42), 15),    # frange : grande mèche vers la gauche
        ((64, 14), (70, 22), (74, 30), (75, 41), 11),    # frange, bord proche
        ((61, 13), (67, 22), (69, 31), (68, 43), 12),
        ((60, 13), (63, 24), (63, 33), (61, 42), 11),
        ((58, 12), (58, 23), (56, 31), (53, 41), 12),
        ((50, 12), (40, 19), (34, 29), (32, 45), 13),
        ((53, 12), (46, 21), (40, 30), (37, 43), 14),
        ((56, 13), (53, 25), (49, 34), (45, 46), 8),     # mèche entre les yeux
    ],
    houpe=((55, 9), (55, 2), (63, 1), (65, 6)),
    dos_sombre=.35, lum_x=.55, iris=(.38, .47), oeil_loin=.72, dx_yeux=(1.2, .5), joues=(3, 4.5), dx_nez=-.04, dx_bouche=.05),
 'face': dict(tete=Tete(50, 37, 22, lacet=0, tangage=4, roulis=0),
    # bob symétrique ; la frange a sa raie un peu à droite pour ne pas faire « casque »
    dos=chemin((21, 36), ((21, 14), (36, 6), (50, 6)), ((64, 6), (79, 14), (79, 36)),
               ((79, 52), (81, 62), (83, 70)), (77, 68), (74, 72), (69, 66), (31, 66), (26, 72),
               (23, 68), (17, 70), ((19, 62), (21, 50), (21, 36))),
    veste=chemin((2, 100), ((4, 90), (12, 85), (24, 83)), ((34, 81), (40, 77), (42, 75)), (58, 75),
                 ((60, 77), (66, 81), (76, 83)), ((88, 85), (96, 90), (98, 100))),
    col=chemin((38, 76), (50, 90), (62, 76), (58, 75), (50, 84), (42, 75)), ombre_veste=66,
    meches=[
        ((29, 28), (23, 42), (22, 56), (26, 70), 9), ((71, 28), (77, 42), (78, 56), (74, 70), 9),   # côtés
        ((48, 12), (38, 16), (31, 26), (28, 42), 14), ((56, 12), (64, 16), (70, 26), (72, 42), 14),
        ((50, 12), (42, 20), (37, 30), (35, 44), 13), ((55, 12), (61, 20), (65, 30), (65, 44), 13),
        ((52, 12), (48, 22), (44, 32), (43, 44), 12), ((54, 12), (56, 22), (58, 32), (57, 43), 12),
        ((53, 12), (52, 24), (51, 34), (50, 47), 9),     # mèche au milieu, entre les yeux
    ],
    houpe=((53, 9), (53, 2), (61, 1), (63, 6)),
    dos_sombre=.05, lum_x=.3, lum_0=.3, iris=(.43, .52), loomis_face={48: (6, 7), 64: (8, 9), 96: (11, 12)}, oeil_loin=1, dx_yeux=(0, 0), joues=(4, 4), dx_nez=0, dx_bouche=0),
}
V = VUES['34']
CHEV = (50, 35, 26)          # sphère des cheveux : le crâne + l'épaisseur des cheveux

def construire(S):
    k = S / 100; T = V['tete']
    lab = np.full((S, S), '.', dtype='<U8'); val = np.zeros((S, S)); tt = np.zeros((S, S))
    ys, xs = np.mgrid[0:S, 0:S]; X = (xs + .5) / k; Y = (ys + .5) / k
    hx, hy, hr = CHEV
    nx, ny = (X - hx) / hr, (Y - hy) / hr
    lumiere = -V['lum_x'] * nx - .8 * ny + V.get('lum_0', 0)                       # lumière en haut à gauche
    def poser(M, nom, v=0, t=None):
        lab[M] = nom; val[M] = v[M] if isinstance(v, np.ndarray) else v
        if t is not None: tt[M] = t[M]
    # 1. masse arrière : un carré court arrondi, deux pointes douces par côté
    dos = V['dos']
    poser(masque(dos, S), 'dos', lumiere - V['dos_sombre'])
    # 2. buste : épaules qui tombent depuis le cou (pas un dôme)
    veste = V['veste']
    poser(masque(veste, S), 'veste', .9 - np.hypot(X - 24, (Y - 84) * 2.2) / 30 - 2 * (X > V['ombre_veste'] + 1.5 * (Y - 74)))
    poser(masque(T.cou(80), S), 'cou')
    col = V['col']
    poser(masque(col, S), 'col')
    # 3. visage : le contour sort de la tête 3D
    poser(masque(T.oreille(1), S), 'oreille')
    vis = masque(T.contour(), S)
    poser(vis, 'peau')
    # plan de côté : une bande étroite le long de la mâchoire proche, pas une plaque
    cote = vis & masque(T.plan_cote(1), S) & (Y > 52)
    poser(cote & ~decale(cote, -max(1, round(2.5 * k)), 0, False), 'peau', 1)
    # 4. calotte de cheveux au-dessus de la ligne du front
    cal = (np.hypot(X - hx, Y - hy) <= hr) & (Y < 27 + .05 * (X - 30))
    poser(cal, 'cal', lumiere)
    # 5. mèches : côtés, puis frange de l'arrière vers l'avant (racine, ctrl, ctrl, pointe, largeur)
    meches = V['meches']
    for i, (a, b, c, d, w) in enumerate(meches):
        M, Tm, Sd = meche(a, b, c, d, w, S, forme=.9)
        poser(M, 'm%d' % i, lumiere - .3 * Sd + .3 - .25 * Tm, Tm)
    houpe, Th, Sh = meche(*V['houpe'], 2.6, S)   # mèche rebelle
    poser(houpe, 'm9', lumiere + .4, Th)
    return lab, val, tt, X, Y, nx, ny

def decale(A, dx, dy, rempli):
    S = A.shape[0]; Z = np.full_like(A, rempli)
    Z[max(dy, 0):S + min(dy, 0), max(dx, 0):S + min(dx, 0)] = A[max(-dy, 0):S + min(-dy, 0), max(-dx, 0):S + min(-dx, 0)]
    return Z

def ombrer(lab, val, tt, X, Y, nx, ny, S):
    k = S / 100
    G = np.full((S, S), '.', dtype='<U1')
    meche_ = np.char.startswith(lab, 'm')
    ch = meche_ | (lab == 'cal') | (lab == 'dos')
    G[ch] = np.where(val[ch] > .55, 'B', np.where(val[ch] > -.3, 'C', 'D'))
    # reflet : anneau cassé sur le dessus, coupé à chaque mèche
    r = np.hypot(nx, ny)
    ep = max(1, round(1.6 * k)) / (CHEV[2] * k)
    anneau = (meche_ | (lab == 'cal')) & (r > .56) & (r < .56 + ep) & (ny < -.15) & (nx < .35) & (nx > -.75)
    G[anneau] = 'A'
    # mèches : séparées par un trait sombre, seulement vers la pointe (anime)
    for dx, dy in ((1, 0), (-1, 0), (0, 1)):
        Z = decale(lab, -dx, -dy, '.')
        bord = meche_ & (Z != lab) & (np.char.startswith(Z, 'm') | (Z == 'cal')) & (tt > .45)
        G[bord & ((dx > 0) | (dy > 0))] = 'D'
    peau = lab == 'peau'
    G[peau] = '1'
    G[lab == 'cou'] = '2'; G[lab == 'oreille'] = '2'
    G[lab == 'col'] = 'W'
    v = lab == 'veste'
    G[v] = np.where(val[v] > .55, 'r', np.where(val[v] > -.6, 'q', '4'))
    # ombres portées sur la peau : sous la frange (vers le bas à droite) et plan de côté
    sous = np.zeros((S, S), bool)
    for d in range(1, max(2, round(2.5 * k)) + 1):
        sous |= np.char.startswith(decale(lab, round(d * .4), d, '.'), 'm')
    G[peau & sous] = '2'
    G[peau & (val > .5)] = '2'
    G[peau & (Y < 39)] = '2'                                 # front : à l'ombre de la frange
    # cou : l'ombre du menton reprend la forme de la mâchoire
    vis = lab == 'peau'; om = np.zeros((S, S), bool)
    for d in range(1, round(3.5 * k) + 1): om |= decale(vis, round(d * .2), d, False)
    G[(lab == 'cou') & om] = '3'
    G[v & decale(lab == 'col', 0, 1, False) & ~(lab == 'col')] = '4'          # ombre sous le col
    # traits : bord de mèche sur la peau (sombre), menton sur le cou (chaud)
    for dx, dy in ((1, 0), (-1, 0), (0, 1), (0, -1)):
        Z = decale(lab, -dx, -dy, '.')
        G[meche_ & (Z == 'peau')] = 'D'
        G[peau & ((Z == 'cou') | (Z == 'col'))] = '4'
        G[(lab == 'cou') & ((Z == 'col') | (Z == 'veste'))] = '3'
    # contour extérieur : marine sur les cheveux et le buste, chaud sur la peau ; plus clair côté lumière
    plein = lab != '.'
    bordx = np.zeros((S, S), bool)
    for dx, dy in ((1, 0), (-1, 0), (0, 1), (0, -1)): bordx |= plein & (decale(lab, dx, dy, '.') == '.')
    G[bordx] = 'O'
    G[bordx & ((lab == 'peau') | (lab == 'cou'))] = '4'
    G[bordx & ch & (nx < -.25) & (ny < -.2)] = 'D'
    return G

def oeil(G, cx, cy, w, h, ext, S, ferme_=False):
    """Œil anime : grand iris haut, blanc seulement sur les côtés, cil épais avec un crochet au
    coin extérieur, deux reflets. ext = +1 si le coin extérieur est à droite."""
    x0 = round(cx - w / 2); y0 = round(cy - h / 2)
    def haut(xi): return h * (.10 + .14 * (xi - .15) ** 2)            # paupière du haut
    def bas(xi): return h * (.97 - .22 * xi ** 2 + .06 * xi)          # paupière du bas
    ic = w * ((.47 if ext > 0 else .53) if V['dx_yeux'][0] else .5)  # 3/4 : regard un peu à gauche
    rx_i, ry_i = V['iris']
    for j in range(h):
        for i in range(w):
            xi = ((i + .5) / w * 2 - 1) * ext; y = j + .5
            if not (haut(xi) <= y <= bas(xi)): continue
            dxi = (i + .5 - ic) / (w * rx_i); dyi = (y - h * .56) / (h * ry_i)
            if dxi * dxi + dyi * dyi <= 1:
                tv = (y - haut(xi)) / (h * .85)
                c = '4' if tv < .28 else 'j' if tv < .70 else 'Y'
                if ((i + .5 - ic) / (w * .14)) ** 2 + ((y - h * .52) / (h * .2)) ** 2 <= 1: c = 'O'
            else:
                c = 'W'
            G[y0 + j][x0 + i] = c
    # cil du haut : plus épais vers le coin extérieur, dépasse d'un pixel
    ep_max = 3 if w >= 11 else 2 if w >= 7 else 1
    for i in range(-1, w + 1):
        xi = ((i + .5) / w * 2 - 1) * ext
        yt = y0 + round(haut(max(-1, min(1, xi)))) - 1
        ep = ep_max if xi > .1 else max(1, ep_max - 1)
        for e in range(ep):
            if 0 <= yt - e + (1 if e == 0 and xi > .9 else 0) < S: G[yt - e][x0 + i] = 'O'
    xo = x0 + w if ext > 0 else x0 - 1                               # crochet vers le bas
    for e in range(2 if w >= 9 else 1):
        G[y0 + round(h * .14) + e][xo + (e + 1) * (1 if ext > 0 else -1) - (1 if ext > 0 else -1)] = 'O'
    # reflets : un grand en haut côté lumière, un petit en bas de l'autre côté
    rw, rh = (2, 3) if w >= 9 else (1, 2) if w >= 6 else (1, 1)
    xr = x0 + round(ic - w * .26); yr = y0 + round(h * .30)
    for a in range(rw):
        for b in range(rh): G[yr + b][xr + a] = 'W'
    if w >= 7: G[y0 + round(h * .72)][x0 + round(ic + w * .18)] = 'W'
    # paupière du bas : un petit trait chaud au coin extérieur
    if w >= 7:
        for i in range(w):
            xi = ((i + .5) / w * 2 - 1) * ext
            if xi > .35:
                yb = y0 + round(bas(xi)) 
                if G[yb][x0 + i] in '12': G[yb][x0 + i] = '4'

def sourcil(G, cx, top, w, ext, haut):
    """Sourcil fin (1 px) en arc, posé par-dessus la frange : trait chaud sur la peau,
    cheveux sombres sur les mèches."""
    for i in range(w):
        xi = ((i + .5) / w * 2 - 1) * ext
        y = round(top - haut - 1.3 * (1 - (xi - .1) ** 2))
        x = round(cx - w / 2) + i
        c = G[y][x]
        G[y][x] = '4' if c in '123k' else 'D' if c in 'ABC' else c

def ferme(G, cx, cy, w, h, ext):
    """Œil fermé (clin d'œil) : arc de cils vers le bas, crochet au coin extérieur."""
    x0 = round(cx - w / 2)
    for i in range(w):
        xi = ((i + .5) / w * 2 - 1)
        y = round(cy + h * .1 - h * .25 * (1 - xi * xi))
        G[y][x0 + i] = 'O'
        if abs(xi) < .6 and w >= 9: G[y - 1][x0 + i] = 'O'
    xo = x0 + w if ext > 0 else x0 - 1
    G[round(cy + h * .1) + 1][xo] = 'O'

def visage(G, S, expr='sourire'):
    """Traits posés depuis la tête 3D : yeux sur la ligne des yeux, nez et bouche sur l'axe."""
    k = S / 100; T = V['tete']
    w, h = {48: (6, 7), 64: (8, 9), 96: (12, 13)}[S]
    wl = max(4, round(w * V['oeil_loin']))                       # œil lointain raccourci (3/4)
    (xl, yl), _ = T.regard(-1); (xp, yp), _ = T.regard(1)
    xl += V['dx_yeux'][0]; xp += V['dx_yeux'][1]
    if 'loomis_face' in V:
        # Loomis de face : un œil d'écart entre les yeux, les yeux dans le tiers du milieu
        # (≈ 45 % entre la ligne des sourcils et le nez), le sourcil SUR la ligne des sourcils.
        w, h = V['loomis_face'][S]
        xs, ys_ = T.point('sourcils'); _, yn_ = T.point('nez')
        xl, xp = xs - w / k, xs + w / k
        yl = yp = ys_ + .45 * (yn_ - ys_)
        wl = w
    oeil(G, xl * k, yl * k, wl, h, -1, S)
    if expr == 'clin': ferme(G, xp * k, yp * k, w, h, 1)
    else: oeil(G, xp * k, yp * k, w, h, 1, S)
    if S >= 64:
        hs = 2 if expr == 'surprise' else 0
        yb = (T.point('sourcils')[1] * k + 1) if 'loomis_face' in V else None
        sourcil(G, xl * k, yb or yl * k - h / 2 - 1.5, wl + 1, -1, hs)
        sourcil(G, xp * k + .5, yb or yp * k - h / 2 - 1.5, w + 1, 1, hs)
    # joues : petite ellipse rose sous chaque œil, seulement sur la peau claire
    for (q, rx) in ((T.p2((-.44, .65, .78)), V['joues'][0]), (T.p2((.46, .65, .78)), V['joues'][1])):
        for y in range(S):
            for x in range(S):
                if ((x + .5) / k - q[0]) ** 2 / rx ** 2 + ((y + .5) / k - q[1]) ** 2 / 1.3 ** 2 <= 1 and G[y][x] == '1':
                    G[y][x] = 'k'
    xn, yn = [round(v * k) for v in T.point('nez', V['dx_nez'])]      # nez : petite ombre côté lointain
    G[yn][xn] = '3'
    if S >= 96: G[yn - 1][xn] = '3'
    xm, ym = [round(v * k) for v in T.point('bouche', V['dx_bouche'])]
    B = {48: ['44'], 64: ['4O4', '.k'], 96: ['4OOO4', '.Okk', '..44']}[S]
    if 'loomis_face' in V and expr == 'sourire' and S >= 96: B = ['4...4', '.OOO.']   # sourire symétrique
    if expr == 'clin' and S >= 64: B = ['4OOO4', '.Okk.'] if S >= 96 else ['4OO4', '.kk']
    if expr == 'surprise' and S >= 64: B = ['.44.', '4OO4', '4kk4', '.44.'] if S >= 96 else ['4O4', '.4']
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

def portrait(S, etape=99, expr='sourire', vue='34'):
    global V
    V = VUES[vue]
    lab, val, tt, X, Y, nx, ny = construire(S)
    if etape == 1:
        return [['O' if c != '.' else '.' for c in r] for r in lab]
    G = nettoyer(ombrer(lab, val, tt, X, Y, nx, ny, S).tolist())
    if etape == 2: return G
    visage(G, S, expr)
    return G
