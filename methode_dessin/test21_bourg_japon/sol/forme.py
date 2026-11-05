"""Ecrit les hline de la forme d'autotile decidee (R3 : les valeurs ci-dessous sont mes decisions).
usage: forme.py bloc|interieur LETTRE > cXX.txt
bloc 48x48 : bords a MARGE px + ondulation ONDE (periode 8, ONDE[0]=ONDE[7]=0 pour raccorder les quarts),
             coins arrondis rayon RAYON centres sur le coin du quart exterieur.
interieur 32x32 : tout plein sauf un quart de cercle d'herbe de rayon RAYON au point (16,16).
"""
import sys
MARGE, RAYON = 4, 4.5
ONDE = [0, 0, 1, 1, 2, 1, 1, 0]   # R5 : [0,0,1,1,1,1,0,0] faisait des creneaux
kind, L = sys.argv[1], sys.argv[2]
def plein_bloc(x, y):
    cx = x < 8 or x >= 40; cy = y < 8 or y >= 40
    if cx and cy:
        ox = 8 if x < 8 else 40; oy = 8 if y < 8 else 40
        return (x + .5 - ox) ** 2 + (y + .5 - oy) ** 2 <= RAYON ** 2 or (abs(x + .5 - ox) < 0 )
    if y < 8 and y < MARGE + ONDE[x % 8]: return False
    if y >= 40 and 47 - y < MARGE + ONDE[x % 8]: return False
    if x < 8 and x < MARGE + ONDE[y % 8]: return False
    if x >= 40 and 47 - x < MARGE + ONDE[y % 8]: return False
    return True
def plein_int(x, y):
    return (x + .5 - 16) ** 2 + (y + .5 - 16) ** 2 > RAYON ** 2
f, n = (plein_bloc, 48) if kind == 'bloc' else (plein_int, 32)
print(f'# {kind} : forme decidee (marge {MARGE}, onde {ONDE}, rayon {RAYON})')
for y in range(n):
    x = 0
    while x < n:
        if f(x, y):
            x0 = x
            while x < n and f(x, y): x += 1
            print(f'hline {L} {x0} {x-1} {y}')
        else: x += 1
