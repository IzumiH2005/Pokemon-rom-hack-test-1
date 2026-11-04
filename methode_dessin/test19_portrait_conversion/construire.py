"""Reconstruit le portrait calque par calque (128x128).

Chaque calque est une petite liste de formes posées à la main (fNN_*.txt,
lues par ../outils/formes.py) ou de rangées de pixels (cNN_*.txt, lues par
../outils/peindre.py). L'illustration source n'est pas dans le dépôt.
Usage : python3 construire.py
"""
import subprocess, sys

F, P = '../outils/formes.py', '../outils/peindre.py'
ETAPES = [
    ('NEW:128x128', 'calque01.txt', F, 'f01_silhouettes.txt'),
    ('calque01.txt', 'calque02.txt', F, 'f02_peau.txt'),
    ('calque02.txt', 'calque03.txt', F, 'f03_meches.txt'),
    ('calque03.txt', '_a.txt', F, 'f04_traits.txt'),
    ('_a.txt', '_b.txt', P, 'c30_yeux.txt'),
    ('_b.txt', '_c.txt', F, 'f025_sourcils.txt'),
    ('_c.txt', 'calque04.txt', P, 'c31_bouche.txt'),
    ('calque04.txt', 'calque05.txt', F, 'f05_cheveux.txt'),
    ('calque05.txt', 'calque06.txt', F, 'f06_cou_kimono.txt'),
    ('calque06.txt', 'calque07.txt', F, 'f07_sang.txt'),
    ('calque07.txt', 'portrait.txt', F, 'f08_contour.txt'),
]
for src, dst, outil, cmds in ETAPES:
    subprocess.run([sys.executable, outil, src, dst, cmds], check=True)
for t in ('_a.txt', '_b.txt', '_c.txt'):
    subprocess.run(['rm', '-f', t])
