"""Lina en chibi (64×64) : tête ≈ moitié du corps, visage large et court, grands yeux bas."""
import numpy as np
from PIL import Image

S = 64
PAL = {
    '.': None,
    'H0': (34, 52, 86), 'H1': (44, 96, 126), 'H2': (60, 150, 160), 'H3': (112, 200, 194), 'H4': (214, 246, 236),
    'P0': (170, 92, 96), 'P1': (255, 232, 212), 'P2': (244, 196, 176), 'P3': (246, 158, 156),
    'E0': (40, 30, 52), 'E1': (140, 56, 44), 'E2': (226, 118, 44), 'E3': (255, 204, 86), 'EW': (255, 255, 255),
    'V0': (110, 36, 56), 'V1': (160, 52, 70), 'V2': (212, 78, 66), 'V3': (244, 128, 86),
    'W0': (120, 120, 150), 'W1': (206, 210, 222), 'W2': (248, 248, 244),
    'J0': (34, 34, 54), 'J1': (62, 62, 88), 'J2': (92, 92, 120),
    'C0': (80, 44, 52), 'C1': (130, 72, 70), 'C2': (176, 108, 96),
}
OUT = {'H': 'H0', 'P': 'P0', 'E': 'E0', 'V': 'V0', 'W': 'W0', 'J': 'J0', 'C': 'C0'}

ys, xs = np.mgrid[0:S, 0:S] + .5
G = np.full((S, S), '.', dtype='<U2')
R = np.full((S, S), '.', dtype='<U1')         # région (pour le contour)

def ell(cx, cy, rx, ry, p=2):
    return (np.abs(xs - cx) / rx) ** p + (np.abs(ys - cy) / ry) ** p <= 1

def peindre(M, c, reg=None):
    G[M] = c; R[M] = reg or c[0]

def ombre_sphere(M, cx, cy, r, noms, seuils):
    nx, ny = (xs - cx) / r, (ys - cy) / r
    v = -.45 * nx - .75 * ny
    c = np.select([v > s for s in seuils], noms[:-1], noms[-1])
    G[M] = c[M]; R[M] = noms[0][0]

# --- cheveux de derrière : gros volume rond qui tombe en boucles jusqu'aux épaules
dos = ell(32, 22, 21, 18) | ell(16, 35, 5, 8) | ell(48, 35, 5, 8) | ell(14, 42, 3.5, 3.5) | ell(50, 42, 3.5, 3.5)
ombre_sphere(dos, 32, 18, 22, ['H2', 'H1'], [.35])

# --- corps : petit, la veste en trapèze, manches ouvertes
corps = (ys >= 40) & (ys < 54) & (np.abs(xs - 32) < 8 + (ys - 40) * .45)
peindre(corps, 'V2')
peindre(corps & (xs > 36 + (ys - 40) * .3), 'V1')
peindre(corps & (xs < 25) & (ys < 48), 'V3')
t = (ys >= 40) & (ys < 52) & (np.abs(xs - 32) < 3.6 - (ys - 40) * .1)    # t-shirt blanc
peindre(t, 'W2'); peindre(t & (ys < 42), 'W1')
peindre((ys >= 52) & (ys < 55) & (np.abs(xs - 32) < 8.5), 'J1')          # short
for cx in (28, 36):                                                     # jambes
    peindre((ys >= 55) & (ys < 58) & (np.abs(xs - cx) < 2.5), 'P1')
    peindre((ys >= 58) & (ys < 61) & (np.abs(xs - cx) < 2.5), 'W2')
    peindre((ys >= 61) & (ys < 63) & (np.abs(xs - cx) < 3.2), 'C1')
    peindre((ys >= 61) & (ys < 62) & (np.abs(xs - cx) < 1.6), 'C2')
for cx in (21, 43):                                                     # mains
    peindre(ell(cx, 51.5, 2.2, 2), 'P1')

# --- visage : large et court, joues rondes, menton à peine marqué
face = ell(32, 28, 15, 12, 2.6) & (ys < 40)
peindre(face, 'P1')
peindre(face & (ys < 24), 'P2')                                          # ombre de la frange
# --- frange : couvre le front jusqu'au-dessus des yeux, pointes irrégulières
pointes = np.interp(xs, [16, 19, 22, 25, 28, 31, 33, 36, 39, 42, 45, 48],
                        [32, 26, 24, 27, 23, 26, 24, 27, 23, 26, 25, 32])
