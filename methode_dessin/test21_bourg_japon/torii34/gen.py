"""Torii 3/4 vue de dessus : on part du torii valide (torii/toriiW.txt) et on ajoute les faces
superieures que voit une camera en surplomb. c06 = commandes, toriiW.txt = resultat."""
import subprocess
OUT = '/home/user/Pokemon-rom-hack-test-1/methode_dessin/outils/'
for W in (48, 64, 96):
    G = [list(l.rstrip('\n')) for l in open(f'../torii/torii{W}.txt')]
    C = [f'# c06 torii{W} : faces superieures (vue de dessus)']
    def put(c, x, y): G[y][x] = c; C.append(f'px {c} {x} {y}')
    for x in range(2, W - 2): put('s', x, 1)            # dessus du shimaki (laque sombre sous le ciel)
    for x in range(2, W // 3): put('q', x, 1)           # reflet cote lumiere
    for x in range(1, W - 1): put('s', x, 2)            # le dessus fait 2 rangs : on le voit de haut
    put('A', 1, 2); put('A', W - 2, 2)
    for x in range(1, W - 1): put('m', x, 4)            # dessus du kasagi
    pl, pr = (5, 10), (W - 11, W - 6)
    for a, b in (pl, pr):                               # poteaux : dessus du kamebara en anneau clair
        for x in range(a - 1, b + 2): put('q', x, 28)
        put('s', b + 1, 28); put('s', b, 28)
        for x in range(a - 1, b + 2): put('s', x, 29)
        put('A', a - 1, 29); put('A', b + 1, 29)
    open(f'c06_{W}.txt', 'w').write('\n'.join(C) + '\n')
    open(f'torii{W}.txt', 'w').write('\n'.join(''.join(r) for r in G) + '\n')
    subprocess.run(['python3', OUT + 'px.py', f'torii{W}.txt', '8', 'palette.json'], check=True)
