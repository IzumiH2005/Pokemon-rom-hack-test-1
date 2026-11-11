#!/usr/bin/env python3
"""Passe les intérieurs des villes et des routes de Kanto sur les décors Heart & Soul.

Usage : python3 basculer_interieurs.py <pokemonHnS> <jeu>     (après basculer_exterieurs.py)

Les paires se déduisent des portes : une porte Rouge Feu et une porte HnS posées sur la même case
d'un extérieur mènent au même bâtiment. Chaque intérieur reprend le décor et les portes de HnS,
et garde les PNJ et les scripts de Rouge Feu, replacés sur les emplacements des PNJ de HnS.
Le script repart des copies `map.json.rougefeu` et écrit `rapport_interieurs.txt`.
"""
import json, os, struct, sys, re, shutil, copy
from collections import deque
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from tables import PORTES, PLACES

HNS, JEU = sys.argv[1], sys.argv[2]
ICI = os.path.dirname(os.path.abspath(__file__))
LAYOUTS_HNS = json.load(open(f'{ICI}/layouts_kanto_hns.json'))
NOM_HNS = {'Route21_North': 'Route21'}
EXT = ['PalletTown', 'ViridianCity', 'PewterCity', 'CeruleanCity', 'LavenderTown', 'VermilionCity', 'CeladonCity',
       'FuchsiaCity', 'CinnabarIsland', 'SaffronCity'] + [f'Route{i}' for i in range(1, 21)] + \
      ['Route21_North', 'Route22', 'Route24', 'Route25']
ETAGES = {  # étages sans porte sur l'extérieur : Rouge Feu -> HnS
 'PalletTown_PlayersHouse_2F': 'PalletTown_RedsHouse_2F', 'PewterCity_Museum_2F': 'PewterCity_Museum_2F',
 'CeladonCity_DepartmentStore_2F': 'CeladonCity_DepartmentStore_2F',
 'CeladonCity_DepartmentStore_3F': 'CeladonCity_DepartmentStore_3F',
 'CeladonCity_DepartmentStore_4F': 'CeladonCity_DepartmentStore_4F',
 'CeladonCity_DepartmentStore_5F': 'CeladonCity_DepartmentStore_5F',
 'CeladonCity_DepartmentStore_Roof': 'CeladonCity_DepartmentStore_RoofDay',
 'CeladonCity_Condominiums_2F': 'CeladonCity_Apartments_2F', 'CeladonCity_Condominiums_3F': 'CeladonCity_Apartments_3F',
 'CeladonCity_Condominiums_Roof': 'CeladonCity_Apartments_RoofDay',
 'CeladonCity_Condominiums_RoofRoom': 'CeladonCity_Apartments_RoofHouse',
 'SaffronCity_CopycatsHouse_2F': 'SaffronCity_CopyCatsHouse_2F',
}
DONJONS = ('VIRIDIAN_FOREST', 'MT_MOON', 'ROCK_TUNNEL', 'DIGLETTS_CAVE', 'SEAFOAM', 'CERULEAN_CAVE', 'VICTORY_ROAD',
           'POWER_PLANT', 'POKEMON_TOWER', 'SILPH_CO', 'UNDERGROUND_PATH', 'SSANNE', 'SAFARI_ZONE', 'POKEMON_MANSION')
rapport = []


def lire(p): return json.load(open(p))


def ecrire(p, j):
    json.dump(j, open(p, 'w'), indent=2, ensure_ascii=False); open(p, 'a').write('\n')


def dossier(ident):
    return DOSSIER[ident]


DOSSIER = {}
for d in os.listdir(f'{JEU}/data/maps'):
    p = f'{JEU}/data/maps/{d}/map.json'
    if d.endswith('_Frlg') and os.path.exists(p): DOSSIER[lire(p)['id']] = d
HDOSSIER = {}
for d in os.listdir(f'{HNS}/data/maps'):
    p = f'{HNS}/data/maps/{d}/map.json'
    if os.path.exists(p): HDOSSIER[lire(p)['id']] = d


def chemin(d): return f'{JEU}/data/maps/{d}/map.json'


def origine(d):
    p = chemin(d)
    if not os.path.exists(p + '.rougefeu'): shutil.copy(p, p + '.rougefeu')
    return lire(p + '.rougefeu')


def hns(d): return lire(f'{HNS}/data/maps/{d}/map.json')


# 1. Paires d'extérieurs, puis paires d'intérieurs par les portes.
paire = {}      # dossier Rouge Feu -> dossier HnS
for n in EXT: paire[n + '_Frlg'] = NOM_HNS.get(n, n)
exterieurs = set(paire)
for n in EXT:
    f = lire(chemin(n + '_Frlg')); h = hns(NOM_HNS.get(n, n)); av = origine(n + '_Frlg')
    absentes = {i for i, w in enumerate(av['warp_events']) if PORTES.get(n, {}).get((w['x'], w['y']), 0) is None}
    for i, w in enumerate(f['warp_events']):
        if i in absentes or w['dest_map'] not in DOSSIER: continue
        if any(k in w['dest_map'] for k in DONJONS): continue
        hw = next((x for x in h['warp_events'] if (x['x'], x['y']) == (w['x'], w['y'])), None)
        if not hw or hw['dest_map'] not in HDOSSIER: continue
        fd, hd = DOSSIER[w['dest_map']], HDOSSIER[hw['dest_map']]
        if hd not in LAYOUTS_HNS or fd in paire or hd in paire.values(): continue
        paire[fd] = hd
