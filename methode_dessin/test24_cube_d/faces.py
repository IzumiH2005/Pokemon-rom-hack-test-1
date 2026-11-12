"""Écrit les commandes qui remplissent les trois faces décidées (R3 : remplir une forme
décidée). Sommets : arrière (31,4), gauche (2,18), droite (60,18), avant (31,32),
bas (31,60). Arêtes 2:1 en marches de 2 px exactement.
Usage : python3 faces.py HAUT GAUCHE DROITE > cXX.txt"""
import sys
h,g,d=sys.argv[1:4]
print('# dessus : rangées 4..32, marches de 2 px')
for y in range(4,33):
    k = y-4 if y<=18 else 32-y
    print(f'hline {h} {30-2*k+ (0)} {32+2*k} {y}'.replace(f' {30-2*k} ',f' {max(2,30-2*k)} ').replace(f' {32+2*k} ',f' {min(60,32+2*k)} '))
print('# côtés : une colonne par x, 28 px sous le bord du dessus')
for x in range(2,31):
    y0 = 18+(x-2)//2+1
    print(f'vline {g} {x} {y0} {y0+27}')
for x in range(32,61):
    y0 = 18+(60-x)//2+1
    print(f'vline {d} {x} {y0} {y0+27}')
print(f'vline {g} 31 33 60')
