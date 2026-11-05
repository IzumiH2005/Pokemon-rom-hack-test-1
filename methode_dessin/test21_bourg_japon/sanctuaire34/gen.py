"""Sanctuaire 3/4 vue de dessus (80x64). Toit a pignons (kirizuma) : pan avant vu de dessus,
mince pan arriere, chigi aux bouts, katsuogi sur le faitage. Facade courte, plateforme de pierre."""
import subprocess, sys
W, H = 80, 64
OUT = '/home/user/Pokemon-rom-hack-test-1/methode_dessin/outils/'
G = [['.'] * W for _ in range(H)]
def put(c, x, y):
    if 0 <= x < W and 0 <= y < H: G[y][x] = c
def rect(c, x1, y1, x2, y2):
    for y in range(y1, y2 + 1):
        for x in range(x1, x2 + 1): put(c, x, y)
def el(y): return round(6 - (y - 9) * 4 / 26)     # rive gauche du pan avant (s'evase vers l'egout)
def er(y): return 79 - el(y)
KAT = (21, 32, 44, 55)                             # katsuogi (x gauche, 3 px)

def step(name, note, f):
    before = [r[:] for r in G]; f()
    cmds = [f'# {name} : {note}']
    for y in range(H):
        x = 0
        while x < W:
            if G[y][x] != before[y][x]:
                c = G[y][x]; x2 = x
                while x2 + 1 < W and G[y][x2 + 1] == c and G[y][x2 + 1] != before[y][x2 + 1]: x2 += 1
                cmds.append(f'hline {c} {x} {x2} {y}' if c != '.' else f'rect . {x} {y} {x2} {y}')
                x = x2 + 1
            else: x += 1
    open(f'{name}.txt', 'w').write('\n'.join(cmds) + '\n')
    e = 'e' + name[1:]
    open(f'{e}.txt', 'w').write('\n'.join(''.join(r) for r in G) + '\n')
    subprocess.run(['python3', OUT + 'px.py', f'{e}.txt', '8', 'palette.json'], check=True)

