# Panache spectral : 3 rubans en S posés point par point (x, y, rayon), du fond vers le devant.
# Usage : python3 c21_panache.py calque21_panache.txt
import sys, os; sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', 'outils'))
from tube import peindre, coeur
G = [['.'] * 128 for _ in range(128)]
bas    = [(58,6,0.7),(54,10,0.6),(51,13,0.4),(50,15.5,0.2),(52,16.5,0)]          # mèche courte, pointe relevée
milieu = [(56,4,1.0),(50,7,1.0),(45,10.5,0.9),(40,13,0.7),(34,14,0.5),(29,13,0.3),(26,11,0.1),(26,9.5,0)]
haut   = [(62,2,1.2),(55,1,1.4),(47,2,1.4),(41,5,1.3),(36,8,1.1),(30,9,0.9),(24,7.5,0.7),(19,5,0.5),(14,4,0.3),(10,5,0.1),(8,7,0)]
for b in (bas, milieu, haut):
    peindre(G, b); coeur(G, b)
open(sys.argv[1], 'w').write('\n'.join(''.join(r) for r in G) + '\n')
