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
from tables import (PORTES, PLACES, PAIRES_FIXES, DEJA, FUSIONS, NOUVELLES, SCRIPTS_RETIRES, HABITANTS, DECLENCHEURS,
                    PORTES_AJOUTEES, TRANSFERTS, REMPLACEMENTS, SCRIPTS_AJOUTES,
                    DECLENCHEURS_AJOUTES, PANNEAUX, PORTES_FORCEES)
PAIRES_FIXES = dict(PAIRES_FIXES, **{n: n for n in NOUVELLES})

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
for fd, hd in PAIRES_FIXES.items():
    if os.path.exists(chemin(fd + '_Frlg')) and hd in LAYOUTS_HNS: paire[fd + '_Frlg'] = hd
    else: rapport.append(f'{fd}: carte ou décor introuvable ({hd})')
inverse = {v: k for k, v in paire.items()}
for fd, hd in DEJA.items(): inverse[hd] = fd + '_Frlg'
interieurs = [f for f in paire if f not in exterieurs]

LAY = {x['id']: x for x in lire(f'{JEU}/data/layouts/layouts.json')['layouts'] if x}
META = open(f'{JEU}/src/data/tilesets/metatiles.h').read()
EAU = set(range(0x10, 0x18))      # comportements de métatuile : eau
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

    def brut(self, x, y): return struct.unpack_from('<H', self.d, 2 * (x + y * self.w))[0]

    def libre(self, x, y): return 0 <= x < self.w and 0 <= y < self.h and (self.brut(x, y) >> 10) & 3 == 0

    def eau(self, x, y):
        m = self.brut(x, y) & 0x3FF
        a = attributs(self.l['primary_tileset' if m < 640 else 'secondary_tileset']); i = m if m < 640 else m - 640
        return (a[i] & 0x1FF if i < len(a) else 0) in EAU

    def sec(self, x, y): return self.libre(x, y) and not self.eau(x, y)


def accessibles(decor, portes):
    """Cases où le joueur peut marcher à pied depuis une porte. Sans porte : depuis les bords de la carte."""
    vus = set(); file = deque()
    departs = [(w['x'] + dx, w['y'] + dy) for w in portes for dx, dy in ((0, 0), (0, -1), (0, 1), (1, 0), (-1, 0))]
    if not portes:
        departs = [(x, y) for x in range(decor.w) for y in range(decor.h) if x in (0, decor.w - 1) or y in (0, decor.h - 1)]
    for c in departs:
        if decor.sec(*c) and c not in vus: vus.add(c); file.append(c)
    while file:
        cx, cy = file.popleft()
        for dx, dy in ((0, 1), (1, 0), (0, -1), (-1, 0)):
            c = (cx + dx, cy + dy)
            if c not in vus and decor.sec(*c): vus.add(c); file.append(c)
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


OBSTACLES = ('BOULDER', 'BREAKABLE_ROCK', 'CUTTABLE_TREE')   # liés au relief : seulement sur ceux de HnS


def role(o):
    g = o['graphics_id']
    if 'NURSE' in g: return 'infirmiere'
    if 'MART_EMPLOYEE' in g or 'CLERK' in g: return 'vendeur'
    if 'ITEM_BALL' in g: return 'objet'
    for k in OBSTACLES:
        if k in g: return k
    if o.get('trainer_type', 'TRAINER_TYPE_NONE') not in ('TRAINER_TYPE_NONE', '0'): return 'dresseur'
    return 'passant'


def fixer(o, place, decor):
    """Pose un PNJ sur une case choisie à la main : (x, y) ou (x, y, type de mouvement)."""
    o['x'], o['y'] = place[:2]
    if len(place) > 2: o['movement_type'] = place[2]
    e = decor.brut(o['x'], o['y']) >> 12
    if 1 <= e <= 14: o['elevation'] = e


def declencheurs(originaux, places, decor, nom):
    """Déclencheurs de Rouge Feu reposés sur les cases de la table. Un script garde une case, ou une liste de cases :
    la i-ème case reçoit le i-ème déclencheur d'origine de ce script, le dernier est recopié s'il en manque."""
    gardes, par = [], {}
    for c in originaux: par.setdefault(c.get('script'), []).append(c)
    for s, cs in par.items():
        if s not in places:
            rapport.append(f'{nom}: déclencheur {s} retiré, à réécrire'); continue
        cases = places[s] if isinstance(places[s], list) else [places[s]]
        for i, (x, y) in enumerate(cases):
            gardes.append(dict(copy.deepcopy(cs[min(i, len(cs) - 1)]), x=x, y=y, elevation=decor.brut(x, y) >> 12))
    return gardes


