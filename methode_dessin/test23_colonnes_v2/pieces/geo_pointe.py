"""Écrit pieces/c_pointe.txt : lame et collier d'une colonne pointue, vue plongeante (~30°).
Géométrie relevée sur un modèle three.js : lame conique à 8 facettes, pointe centrée,
hauteur 1,9 fois le rayon, posée sur un collier rond dont on voit le dessus en ellipse.
Vue de face, la lame fait /\\ : côté gauche clair, facette avant moyenne, côté droit sombre.
Chaque règle (largeur par rangée, frontières de facettes, ellipses) est décidée ici ;
trace.py ne fait que poser les segments.
Le script donne les rangées 0 à 12 (lame) ; les rangées 13 à 24 (entrée de la lame dans le
collier, dessus et lèvre du collier) sont tracées à la main dans pointe.txt (22x25)."""
import math
W, C = 22, 11.0                    # pièce 22 de large, axe entre x10 et x11
HAUT = 24
# collier : dessus en ellipse, lèvre de 3 px teintée comme le fût
CA, CB, CY = 11.0, 3.5, 15.5
LEVRE = 3
FUT = 'DBBmWWWWWBLLLmnnddDD'       # tons du fût par colonne x1..x20 ; x0 et x21 font le contour
# lame : rangée 0 = pointe (2 px), demi-largeur +3 toutes les 5 rangées jusqu'à 8 (rangée 12) ;
# hauteur vue ~0,85 fois la largeur, comme le cône du modèle (1,9 x rayon) vu à 30°
# base de la lame : ellipse plus petite que le dessus du collier, même centre en x
LA, LB, LY = 8.5, 2.3, 14.5
# tons des facettes selon la distance à l'axe (fraction de la demi-largeur), symétriques
def ton(f, gauche):
    if f < 0.36: return 'B'
    if f < 0.78: return 'L' if gauche else 'n'
    return 'W' if gauche else 'd'

g = [['.'] * W for _ in range(HAUT)]
def bas_ellipse(x, a, b, cy):
    u = (x + .5 - C) / a
    return None if abs(u) > 1 else cy + b * math.sqrt(1 - u * u)
def haut_ellipse(x, a, b, cy):
    u = (x + .5 - C) / a
    return None if abs(u) > 1 else cy - b * math.sqrt(1 - u * u)

# 1. collier : dessus W, bord avant L, lèvre aux tons du fût, contour O
for x in range(W):
    yt, yb = haut_ellipse(x, CA, CB, CY), bas_ellipse(x, CA, CB, CY)
    if yt is None: continue
    yt, yb = round(yt), round(yb)
    for y in range(yt, yb + 1): g[y][x] = 'W'
    g[yt - 1][x] = 'O'
    g[yb][x] = 'L'
    for y in range(yb + 1, yb + LEVRE + 1): g[y][x] = FUT[min(19, max(0, x - 1))]
    g[yb + LEVRE + 1][x] = 'O'
    if x in (0, W - 1):
        for y in range(yt - 1, yb + LEVRE + 2): g[y][x] = 'O'

# 2. lame, coupée en bas par l'ellipse de sa base
for y in range(0, 18):
    h = min(8, 1 + 3 * y // 5)
    for x in range(10 - h, 12 + h):
        yb = bas_ellipse(x, LA, LB, LY)
        if yb is None or y > round(yb): continue
        if y == 0: c = 'O' if x in (10, 11) else None
        elif x in (10 - h, 11 + h): c = 'O'
        else:
            k = (10 - x) if x <= 10 else (x - 11)
            c = ton((k + .5) / h, x <= 10)
        if c: g[y][x] = c

# 3. ombre portée par la lame sur le dessus du collier : un pixel sous l'arc de sa base
for x in range(W):
    yb = bas_ellipse(x, LA, LB, LY)
    if yb is None: continue
    yb = round(yb)
    u = abs(x + .5 - C) / LA
    # pli sombre au contact : d sur les côtés, n devant ; contour O au bas des deux colonnes extrêmes
    if g[yb + 1][x] in 'WL': g[yb + 1][x] = 'd' if u > .6 else 'n'
    if u > .75: g[yb][x] = 'O'

# commandes : un segment hline par suite de même ton
cmds = []
for y, r in enumerate(g):
    x = 0
    while x < W:
        if r[x] == '.': x += 1; continue
        e = x
        while e + 1 < W and r[e + 1] == r[x]: e += 1
        cmds.append(f'hline {r[x]} {x} {e} {y}')
        x = e + 1
open('pieces/c_pointe.txt', 'w').write('# lame et collier, écrits par geo_pointe.py\n' + '\n'.join(cmds) + '\n')
