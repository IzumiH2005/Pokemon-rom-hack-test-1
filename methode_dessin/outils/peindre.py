"""Pose des chaînes de pixels décidées à la main (R3 : ne calcule rien).
Usage : python3 peindre.py in.txt|NEW:128x128 out.txt cmds.txt
Lignes : y x chaine     -> écrit 'chaine' à partir de (x, y) ; '.' = laisse tel quel.
         '#' = commentaire.
"""
import sys
sys.path.insert(0, __file__.rsplit('/', 1)[0])
from trace import lire, ecrire
G = lire(sys.argv[1])
for l in open(sys.argv[3]):
    l = l.split('#')[0].split()
    if len(l) != 3:
        continue
    y, x, s = int(l[0]), int(l[1]), l[2]
    for i, c in enumerate(s):
        if c != '.' and 0 <= x + i < len(G[0]):
            G[y][x + i] = c
ecrire(G, sys.argv[2])
