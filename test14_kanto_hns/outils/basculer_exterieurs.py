#!/usr/bin/env python3
"""Passe tous les extérieurs de Kanto sur les décors Heart & Soul.

Usage : python3 basculer_exterieurs.py <pokemonHnS> <jeu>     (après basculer_zone1.py)

Le script garde les PNJ, scripts et dialogues de Rouge Feu et les replace sur le nouveau décor :
  - les portes suivent la table PORTES (case d'origine -> case HnS) ;
  - le décalage médian des portes d'une carte sert à replacer le reste ;
  - un PNJ dont la case n'est plus valide prend la place libre d'un PNJ HnS de même rôle
    (dresseur, objet, obstacle, passant), sinon la case valide la plus proche ;
  - les connexions entre cartes reprennent celles de HnS.
La première exécution garde une copie `map.json.rougefeu` de chaque carte ; les suivantes repartent
de cette copie, donc le script peut être relancé. Il écrit un rapport `rapport_exterieurs.txt`.
"""
import json, os, struct, sys, re, shutil, statistics, copy
from collections import deque

HNS, JEU = sys.argv[1], sys.argv[2]
ICI = os.path.dirname(os.path.abspath(__file__))
LAYOUTS_HNS = json.load(open(f'{ICI}/layouts_kanto_hns.json'))
ZONE1 = {'PalletTown', 'Route1', 'ViridianCity'}          # déjà traitées par basculer_zone1.py
NOM_HNS = {'Route21_North': 'Route21'}
VILLES = ['PalletTown', 'ViridianCity', 'PewterCity', 'CeruleanCity', 'LavenderTown', 'VermilionCity',
          'CeladonCity', 'FuchsiaCity', 'CinnabarIsland', 'SaffronCity']
CARTES = VILLES + [f'Route{i}' for i in range(1, 21)] + ['Route21_North', 'Route22', 'Route24', 'Route25']
# Route 23 et Plateau Indigo attendent la zone de la Ligue (Routes 26 et 27, Route Victoire).

from tables import PORTES, PORTE_DEPLACEE, RETOUCHES

EAU = set(range(0x10, 0x18))
rapport = []


def lire(p): return json.load(open(p))


def ecrire(p, j):
    json.dump(j, open(p, 'w'), indent=2, ensure_ascii=False); open(p, 'a').write('\n')


LAY = {x['id']: x for x in lire(f'{JEU}/data/layouts/layouts.json')['layouts'] if x}
META = open(f'{JEU}/src/data/tilesets/metatiles.h').read()
_attr = {}


