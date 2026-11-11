#!/usr/bin/env python3
"""Crée dans le jeu les cartes de Heart & Soul qui n'ont pas d'équivalent dans Rouge Feu.

Usage : python3 creer_cartes.py <pokemonHnS> <jeu>     (après importer_kanto_hns.py, avant basculer_interieurs.py)

Chaque carte naît vide (aucun PNJ, aucun script) sur son décor Heart & Soul. basculer_interieurs.py pose
ensuite ses portes et ses connexions comme pour les autres. Le script peut être relancé.
"""
import json, os, sys
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from tables import NOUVELLES, ZONES

HNS, JEU = sys.argv[1], sys.argv[2]
ICI = os.path.dirname(os.path.abspath(__file__))
LAYOUTS_HNS = json.load(open(f'{ICI}/layouts_kanto_hns.json'))
GROUPE = 'gMapGroup_KantoHns_Frlg'
MARQUE = '@ --- Import Heart & Soul : cartes ajoutees a Kanto ---'


def ecrire(p, j):
    json.dump(j, open(p, 'w'), indent=2, ensure_ascii=False); open(p, 'a').write('\n')


existants = set()
for d in os.listdir(f'{JEU}/data/maps'):
    p = f'{JEU}/data/maps/{d}/map.json'
    if os.path.exists(p) and d[:-5] not in NOUVELLES: existants.add(json.load(open(p))['id'])

for nom, (musique, zone) in NOUVELLES.items():
    h = json.load(open(f'{HNS}/data/maps/{nom}/map.json'))
    assert h['id'] not in existants, h['id']
    grotte = h['map_type'] == 'MAP_TYPE_UNDERGROUND'; dedans = h['map_type'] == 'MAP_TYPE_INDOOR'
    m = {'id': h['id'], 'name': nom + '_Frlg', 'layout': LAYOUTS_HNS[nom], 'music': musique,
         'region': 'REGION_KANTO', 'region_map_section': zone, 'requires_flash': False,
         'weather': 'WEATHER_NONE' if grotte or dedans else 'WEATHER_SUNNY', 'map_type': h['map_type'],
         'allow_cycling': not dedans, 'allow_escaping': grotte, 'allow_running': True,
         'show_map_name': not dedans, 'floor_number': 0, 'battle_scene': 'MAP_BATTLE_SCENE_NORMAL',
         'connections': None, 'object_events': [], 'warp_events': [], 'coord_events': [], 'bg_events': []}
    d = f'{JEU}/data/maps/{nom}_Frlg'
    os.makedirs(d, exist_ok=True)
    ecrire(d + '/map.json.rougefeu', m)
    if not os.path.exists(d + '/map.json'): ecrire(d + '/map.json', m)
    if not os.path.exists(d + '/scripts.inc'):
        open(d + '/scripts.inc', 'w').write(f'{nom}_Frlg_MapScripts::\n\t.byte 0\n')

p = f'{JEU}/data/maps/map_groups.json'
G = json.load(open(p))
if GROUPE not in G['group_order']: G['group_order'].append(GROUPE)
G[GROUPE] = [n + '_Frlg' for n in NOUVELLES]
ecrire(p, G)

p = f'{JEU}/data/event_scripts.s'
t = open(p).read()
if MARQUE in t: t = t[:t.index(MARQUE)].rstrip('\n') + '\n'
open(p, 'w').write(t + '\n' + MARQUE + '\n.if IS_FRLG\n'
                   + ''.join(f'\t.include "data/maps/{n}_Frlg/scripts.inc"\n' for n in NOUVELLES) + '.endif\n')

p = f'{JEU}/src/data/region_map/region_map_sections.json'
S = json.load(open(p))
for i, (n, x, y) in ZONES.items():
    if not any(s['id'] == i for s in S['map_sections']):
        S['map_sections'].append({'id': i, 'name': n, 'x': x, 'y': y, 'width': 1, 'height': 1})
ecrire(p, S)
print(len(NOUVELLES), 'cartes créées')
