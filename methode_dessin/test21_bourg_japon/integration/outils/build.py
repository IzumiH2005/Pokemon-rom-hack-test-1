# Compose the Japanese Littleroot: builds the "japon" secondary tileset, the map blocks and door animations.
import struct, os
from PIL import Image
import assets as O
from kit import Canvas, N, PALS

ROOT = '/home/user/pokeemeraude-expansion'
W = H = 20
GRASS = [0x2002, 0x2003, 0x2003, 0x2002]
LAYER_NORMAL, LAYER_COVERED = 0, 1

class Cell:
    def __init__(s):
        s.bottom = None          # None = plain primary grass; else Canvas 16x16
        s.top = None
        s.layer = LAYER_NORMAL
        s.prim = None
        s.orig = None
        s.block = False
        s.beh = 0
        s.label = None
cells = {(x, y): Cell() for x in range(W) for y in range(H)}

def crop(c, cx, cy): return c.crop(cx * 16, cy * 16, 16, 16)

def place(obj, x0, y0, coll=None, normal_rows=(), label_cells=None):
    """Put a multi-cell object on the top layer. coll: list of strings, 'X' = blocked."""
    for cy in range(obj.h // 16):
        for cx in range(obj.w // 16):
            cell = cells.get((x0 + cx, y0 + cy))
            if cell is None: continue
            part = crop(obj, cx, cy)
            if cell.top is not None:      # merge with what is already there
                part2 = Canvas(16, 16); part2.paste(cell.top, 0, 0); part2.paste(part, 0, 0); part = part2
            cell.top = part
            cell.block = (coll[cy][cx] == 'X') if coll else True
            # blocked = NORMAL (sprite in front); walkable overhang (roof back, torii beam) = COVERED
            cell.layer = LAYER_NORMAL if cell.block else LAYER_COVERED

def region(cellset, fn, virtual=()):
    reg = set(cellset) | set(virtual)
    for (x, y) in cellset:
        cells[(x, y)].bottom = fn(reg, x, y)

def recolor(c, m):
    out = Canvas(c.w, c.h); out.p = [[m.get(v, v) if v else None for v in row] for row in c.p]; return out
def dirt(reg, x, y): return O.ground('terre', reg, x, y)
def gravel_c(reg, x, y): return O.ground('gravier', reg, x, y)
def pond_c(reg, x, y): return O.ground('etang', reg, x, y)

# ------------------------------------------------------------------ ground regions
road = {(x, y) for x in (10, 11) for y in range(0, 9)} | {(x, y) for x in range(2, 18) for y in range(9, 12)} \
     | {(x, y) for x in (10, 11) for y in range(12, 17)}
gravel = {(x, y) for x in range(2, 19) for y in (17, 18)} | {(2, 16)} | {(x, 16) for x in range(10, 19)}
pond = {(x, y) for x in (12, 13) for y in range(12, 16)}
grove = {(x, y) for x in (0, 1) for y in range(20)} | {(x, 19) for x in range(20)} \
      | {(x, y) for x in (18, 19) for y in range(10)} | {(19, y) for y in range(10, 20)}
outside = {(x, y) for x in range(-1, 21) for y in range(-1, 21) if not (0 <= x < 20 and 0 <= y < 20)}
gravel -= road

region(road, dirt, virtual={(10, -1), (11, -1)})
region(gravel, gravel_c, virtual=road)
region(pond, pond_c)
for p in pond: cells[p].block = True
O.stamp(cells[(12, 13)].bottom, O.KOI, 8, 5, 6); O.stamp(cells[(13, 14)].bottom, O.KOI_G, 8, 4, 8)
O.stamp(cells[(12, 12)].bottom, O.LYS, 8, 8, 9); O.stamp(cells[(13, 15)].bottom, O.LYS, 8, 4, 4)

BAM = O.bamboo()
def bamboo_cell(below_in, x):
    c = BAM.crop(0, 0 if below_in else 16, 16, 16)
    return c.mirror() if x % 2 else c
def bamboo(gr):
    greg = gr | outside
    for p in gr:
        cells[p].top = bamboo_cell((p[0], p[1] + 1) in greg, p[0]); cells[p].block = True; cells[p].layer = LAYER_NORMAL
bamboo(grove)

# ------------------------------------------------------------------ buildings
HOUSE = ['.....', 'XXXXX', 'XXXXX', 'XXXXX', 'XXXXX']
place(O.house(), 2, 4, HOUSE)
place(O.red_house(), 13, 4, HOUSE)
place(O.lab(), 3, 12, ['.......'] + ['XXXXXXX'] * 4)
place(O.shrine(), 14, 12)
DOORS = {(5, 8): 'House_Left', (14, 8): 'House_Right', (7, 16): 'Lab'}
for p in DOORS: cells[p].beh = 0x69; cells[p].layer = LAYER_NORMAL; cells[p].block = False

place(O.torii(64), 9, 0, ['X..X', 'X..X'])
place(O.torii(48), 15, 16, ['X.X', 'X.X'])
for (x, y, s) in ((2, 0, 1), (4, 0, 2), (6, 0, 3), (14, 0, 4), (16, 0, 5), (2, 2, 6), (16, 2, 7), (17, 10, 8)):
    place(O.sakura(s % 2 == 0), x, y)
for (x, y) in ((8, 0), (13, 0), (14, 16), (18, 16)):
    place(O.lantern(), x, y)
place(O.bamboo(), 2, 13)
place(O.nameplate(), 7, 8); place(O.nameplate(), 12, 8)
place(O.signboard(), 6, 17); place(O.signboard(), 16, 11)
for p in ((2, 18), (12, 18)): place(O.rock(), *p)
for i, p in enumerate(((4, 2), (5, 3), (15, 3), (13, 2), (8, 3), (2, 12), (2, 15), (7, 2), (16, 9))):
    if cells[p].top is None: cells[p].top = O.petals(i % 3 + 1)
town_cells = cells

# ------------------------------------------------------------------ Route 101 (original collision kept for the Birch scripts)
RROOT = ROOT + '/data/layouts/Route101/'
_orig = struct.unpack('<400H', open(RROOT + 'map.bin.orig', 'rb').read())
cells = {(x, y): Cell() for x in range(W) for y in range(H)}
PRIM_KEEP = {0x001, 0x00D, 0x06E, 0x087, 0x08E, 0x0D5, 0x0D6}
for (x, y), c in cells.items():
    v = _orig[y * 20 + x]; c.orig = v; c.block = bool(v >> 10 & 3)
    c.prim = (v & 0x3ff) if (v & 0x3ff) in PRIM_KEEP else (0x001 if not c.block else None)
r_sakura = [(11, 6), (13, 7), (11, 8), (12, 14), (2, 9), (2, 11)]
r_lant = [(9, 18), (12, 18)]
special = {(x + i, y + j) for (x, y) in r_sakura for i in (0, 1) for j in (0, 1)} | {(x, y + j) for (x, y) in r_lant for j in (0, 1)} \
        | {(7, 0), (7, 1), (12, 0), (12, 1), (5, 9)}
rgrove = {p for p, c in cells.items() if c.block and c.prim is None} - special
bamboo(rgrove)
rroad = {(x, y) for x in range(8, 12) for y in range(0, 6)} | {(10, y) for y in range(7, 13)} | {(x, y) for x in (10, 11) for y in range(14, 20)}
rroad = {p for p in rroad if cells[p].prim == 0x001}
region(rroad, dirt, virtual={(8, -1), (9, -1), (10, -1), (11, -1), (10, 20), (11, 20)})
for p in special: cells[p].prim = None if cells[p].block else 0x001
for i, (x, y) in enumerate(r_sakura): place(O.sakura(i % 2 == 1), x, y)
for p in r_lant: place(O.lantern(), *p)
place(O.torii(96), 7, 0, ['X....X', 'X....X'])
place(O.signboard(), 5, 9)
for i, p in enumerate(((6, 9), (8, 10), (17, 8), (3, 15), (17, 15), (7, 17), (13, 5))):
    c = cells[p]
    if c.prim == 0x001 and c.top is None and p not in rroad: c.top = O.petals(i % 3 + 1); c.prim = None
for p, c in cells.items():
    if c.bottom is not None or c.top is not None: c.prim = None
route_cells = cells
cells = town_cells

# ------------------------------------------------------------------ tile + metatile export
tiles, tile_index = [], {}
def flips(t):
    rows = [t[i * 8:(i + 1) * 8] for i in range(8)]
    h = tuple(v for r in rows for v in r[::-1]); v = tuple(v for r in rows[::-1] for v in r)
    hv = tuple(v for r in rows[::-1] for v in r[::-1])
    return ((t, 0, 0), (h, 1, 0), (v, 0, 1), (hv, 1, 1))
def reg_tile(t):
    for cand, hf, vf in flips(t):
        if cand in tile_index: return tile_index[cand], hf, vf
    tile_index[t] = len(tiles); tiles.append(t); return len(tiles) - 1, 0, 0

def entries(c, default):
    if c is None: return default
    out = []
    for qy in (0, 8):
        for qx in (0, 8):
            names = [c.p[qy + y][qx + x] for y in range(8) for x in range(8)]
            used = {n for n in names if n}
            if not used: out.append(0); continue
            pals = {N[n][0] for n in used}
            assert len(pals) == 1, f'mixed palettes in tile: {used}'
            pal = pals.pop()
            idx, hf, vf = reg_tile(tuple(N[n][1] if n else 0 for n in names))
            out.append((512 + idx) | hf << 10 | vf << 11 | pal << 12)
    return out

metatiles, mt_index = [], {}
def reg_mt(cell):
    key = (tuple(entries(cell.bottom, GRASS)), tuple(entries(cell.top, [0, 0, 0, 0])), cell.beh | cell.layer << 12)
    if key not in mt_index: mt_index[key] = len(metatiles); metatiles.append(key)
    return mt_index[key]

def ids_for(cs, first=()):
    out = {}
    for p in list(first) + [p for p in sorted(cs, key=lambda p: (p[1], p[0])) if p not in first]:
        c = cs[p]
        if c.prim is not None: out[p] = c.prim; continue
        if c.bottom is None and c.top is None and c.beh == 0:
            out[p] = 0x001; continue      # plain primary grass
        out[p] = 0x200 + reg_mt(c)
    return out
block_ids = ids_for(town_cells, DOORS)
route_ids = ids_for(route_cells)
door_ids = {name: block_ids[p] for p, name in DOORS.items()}

# border: 2x2 of bamboo interior
border_ids = []
for (x, y) in ((0, 0), (1, 0), (0, 1), (1, 1)):
    bc = Cell(); bc.top = bamboo_cell(True, x); bc.block = True
    border_ids.append(0x200 + reg_mt(bc))

print('tiles', len(tiles), 'metatiles', len(metatiles))
assert len(tiles) <= 512 and len(metatiles) <= 512

TS = ROOT + '/data/tilesets/secondary/japon'
os.makedirs(TS + '/palettes', exist_ok=True)
rows = (len(tiles) + 15) // 16
img = Image.new('P', (128, rows * 8), 0)
flat = []
for i in range(16):
    flat += list(PALS[6][i]) if i else [255, 0, 255]
img.putpalette(flat + [0] * (768 - len(flat)))
px = img.load()
for i, t in enumerate(tiles):
    for y in range(8):
        for x in range(8): px[(i % 16) * 8 + x, (i // 16) * 8 + y] = t[y * 8 + x]
img.save(TS + '/tiles.png')
for i in range(16):
    cols = PALS.get(i)
    cols = [(0, 0, 0)] * 16 if cols is None else [(255, 0, 255)] + list(cols[1:])
    with open(f'{TS}/palettes/{i:02d}.pal', 'w') as f:
        f.write('JASC-PAL\r\n0100\r\n16\r\n' + ''.join(f'{r} {g} {b}\r\n' for r, g, b in cols))
with open(TS + '/metatiles.bin', 'wb') as f:
    for b, t, a in metatiles: f.write(struct.pack('<8H', *b, *t))
with open(TS + '/metatile_attributes.bin', 'wb') as f:
    for b, t, a in metatiles: f.write(struct.pack('<H', a))

with open(ROOT + '/data/layouts/LittlerootTown/map.bin', 'wb') as f:
    for y in range(H):
        for x in range(W):
            c = cells[(x, y)]
            v = block_ids[(x, y)] | ((1 << 10) if c.block else 0) | ((0 if c.block else 3) << 12)
            f.write(struct.pack('<H', v))
with open(RROOT + 'map.bin', 'wb') as f:
    for y in range(H):
        for x in range(W):
            c = route_cells[(x, y)]
            f.write(struct.pack('<H', route_ids[(x, y)] | (c.orig & 0xFC00)))
with open(RROOT + 'border.bin', 'wb') as f:
    f.write(struct.pack('<4H', *[b | 1 << 10 for b in border_ids]))
with open(ROOT + '/data/layouts/LittlerootTown/border.bin', 'wb') as f:
    f.write(struct.pack('<4H', *[b | 1 << 10 for b in border_ids]))

# ------------------------------------------------------------------ door animations (3 frames of 16x32)
def door_png(make, col, pal, name):
    im = Image.new('P', (16, 96)); im.putpalette(flat + [0] * (768 - len(flat))); p = im.load()
    for f in range(3):
        c = make(f + 1)
        for y in range(32):
            for x in range(16):
                n = c.get(col * 16 + x, 48 + y)
                p[x, f * 32 + y] = N[n][1] if n else 0
                assert not n or N[n][0] == pal, (name, n)
    im.save(f'{ROOT}/graphics/door_anims/{name}.png')
door_png(lambda s: O.house(O.DOOR_FRAMES[s - 1]), 3, 6, 'japon_house_left')
door_png(lambda s: O.red_house(O.DOOR_FRAMES[s - 1]), 1, 11, 'japon_house_right')
door_png(lambda s: O.lab(O.DOOR_FRAMES[s - 1]), 4, 6, 'japon_lab')

with open(os.path.dirname(__file__) + '/../build_info.txt', 'w') as f:
    f.write(f'tiles={len(tiles)}\nmetatiles={len(metatiles)}\n')
    for n, v in door_ids.items(): f.write(f'door_{n}={v:#x}\n')
print('doors', {n: hex(v) for n, v in door_ids.items()})

# keep the declared tile count in sync with the exported tileset
import re as _re
_p = ROOT + '/src/data/tilesets/graphics.h'
_s = open(_p).read()
_s = _re.sub(r'(japon/tiles\.png", "\.4bpp\.fastSmol", "-num_tiles )\d+', rf'\g<1>{len(tiles)}', _s)
open(_p, 'w').write(_s)
