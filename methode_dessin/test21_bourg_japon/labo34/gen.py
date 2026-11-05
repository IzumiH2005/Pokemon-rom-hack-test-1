"""Labo 3/4 vue de dessus (112x80). Chaque etape modifie la grille ; cXX.txt = les px poses
(runs horizontaux), eXX.txt = l'etat. Toit 0-47 (60 %), mur 48-76, marche 77-79."""
import subprocess, sys
W, H = 112, 80
OUT = '/home/user/Pokemon-rom-hack-test-1/methode_dessin/outils/'
G = [['.'] * W for _ in range(H)]
def xl(y): return round(16 + (1 - 16) * (y - 9) / 38)
def xr(y): return round(95 + (110 - 95) * (y - 9) / 38)
GX = 71.5                       # axe du pignon
# petit toit vu de dessus : noues en V depuis y16, puis rives verticales x57/86 (faitage vers nous)
def gl(y): return max(57, round(71 - (y - 16) * 1.4))
def gr(y): return min(86, round(72 + (y - 16) * 1.4))
def bl(y): return round(71 - (y - 30) * 14 / 8)            # planches de rive y30..38
def br(y): return round(72 + (y - 30) * 14 / 8)
OLD = [l.rstrip('\n') for l in open('../labo/etape06_final.txt')]
WALL = [OLD[y] for y in range(44, 80) if y not in (46, 50, 71, 72)]   # 32 rangs -> y48..79

steps = []
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
    steps.append(e)

def put(c, x, y):
    if 0 <= x < W and 0 <= y < H: G[y][x] = c

def s02():   # aplats par matiere
    for y in range(3, 48):
        for x in range(1, 111): put('C', x, y)
    for y, (a, b) in zip(range(3, 9), ((1, 110), (4, 108), (6, 105), (8, 102), (11, 100), (14, 98))):
        for x in range(1, 111): put('D' if a <= x <= b else '.', x, y)
    for y in range(8, 11):
        for x in range(16, 96): put('CBA'[y - 8], x, y)
    for y in range(11, 48):
        for x in range(1, xl(y) + 1): put('D', x, y)       # croupe gauche eclairee
        for x in range(xr(y), 111): put('B', x, y)         # croupe droite ombre
    for y in range(16, 39):                                # petit toit du pignon
        for x in range(gl(y), gr(y) + 1): put('D' if x <= 71 else 'B', x, y)
    for y in range(31, 39):                                # face triangulaire bois
        for x in range(bl(y) + 1, br(y)): put('w', x, y)
    for y in range(44, 48):
        for x in range(1, 111): put('C', x, y)
    for i, r in enumerate(WALL):
        for x, c in enumerate(r): put(c, x, 48 + i)

def s03():   # lumiere haut-gauche
    for y in range(40, 45):
        for x in range(1, xl(y) + 1):
            if G[y][x] == 'D': put('C', x, y)
        for x in range(xr(y), 111):
            if G[y][x] == 'B': put('A', x, y)
    for y in range(31, 39):                                # face : moitie droite a l'ombre
        for x in range(72, br(y)): put('v', x, y)
    for x in range(56, 88): put('B', x, 39)                # ombre portee sous le pignon
    for y in range(24, 40): put('B', 87, y); put('B', 88, y)  # et a sa droite
    for x in range(1, 111): put('B', x, 46)
    for x in range(1, 111): put('A', x, 47)

def s04():   # contour : trait O dehors, selout A/B sur le toit
    open('_t.txt', 'w').write('\n'.join(''.join(r) for r in G) + '\n')
    subprocess.run(['python3', OUT + 'contour.py', '_t.txt', '_t.txt'], check=True)
    T = [list(l.rstrip('\n')) for l in open('_t.txt')]
    for y in range(H):
        for x in range(W):
            if T[y][x] == 'O' and G[y][x] != 'O':
                c = 'A' if y < 48 else G[y][x]
                if y < 48 and (y == 3 and x < 56 or x <= 1 and y < 44): c = 'B'
                put(c, x, y)
    for y in range(11, 44):                                # arretiers
        put('C', xl(y) + 1, y); put('A', xr(y) - 1, y)
    for y in range(16, 39):                                # rives du petit toit
        put('A', gl(y) - 1, y); put('A', gr(y) + 1, y); put('A', 72, y) if y < 30 else None
    for y in range(30, 39):                                # bargeboards (planche de rive bois)
        put('t', bl(y), y); put('t', br(y), y)
    

def s05():   # details : cannelures de tuiles, faitage, onigawara, egout, gegyo
    for y in range(11, 44):
        for x in range(xl(y) + 2, xr(y) - 1):
            if G[y][x] == 'C' and x % 4 == 2: put('B', x, y)
    for x in range(17, 95, 4): put('D', x, 11); put('D', x, 12)  # reflet sous le faitage
    for y in range(16, 44, 5):                             # rangs de tuiles des croupes
        for x in range(2, xl(y) + 1): put('C', x, y)
        for x in range(xr(y) + 1, 110): put('A', x, y)
    for y in range(20, 38, 4):                             # rangs du petit toit (paralleles au faitage = colonnes)
        pass
    for y in range(17, 38):
        for x in range(gl(y), gr(y) + 1):
            if G[y][x] in 'DB' and y % 3 == 0: put('C' if x < 72 else 'A', x, y)
    for ox in (13, 93):                                    # onigawara
        for y in range(5, 11):
            for x in range(ox, ox + 5): put('A' if x in (ox, ox + 4) or y == 5 else 'B', x, y)
        put('D', ox + 1, 6); put('D', ox + 2, 6)
    for y in range(27, 31):                                # onigawara du pignon (bout de faitage)
        for x in range(70, 74): put('A' if x in (70, 73) or y == 30 else 'B', x, y)
    put('D', 71, 28)
    for y in range(33, 39): put('t', 71, y); put('t', 72, y)
    put('u', 70, 37); put('u', 73, 37)
    for x in range(2, 110): put('C', x, 44)
    for x in range(1, 111):                                # bouts de tuiles rondes
        put('ADCC'[x % 4], x, 45)
    put('A', 0, 43); put('A', 0, 44); put('B', 0, 45); put('A', 111, 43); put('A', 111, 44); put('B', 111, 45)

def s06():   # nettoyage : cannelures qui mordent le pignon, rive gauche lumiere
    pass
    for y in range(4, 44):
        if G[y][1] == 'A': put('B', 1, y)

for n, note, f in (('c02', 'aplats par matiere', s02), ('c03', 'lumiere haut-gauche', s03),
                   ('c04', 'contour et selout', s04), ('c05', 'details', s05), ('c06', 'nettoyage', s06)):
    step(n, note, f)
import os; os.remove('_t.txt')