# 2. Intérieurs.
nouveau = {}
for fd in interieurs:
    hd = paire[fd]; f = origine(fd); h = hns(hd)
    avant = LAY[f['layout']]; f['layout'] = LAYOUTS_HNS[hd]; decor = Decor(f['layout'])
    # Portes : la liste HnS, traduite. Les portes HnS vers une carte non reprise reçoivent, dans l'ordre,
    # les portes Rouge Feu qui mènent à une carte restée en place.
    restees = [w for w in f['warp_events'] if DOSSIER.get(w['dest_map']) not in paire
               and DOSSIER.get(w['dest_map']) not in inverse.values()]
    portes = []
    for i, w in enumerate(h['warp_events']):
        n = {'x': max(w['x'], 0), 'y': max(w['y'], 0), 'elevation': w['elevation'], 'dest_map': f['id'], 'dest_warp_id': str(i)}
        cible = inverse.get(HDOSSIER.get(w['dest_map']))
        if cible in exterieurs:
            ext = lire(chemin(cible)); hext = hns(paire[cible])
            k = int(w['dest_warp_id'])
            pos = (hext['warp_events'][k]['x'], hext['warp_events'][k]['y']) if k < len(hext['warp_events']) else None
            idx = [a for a, e in enumerate(ext['warp_events']) if (e['x'], e['y']) == pos and e['dest_map'] == f['id']] \
                or [a for a, e in enumerate(ext['warp_events']) if (e['x'], e['y']) == pos] \
                or [a for a, e in enumerate(ext['warp_events']) if e['dest_map'] == f['id']]
            if idx: n['dest_map'] = ext['id']; n['dest_warp_id'] = str(idx[0])
            else: rapport.append(f'{fd}: sortie {i} sans porte côté extérieur')
        elif cible:
            n['dest_map'] = lire(chemin(cible))['id']; n['dest_warp_id'] = str(w['dest_warp_id'])
        elif restees:
            r = restees.pop(0); n['dest_map'] = r['dest_map']; n['dest_warp_id'] = r['dest_warp_id']
            rapport.append(f'{fd}: porte {i} ({w["x"]},{w["y"]}) reliée à {r["dest_map"]}, carte de Rouge Feu gardée')
        else:
            rapport.append(f'{fd}: porte {i} ({w["x"]},{w["y"]}) vers {w["dest_map"]} sans carte')
        portes.append(n)
    for x, y, carte, num in PORTES_AJOUTEES.get(fd[:-5], []):
        portes.append({'x': x, 'y': y, 'elevation': 0, 'dest_map': carte, 'dest_warp_id': num})
        restees = [r for r in restees if r['dest_map'] != carte]
    for r in restees: rapport.append(f'{fd}: accès perdu vers {r["dest_map"]}')
    f['warp_events'] = portes
    # PNJ sur les emplacements des PNJ HnS.
    sx, sy = decor.w / avant['width'], decor.h / avant['height']
    libres = [o for o in h['object_events'] if 'LIGHT_SPRITE' not in o['graphics_id']]
    pris = {(w['x'], w['y']) for w in portes} | {(w['x'], w['y'] - 1) for w in portes} | {(w['x'], w['y'] + 1) for w in portes}
    sol = accessibles(decor, portes); fixes = PLACES.get(fd[:-5], {})
    for o in f['object_events']: o['_dim'] = (avant['width'], avant['height'])
    for autre in FUSIONS.get(fd[:-5], []):
        a = origine(autre + '_Frlg'); dim = (LAY[a['layout']]['width'], LAY[a['layout']]['height'])
        for o in a['object_events']:
            if role(o) in ('dresseur', 'objet') and not o.get('local_id'):
                o['_dim'] = dim; f['object_events'].append(o)
        rapport.append(f'{autre}: étage sans équivalent, dresseurs et objets déplacés dans {fd[:-5]}, scènes à réécrire')
    for autre in HABITANTS.get(fd[:-5], []):
        a = origine(autre + '_Frlg'); dim = (LAY[a['layout']]['width'], LAY[a['layout']]['height'])
        for o in a['object_events']: o['_dim'] = dim; f['object_events'].append(o)
        rapport.append(f'{autre}: bâtiment absent de Heart & Soul, ses occupants sont dehors dans {fd[:-5]}')
    f['object_events'] = f['object_events'][:64]
    retires = {}
    for k, o in enumerate(f['object_events']): o['_cle'] = next((c for c in (o.get('local_id'), o['script'], k) if c in fixes), None)
    for o in sorted(f['object_events'], key=lambda o: role(o) == 'passant'):
        cle = o.pop('_cle'); dw, dh = o.pop('_dim'); cx, cy = round(o['x'] * decor.w / dw), round(o['y'] * decor.h / dh); r = role(o)
        cand = [c for c in libres if role(c) == r and (c['x'], c['y']) not in pris]
        if cle is not None:
            fixer(o, fixes[cle], decor); pris.add((o['x'], o['y'])); continue
        if not cand and r in ('dresseur', 'passant'):
            cand = [c for c in libres if role(c) in ('dresseur', 'passant') and (c['x'], c['y']) not in pris]
        if not cand and r in OBSTACLES and not o.get('local_id'):
            o['_retire'] = True; retires[r] = retires.get(r, 0) + 1; continue
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
    f['object_events'] = [o for o in f['object_events'] if not o.pop('_retire', False)]
    for r, k in retires.items(): rapport.append(f'{fd}: {k} obstacle(s) {r} sans place dans le décor, retiré(s)')
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
    f['coord_events'] = declencheurs(f['coord_events'], DECLENCHEURS.get(fd[:-5], {}), decor, fd) + [{'type': 'trigger', 'x': x, 'y': y, 'elevation': 0, 'var': v, 'var_value': '0', 'script': s}
                                  for x, y, v, s in DECLENCHEURS_AJOUTES.get(fd[:-5], [])]
    for c in f['coord_events']: c['elevation'] = decor.brut(c['x'], c['y']) >> 12
    conn = []
    for c in h['connections'] or []:
        cible = inverse.get(HDOSSIER.get(c['map']))
        if cible: conn.append({'map': lire(chemin(cible))['id'], 'offset': c['offset'], 'direction': c['direction']})
    f['connections'] = conn or None
    nouveau[fd] = f

