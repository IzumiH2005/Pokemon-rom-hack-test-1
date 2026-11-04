# Portrait anime de Lina (buste de face), en 32, 48 et 64 px.
# Construction commune en unités u = S/32 (zones), ombrage par la forme, puis yeux, nez,
# bouche refaits pour chaque taille : on ne réduit pas le grand portrait (B4b, C10).
from base import *

PALP = dict(PAL, w=(210, 222, 238), k=(246, 160, 150), d=(170, 86, 96))   # blanc bleuté, joues, ombre profonde

def tri(x):
    """Dent de scie : 0 au bout d'une mèche, 1 au creux entre deux mèches."""
    return abs((x % 1) - .5) * 2

def zones(S):
    u = S / 32; c = S / 2 - .5
    Z = [['.'] * S for _ in range(S)]
    for y in range(S):
        for x in range(S):
            d = abs(x - c) / u; v = (y + .5) / u; s = (x - c) / u
            z = None
            if v >= 25.5 and d <= min(15.5, 3.2 + (v - 25.5) * 2.4): z = 'J'          # épaules
            if 20 <= v < 27 and d <= 2.4: z = 'N'                                  # cou
            if (d / 10.4) ** 2 + ((v - 12) / 10.6) ** 2 <= 1 and v < 12: z = 'H'    # calotte
            # côtés du carré : collent aux joues, se resserrent vers le bas, 2 pointes par côté
            if 12 <= v:
                dout = 10.4 - (v - 12) * .17
                fin = 22.6 + 1.6 * (1 - tri((d - 6) / 2.3))
                if 6 <= d <= dout and v < fin: z = 'H'
            # visage : joues pleines jusqu'aux yeux, menton court et doux
            if 9 <= v < 22.6:
                hw = 7.3 if v < 16.5 else 7.3 * (1 - ((v - 16.5) / 6.3) ** 1.8) + .4
                if d <= hw: z = 'S'
            # frange : mèches en pointe, longueur irrégulière, raie décalée à droite
            if 4 <= v < 14 and d <= 8.2:
                ph = (s + 9.3) / 3.1
                bas = 13.2 - 2.4 * tri(ph) - (.9 if int(ph) % 2 else 0)
                if v < bas: z = 'H'
            if z: Z[y][x] = z
    for y in range(S):                                                             # bandeau
        for x in range(S):
            v = (y + .5) / u
            if 4.6 <= v < 5.6 + (.4 if S >= 48 else 0) and Z[y][x] == 'H': Z[y][x] = 'Y'
    return Z

def ombrer(Z, S):
    u = S / 32; c = S / 2 - .5
    G = [['.'] * S for _ in range(S)]
    dans = lambda x, y: 0 <= x < S and 0 <= y < S
    for y in range(S):
        for x in range(S):
            z = Z[y][x]
            if z == '.': continue
            s = (x - c) / u; v = (y + .5) / u
            if z == 'H':
                # forme : sphère éclairée en haut à gauche ; les côtés s'assombrissent vers le bas
                L = -s / 10.4 * .9 - (v - 9) / 14 * .6
                G[y][x] = 'a' if L > .55 else 'b' if L > -.35 else 'c'
            elif z == 'S': G[y][x] = '1' if s < 4.6 else '2'
            elif z == 'N': G[y][x] = '2'
            elif z == 'J': G[y][x] = 'r' if s < -7 else 'q' if s < 6 else 'p'
            elif z == 'Y': G[y][x] = 'Y'
    for y in range(S):
        for x in range(S):
            z = Z[y][x]; s = (x - c) / u; v = (y + .5) / u
            if z == 'S':      # ombre portée de la frange (épaisseur ≈ u) et des côtés
                if any(dans(x, y - k) and Z[y - k][x] == 'H' for k in range(1, max(1, round(u)) + 1)): G[y][x] = '2'
                if any(dans(x + dx, y) and Z[y][x + dx] == 'H' for dx in (-1, 1)) and v > 13: G[y][x] = '2'
            if z == 'N':      # ombre du menton sur le cou
                if any(dans(x, y - k) and Z[y - k][x] == 'S' for k in range(1, round(1.5 * u) + 1)): G[y][x] = '3'
            if z == 'H':
                # anneau de reflet cassé sur la calotte (sous le bandeau)
                r = ((s / 10.4) ** 2 + ((v - 12) / 10.6) ** 2) ** .5
                if .64 < r < .64 + .9 / (10.6 * u) + .04 and -7 < s < 3 and int((s + 20) * 1.3) % 3: G[y][x] = 'a'
                # mèches : lignes sombres qui suivent le flux sur les côtés
                if S >= 48 and v > 13 and abs(abs(s) - 8.3) < .5 / u + .05: G[y][x] = 'c' if s > 0 else 'b'
                # bout de mèche contre la peau en ton sombre (côté ombre) ou de base (côté lumière)
                if dans(x, y + 1) and Z[y + 1][x] == 'S': G[y][x] = 'c' if s > -2 else 'b'
    for y in range(S):        # col blanc en V
        for x in range(S):
            v = (y + .5) / u; d = abs(x - c) / u
            if Z[y][x] == 'J' and v >= 26 and 2.4 - (v - 26) * 1.2 < d < 4 - (v - 26) * .9: G[y][x] = 'W'
    for y in range(S):        # contour extérieur
        for x in range(S):
            if Z[y][x] == '.' and any(dans(x + dx, y + dy) and Z[y + dy][x + dx] != '.' for dx, dy in ((1, 0), (-1, 0), (0, 1), (0, -1))):
                G[y][x] = 'O'
    return G