def s01():   # construction : masses (toit / facade / plateforme / marches)
    rect('i', 8, 4, 71, 8)                          # pan arriere
    for y in range(9, 37): rect('h', el(y), y, er(y), y)
    for x in KAT: rect('w', x, 3, x + 3, 10)        # katsuogi : rondins en travers du faitage
    for cx in (7, 72):                              # chigi : planches croisees en V au bout du faitage
        for k in range(8):
            for d in (0, 1):
                put('h', cx - k // 2 * 1 - k // 2 + d - 1, 8 - k) if False else None
        for k in range(8):
            y = 8 - k; a = cx - (k + 1) // 2 - k // 4; b = cx + 1 + (k + 1) // 2 + k // 4
            for d in (0, 1): put('h', a - d, y); put('h', b + d, y)
    rect('Q', 7, 37, 72, 50)
    rect('q', 2, 50, 77, 52); rect('s', 2, 53, 77, 57)
    rect('q', 29, 58, 50, 63)

def s02():   # aplats par matiere
    rect('j', 8, 4, 71, 5)                          # pan arriere eclaire
    rect('j', 8, 7, 71, 7); rect('g', 8, 8, 71, 8)  # faitage (cylindre)
    for x in KAT: rect('w', x, 3, x + 3, 10)        # les rondins passent par-dessus le faitage
    for x in (8, 28, 49, 69): rect('l', x, 37, x + 2, 50)   # piliers vermillon
    rect('t', 31, 39, 48, 50)                       # baie centrale ouverte (interieur sombre)
    rect('Q', 11, 41, 27, 49); rect('Q', 52, 41, 68, 49)    # panneaux blancs
    rect('l', 7, 37, 72, 38)                        # poutre haute rouge
    rect('w', 34, 45, 45, 50)                       # tronc a offrandes
    for y in range(58, 64): rect('q' if y % 2 == 0 else 's', 29, y, 50, y)

def s03():   # lumiere haut-gauche
    for y in range(9, 37):                          # pan avant : bord gauche clair, bord droit sombre
        put('i', el(y), y); put('i', el(y) + 1, y); put('g', er(y), y); put('g', er(y) - 1, y)
    rect('i', 7, 9, 72, 10)                         # reflet sous le faitage
    for x in (8, 28, 49, 69):
        rect('m', x, 39, x, 50); rect('k', x + 2, 39, x + 2, 50)
    rect('k', 7, 39, 72, 40)                        # ombre de l'avant-toit sur la facade
    rect('O', 31, 39, 48, 39)                       # fond de la baie : ombre sous la poutre
    rect('z', 34, 45, 45, 45); rect('t', 45, 46, 45, 50)   # tronc : dessus clair, cote ombre
    rect('j', 2, 50, 77, 50)                        # arete de la plateforme
    for x in KAT:                                   # rondin : dessus clair, cote droit sombre, bouts dores
        rect('z', x, 3, x + 3, 3); rect('z', x, 10, x + 3, 10); rect('t', x + 3, 4, x + 3, 9); rect('z', x, 4, x, 9)
    for cx in (7, 72):
        for k in range(8):
            y = 8 - k; a = cx - (k + 1) // 2 - k // 4
            put('j', a - 1, y)

def s04():   # contour
    open('_t.txt', 'w').write('\n'.join(''.join(r) for r in G) + '\n')
    subprocess.run(['python3', OUT + 'contour.py', '_t.txt', '_t.txt'], check=True)
    T = [list(l.rstrip('\n')) for l in open('_t.txt')]
    for y in range(H):
        for x in range(W):
            if T[y][x] == 'O' and G[y][x] != 'O':
                c = 'O'
                if y < 37 and (x < 40 and y < 12 or x <= el(y)): c = 'g'      # rive eclairee : trait couleur
                if y >= 50: c = 'A' if y >= 53 else 'O'
                put(c, x, y)
    for x in KAT: rect('g', x + 1, 11, x + 4, 11)   # ombre des katsuogi sur le pan

def s05():   # details
    for y in range(11, 34):                         # cannelures de cuivre (bandes)
        for x in range(el(y) + 2, er(y) - 1):
            if x % 4 == 1: put('g', x, y)
    for y in range(11, 34):                         # reflet d'arete a gauche de chaque cannelure
        for x in range(el(y) + 2, er(y) - 1):
            if x % 4 == 2 and y < 16: put('i', x, y)
    rect('j', el(34) + 1, 34, er(34) - 1, 34)       # rive d'egout : arete claire
    rect('g', el(35), 35, er(35), 35)
    for x in (2, 3, 76, 77): put('j', x, 34)        # coins releves
    for x in range(34, 46, 3): put('t', x, 47); put('t', x + 1, 47)    # grille du tronc
    for x in range(31, 49):                         # shimenawa : corde torsadee, plus epaisse au centre
        sag = 1 if 35 <= x <= 44 else 0
        put('z' if x % 2 else 'w', x, 40 + sag); put('w' if x % 2 else 'z', x, 41 + sag)
        if 37 <= x <= 42: put('w', x, 42 + sag)
    for x in (34, 39, 44):                          # shide : bandes de papier blanc
        rect('Q', x, 43, x, 45); put('q', x + 1, 44)
    for x in (13, 21, 54, 62): rect('q', x, 42, x, 48)   # montants des panneaux
    rect('q', 11, 45, 27, 45); rect('q', 52, 45, 68, 45)
    for x in range(10, 77, 12): rect('A', x, 54, x, 56)   # joints de pierre
    for x in range(4, 77, 12): rect('A', x, 51, x, 52) if 8 < x < 72 else None
    for x in KAT: put('j', x, 3); put('Q', x, 4) if False else None

def s06():   # nettoyage
    for x in KAT: put('O', x - 1, 4) if G[4][x - 1] == '.' else None

for n, note, f in (('c01', 'construction', s01), ('c02', 'aplats par matiere', s02), ('c03', 'lumiere', s03),
                   ('c04', 'contour', s04), ('c05', 'details', s05), ('c06', 'nettoyage', s06)):
    step(n, note, f)
import os; os.remove('_t.txt')
