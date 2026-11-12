"""Commandes des trois panneaux sertis (biseau de 4 unités, R6). Formes décidées :
dessus = losange (31,8) (10,18) (52,18) (31,28) ; gauche x 6..26, haut 23+(x-2)//2 ;
droite x 36..56, haut 23+(60-x)//2 ; 20 rangées. Remplissage seulement (R3).
Usage : python3 panneaux.py HAUT GAUCHE DROITE"""
import sys
h,g,d=sys.argv[1:4]
for y in range(8,29):
    k = y-8 if y<=18 else 28-y
    print(f'hline {h} {30-2*k} {32+2*k} {y}')
for x in range(6,27):
    y0=23+(x-2)//2; print(f'vline {g} {x} {y0} {y0+19}')
for x in range(36,57):
    y0=23+(60-x)//2; print(f'vline {d} {x} {y0} {y0+19}')