def oeil(w, h, droite):
    """Recette d'œil par taille (C4-F) : paupière sombre, blanc bleuté, iris sombre en haut et
    clair en bas, pupille, reflet du côté de la lumière (gauche) sur les deux yeux."""
    g = [['.'] * w for _ in range(h)]
    blanc_ext = 1; blanc_int = 1 if w >= 6 else 0
    i0, i1 = (blanc_int, w - 1 - blanc_ext) if droite else (blanc_ext, w - 1 - blanc_int)
    iw = i1 - i0 + 1
    for x in range(w): g[0][x] = 'O'
    for y in range(1, h - 1):
        for x in range(w):
            if i0 <= x <= i1:
                t = (y - 1) / max(1, h - 3)
                g[y][x] = 'c' if t < .34 else 'b' if t < .75 else 'a'
            elif y < h - 2: g[y][x] = 'w'
    pw = 1 if iw <= 3 else 2
    p0 = i0 + (iw - pw) // 2 + (iw - pw) % 2
    for y in range(1, h - 2):
        for x in range(p0, p0 + pw): g[y][x] = 'E'
    if w >= 8:
        for x in range(1, w - 1): g[1][x] = 'p'           # paupière doublée d'un ton coloré
    rw = 1 if w < 6 else 2
    for y in range(1 + (1 if w >= 8 else 0), 1 + (1 if w >= 8 else 0) + rw):
        for x in range(i0, i0 + rw): g[y][x] = 'W'
    if h >= 6: g[h - 2][i1 - (1 if w >= 8 else 0)] = 'w'   # petit second reflet en bas, côté opposé
    for x in range(i0 + 1, i1): g[h - 1][x] = '3'          # paupière du bas fine et cassée
    g[h - 1][i0] = '.'; g[h - 1][i1] = '.'
    return g

TAILLE_OEIL = {32: (4, 4), 48: (6, 6), 64: (8, 8)}

def visage(G, S):
    u = S / 32; c = S / 2 - .5
    w, h = TAILLE_OEIL[S]
    y0 = round(14 * u)
    ecart = {32: 4, 48: 5, 64: 6}[S]                     # pixels de peau entre les deux yeux
    xg = round(c - ecart / 2) - w + 1; xd = round(c + ecart / 2)
    if S == 32: xd = round(c + ecart / 2) + 0
    for x0, dr in ((xg, False), (xd, True)):
        g = oeil(w, h, dr)
        for j in range(h):
            for i in range(w):
                if g[j][i] != '.': G[y0 + j][x0 + i] = g[j][i]
        cil = x0 + w if dr else x0 - 1                    # cil au coin extérieur
        G[y0][cil] = 'O'; G[y0 + 1][cil] = 'O' if S >= 48 else G[y0 + 1][cil]
        if S >= 64: G[y0 - 1][cil + (1 if dr else -1)] = 'O'
    if S >= 48:                                           # sourcils fins, visibles entre les mèches
        yb = y0 - round(1.6 * u)
        for x0 in (xg, xd):
            for i in range(1, w - 1):
                if G[yb][x0 + i] in '12': G[yb][x0 + i] = 'c'
        for x0 in (xg, xd + w - round(1.5 * u)):          # joues
            for i in range(round(1.5 * u)): G[y0 + h + 1][x0 + i] = 'k'
    xn = round(c); yn = round(18.4 * u)
    nez = {32: [(1, 0, '2')], 48: [(1, 0, '2'), (1, 1, '3')], 64: [(1, 0, '2'), (1, 1, '3'), (2, 1, '2')]}
    for dx, dy, ch in nez[S]: G[yn + dy][xn + dx] = ch
    yb = round(20.4 * u)
    bouche = {32: [(0, 0, '3')], 48: [(-1, 0, '3'), (0, 0, 'd'), (1, 0, '3')],
              64: [(-2, 0, '3'), (-1, 0, 'd'), (0, 0, 'd'), (1, 0, 'd'), (2, 0, '3'), (0, 1, '2')]}
    for dx, dy, ch in bouche[S]: G[yb + dy][round(c) + dx] = ch
    return G

def portrait(S, etape=99):
    Z = zones(S)
    if etape == 1: return chaine([['#' if ch != '.' else '.' for ch in r] for r in Z])
    G = ombrer(Z, S)
    if etape == 2: return chaine(G)
    return chaine(visage(G, S))

P32, P48, P64 = portrait(32), portrait(48), portrait(64)
