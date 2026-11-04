"""Lina chibi v2 : gabarit « grosse tête ronde » (tête ≈ 60 % de la hauteur).

Proportions mesurées sur le gabarit de référence (≈ 52×66 px) puis reconstruites :
dôme de cheveux 48 px de large, frange épaisse jusqu'aux cils, visage très large
et court, yeux 10×10 bas et écartés, joues roses en bande, bouche = 1 point,
cou caché, petit corps (veste ample), jambes courtes, grosses chaussures.
"""
import numpy as np
from PIL import Image

W, H = 64, 72
PAL = {
    'H0': (28, 38, 66), 'H1': (38, 72, 104), 'H2': (48, 112, 134), 'H3': (70, 156, 162),
    'H4': (118, 200, 192), 'H5': (196, 240, 224),
    'P0': (156, 84, 88), 'P1': (238, 182, 168), 'P2': (250, 214, 196), 'P3': (255, 236, 222),
    'B1': (246, 170, 164), 'B2': (234, 138, 142),
    'E0': (50, 24, 40), 'E1': (122, 44, 42), 'E2': (198, 92, 44), 'E3': (238, 146, 58),
    'E4': (255, 204, 108), 'EW': (255, 255, 255), 'EL': (232, 226, 236),
    'V0': (92, 28, 48), 'V1': (148, 44, 60), 'V2': (198, 68, 66), 'V3': (232, 110, 88),
    'W0': (130, 128, 160), 'W1': (206, 208, 224), 'W2': (250, 250, 246),
    'J0': (30, 30, 52), 'J1': (56, 56, 84), 'J2': (86, 86, 116),
    'C0': (70, 34, 46), 'C1': (122, 58, 62), 'C2': (172, 96, 90),
    'S0': (206, 212, 232),
}
# couleur de contour (teintée, jamais noire) de chaque région
OUT = {'H': 'H0', 'P': 'P0', 'E': 'E0', 'V': 'V0', 'W': 'W0', 'J': 'J0', 'C': 'C0', 'B': 'P0'}

ys, xs = np.mgrid[0:H, 0:W] + .5
G = np.full((H, W), '', dtype='<U2')


def ell(cx, cy, rx, ry, p=2.0):
    return (np.abs(xs - cx) / rx) ** p + (np.abs(ys - cy) / ry) ** p <= 1


def mir(M):                       # symétrique gauche/droite
    return M | M[:, ::-1]


def put(M, c):
    G[M] = c


def ligne(x0, y0, x1, y1, c, dans=None):
    n = int(max(abs(x1 - x0), abs(y1 - y0))) + 1
    for t in np.linspace(0, 1, n):
        x, y = int(round(x0 + (x1 - x0) * t)), int(round(y0 + (y1 - y0) * t))
        if dans is None or dans[y, x]:
            G[y, x] = c


CX, CY, RX, RY = 32, 25, 24, 21          # dôme de la tête (cheveux)
nx, ny = (xs - CX) / RX, (ys - CY) / RY
lum = -.5 * nx - .8 * ny                 # lumière en haut à gauche

# ---------- 1. cheveux de derrière : longues mèches ondulées jusqu'à la taille
dos = ell(CX, CY, RX, RY)
for cx, cy, rx, ry in ((13, 37, 6, 11), (12, 47, 5.5, 7), (13.5, 55, 4.5, 5)):
    dos |= mir(ell(cx, cy, rx, ry))
put(dos, 'H2')
put(dos & (ys > 30) & (np.abs(xs - 32) > 13), 'H3')
put(dos & (ys > 30) & (np.abs(xs - 32) > 13) & (np.abs(xs - 32) < 16.5), 'H2')
put(dos & (ys > 40) & (((ys + xs * .6) % 7) < 1.2), 'H2')          # ondulations
put(dos & (ys > 30) & (np.abs(xs - 32) < 13), 'H1')               # derrière le corps

