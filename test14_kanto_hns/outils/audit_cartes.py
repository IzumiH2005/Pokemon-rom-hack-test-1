#!/usr/bin/env python3
"""audit_cartes.py <jeu> : contrôle statique des cartes importées de Heart & Soul.

Signale les PNJ posés sur une case infranchissable ou à la mauvaise hauteur, les PNJ empilés, les PNJ et objets
hors d'atteinte, les déclencheurs sur un mur, les portes sans case d'accès ou sans arrivée, les points de soin et
les téléportations de script qui tombent dans le décor.
"""
import json, glob, os, re, struct, sys
from collections import deque
from tables import PORTES, PORTE_DEPLACEE
J = sys.argv[1]
L = {l['id']: l for l in json.load(open(f'{J}/data/layouts/layouts.json'))['layouts'] if l and 'id' in l}
cartes = {}
for f in sorted(glob.glob(f'{J}/data/maps/*/map.json')):
    j = json.load(open(f)); j['_dossier'] = os.path.basename(os.path.dirname(f)); cartes[j['id']] = j

ATTR = dict(re.findall(r'gMetatileAttributes_(\w+)\[\] = INCBIN_U16\("([^"]+)"', open(f'{J}/src/data/tilesets/metatiles.h').read()))
SAUT = {56: (1, 0), 57: (-1, 0), 58: (0, -1), 59: (0, 1)}     # MB_JUMP_EAST, WEST, NORTH, SOUTH

V = [(0, -1), (0, 1), (-1, 0), (1, 0)]
def cle(o, rangs):
    """Identité d'un PNJ d'une version à l'autre : apparence, script et rang parmi ses semblables."""
    k = (o['graphics_id'], o.get('script')); rangs[k] = rangs.get(k, 0) + 1; return k + (rangs[k],)
class Decor:
    def __init__(s, lid):
        l = L[lid]; s.frlg = l.get('layout_version') == 'frlg'; s.np = 640 if s.frlg else 512; s.w, s.h = l['width'], l['height']; s.d = open(f"{J}/{l['blockdata_filepath']}", 'rb').read()
        s.att = [open(f"{J}/{ATTR[l[k][9:]]}", 'rb').read() if l[k][9:] in ATTR else b'' for k in ('primary_tileset', 'secondary_tileset')]
    def bloc(s, x, y): return struct.unpack_from('<H', s.d, 2 * (y * s.w + x))[0]
    def dedans(s, x, y): return 0 <= x < s.w and 0 <= y < s.h
    def mur(s, x, y): return not s.dedans(x, y) or (s.bloc(x, y) >> 10) & 3 != 0
    def haut(s, x, y): return s.bloc(x, y) >> 12
    def comp(s, x, y):
        if not s.dedans(x, y): return 0
        m = s.bloc(x, y) & 1023; t, m = (s.att[0], m) if m < s.np else (s.att[1], m - s.np)
        if s.frlg: return struct.unpack_from('<I', t, 4 * m)[0] & 0x1FF if 4 * m + 4 <= len(t) else 0   # u32, format Rouge Feu
        return t[2 * m] if 2 * m < len(t) else 0
    def pas(s, x, y, e, dx, dy):
        """Hauteur après un pas depuis (x, y) à la hauteur e, ou None si le pas est bloqué (mur ou écart de hauteur,
        sauf mise à l'eau ou accostage : l'eau est à la hauteur 1). Les rebords se sautent dans leur sens."""
        n = (x + dx, y + dy)
        if SAUT.get(s.comp(*n)) == (dx, dy): n = (x + 2 * dx, y + 2 * dy)
        if s.mur(*n): return None
        h = s.haut(*n)
        if e != 0 and h not in (0, 15) and h != e and 1 not in (e, h): return None
        return n, (e if h == 15 else h)
    def depart(s, x, y): h = s.haut(x, y); return 3 if h == 15 else h
    def atteint(s, graines):
        """Cases accessibles à pied ou en surf depuis les graines, rebords à saut et hauteurs compris."""
        vus = set((g, s.depart(*g)) for g in graines if s.dedans(*g)); file = deque(vus)
        while file:
            (x, y), e = file.popleft()
            for dx, dy in V:
                r = s.pas(x, y, e, dx, dy)
                if r and r not in vus: vus.add(r); file.append(r)
        return {c for c, e in vus}
    def graines(s, j):
        g = [(w['x'], w['y']) for w in j['warp_events']]
        if j.get('connections'):
            g += [(x, y) for x in range(s.w) for y in range(s.h) if (x in (0, s.w - 1) or y in (0, s.h - 1)) and not s.mur(x, y)]
        return g

# Parcours du monde entier depuis la chambre du joueur : marche, surf, rebords, portes, bords de carte reliés,
# arrivées écrites dans les scripts et points de soin.
DEC = {}
def decor(mid):
    if mid not in DEC: DEC[mid] = Decor(cartes[mid]['layout'])
    return DEC[mid]