for fd, f in nouveau.items(): ecrire(chemin(fd), f)

def relier(f, h):
    """Ajoute les connexions HnS vers les cartes créées, absentes de Rouge Feu."""
    f['connections'] = f['connections'] or []
    for c in h['connections'] or []:
        cible = inverse.get(HDOSSIER.get(c['map']))
        if cible and cible[:-5] in NOUVELLES:
            ident = nouveau[cible]['id']
            f['connections'] = [x for x in f['connections'] if x['direction'] != c['direction'] or x['map'] == ident]
            if not any(x['map'] == ident for x in f['connections']):
                f['connections'].append({'map': ident, 'offset': c['offset'], 'direction': c['direction']})
    f['connections'] = f['connections'] or None


# 3. Portes des extérieurs : numéro d'arrivée repris de la porte HnS posée sur la même case.
for n in EXT:
    fd = n + '_Frlg'; f = lire(chemin(fd)); h = hns(paire[fd])
    for w in f['warp_events']:
        cible = DOSSIER.get(w['dest_map'])
        hw = next((x for x in h['warp_events'] if (x['x'], x['y']) == (w['x'], w['y'])
                   and inverse.get(HDOSSIER.get(x['dest_map'])) in nouveau), None)
        if hw: w['dest_map'] = nouveau[inverse[HDOSSIER[hw['dest_map']]]]['id']
        if not hw and cible not in nouveau: continue
        w['dest_warp_id'] = str(hw['dest_warp_id']) if hw else '0'
        if not hw: rapport.append(f'{fd}: porte ({w["x"]},{w["y"]}) vers {cible} sans porte Heart & Soul sur la même case')
    relier(f, h)
    ecrire(chemin(fd), f)
for fd, hd in DEJA.items():
    f = lire(chemin(fd + '_Frlg')); relier(f, hns(hd)); ecrire(chemin(fd + '_Frlg'), f)

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