def attributs(sym):
    if sym not in _attr:
        m = re.search(r'gMetatileAttributes_%s\[\]\s*=\s*INCBIN_U\d+\("([^"]+)"' % sym[len('gTileset_'):], META)
        d = open(f'{JEU}/{m.group(1)}', 'rb').read() if m else b''
        _attr[sym] = struct.unpack('<%dI' % (len(d) // 4), d)
    return _attr[sym]


class Decor:
    def __init__(self, lid):
        self.l = LAY[lid]; self.w, self.h = self.l['width'], self.l['height']
        self.d = open(f'{JEU}/{self.l["blockdata_filepath"]}', 'rb').read()

    def case(self, x, y):
        """(collision, eau) ou None hors carte."""
        if not (0 <= x < self.w and 0 <= y < self.h): return None
        v = struct.unpack_from('<H', self.d, 2 * (x + y * self.w))[0]
        m = v & 0x3FF
        a = attributs(self.l['primary_tileset' if m < 640 else 'secondary_tileset'])
        i = m if m < 640 else m - 640
        comp = a[i] & 0x1FF if i < len(a) else 0
        return ((v >> 10) & 3, comp in EAU)


def niveau(decor, o):
    """Aligne l'élévation d'un PNJ sur celle de sa case."""
    e = struct.unpack_from('<H', decor.d, 2 * (o['x'] + o['y'] * decor.w))[0] >> 12
    if 1 <= e <= 14: o['elevation'] = e


def role(o):
    g = o['graphics_id']
    if 'CUTTABLE_TREE' in g: return 'arbre'
    if 'BREAKABLE_ROCK' in g: return 'rocher'
    if 'BOULDER' in g: return 'bloc'
    if 'ITEM_BALL' in g: return 'objet'
    if o.get('trainer_type', 'TRAINER_TYPE_NONE') not in ('TRAINER_TYPE_NONE', '0'): return 'dresseur'
    return 'passant'


def plus_proche(decor, x, y, eau, pris):
    """Case libre de même nature la plus proche de (x, y)."""
    x = min(max(x, 0), decor.w - 1); y = min(max(y, 0), decor.h - 1)
    vus = {(x, y)}; file = deque([(x, y)])
    while file:
        cx, cy = file.popleft()
        if decor.case(cx, cy) == (0, eau) and (cx, cy) not in pris: return cx, cy
        for dx, dy in ((0, 1), (1, 0), (0, -1), (-1, 0)):
            n = (cx + dx, cy + dy)
            if n not in vus and decor.case(*n) is not None: vus.add(n); file.append(n)
    return x, y


def chemin(nom): return f'{JEU}/data/maps/{nom}_Frlg/map.json'


def origine(nom):
    p = chemin(nom)
    if not os.path.exists(p + '.rougefeu'): shutil.copy(p, p + '.rougefeu')
    return lire(p + '.rougefeu')


# Entrées creusées dans le décor importé (l'import recopie le décor d'origine à chaque passage).
for dossier, blocs in RETOUCHES.items():
    p = f'{JEU}/data/layouts/{dossier}/map.bin'; d = bytearray(open(p, 'rb').read())
    w = next(l['width'] for l in LAY.values() if l['blockdata_filepath'].endswith(f'/{dossier}/map.bin'))
    for x, y, bloc in blocs: struct.pack_into('<H', d, 2 * (x + y * w), bloc)
    open(p, 'wb').write(d)

ID = {NOM_HNS.get(n, n): lire(chemin(n))['id'] for n in CARTES}
ID_HNS = {lire(f'{HNS}/data/maps/{h}/map.json')['id']: i for h, i in ID.items()}
pc = {}

for nom in CARTES:
    hnom = NOM_HNS.get(nom, nom)
    h = lire(f'{HNS}/data/maps/{hnom}/map.json')
    # Connexions : celles de HnS, limitées aux cartes basculées.
    conn = []
    for c in h.get('connections') or []:
        if c['map'] in ID_HNS:
            n = {'map': ID_HNS[c['map']], 'offset': c['offset'], 'direction': c['direction']}
            if n not in conn: conn.append(n)
    if nom in ZONE1:
        j = lire(chemin(nom)); j['connections'] = conn; ecrire(chemin(nom), j); continue

    j = origine(nom)
    avant = Decor(j['layout']); apres = Decor(LAYOUTS_HNS[hnom])
    j['layout'] = LAYOUTS_HNS[hnom]; j['connections'] = conn
    table = PORTES.get(nom, {})

    # Portes, puis décalage médian de la carte.
    dx = dy = 0
    deltas = [(b[0] - a[0], b[1] - a[1]) for a, b in table.items() if b]
    if deltas:
        dx = int(statistics.median(d[0] for d in deltas)); dy = int(statistics.median(d[1] for d in deltas))
    regulier = len(set(deltas)) <= 1 and (avant.w, avant.h) == (apres.w - 0, apres.h) or len(set(deltas)) == 1
    secours = next((b for b in table.values() if b), None)
    for w in j['warp_events']:
        a = (w['x'], w['y'])
        if a not in table: rapport.append(f'{nom}: porte {a} hors table'); continue
        b = table[a]
        if b is None:
            meme = [table[(v['x'], v['y'])] for v in j['warp_events']
                    if v['dest_map'] == w['dest_map'] and table.get((v['x'], v['y']))]
            b = meme[0] if meme else (secours or a)
            rapport.append(f'{nom}: porte {a} vers {w["dest_map"]} sans bâtiment dans HnS')
        w['_n'] = b
    for w in j['warp_events']:
        if '_n' in w: w['x'], w['y'] = w.pop('_n')
        w['elevation'] = 0      # la porte vaut pour toute altitude : celles de Rouge Feu ne suivent pas le relief HnS
        if 'POKEMON_CENTER' in w['dest_map']: pc[j['id']] = (w['x'], w['y'] + 1)
    portes = {(w['x'], w['y']) for w in j['warp_events']}

    # PNJ.
    libres = {}
    for o in h['object_events']:
        if any(k in o['graphics_id'] for k in ('BERRY_TREE', 'POKE_BALL', 'LIGHT_SPRITE')): continue
        libres.setdefault(role(o), []).append(o)
    pris = set(portes) | {(x, y + 1) for x, y in portes}
    places = 0
    en_attente = []
    for o in j['object_events']:
        k = apres.case(o['x'] + dx, o['y'] + dy); k0 = avant.case(o['x'], o['y'])
        eau = bool(k0 and k0[1])
        r = role(o)
        if k == (0, eau) and (o['x'] + dx, o['y'] + dy) not in pris and r in ('passant', 'dresseur', 'objet'):
            o['x'] += dx; o['y'] += dy; pris.add((o['x'], o['y'])); places += 1
        else:
            en_attente.append((o, eau, r))
    for o, eau, r in en_attente:
        cx, cy = o['x'] + dx, o['y'] + dy
        cand = [c for c in libres.get(r, []) if (c['x'], c['y']) not in pris
                and (apres.case(c['x'], c['y']) or (1, 0))[1] == eau]
        if cand:
            c = min(cand, key=lambda c: abs(c['x'] - cx) + abs(c['y'] - cy))
            o['x'], o['y'] = c['x'], c['y']
            if r == 'dresseur':
                for cle in ('movement_type', 'movement_range_x', 'movement_range_y'): o[cle] = c[cle]
            libres[r].remove(c)
        elif r in ('arbre', 'rocher', 'bloc') and 'local_id' not in o:
            o['_retire'] = True; continue          # obstacle sans équivalent dans le décor HnS
        else:
            o['x'], o['y'] = plus_proche(apres, cx, cy, eau, pris)
            if r != 'passant': rapport.append(f'{nom}: {r} {o["graphics_id"][14:]} placé au plus près en ({o["x"]},{o["y"]})')
        pris.add((o['x'], o['y']))
    j['object_events'] = [o for o in j['object_events'] if not o.get('_retire')]
    for o in j['object_events']: niveau(apres, o)
    # Obstacles HnS sans équivalent : clonés depuis un obstacle Rouge Feu.
    for r, gfx, script in (('arbre', 'OBJ_EVENT_GFX_CUTTABLE_TREE_FRLG', 'EventScript_CutTree'),
                           ('rocher', 'OBJ_EVENT_GFX_BREAKABLE_ROCK_FRLG', 'EventScript_RockSmash'),
                           ('bloc', 'OBJ_EVENT_GFX_PUSHABLE_BOULDER_FRLG', 'EventScript_StrengthBoulder')):
        for c in libres.get(r, []):
            if (c['x'], c['y']) in pris: continue
            j['object_events'].append({"type": "object", "graphics_id": gfx, "x": c['x'], "y": c['y'],
                "elevation": 3, "movement_type": "MOVEMENT_TYPE_FACE_DOWN", "movement_range_x": 1,
                "movement_range_y": 1, "trainer_type": "TRAINER_TYPE_NONE",
                "trainer_sight_or_berry_tree_id": "0", "script": script,
                "flag": f"FLAG_TEMP_{0x11 + len([1 for o in j['object_events'] if o['script'] == script]) % 14:X}"})
            pris.add((c['x'], c['y']))

    # Panneaux et objets cachés.
    panneaux = [b for b in h['bg_events'] if b['type'] == 'sign']
    garde = []
    for b in j['bg_events']:
        cx, cy = b['x'] + dx, b['y'] + dy
        k = apres.case(cx, cy)
        if b['type'] != 'sign':
            b['x'], b['y'] = (cx, cy) if k == (0, False) else plus_proche(apres, cx, cy, False, set())
            garde.append(b); continue
        if (cx, cy) in portes or (k and k[0] != 0 and any((p['x'], p['y']) == (cx, cy) for p in panneaux)):
            b['x'], b['y'] = cx, cy; garde.append(b)
            panneaux = [p for p in panneaux if (p['x'], p['y']) != (cx, cy)]
        else:
            b['_att'] = (cx, cy); garde.append(b)
    for b in [b for b in garde if '_att' in b]:
        cx, cy = b.pop('_att')
        if panneaux:
            p = min(panneaux, key=lambda p: abs(p['x'] - cx) + abs(p['y'] - cy))
            b['x'], b['y'] = p['x'], p['y']; panneaux.remove(p)
        else:
            garde.remove(b); rapport.append(f'{nom}: panneau {b["script"]} retiré (aucun panneau libre dans le décor)')
    j['bg_events'] = garde

    # Déclencheurs : gardés seulement quand la carte s'est décalée d'un bloc.
    garde = []
    for c in j['coord_events']:
        k = apres.case(c['x'] + dx, c['y'] + dy)
        if len(set(deltas)) <= 1 and k and k[0] == 0:
            c['x'] += dx; c['y'] += dy; garde.append(c)
        else:
            rapport.append(f'{nom}: déclencheur {c.get("script")} retiré, à réécrire')
    j['coord_events'] = garde
    ecrire(chemin(nom), j)
    print(f'{nom:16} {avant.w}x{avant.h} -> {apres.w}x{apres.h}  décalage ({dx},{dy})  PNJ en place {places}/{len(j["object_events"])}')

# Route 21 : HnS n'a qu'une carte. Les PNJ de la moitié sud rejoignent la carte nord.
nord = lire(chemin('Route21_North')); sud = origine('Route21_South'); decor = Decor(nord['layout'])
pris = {(o['x'], o['y']) for o in nord['object_events']}
for o in copy.deepcopy(sud['object_events']):
    o['x'], o['y'] = plus_proche(decor, o['x'], o['y'] + 50, True, pris); pris.add((o['x'], o['y']))
    nord['object_events'].append(o); niveau(decor, o)
ecrire(chemin('Route21_North'), nord)

# Cave Taupiqueur : la sortie sud passe de la Route 11 à Carmin.
src, case, dst, ncase, interieur = PORTE_DEPLACEE
r11 = origine(src); v = lire(chemin(dst))
w = copy.deepcopy(next(w for w in r11['warp_events'] if (w['x'], w['y']) == case))
w['x'], w['y'] = ncase
if not any((x['x'], x['y']) == ncase for x in v['warp_events']): v['warp_events'].append(w)
ecrire(chemin(dst), v)
p = chemin(interieur); i = origine(interieur)
for x in i['warp_events']:
    if x['dest_map'] == r11['id']: x['dest_map'] = v['id']; x['dest_warp_id'] = str(len(v['warp_events']) - 1)
ecrire(p, i)

# Safran : les routes se raccordaient à une carte relais, elles se raccordent maintenant à la ville.
# Points de soin : devant la porte du Centre.
p = f'{JEU}/src/data/heal_locations.json'
if not os.path.exists(p + '.rougefeu'): shutil.copy(p, p + '.rougefeu')
s = lire(p + '.rougefeu')
for e in s['heal_locations']:
    if e['map'] in pc and e['id'].startswith('HEAL_LOCATION_') and 'respawn_map' in e and 'POKEMON_CENTER' in e['respawn_map']:
        e['x'], e['y'] = pc[e['map']]
ecrire(p, s)
open(f'{ICI}/rapport_exterieurs.txt', 'w').write('\n'.join(rapport) + '\n')
print(len(rapport), 'points dans le rapport')