# ---------- 2. corps : veste rouge ample, t-shirt blanc, short, jambes, chaussures
dy = ys - 45
torse = (ys >= 45) & (ys < 58) & (np.abs(xs - 31.5) < 8.5 + dy * .3)
put(torse, 'V2')
put(torse & (xs > 36 + dy * .2), 'V1')
put(torse & (xs < 27) & (ys < 51), 'V3')
for cx, cl in ((19.5, 'V3'), (43.5, 'V1')):                       # manches bouffantes
    m = ell(cx, 51.5, 4.3, 6.8)
    put(m, 'V2'); put(m & (np.abs(xs - cx) > 1.5) & ((xs < cx) == (cx < 32)), cl)
    put(m & (ys > 56.5), 'V1')
chem = (ys >= 45) & (ys < 57) & (np.abs(xs - 31.5) < 3.2)
put(chem, 'W2'); put(chem & (xs > 33), 'W1'); put(chem & (ys < 46.5), 'W1')
put((ys >= 45) & (ys < 47) & (np.abs(xs - 31.5) < 4.2) & ~chem, 'W2')   # col
put((ys >= 57) & (ys < 60.5) & (np.abs(xs - 31.5) < 8.5), 'J1')
put((ys >= 57) & (ys < 58.5) & (np.abs(xs - 31.5) < 8.5), 'J2')
for cx in (19.5, 43.5):                                            # mains
    put(ell(cx, 58, 2.6, 2.2), 'P3')
for cx in (28, 35):                                                # jambes
    put((ys >= 60.5) & (ys < 63) & (np.abs(xs - cx) < 2.6), 'P3')
    put((ys >= 62) & (ys < 65) & (np.abs(xs - cx) < 2.6), 'W2')
    put((ys >= 64.5) & (ys < 68) & (np.abs(xs - cx) < 3.4), 'C1')
    put((ys >= 64.5) & (ys < 65.5) & (np.abs(xs - cx) < 2.2), 'C2')

# ---------- 3. visage : très large, court, joues pleines
face = ell(32, 34, 18.5, 12.8, 2.4) & (ys > 20)
put(face, 'P3')
put(face & (xs > 46.5), 'P2')                                      # côté ombre
put(face & (ys > 45) & (np.abs(xs - 32) < 8), 'P2')               # dessous du menton

# ---------- 4. cheveux de devant : frange épaisse et carrée + mèches latérales
bas = np.interp(xs[0], [12, 15, 17, 20, 22, 24, 26, 29, 31.5, 34, 37, 39, 41, 43, 46, 48, 52],
                       [44, 30, 26, 27, 29, 27, 26, 27, 31, 27, 26, 27, 29, 27, 26, 30, 44])
frange = ell(CX, CY, RX, RY) & (ys < bas[None, :])
lat = mir(ell(14.6, 35, 3.2, 12.5) & (ys > 22))                    # mèches devant les oreilles
avant = frange | lat
put(avant, 'H3')
put(avant & (lum > .35), 'H4')
put(avant & (lum < -.25), 'H2')
put(frange & (ys > bas[None, :] - 2.2), 'H2')                      # ombre au bas de la frange
put(lat & (np.abs(xs - 32) > 17), 'H2')
# séparations des mèches (lignes sombres qui descendent vers les pointes)
for x0, y0, x1, y1 in ((26, 11, 22, 28), (32, 8, 31.5, 30), (38, 11, 41, 28),
                       (20, 15, 16.5, 26), (44, 15, 47, 26)):
    ligne(x0, y0, x1, y1, 'H2', frange)
