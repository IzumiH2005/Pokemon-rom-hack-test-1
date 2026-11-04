"""Pose des primitives décidées à la main sur une grille texte (1 caractère = 1 pixel).

Usage : python3 trace.py in.txt|NEW:64x64 out.txt cmds.txt

Le script ne décide rien (R3) : il pose exactement ce que disent les commandes.
'.' = vide. Commandes (une par ligne, '#' = commentaire) :
  px    C x y [x y ...]          pixels isolés
  hline C x1 x2 y                ligne horizontale
  vline C x y1 y2                ligne verticale
  rect  C x1 y1 x2 y2            rectangle plein
  frame C x1 y1 x2 y2            cadre de 1 px
  line  C x1 y1 x2 y2            segment entre deux points décidés (fil de fer)
  disc  C cx cy r                disque plein
  ring  C cx cy r                cercle de 1 px
  rows  C y x1 x2 [x1 x2 ...]    une paire x1 x2 par rangée, à partir de la rangée y
  rep   A B x1 y1 x2 y2          remplace A par B dans la zone (A = '*' : tout pixel plein)
  stamp piece.txt x y            pose une pièce (calque) dont le coin haut-gauche va en x y ;
                                 les '.' de la pièce restent transparents (E6-E)
"""
import sys


def lire(path):
    if path.startswith('NEW:'):
        w, h = map(int, path[4:].split('x'))
        return [['.'] * w for _ in range(h)]
    with open(path) as f:
        return [list(l.rstrip('\n')) for l in f if l.strip()]


def ecrire(G, path):
    with open(path, 'w') as f:
        f.write('\n'.join(''.join(r) for r in G) + '\n')


def appliquer(G, cmds):
    H, W = len(G), len(G[0])

    def put(c, x, y):
        if 0 <= x < W and 0 <= y < H:
            G[y][x] = c

    for n, ligne in enumerate(cmds, 1):
        ligne = ligne.split('#')[0].split()
        if not ligne:
            continue
        op, c, a = ligne[0], ligne[1], [int(v) for v in ligne[2:] if v.lstrip('-').isdigit()]
        if op == 'stamp':
            P = lire(c)
            for dy, r in enumerate(P):
                for dx, ch in enumerate(r):
                    if ch != '.':
                        put(ch, a[0] + dx, a[1] + dy)
        elif op == 'px':
            for x, y in zip(a[::2], a[1::2]):
                put(c, x, y)
        elif op == 'hline':
            for x in range(a[0], a[1] + 1):
                put(c, x, a[2])
        elif op == 'vline':
            for y in range(a[1], a[2] + 1):
                put(c, a[0], y)
        elif op == 'rect':
            for y in range(a[1], a[3] + 1):
                for x in range(a[0], a[2] + 1):
                    put(c, x, y)
        elif op == 'frame':
            for x in range(a[0], a[2] + 1):
                put(c, x, a[1]); put(c, x, a[3])
            for y in range(a[1], a[3] + 1):
                put(c, a[0], y); put(c, a[2], y)
        elif op == 'line':
            x1, y1, x2, y2 = a
            n = max(abs(x2 - x1), abs(y2 - y1)) or 1
            for i in range(n + 1):
                put(c, round(x1 + (x2 - x1) * i / n), round(y1 + (y2 - y1) * i / n))
        elif op in ('disc', 'ring'):
            cx, cy, r = a
            for y in range(cy - r, cy + r + 1):
                for x in range(cx - r, cx + r + 1):
                    d = (x - cx) ** 2 + (y - cy) ** 2
                    if d <= r * r + r and (op == 'disc' or d >= r * r - r):
                        put(c, x, y)
        elif op == 'rows':
            y = a[0]
            for x1, x2 in zip(a[1::2], a[2::2]):
                for x in range(x1, x2 + 1):
                    put(c, x, y)
                y += 1
        elif op == 'rep':
            b = ligne[2]
            x1, y1, x2, y2 = [int(v) for v in ligne[3:7]]
            for y in range(max(0, y1), min(H, y2 + 1)):
                for x in range(max(0, x1), min(W, x2 + 1)):
                    if G[y][x] == c or (c == '*' and G[y][x] != '.'):
                        G[y][x] = b
        else:
            raise SystemExit(f'ligne {n} : commande inconnue {op}')
    return G


if __name__ == '__main__':
    src, dst, cmd = sys.argv[1:4]
    G = lire(src)
    with open(cmd) as f:
        appliquer(G, f.readlines())
    ecrire(G, dst)