def monde():
    vus = set(); file = deque()
    def seme(mid, x, y, e=None):
        if mid not in cartes or not decor(mid).dedans(x, y): return
        k = (mid, x, y, decor(mid).depart(x, y) if e is None else e)
        if k not in vus: vus.add(k); file.append(k)
    dep = 'MAP_PALLET_TOWN_PLAYERS_HOUSE_2F'; d = decor(dep)
    for x in range(d.w):
        for y in range(d.h):
            if not d.mur(x, y): seme(dep, x, y)
    for h in json.load(open(f'{J}/src/data/heal_locations.json'))['heal_locations']: seme(h['map'], int(h['x']), int(h['y']))
    for f in glob.glob(f'{J}/data/maps/*/scripts.inc') + glob.glob(f'{J}/data/scripts/*.inc'):
        for m in re.finditer(r'\b(?:warp\w*)\s+(MAP_\w+),\s*(\d+),\s*(\d+)', open(f).read()): seme(m[1], int(m[2]), int(m[3]))
    portes = {mid: {(w['x'], w['y']): w for w in j.get('warp_events', [])} for mid, j in cartes.items()}
    while file:
        mid, x, y, e = file.popleft(); d = decor(mid); j = cartes[mid]
        w = portes[mid].get((x, y))
        if w and w['dest_map'] in cartes:
            try:
                c = cartes[w['dest_map']].get('warp_events', [])[int(w['dest_warp_id'])]; seme(w['dest_map'], c['x'], c['y'])
            except (ValueError, IndexError): pass
        for dx, dy in V:
            nx, ny = x + dx, y + dy
            if not d.dedans(nx, ny):
                for c in j.get('connections') or []:
                    if c['map'] not in cartes or c['direction'] not in ('up', 'down', 'left', 'right'): continue
                    f = decor(c['map']); o = c['offset']
                    cible = {'up': (nx - o, f.h - 1), 'down': (nx - o, 0), 'left': (f.w - 1, ny - o), 'right': (0, ny - o)}[c['direction']]
                    if (dx, dy) == {'up': (0, -1), 'down': (0, 1), 'left': (-1, 0), 'right': (1, 0)}[c['direction']] and not f.mur(*cible):
                        seme(c['map'], *cible)
                continue
            if (nx, ny) in portes[mid]: seme(mid, nx, ny, e); continue      # une porte se prend même posée sur un mur
            r = d.pas(x, y, e, dx, dy)
            if r: seme(mid, *r[0], r[1])
    return {(m, x, y) for m, x, y, e in vus}
MONDE = monde()

def parlable(d, vus, x, y):
    """On peut parler au PNJ : une case voisine est accessible, ou un comptoir (MB_COUNTER) l'en sépare."""
    if (x, y) in vus: return True
    return any((x + dx, y + dy) in vus or (d.comp(x + dx, y + dy) == 128 and (x + 2 * dx, y + 2 * dy) in vus) for dx, dy in V)

# Collisions : une tuile bloquante presque partout où elle est posée, mais franchissable ici (façade, barrière, arbre...).
STATS = {}
def cle_tuile(l, m): return (l['primary_tileset'], m) if m < (640 if l.get('layout_version') == 'frlg' else 512) else (l['secondary_tileset'], m)
for lid, l in L.items():
    try: dd = Decor(lid)
    except (OSError, KeyError): continue
    for i in range(dd.w * dd.h):
        v = struct.unpack_from('<H', dd.d, 2 * i)[0]; k = cle_tuile(l, v & 1023); n = STATS.setdefault(k, [0, 0])
        n[(v >> 10) & 3 != 0] += 1
def douteuse(l, v):
    libre, bloque = STATS.get(cle_tuile(l, v & 1023), (0, 0))
    return (v >> 10) & 3 == 0 and bloque >= 6 and bloque >= 9 * libre

