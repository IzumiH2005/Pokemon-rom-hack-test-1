"""Écrit colonnes/c_couchee.txt : colonne couchée nord-sud, vue plongeante (~30°).
Relevé sur un modèle three.js (cylindre couché, joints, bout sud cassé) : vus d'en haut,
le bout nord et les joints sont des arcs en ∩ (on voit le dessus des anneaux verticaux),
les pans du fût deviennent des bandes en long. La section cassée du sud reprend les
rangées tracées à la main (46 à 61) ; ses coins hauts sont couverts par le fût, ce qui
donne au bord de la cassure le même arc que les joints."""
import math
W, C = 22, 11.0
FUT = 'DBBmWWWWWBLLLmnnddDO'           # tons du fût, x1..x20
F = 5                                   # flèche des arcs, relevée sur le rendu 3D (~1/4 de la largeur)
def arc(x, fleche):                     # décalage vers le bas d'un arc ∩ de flèche donnée
    u = (x + .5 - C) / 11
    return round(fleche - fleche * math.sqrt(max(0, 1 - u * u)))
SECTION = [
 "OOWWWWWWWWWmmmmmmmmmOO", "OmWWWWWWLLLLLmmmmmmmmO", "OmWWWWLLLLLmmmmdmmmmmO",
 "OmWWWLLLLDmmmmmmdmmmmO", "OmmmmLLLmmDmmmmmdmmmmO", "OmmmLLLmmmDmmmmmmdmmmO",
 "OmmmLLDmmmmDmmmmmmmmmO", "OmmmmmmDmmmmDmmmmmmmmO", "OmnnnnnnnnnnDnnnnnnnmO",
 "OmmnnnnnnnnnDnnnnnnmmO", "OmmmnnnnnnnDnnnnnnmmmO", ".OmmmddddddDdddddmmmO.",
 "..OOmmmddddddddmmmOO..", "....OOmmmmmmmmmmOO....", "......OOOOOOOOOO......"]
g = [['.'] * 24 for _ in range(62)]
# fût : de l'arc nord (rangée 0 au centre) jusqu'à la cassure
for x in range(W):
    for y in range(arc(x, F), 46 + arc(x, F)):
        g[y][x] = 'O' if x in (0, W - 1) or y == arc(x, F) else FUT[x - 1]
# joints en ∩ : trait n (D sur le flanc droit), reflet W dessous côté éclairé
for J in (15, 30):
    for x in range(1, W - 1):
        y = J + arc(x, F)
        g[y][x] = 'D' if x >= 18 else 'n'
        if 2 <= x <= 7: g[y + 1][x] = 'W'
# section cassée : posée sous l'arc ; les pixels transparents des coins laissent le fût
for i, r in enumerate(SECTION):
    for x, c in enumerate(r):
        if c != '.' and 46 + i > 46 + arc(x, F): g[46 + i][x] = c
# bord de la cassure : même arc que les joints, trait D
for x in range(1, W - 1): g[46 + arc(x, F)][x] = 'D'
# contour des flancs, du bout nord jusqu'au bas arrondi de la section
for y in range(arc(0, F), 57): g[y][0] = g[y][W - 1] = 'O'
# ombre portée à droite et au sud
for y in range(2, 59): g[y][22] = 'g'
for y in range(3, 60): g[y][23] = 'g'
for x in range(7, 19): g[61][x] = 'g'
cmds = []
for y, r in enumerate(g):
    x = 0
    while x < 24:
        if r[x] == '.': x += 1; continue
        e = x
        while e + 1 < 24 and r[e + 1] == r[x]: e += 1
        cmds.append(f'hline {r[x]} {x} {e} {y}'); x = e + 1
open('colonnes/c_couchee.txt', 'w').write('# colonne couchée, écrite par geo_couchee.py\n' + '\n'.join(cmds) + '\n')
