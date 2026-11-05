# Loads the hand-drawn letter grids from methode_dessin and maps them to GBA palette slots 6..11.
import json
from PIL import Image
import kit
from kit import Canvas

A = '/home/user/Pokemon-rom-hack-test-1/methode_dessin/test21_bourg_japon/'
# slot -> (palette.json, letters in index order 1..15, renames for the json lookup)
SLOTS = {
    6: ('maison', 'O A B C D Q q t u v w N n y s'),
    11: ('maison', 'O A B C D Q q t u v w R r y s'),
    10: ('sanctuaire', 'O g h i j k l m t w z Q s q A'),
    7: ('sakura', 'O a b c d e f t u v G H I J K'),
    9: ('sol', 'a b c d g h i k e f j l m n'),
    8: ('sol/etang', 'p q r s w x y K W L'),
}

def r8(h):
    return tuple(min(248, (int(h[i:i + 2], 16) + 4) // 8 * 8) for i in (1, 3, 5))

kit.PALS.clear(); kit.N.clear()
for s, (d, letters) in SLOTS.items():
    pj = json.load(open(A + d + '/palette.json'))
    L = letters.split()
    kit.PALS[s] = ['_'] + [r8(pj[c]) for c in L] + [(0, 0, 0)] * (15 - len(L))
    for i, c in enumerate(L, 1): kit.N[f'{s}{c}'] = (s, i)

# the ground palette's grass must equal primary palette 2 entries 12..14 exactly
_prim = open('/home/user/pokeemeraude-expansion/data/tilesets/primary/general/palettes/02.pal').read().split()[3:]
for c, k in (('g', 12), ('h', 13), ('i', 14)):
    want = tuple(int(v) >> 3 for v in _prim[k * 3:k * 3 + 3])
    got = tuple(v >> 3 for v in kit.PALS[9][kit.N['9' + c][1]])
    assert want == got, (c, want, got)

_pim = Image.open('/home/user/pokeemeraude-expansion/data/tilesets/primary/general/tiles.png').load()
def herbe(x, y):
    t = [[2, 3], [3, 2]][(y % 16) // 8][(x % 16) // 8]
    v = _pim[(t % 16) * 8 + x % 8, (t // 16) * 8 + y % 8] & 15
    return {0xd: 'h', 0xe: 'i', 0xc: 'g'}[v]

def grid(path):
    return [l.rstrip('\n') for l in open(A + path) if l.strip()]

def canvas(rows, slot, grass=False):
    c = Canvas(len(rows[0]), len(rows))
    for y, r in enumerate(rows):
        for x, ch in enumerate(r):
            if ch == '.':
                if grass: c.p[y][x] = '9' + herbe(x, y)
                continue
            c.p[y][x] = f'{slot}{ch}'
    return c

def load(path, slot): return canvas(grid(path), slot)

def stamp(c, rows, slot, ox, oy):
    for y, r in enumerate(rows):
        for x, ch in enumerate(r):
            if ch != '.': c.set(ox + x, oy + y, f'{slot}{ch}')

# ---------------------------------------------------------------- assets
def house(door=None):
    c = load('maison/etape06_final.txt', 6)
    if door: stamp(c, grid(f'maison/{door}.txt'), 6, 48, 48)
    return c
def red_house(door=None):
    c = load('maison/maison_rouge.txt', 11)
    if door:
        stamp(c, [r.replace('N', 'R').replace('n', 'r') for r in grid(f'maison/{door}.txt')], 11, 48, 48)
    return c.mirror()
def lab(door=None):
    c = load('labo/etape06_final.txt', 6)
    if door: stamp(c, grid(f'labo/{door}.txt'), 6, 64, 48)
    return c
DOOR_FRAMES = ('porte1_fermee', 'porte2_mi', 'porte3_ouverte')
def shrine(): return load('sanctuaire/etape06_final.txt', 10)
def torii(w): return load(f'torii/torii{w}.txt', 10)
def sakura(flip=False):
    c = load('sakura/sakura.txt', 7); return c.mirror() if flip else c
def lantern(): return load('lanterne/lanterne.txt', 6)
def bamboo(): return load('bambou/bambou.txt', 7)
def signboard(): return load('panneau/panneau.txt', 6)
def nameplate(): return load('plaque/plaque.txt', 6)
def rock(): return load('rocher/rocher.txt', 8)
def petals(i): return load(f'petales/petales{i}.txt', 7)

# ---------------------------------------------------------------- ground autotiles
import sys as _s; _s.path.insert(0, A + 'sol'); import autotile as _at
_G = {k: (grid(f'sol/{k}/{k}.txt'), grid(f'sol/{k}/{k}_int.txt')) for k in ('terre', 'gravier', 'etang')}
_SLOT = {'terre': 9, 'gravier': 9, 'etang': 8}
def ground(kind, reg, x, y):
    B, I = _G[kind]
    return canvas([''.join(r) for r in _at.case(B, I, reg, x, y)], _SLOT[kind], grass=True)
KOI, KOI_G, LYS = grid('sol/etang/koi.txt'), grid('sol/etang/koi_g.txt'), grid('sol/etang/lys.txt')
