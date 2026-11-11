"""Écrit pieces/pointe.txt (22 de large) : lame conique et bague d'une colonne pointue, vue à 30°.
Géométrie reprise du modèle three.js (rayon du fût = 10 px) :
  cône à 8 facettes, rayon 10, hauteur 1,9 x rayon, une arête tournée vers l'avant ;
  bague de rayon 11, épaisseur 0,3 x rayon, posée sous le cône.
À 30°, un cercle de rayon r se voit en ellipse r x r/2, et une hauteur h se voit 0,87 h.
Chaque règle est décidée ici ; les retouches de détail se font ensuite dans pointe.txt."""
import math
W, C = 22, 11.0                     # axe entre x10 et x11
HL = 1.9 * 10 * .866                # hauteur vue de la lame : 16,5 px
CY = HL                             # centre de l'ellipse de base du cône (apex en y = 0)
RA, RB = 10.0, 5.0                  # ellipse de base du cône
BA, BB = 11.0, 5.5                  # dessus de la bague
BY2 = CY + 2.6                      # centre de l'ellipse du bas de la bague
HAUT = 26
# sortie : pointe_geo.txt ; pointe.txt en reprend les rangées 0 à 13 et trace le reste à la main
FUT = 'DBBmWWWWWBLLLmnnddDO'        # tons du fût, x1..x20
# tons des quatre facettes vues, de gauche à droite (lumière en haut à gauche)
FACETTES = 'WLnd'

def facette(X, Y):
    """angle (degrés) du point de base visé depuis l'apex, ou None hors du cône"""
    best = None
    for i in range(-900, 901):
        p = math.radians(i / 10)
        bx, by = RA * math.sin(p), CY + RB * math.cos(p)
        s = Y / by
        if s <= 0 or s > 1.0001: continue
        e = abs(s * bx - X)
        if best is None or e < best[0]: best = (e, i / 10)
    return best[1] if best and best[0] < .5 else None

def dans_cone(X, Y):
    if Y < 0: return False
    tx, ty = RA * math.sqrt(1 - (RB / CY) ** 2), CY - RB * RB / CY   # points de tangence
    if Y <= ty: return abs(X) <= tx * Y / ty
    u = X / RA
    return abs(u) <= 1 and Y <= CY + RB * math.sqrt(1 - u * u)

def dans_ellipse(X, Y, a, b, cy):
    u = X / a
    return abs(u) <= 1 and abs(Y - cy) <= b * math.sqrt(1 - u * u)

g = [['.'] * W for _ in range(HAUT)]
for y in range(HAUT):
    for x in range(W):
        X, Y = x + .5 - C, y + 1.5         # apex dans la rangée 0
        if dans_cone(X, Y):
            f = facette(X, Y)
            k = 0 if f is None or f < -45 else 1 if f < 0 else 2 if f < 45 else 3
            g[y][x] = FACETTES[k]
        elif dans_ellipse(X, Y, BA, BB, CY):
            g[y][x] = 'W'                                   # rebord du dessus de la bague
        elif abs(X) <= BA and Y > CY and (dans_ellipse(X, Y, BA, BB, BY2) or Y < BY2):
            g[y][x] = FUT[min(19, max(0, x - 1))]           # flanc de la bague
# pli à la base du cône, là où il touche le rebord ou le flanc de la bague
for y in range(HAUT - 1):
    for x in range(W):
        if g[y][x] in FACETTES and g[y + 1][x] not in FACETTES + '.':
            g[y][x] = 'd' if x <= 10 else 'D'
# contour : tout pixel posé qui touche le vide
out = [r[:] for r in g]
for y in range(HAUT):
    for x in range(W):
        if g[y][x] == '.': continue
        for dx, dy in ((1, 0), (-1, 0), (0, 1), (0, -1)):
            xx, yy = x + dx, y + dy
            if not (0 <= xx < W and 0 <= yy < HAUT) or g[yy][xx] == '.':
                if not (dy == 1 and yy >= HAUT): out[y][x] = 'O'
open('pieces/pointe_geo.txt', 'w').write('\n'.join(''.join(r) for r in out) + '\n')