frange = ell(32, 20, 18, 14) & (ys < pointes)
ombre_sphere(frange, 32, 14, 20, ['H3', 'H2', 'H1'], [.0, -.55])
peindre(frange & (ys > pointes - 2), 'H2')
# séparations entre les mèches : un trait sombre qui part du creux et remonte en s'inclinant
for xv in (22, 28, 33, 39):
    yv = int(np.interp(xv, [16, 19, 22, 25, 28, 31, 33, 36, 39, 42, 45, 48],
                           [32, 26, 24, 27, 23, 26, 24, 27, 23, 26, 25, 32]))
    for d in range(6):
        x = int(round(xv + (xv - 32) * .08 * d)); y = yv - d
        if frange[y, x]: G[y, x] = 'H1'
# bord bas de la frange : trait sombre là où la mèche touche le visage
bas = frange & np.roll(face & ~frange, -1, 0)
peindre(bas, 'H1', 'H')
# mèches de côté devant les joues
for s in (-1, 1):
    m = ell(32 + s * 17.5, 31, 2.6, 9) & (ys > 22)
    ombre_sphere(m, 32 + s * 16, 26, 10, ['H2', 'H1'], [-.2 if s < 0 else .3])
# reflets en blocs + mèche rebelle
for (x0, y0, w, h) in ((22, 9, 3, 2), (25, 8, 2, 1), (37, 10, 2, 2), (19, 13, 1, 2)):
    G[y0:y0 + h, x0:x0 + w] = 'H4'
for (x, y) in ((32, 4), (32, 3), (33, 2), (34, 2), (35, 3)):
    G[y, x] = 'H2'; R[y, x] = 'H'

# --- yeux : grands, bas, presque aux bords du visage
def oeil(x0, y0, w=8, h=10, ext=1):
    """Œil chibi : paupière en arc (coins plus bas), iris en dégradé sombre → clair,
    pupille haute, deux reflets, aile de cil vers l'extérieur."""
    off = [round(1.3 * ((i + .5) / w * 2 - 1) ** 2) for i in range(w)]
    for i in range(w):
        u = (i + .5) / w * 2 - 1
        for j in range(off[i] + 1, h):
            if j >= h - 1 and abs(u) > .6: continue                    # coins du bas arrondis
            c = 'E1' if j < 4 else 'E2' if j < 7 else 'E3'
            if 2 <= j <= 5 and abs(u) < .3: c = 'E0'
            if u * ext < -.75 and j > 3: c = 'EW'                         # un peu de blanc côté nez
            G[y0 + j, x0 + i] = c
        G[y0 + off[i], x0 + i] = 'E0'                                    # cil : 2 px au milieu
        if off[i] == 0 or u * ext > .3: G[y0 + off[i] - 1, x0 + i] = 'E0'
    xo = x0 + w if ext > 0 else x0 - 1                                   # aile du cil
    G[y0 + off[-1 if ext > 0 else 0], xo] = 'E0'
    G[y0 + off[-1 if ext > 0 else 0] + 1, xo + (1 if ext > 0 else -1)] = 'E0'
    xr = x0 + (1 if ext < 0 else w - 4)                                  # reflet côté lumière (gauche)
    xr = x0 + 1
    G[y0 + 2:y0 + 4, xr:xr + 2] = 'EW'; G[y0 + 7, x0 + w - 2] = 'EW'
oeil(19, 26, ext=-1); oeil(37, 26, ext=1)
# joues, bouche
for cx in (21, 43):
    G[37, cx - 2:cx + 3] = 'P3'
G[38, 31:33] = 'P0'

# --- contour teinté (pas noir) sur le bord extérieur
plein = G != '.'
bord = np.zeros_like(plein)
for dx, dy in ((1, 0), (-1, 0), (0, 1), (0, -1)):
    bord |= plein & ~np.roll(np.roll(plein, dy, 0), dx, 1)
for y, x in zip(*np.nonzero(bord)):
    G[y, x] = OUT.get(R[y, x], G[y, x])
# séparation visage / cheveux : trait doux
for y, x in zip(*np.nonzero(R == 'P')):
    if G[y, x] in ('P1', 'P2') and any(R[y + dy, x + dx] == 'V' for dx, dy in ((0, 1),)):
        G[y, x] = 'P0'

def png(nom, k=1):
    im = Image.new('RGBA', (S, S))
    im.putdata([(*PAL[c], 255) if PAL.get(c) else (0, 0, 0, 0) for c in G.flat])
    if k > 1: im = im.resize((S * k, S * k), Image.NEAREST)
    im.save(nom); return im

if __name__ == '__main__':
    import sys
    png('lina_chibi64.png')
    im = png(sys.argv[1] if len(sys.argv) > 1 else 'lina_chibi_x8.png', 8)