FIXES = ('CUT_TREE', 'ROCK_SMASH', 'STRENGTH_BOULDER', 'PUSHABLE_BOULDER', 'ITEM_BALL')
out = []
EXEMPLES = {}
for mid, j in cartes.items():
    if not j['layout'].startswith('LAYOUT_HNS_'): continue
    d = Decor(j['layout']); nom = j['_dossier']
    def dit(t): out.append(f'{nom}: {t}')
    objs = j['object_events']
    def qui(i, o): return f"{o.get('local_id', i + 1)} {o['graphics_id'][14:]} ({o['x']},{o['y']})"
    vus = {(x, y) for m, x, y in MONDE if m == mid}
    # L'original Rouge Feu : un PNJ déjà sur un meuble ou déjà isolé là-bas n'est pas un défaut de l'import.
    orig = {}; rangs_o = {}; rangs = {}
    fo = f'{J}/data/maps/{nom}/map.json.rougefeu'
    if os.path.exists(fo):
        jo = json.load(open(fo)); do = Decor(jo['layout']); vo = do.atteint(do.graines(jo))
        for o in jo['object_events']:
            x, y = o['x'], o['y']; k = cle(o, rangs_o)
            orig[k] = (do.mur(x, y), not parlable(do, vo, x, y))
    places = {}
    for i, o in enumerate(objs):
        x, y = o['x'], o['y']
        if not d.dedans(x, y): dit(f'PNJ {qui(i, o)} hors de la carte'); continue
        om, oi = orig.get(cle(o, rangs), (False, False))
        if d.mur(x, y) and not om: dit(f'PNJ {qui(i, o)} sur une case infranchissable (bloc {d.bloc(x, y) & 1023:#05x})')
        e = d.haut(x, y)
        if e not in (0, 15) and o['elevation'] != e: dit(f'PNJ {qui(i, o)} hauteur {o["elevation"]} sur case de hauteur {e}')
        if o.get('flag', '0') in ('0', 0) and (x, y) in places: dit(f'PNJ {qui(i, o)} empilé sur {places[(x, y)]}')
        if o.get('flag', '0') in ('0', 0): places[(x, y)] = qui(i, o)
        if not oi and not parlable(d, vus, x, y):
            dit(f'PNJ {qui(i, o)} hors d\'atteinte')
    trous = sorted((x, y) for x, y in vus if d.dedans(x, y) and douteuse(L[j['layout']], d.bloc(x, y)))
    for x, y in vus:
        if d.dedans(x, y) and not d.mur(x, y): EXEMPLES.setdefault(cle_tuile(L[j['layout']], d.bloc(x, y) & 1023), []).append((nom, x, y))
    if trous: dit(f"{len(trous)} case(s) franchissable(s) sur une tuile d'ordinaire bloquante : {trous[:12]}")
    for c in j['coord_events']:
        if d.mur(c['x'], c['y']): dit(f"déclencheur {c.get('script')} ({c['x']},{c['y']}) sur un mur")
        elif (c['x'], c['y']) not in vus: dit(f"déclencheur {c.get('script')} ({c['x']},{c['y']}) hors d'atteinte")
    # Portes de bâtiments absents de Heart & Soul : gardées pour la numérotation, sans accès voulu.
    mortes = set()
    if os.path.exists(fo):
        for i, w in enumerate(jo['warp_events']):
            a = (w['x'], w['y'])
            if PORTES.get(nom[:-5], {}).get(a, 1) is None or (nom[:-5], a) == PORTE_DEPLACEE[:2]: mortes.add(i)
    for i, w in enumerate(j['warp_events']):
        x, y = w['x'], w['y']
        if not d.dedans(x, y): dit(f'porte {i} hors de la carte'); continue
        if i in mortes: continue
        if d.mur(x, y) and all(d.mur(x + dx, y + dy) for dx, dy in V): dit(f'porte {i} ({x},{y}) emmurée')
        if not d.mur(x, y) and all(d.mur(x + dx, y + dy) for dx, dy in V): dit(f'porte {i} ({x},{y}) sans case voisine libre')
        dm = w['dest_map']
        if dm in ('MAP_DYNAMIC', 'MAP_UNDEFINED'): continue
        if dm not in cartes: dit(f'porte {i} vers {dm} inconnue'); continue
        try:
            if int(w['dest_warp_id']) >= len(cartes[dm]['warp_events']): dit(f"porte {i} ({x},{y}) vers {dm} porte {w['dest_warp_id']} inexistante")
        except ValueError: pass
    for b in j['bg_events']:
        if not d.dedans(b['x'], b['y']): dit(f"décor {b.get('script', b.get('item'))} hors de la carte")
        elif b['type'] == 'hidden_item' and (b['x'], b['y']) not in vus and not any((b['x'] + dx, b['y'] + dy) in vus for dx, dy in V):
            dit(f"objet caché {b.get('item')} ({b['x']},{b['y']}) hors d'atteinte")

# Points de soin et téléportations écrites dans les scripts ou le C.
def controle(source, mid, x, y):
    j = cartes.get(mid)
    if x == 255: return
    if not j or not j['layout'].startswith('LAYOUT_HNS_'): return
    d = Decor(j['layout'])
    if d.mur(x, y): out.append(f'{source}: arrivée {mid} ({x},{y}) dans le décor')
for h in json.load(open(f'{J}/src/data/heal_locations.json'))['heal_locations']:
    controle('soin ' + h['id'], h['map'], int(h['x']), int(h['y']))
for f in glob.glob(f'{J}/data/maps/*/scripts.inc') + glob.glob(f'{J}/data/scripts/*.inc'):
    for m in re.finditer(r'\b(?:warp\w*|setwarp|setdynamicwarp|setescapewarp|setdivewarp|setholewarp)\s+(MAP_\w+),\s*(\d+),\s*(\d+)', open(f).read()):
        controle(os.path.relpath(f, J), m[1], int(m[2]), int(m[3]))
print('\n'.join(out)); print(len(out), 'signalement(s)')

if os.environ.get('LISTE'):
    # Tuiles atteintes à pied qui sont bloquées ailleurs au moins une fois sur trois : à vérifier à l'œil.
    for k, ex in sorted(EXEMPLES.items(), key=lambda e: -len(e[1])):
        libre, bloque = STATS.get(k, (0, 0))
        if bloque >= 2 and 2 * bloque >= libre: print('LISTE', k[0], hex(k[1]), libre, bloque, len(ex), ex[0][0], ex[0][1], ex[0][2])