for fd, hd in ETAGES.items():
    if os.path.exists(chemin(fd + '_Frlg')) and hd in LAYOUTS_HNS: paire[fd + '_Frlg'] = hd
    else: rapport.append(f'{fd}: étage introuvable')
inverse = {v: k for k, v in paire.items()}
interieurs = [f for f in paire if f not in exterieurs]

LAY = {x['id']: x for x in lire(f'{JEU}/data/layouts/layouts.json')['layouts'] if x}


class Decor:
    def __init__(self, lid):
        self.l = LAY[lid]; self.w, self.h = self.l['width'], self.l['height']
        self.d = open(f'{JEU}/{self.l["blockdata_filepath"]}', 'rb').read()

    def brut(self, x, y): return struct.unpack_from('<H', self.d, 2 * (x + y * self.w))[0]

    def libre(self, x, y): return 0 <= x < self.w and 0 <= y < self.h and (self.brut(x, y) >> 10) & 3 == 0


def accessibles(decor, portes):
    """Cases où le joueur peut marcher depuis une porte."""
    vus = set(); file = deque()
    for w in portes:
        for dx, dy in ((0, 0), (0, -1), (0, 1), (1, 0), (-1, 0)):
            c = (w['x'] + dx, w['y'] + dy)
            if decor.libre(*c) and c not in vus: vus.add(c); file.append(c)
    while file:
        cx, cy = file.popleft()
        for dx, dy in ((0, 1), (1, 0), (0, -1), (-1, 0)):
            c = (cx + dx, cy + dy)
            if c not in vus and decor.libre(*c): vus.add(c); file.append(c)
    return vus


def plus_proche(decor, x, y, pris, sol):
    x = min(max(x, 0), decor.w - 1); y = min(max(y, 0), decor.h - 1)
    vus = {(x, y)}; file = deque([(x, y)])
    while file:
        cx, cy = file.popleft()
        if (cx, cy) in sol and (cx, cy) not in pris: return cx, cy
        for dx, dy in ((0, 1), (1, 0), (0, -1), (-1, 0)):
            n = (cx + dx, cy + dy)
            if n not in vus and 0 <= n[0] < decor.w and 0 <= n[1] < decor.h: vus.add(n); file.append(n)
    return x, y


def role(o):
    g = o['graphics_id']
    if 'NURSE' in g: return 'infirmiere'
    if 'MART_EMPLOYEE' in g or 'CLERK' in g: return 'vendeur'
    if 'ITEM_BALL' in g: return 'objet'
    if o.get('trainer_type', 'TRAINER_TYPE_NONE') not in ('TRAINER_TYPE_NONE', '0'): return 'dresseur'
    return 'passant'