# 4 bis. PNJ et déclencheurs d'un extérieur qui suivent leur lieu dans une autre carte.
for source, cle, cible, x, y in TRANSFERTS:
    av = origine(source + '_Frlg'); s = lire(chemin(source + '_Frlg')); c = lire(chemin(cible + '_Frlg'))
    o = next((o for o in av['object_events'] if cle in (o.get('local_id'), o['script'])), None)
    if o:
        s['object_events'] = [e for e in s['object_events'] if cle not in (e.get('local_id'), e['script'])]
        o = dict(o, x=x, y=y, elevation=Decor(c['layout']).brut(x, y) >> 12 or 3); c['object_events'].append(o)
    else:
        e = dict(next(e for e in av['coord_events'] if e.get('script') == cle), x=x, y=y,
                 elevation=Decor(c['layout']).brut(x, y) >> 12)
        c['coord_events'].append(e)
    ecrire(chemin(source + '_Frlg'), s); ecrire(chemin(cible + '_Frlg'), c)

# 4 ter. Extérieurs : PNJ et déclencheurs des scènes reposés à la main, d'après la copie Rouge Feu.
for nom in sorted(set(PLACES) | set(DECLENCHEURS) | set(PANNEAUX)):
    fd = nom + '_Frlg'
    if fd in interieurs: continue
    av = origine(fd); c = lire(chemin(fd)); decor = Decor(c['layout'])
    for o in c['object_events']:
        cle = next((k for k in (o.get('local_id'), o['script']) if k in PLACES.get(nom, {})), None)
        if cle: fixer(o, PLACES[nom][cle], decor)
    if nom in DECLENCHEURS:
        hors = [e for e in c['coord_events'] if e.get('script') not in {a.get('script') for a in av['coord_events']}]
        c['coord_events'] = declencheurs(av['coord_events'], DECLENCHEURS[nom], decor, fd) + hors
    if nom in PANNEAUX:
        t = PANNEAUX[nom]
        c['bg_events'] = [b for b in c['bg_events'] if b.get('script') not in t and (b['x'], b['y']) not in t.values()]
        for b in copy.deepcopy(av['bg_events']):
            if b.get('script') in t and b['script'] not in {x.get('script') for x in c['bg_events']}:
                b['x'], b['y'] = t[b['script']]; b['elevation'] = 0; c['bg_events'].append(b)
    ecrire(chemin(fd), c)

# 4 quater. Portes dont l'arrivée est imposée.
for nom, t in PORTES_FORCEES.items():
    c = lire(chemin(nom + '_Frlg'))
    for i, (carte, num) in t.items(): c['warp_events'][i]['dest_map'] = carte; c['warp_events'][i]['dest_warp_id'] = num
    ecrire(chemin(nom + '_Frlg'), c)

# 5. Scripts : sur un décor Heart & Soul, les commandes qui redessinent l'ancien décor sont neutralisées.
for fd in interieurs:
    p = f'{JEU}/data/maps/{fd}/scripts.inc'
    if not os.path.exists(p + '.rougefeu'): shutil.copy(p, p + '.rougefeu')
    lignes = open(p + '.rougefeu').read().split('\n'); k = 0
    for i, l in enumerate(lignes):
        if l.strip().startswith('setmetatile'): lignes[i] = '\t@ ancien décor : ' + l.strip(); k += 1
        if any(l.strip().startswith('map_script ' + s) for s in SCRIPTS_RETIRES.get(fd[:-5], ())):
            lignes[i] = '\t@ ancien décor : ' + l.strip(); k += 1
    open(p, 'w').write('\n'.join(lignes) + SCRIPTS_AJOUTES.get(fd[:-5], ''))
    if k: rapport.append(f'{fd}: {k} commande(s) de script liées à l\'ancien décor neutralisées')

# 6. Scripts qui visent une case précise de l'ancien décor : coordonnées et pas réécrits.
for rel, echanges in REMPLACEMENTS.items():
    p = f'{JEU}/{rel}'; deja = os.path.exists(p + '.rougefeu')
    if not deja: shutil.copy(p, p + '.rougefeu')
    t = open(p if rel.split('/')[-2] in interieurs else p + '.rougefeu').read()
    for a, b in echanges:
        if a not in t: rapport.append(f'{rel}: texte à remplacer introuvable ({a.strip()[:40]})')
        t = t.replace(a, b)
    open(p, 'w').write(t)

open(f'{ICI}/rapport_interieurs.txt', 'w').write('\n'.join(rapport) + '\n')
json.dump({k: v for k, v in sorted(paire.items()) if k not in exterieurs}, open(f'{ICI}/paires_interieurs.json', 'w'), indent=1)
print(len(interieurs), 'intérieurs basculés,', len(rapport), 'points dans le rapport')
