"""Écrit pieces/c_pointe.txt : commandes de la lame et du collier en vue plongeante (~25°).
# Le script pose la lame (rangées 0 à 31) ; collier (32 à 43) retouché à la main dans pointe.txt.
Géométrie relevée sur un modèle three.js (colonne à 16 pans, lame à 7 facettes, pointe
décalée) ; les sommets, les couleurs de facette et l'ordre de pose sont décidés ici, trace.py
ne fait que remplir les rangées et tirer les segments donnés."""
import math
W, CX, CY = 22, 10.5, 36          # pièce 22 de large ; centre de l'ellipse du collier
A, B = 11, 4                      # demi-axes du dessus du collier
LIP = 3                           # épaisseur visible du collier
a, b, cyb = 9.5, 3.2, 35.0        # base de la lame, posée sur le collier
APEX = (14.0, 1.0)                # pointe, décalée à droite et vers l'arrière
N, T0 = 7, 0.35
# couleur de chaque facette selon l'angle de sa normale (0 = droite, pi/2 = devant)
def teinte(phi):
    # lumière venue d'en haut à gauche et de devant
    l = -math.cos(phi) * 0.9 + math.sin(phi) * 0.2
    for s, c in [(0.55, 'W'), (0.3, 'L'), (0.05, 'B'), (-0.2, 'm'), (-0.45, 'n'), (-0.7, 'd')]:
        if l > s: return c
    return 'D'
cmds = []
def tri(c, p, q, r):
    ys = range(math.floor(min(p[1], q[1], r[1])), math.ceil(max(p[1], q[1], r[1])) + 1)
    for y in ys:
        xs = []
        for (x1, y1), (x2, y2) in ((p, q), (q, r), (r, p)):
            if (y1 <= y + .5 < y2) or (y2 <= y + .5 < y1):
                xs.append(x1 + (y + .5 - y1) * (x2 - x1) / (y2 - y1))
        if len(xs) >= 2:
            x1, x2 = round(min(xs)), round(max(xs)) - 1
            if x2 >= x1: cmds.append(f'hline {c} {x1} {x2} {y}')
# collier : dessus clair, rebord arrière éclairé, lèvre avant teintée comme le fût
FUT = 'DBBmWWWWWBLLLmnnddDO'
for x in range(W):
    dx = (x + .5 - CX) / A
    if abs(dx) > 1: continue
    h = B * math.sqrt(1 - dx * dx)
    yt, yb = round(CY - h), round(CY + h)
    cmds.append(f'vline W {x} {yt} {yb}')
    cmds.append(f'px L {x} {yb}')
    cmds.append(f'px O {x} {yt - 1}')
    c = FUT[min(19, max(0, x - 1))]
    cmds.append(f'vline {c} {x} {yb + 1} {yb + LIP - 1}')
    cmds.append(f'px O {x} {yb + LIP}')
cmds.append(f'vline O 0 {CY - 1} {CY + LIP}')
cmds.append(f'vline O {W - 1} {CY - 1} {CY + LIP}')
# lame : facettes de l'arrière vers l'avant
v = [(CX + a * math.cos(T0 + k * 2 * math.pi / N), cyb + b * math.sin(T0 + k * 2 * math.pi / N)) for k in range(N)]
fac = sorted(range(N), key=lambda k: math.sin(T0 + (k + .5) * 2 * math.pi / N))
# tons des facettes vues (normale vers l'avant), de gauche à droite : W, m, d (4 vues : W, B, n, d)
mid = {k: T0 + (k + .5) * 2 * math.pi / N for k in range(N)}
vues = sorted([k for k in range(N) if math.sin(mid[k]) > -0.25], key=lambda k: math.cos(mid[k]))
TONS = {1: 'm', 2: 'Wd', 3: 'Wmd', 4: 'WBnd', 5: 'WBmnd'}[len(vues)]
ton = {k: TONS[i] for i, k in enumerate(vues)}
for k in fac:
    tri(ton.get(k, 'D'), APEX, v[k], v[(k + 1) % N])
# ombre au pied de la lame : arc avant de sa base
for x in range(1, W - 1):
    dx = (x + .5 - CX) / a
    if abs(dx) <= 1:
        cmds.append(f'px n {x} {round(cyb + b * math.sqrt(1 - dx * dx)) + 1}')
# contour : les deux arêtes extrêmes et l'arc avant
g = min(v, key=lambda p: p[0]); d = max(v, key=lambda p: p[0])
cmds.append(f'line O {round(APEX[0])} {round(APEX[1])} {round(g[0])-1} {round(g[1])}')
cmds.append(f'line O {round(APEX[0])} {round(APEX[1])} {round(d[0])} {round(d[1])}')
open('pieces/c_pointe.txt', 'w').write('# lame et collier, écrits par geo_pointe.py\n' + '\n'.join(cmds) + '\n')