# 2. Intérieurs.
nouveau = {}
for fd in interieurs:
    hd = paire[fd]; f = origine(fd); h = hns(hd)
    avant = LAY[f['layout']]; f['layout'] = LAYOUTS_HNS[hd]; decor = Decor(f['layout'])
    # Portes : la liste HnS, traduite. Les portes HnS vers une carte non reprise reçoivent, dans l'ordre,
    # les portes Rouge Feu qui mènent à une carte restée en place.
    restees = [w for w in f['warp_events'] if DOSSIER.get(w['dest_map']) not in paire]
    portes = []
    for i, w in enumerate(h['warp_events']):
        n = {'x': w['x'], 'y': w['y'], 'elevation': w['elevation'], 'dest_map': f['id'], 'dest_warp_id': str(i)}
        cible = inverse.get(HDOSSIER.get(w['dest_map']))
        if cible in exterieurs:
            ext = lire(chemin(cible)); hext = hns(paire[cible])
            k = int(w['dest_warp_id'])
            pos = (hext['warp_events'][k]['x'], hext['warp_events'][k]['y']) if k < len(hext['warp_events']) else None
            idx = [a for a, e in enumerate(ext['warp_events']) if (e['x'], e['y']) == pos and e['dest_map'] == f['id']] \
                or [a for a, e in enumerate(ext['warp_events']) if e['dest_map'] == f['id']]
            if idx: n['dest_map'] = ext['id']; n['dest_warp_id'] = str(idx[0])
            else: rapport.append(f'{fd}: sortie {i} sans porte côté extérieur')
        elif cible:
            n['dest_map'] = lire(chemin(cible))['id']; n['dest_warp_id'] = str(w['dest_warp_id'])
        elif restees:
            r = restees.pop(0); n['dest_map'] = r['dest_map']; n['dest_warp_id'] = r['dest_warp_id']
        else:
            rapport.append(f'{fd}: porte {i} ({w["x"]},{w["y"]}) vers {w["dest_map"]} sans carte')
        portes.append(n)
    for r in restees: rapport.append(f'{fd}: accès perdu vers {r["dest_map"]}')
    f['warp_events'] = portes
    # PNJ sur les emplacements des PNJ HnS.
    sx, sy = decor.w / avant['width'], decor.h / avant['height']
    libres = [o for o in h['object_events'] if 'LIGHT_SPRITE' not in o['graphics_id']]
    pris = {(w['x'], w['y']) for w in portes} | {(w['x'], w['y'] - 1) for w in portes}
    sol = accessibles(decor, portes); fixes = PLACES.get(fd[:-5], {})
    for o in sorted(f['object_events'], key=lambda o: role(o) == 'passant'):
        cx, cy = round(o['x'] * sx), round(o['y'] * sy); r = role(o)
        cand = [c for c in libres if role(c) == r and (c['x'], c['y']) not in pris]
        if o.get('local_id') in fixes:
            o['x'], o['y'] = fixes[o['local_id']]; pris.add((o['x'], o['y'])); continue
        if not cand and r in ('dresseur', 'passant'):
            cand = [c for c in libres if role(c) in ('dresseur', 'passant') and (c['x'], c['y']) not in pris]
        if cand:
            c = min(cand, key=lambda c: abs(c['x'] - cx) + abs(c['y'] - cy)); libres.remove(c)
            o['x'], o['y'] = c['x'], c['y']
            if r in ('infirmiere', 'vendeur', 'dresseur'):
                for cle in ('movement_type', 'movement_range_x', 'movement_range_y'): o[cle] = c[cle]
        else:
            o['x'], o['y'] = plus_proche(decor, cx, cy, pris, sol)
            if r != 'passant': rapport.append(f'{fd}: {r} placé au plus près en ({o["x"]},{o["y"]})')
        e = decor.brut(o['x'], o['y']) >> 12
        if 1 <= e <= 14: o['elevation'] = e
        pris.add((o['x'], o['y']))
    # Éléments de décor interactifs : sur ceux de HnS, le reste est retiré.
    fonds = [b for b in h['bg_events']]
    garde = []
    for b in f['bg_events']:
        cx, cy = round(b['x'] * sx), round(b['y'] * sy)
        if fonds:
            c = min(fonds, key=lambda c: abs(c['x'] - cx) + abs(c['y'] - cy)); fonds.remove(c)
            b['x'], b['y'] = c['x'], c['y']; garde.append(b)
    if len(garde) < len(f['bg_events']): rapport.append(f'{fd}: {len(f["bg_events"]) - len(garde)} élément(s) de décor retiré(s)')
    f['bg_events'] = garde
    for c in f['coord_events']: rapport.append(f'{fd}: déclencheur {c.get("script")} retiré, à réécrire')
    f['coord_events'] = []
    f['connections'] = None
    nouveau[fd] = f

for fd, f in nouveau.items(): ecrire(chemin(fd), f)

# 3. Portes des extérieurs : numéro d'arrivée repris de la porte HnS posée sur la même case.
for n in EXT:
    fd = n + '_Frlg'; f = lire(chemin(fd)); h = hns(paire[fd])
    for w in f['warp_events']:
        cible = DOSSIER.get(w['dest_map'])
        if cible not in nouveau: continue
        hw = next((x for x in h['warp_events'] if (x['x'], x['y']) == (w['x'], w['y'])
                   and inverse.get(HDOSSIER.get(x['dest_map'])) == cible), None)
        w['dest_warp_id'] = str(hw['dest_warp_id']) if hw else '0'
    ecrire(chemin(fd), f)

# 4. Cartes restées en place : leurs portes vers un intérieur basculé visent la porte qui revient vers elles.
for d in DOSSIER.values():
    if d in paire: continue
    j = origine(d) if os.path.exists(chemin(d) + '.rougefeu') else lire(chemin(d)); change = False
    for w in j['warp_events']:
        cible = DOSSIER.get(w['dest_map'])
        if cible in nouveau:
            retour = [i for i, x in enumerate(nouveau[cible]['warp_events']) if x['dest_map'] == j['id']]
            if not os.path.exists(chemin(d) + '.rougefeu'): shutil.copy(chemin(d), chemin(d) + '.rougefeu')
            w['dest_warp_id'] = str(retour[0]) if retour else '0'; change = True
            if not retour: rapport.append(f'{d}: plus de retour depuis {cible}')
    if change: ecrire(chemin(d), j)

open(f'{ICI}/rapport_interieurs.txt', 'w').write('\n'.join(rapport) + '\n')
json.dump({k: v for k, v in sorted(paire.items()) if k not in exterieurs}, open(f'{ICI}/paires_interieurs.json', 'w'), indent=1)
print(len(interieurs), 'intérieurs basculés,', len(rapport), 'points dans le rapport')