# reflet en anneau (« halo ») coupé en petits blocs
r = np.hypot((xs - CX) / RX, (ys - CY) / RY)
halo = (r > .6) & (r < .74) & (ys < 16) & frange & (((xs + 1) // 3) % 3 != 0)
put(halo, 'H5')
# antenne (ahoge)
for x, y in ((32, 4), (33, 3), (33, 4), (34, 2), (34, 3), (35, 2), (36, 2), (36, 3), (37, 3)):
    G[y, x] = 'H3'

# ---------- 5. yeux 10×10 : cil épais, iris foncé en haut / clair en bas
def oeil(x0, y0, flip):
    for rr in range(12):
        for c in range(-2, 10):
            cc = 9 - c if flip else c
            v = None
            if (rr == 0 and 2 <= c <= 7) or (rr == 1 and 0 <= c <= 9) or (rr == 2 and (c <= 1 or c == 9)):
                v = 'E0'
            elif (rr == 1 and c == -1) or (rr == 2 and c in (-1, -2)):
                v = 'E0'                                           # aile du cil vers l'extérieur
            elif 2 <= rr <= 10 and 1 <= c <= 8 and not (rr == 10 and c in (1, 8)):
                v = {2: 'E1', 3: 'E1', 4: 'E2', 5: 'E2', 6: 'E2', 7: 'E3', 8: 'E3', 9: 'E4', 10: 'E3'}[rr]
                if (3 <= rr <= 7 and 4 <= c <= 5) or (4 <= rr <= 6 and 3 <= c <= 6):
                    v = 'E0'                                       # pupille
                if rr in (3, 4) and c in (2, 3):
                    v = 'EW'                                       # gros reflet
                if (rr == 8 and c == 6) or (rr == 3 and c == 7):
                    v = 'EW'
            elif 3 <= rr <= 9 and c in (0, 9):
                v = 'EL'                                           # un filet de blanc
            if v:
                x = x0 + (9 - c if flip else c)
                G[y0 + rr, x] = v

oeil(18, 27, False)
oeil(36, 27, True)
G[38, 20:26] = np.where(G[38, 20:26] == 'P3', 'P2', G[38, 20:26])
G[38, 38:44] = np.where(G[38, 38:44] == 'P3', 'P2', G[38, 38:44])

# ---------- 6. joues (bande rose) et bouche (un point)
for x in list(range(16, 22)) + list(range(42, 48)):
    G[40, x] = 'B1'; G[41, x] = 'B1'
for x in (17, 19, 43, 45):
    G[40, x] = 'B2'
G[43, 31:33] = 'P0'

# ---------- 7. contour coloré : bord extérieur = teinte sombre de la région
reg = np.vectorize(lambda c: c[:1])(G)
vide = G == ''
contour = np.zeros_like(vide)
for d in ((0, 1), (0, -1), (1, 0), (-1, 0)):
    contour |= np.roll(vide, d, axis=(0, 1))
contour &= ~vide
for k, o in OUT.items():
    G[contour & (reg == k)] = o
# bas de la frange sur le visage : trait sombre doux
haut_peau = (reg == 'P') & (np.roll(reg, 1, 0) == 'H')
G[haut_peau] = 'P1'
cheveux_sur_peau = (reg == 'H') & (np.roll(reg, -1, 0) == 'P')
G[cheveux_sur_peau] = 'H1'
# veste contre cheveux / visage : contour rouge sombre
G[(reg == 'V') & ((np.roll(reg, 1, 1) == 'H') | (np.roll(reg, -1, 1) == 'H'))] = 'V0'
# ombre au sol
sol = ell(31.5, 68.5, 13, 1.6) & (G == '')
G[sol] = 'S0'


def image():
    a = np.zeros((H, W, 4), np.uint8)
    for k, c in PAL.items():
        a[G == k] = (*c, 255)
    return Image.fromarray(a, 'RGBA')


if __name__ == '__main__':
    im = image()
    im.save('lina_chibi2.png')
    big = im.resize((W * 8, H * 8), Image.NEAREST)
    fond = Image.new('RGBA', big.size, (250, 248, 244, 255))
    fond.alpha_composite(big)
    fond.convert('RGB').save('lina_chibi2_x8.png')
