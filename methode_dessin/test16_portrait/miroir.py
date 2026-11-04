"""Miroir mécanique de commandes trace.py autour de l'axe x = 64,5 (x' = 129 - x).
Ne décide rien : recopie à droite ce qui a été posé à la main à gauche.
Usage : python3 miroir.py gauche.txt > droite.txt"""
import sys
for l in open(sys.argv[1]):
    t = l.split('#')[0].split()
    if not t:
        continue
    op, c, a = t[0], t[1], list(map(int, t[2:]))
    m = lambda x: 129 - x
    if op == 'px':
        a = sum([[m(x), y] for x, y in zip(a[::2], a[1::2])], [])
    elif op == 'hline':
        a = [m(a[1]), m(a[0]), a[2]]
    elif op == 'vline':
        a = [m(a[0])] + a[1:]
    elif op in ('rect', 'frame'):
        a = [m(a[2]), a[1], m(a[0]), a[3]]
    elif op == 'rows':
        a = [a[0]] + sum([[m(x2), m(x1)] for x1, x2 in zip(a[1::2], a[2::2])], [])
    print(op, c, *a)
