#!/usr/bin/env python3
"""Complète l'import du Mont Argenté : raccord à la Route 22, intérieurs, panneaux, objets, rencontres.

Usage : python3 completer_mont_argente.py <dossier pokemonHnS> <dossier du jeu>
À lancer après importer_hns.py. Le script peut être relancé : il ne duplique rien.

- Poste de la Route 22 : une sortie ouest est ajoutée, elle mène à la Route 28.
- Centre Pokémon du Mont Argenté (rez-de-chaussée et étage) et maison de la Route 28,
  construits sur les layouts existants de Rouge Feu.
- Panneaux, 7 objets au sol, 5 rochers brisables, Red au sommet (dialogue provisoire).
- Pokémon sauvages repris de Heart & Soul (version de jour).
- Route 28 et Mont Argenté placés sur la carte de région, à l'ouest de la Route 22.
"""
import json, os, re, struct, sys

HNS, JEU = sys.argv[1], sys.argv[2]


def lire(p):
    return json.load(open(f'{JEU}/{p}'))


def ecrire(p, d):
    with open(f'{JEU}/{p}', 'w') as f:
        json.dump(d, f, indent=2, ensure_ascii=False)
        f.write('\n')


def carte(nom):
    return lire(f'data/maps/{nom}/map.json')


def objet(gfx, x, y, script, elevation=3, flag='0', mouvement='MOVEMENT_TYPE_FACE_DOWN', local_id=None):
    o = {'type': 'object', 'graphics_id': gfx, 'x': x, 'y': y, 'elevation': elevation,
         'movement_type': mouvement, 'movement_range_x': 1, 'movement_range_y': 1,
         'trainer_type': 'TRAINER_TYPE_NONE', 'trainer_sight_or_berry_tree_id': '0',
         'script': script, 'flag': flag}
    return dict({'local_id': local_id}, **o) if local_id else o


def panneau(x, y, script):
    return {'type': 'sign', 'x': x, 'y': y, 'elevation': 0,
            'player_facing_dir': 'BG_EVENT_PLAYER_FACING_ANY', 'script': script}


def warp(x, y, dest, wid, elevation=3):
    return {'x': x, 'y': y, 'elevation': elevation, 'dest_map': dest, 'dest_warp_id': str(wid)}


# 1. Poste de la Route 22 : colonne ajoutée à gauche, tapis de sortie ouest
L = lire('data/layouts/layouts.json')
poste = next(l for l in L['layouts'] if l and l.get('id') == 'LAYOUT_ROUTE22_NORTH_ENTRANCE')
if poste['width'] == 15:
    p = f"{JEU}/{poste['blockdata_filepath']}"
    d = open(p, 'rb').read()
    v = list(struct.unpack('<%dH' % (len(d) // 2), d))
    MUR, SOL = 0x0400, 0x3000          # collision / élévation 3
    bord = {4: 0x2D0, 5: 0x2D8, 6: 0x2E0}
    tapis = {4: 0x2D1, 5: 0x2D9, 6: 0x2E1}
    out = []
    for y in range(12):
        ligne = v[y * 15:(y + 1) * 15]
        if y in tapis:
            ligne[0] = tapis[y] | SOL
        out += [bord.get(y, 0x008) | MUR] + ligne
    open(p, 'wb').write(struct.pack('<%dH' % len(out), *out))
    poste['width'] = 16
    ecrire('data/layouts/layouts.json', L)
    m = carte('Route22_NorthEntrance_Frlg')
    for cle in ('object_events', 'warp_events', 'coord_events', 'bg_events'):
        for e in m[cle]:
            e['x'] += 1
    m['warp_events'] += [warp(1, 5, 'MAP_ROUTE28', 0), warp(1, 6, 'MAP_ROUTE28', 0)]
    ecrire('data/maps/Route22_NorthEntrance_Frlg/map.json', m)

# 2. Intérieurs : Centre Pokémon et maison
modele = carte('Route10_PokemonCenter_1F_Frlg')
base = {k: v for k, v in modele.items() if not k.endswith('_events')}
NOUVELLES = {}

c1 = dict(base, id='MAP_MT_SILVER_POKEMON_CENTER_1F', name='MtSilver_PokemonCenter_1F_Frlg',
          region_map_section='MAPSEC_MT_SILVER', connections=None)
c1['object_events'] = [
    objet('OBJ_EVENT_GFX_NURSE_FRLG', 7, 2, 'MtSilver_PokemonCenter_1F_EventScript_Nurse', elevation=0,
          local_id='LOCALID_MT_SILVER_NURSE'),
    objet('OBJ_EVENT_GFX_GENTLEMAN_FRLG', 11, 5, 'MtSilver_PokemonCenter_1F_EventScript_Gentleman'),
]
c1['warp_events'] = [warp(x, 8, 'MAP_MT_SILVER_OUTSIDE', 1) for x in (6, 7, 8)] + \
                    [warp(1, 6, 'MAP_MT_SILVER_POKEMON_CENTER_2F', 0)]
c1['coord_events'], c1['bg_events'] = [], []
NOUVELLES['MtSilver_PokemonCenter_1F_Frlg'] = (c1, '''MtSilver_PokemonCenter_1F_Frlg_MapScripts::
	map_script MAP_SCRIPT_ON_TRANSITION, MtSilver_PokemonCenter_1F_OnTransition
	map_script MAP_SCRIPT_ON_RESUME, CableClub_OnResume
	.byte 0

MtSilver_PokemonCenter_1F_OnTransition::
	setrespawn HEAL_LOCATION_MT_SILVER
	end

MtSilver_PokemonCenter_1F_EventScript_Nurse::
	lock
	faceplayer
	call EventScript_PkmnCenterNurse_Frlg
	release
	end

MtSilver_PokemonCenter_1F_EventScript_Gentleman::
	msgbox MtSilver_PokemonCenter_1F_Text_Gentleman, MSGBOX_NPC
	end

MtSilver_PokemonCenter_1F_Text_Gentleman::
	.string "Peu de DRESSEURS montent\\n"
	.string "jusqu'au MONT ARGENTE.\\p"
	.string "Les POKéMON sauvages y sont\\n"
	.string "d'une force redoutable.$"
''')

m2 = carte('Route10_PokemonCenter_2F_Frlg')
c2 = dict(m2, id='MAP_MT_SILVER_POKEMON_CENTER_2F', name='MtSilver_PokemonCenter_2F_Frlg',
          region_map_section='MAPSEC_MT_SILVER')
c2['warp_events'] = [dict(w, dest_map='MAP_MT_SILVER_POKEMON_CENTER_1F') if w['dest_map'] == 'MAP_ROUTE10_POKEMON_CENTER_1F'
                     else w for w in m2['warp_events']]
NOUVELLES['MtSilver_PokemonCenter_2F_Frlg'] = (c2, '''MtSilver_PokemonCenter_2F_Frlg_MapScripts::
	map_script MAP_SCRIPT_ON_FRAME_TABLE, CableClub_OnFrame_Frlg
	map_script MAP_SCRIPT_ON_WARP_INTO_MAP_TABLE, CableClub_OnWarp_Frlg
	map_script MAP_SCRIPT_ON_LOAD, CableClub_OnLoad_Frlg
	map_script MAP_SCRIPT_ON_TRANSITION, CableClub_OnTransition_Frlg
	.byte 0
''')

m3 = carte('Route2_House_Frlg')
c3 = dict({k: v for k, v in m3.items() if not k.endswith('_events')}, id='MAP_ROUTE28_HOUSE',
          name='Route28_House_Frlg', region_map_section='MAPSEC_ROUTE_28', music='MUS_RG_ROUTE11', connections=None)
c3['object_events'] = [objet('OBJ_EVENT_GFX_GENTLEMAN_FRLG', 4, 4, 'Route28_House_EventScript_Habitant')]
c3['warp_events'] = [warp(x, 7, 'MAP_ROUTE28', 1) for x in (3, 4, 5)]
c3['coord_events'], c3['bg_events'] = [], []
NOUVELLES['Route28_House_Frlg'] = (c3, '''Route28_House_Frlg_MapScripts::
	.byte 0

Route28_House_EventScript_Habitant::
	msgbox Route28_House_Text_Habitant, MSGBOX_NPC
	end

Route28_House_Text_Habitant::
	.string "Je me suis installé ici pour\\n"
	.string "avoir la paix.\\p"
	.string "Personne ne vient jusqu'à la\\n"
	.string "ROUTE 28.$"
''')

for nom, (m, script) in NOUVELLES.items():
    os.makedirs(f'{JEU}/data/maps/{nom}', exist_ok=True)
    ecrire(f'data/maps/{nom}/map.json', m)
    open(f'{JEU}/data/maps/{nom}/scripts.inc', 'w').write(script)

G = lire('data/maps/map_groups.json')
for nom in NOUVELLES:
    if nom not in G['gMapGroup_MtSilver_Frlg']:
        G['gMapGroup_MtSilver_Frlg'].append(nom)
ecrire('data/maps/map_groups.json', G)

p = f'{JEU}/data/event_scripts.s'
s = open(p).read()
MARQUE = '@ --- Mont Argente : interieurs ---'
if MARQUE not in s:
    s += f'\n{MARQUE}\n.if IS_FRLG\n' + ''.join(f'\t.include "data/maps/{n}/scripts.inc"\n' for n in NOUVELLES) + '.endif\n'
    open(p, 'w').write(s)

H = lire('src/data/heal_locations.json')
if not any(h['id'] == 'HEAL_LOCATION_MT_SILVER' for h in H['heal_locations']):
    H['heal_locations'].append({'id': 'HEAL_LOCATION_MT_SILVER', 'map': 'MAP_MT_SILVER_OUTSIDE', 'x': 25, 'y': 15,
                                'respawn_map': 'MAP_MT_SILVER_POKEMON_CENTER_1F', 'respawn_npc': 'LOCALID_MT_SILVER_NURSE'})
    ecrire('src/data/heal_locations.json', H)

# 3. Warps, panneaux, objets, rochers, Red
OBJETS = {  # carte -> [(x, y, objet, drapeau)]
    'MtSilver_Snow':             [(10, 40, 'RARE_CANDY', 'FLAG_0x0B0'), (31, 41, 'NEVER_MELT_ICE', 'FLAG_0x0B1')],
    'MtSilver_1F_WaterfallRoom': [(9, 23, 'FULL_RESTORE', 'FLAG_0x0B2'), (42, 35, 'MAX_POTION', 'FLAG_0x0B3'),
                                  (49, 11, 'DIRE_HIT', 'FLAG_0x0B4'), (9, 35, 'ULTRA_BALL', 'FLAG_0x0B5')],
    'MtSilver_1F_ItemRoom':      [(10, 7, 'SPELL_TAG', 'FLAG_0x0B6')],
}
PANNEAUX = {
    'Route28':          (56, 14, 'ROUTE 28\\n"\n\t.string "MONT ARGENTE - PLATEAU INDIGO'),
    'MtSilver_Outside': (15, 9, 'MONT ARGENTE'),
}
ROCHERS = [(48, 3), (47, 2), (3, 26), (3, 25), (3, 24)]

for nom in ['Route28', 'MtSilver_Outside', 'MtSilver_2F', 'MtSilver_SummitDay'] + list(OBJETS):
    m = carte(nom + '_Frlg')
    script = f'{nom}_Frlg_MapScripts::\n\t.byte 0\n'
    m['object_events'], m['bg_events'] = [], []
    for x, y, item, flag in OBJETS.get(nom, []):
        etiquette = f"{nom}_EventScript_Item{item.title().replace('_', '')}"
        m['object_events'].append(objet('OBJ_EVENT_GFX_ITEM_BALL', x, y, etiquette, flag=flag))
        script += f'\n{etiquette}::\n\tfinditem ITEM_{item}\n\tend\n'
    if nom in PANNEAUX:
        x, y, texte = PANNEAUX[nom]
        m['bg_events'].append(panneau(x, y, f'{nom}_EventScript_Panneau'))
        script += (f'\n{nom}_EventScript_Panneau::\n\tmsgbox {nom}_Text_Panneau, MSGBOX_SIGN\n\tend\n'
                   f'\n{nom}_Text_Panneau::\n\t.string "{texte}$"\n')
    if nom == 'MtSilver_2F':
        m['object_events'] = [objet('OBJ_EVENT_GFX_BREAKABLE_ROCK_FRLG', x, y, 'EventScript_RockSmash',
                                    flag=f'FLAG_TEMP_{i + 1}', mouvement='MOVEMENT_TYPE_LOOK_AROUND')
                              for i, (x, y) in enumerate(ROCHERS)]
    if nom == 'MtSilver_SummitDay':
        m['object_events'] = [objet('OBJ_EVENT_GFX_RED_NORMAL', 10, 6, 'MtSilver_SummitDay_EventScript_Red',
                                    mouvement='MOVEMENT_TYPE_FACE_UP')]
        script += ('\n@ Dialogue provisoire : le combat sera ecrit avec le scenario\n'
                   'MtSilver_SummitDay_EventScript_Red::\n\tmsgbox MtSilver_SummitDay_Text_Red, MSGBOX_NPC\n\tend\n'
                   '\nMtSilver_SummitDay_Text_Red::\n\t.string "… … …$"\n')
    if nom == 'Route28':
        m['warp_events'][0].update(dest_map='MAP_ROUTE22_NORTH_ENTRANCE', dest_warp_id='4')
        m['warp_events'][1].update(dest_map='MAP_ROUTE28_HOUSE', dest_warp_id='1')
    if nom == 'MtSilver_Outside':
        m['warp_events'][1].update(dest_map='MAP_MT_SILVER_POKEMON_CENTER_1F', dest_warp_id='1')
    ecrire(f'data/maps/{nom}_Frlg/map.json', m)
    open(f'{JEU}/data/maps/{nom}_Frlg/scripts.inc', 'w').write(script)

# 4. Pokémon sauvages (tables de jour de Heart & Soul)
LIMITES = {'land_mons': 12, 'water_mons': 5, 'rock_smash_mons': 5, 'fishing_mons': 10}
source = next(g for g in json.load(open(f'{HNS}/src/data/wild_encounters.json'))['wild_encounter_groups']
              if g['label'] == 'gWildMonHeaders')['encounters']
W = lire('src/data/wild_encounters.json')
groupe = next(g for g in W['wild_encounter_groups'] if g['label'] == 'gWildMonHeaders')
groupe['encounters'] = [e for e in groupe['encounters'] if not e['base_label'].startswith('sHns')]
vus = set()
for e in source:
    if not ('SILVER' in e['map'] or e['map'] == 'MAP_ROUTE28') or 'Night' in e['base_label'] or e['map'] in vus:
        continue
    vus.add(e['map'])
    n = {'map': e['map'], 'base_label': 'sHns' + e['base_label'].lstrip('g') + '_FireRed'}
    for cle, limite in LIMITES.items():
        if cle in e and e[cle]['mons'][0]['species'] != 'SPECIES_NONE':
            n[cle] = {'encounter_rate': e[cle]['encounter_rate'], 'mons': e[cle]['mons'][:limite]}
    groupe['encounters'].append(n)
ecrire('src/data/wild_encounters.json', W)

# 5. Carte de région
S = lire('src/data/region_map/region_map_sections.json')
for x in S['map_sections']:
    if x['id'] == 'MAPSEC_ROUTE_28':
        x.update(x=1, y=8, width=1, height=1)
    if x['id'] == 'MAPSEC_MT_SILVER':
        x.update(x=0, y=8, width=1, height=1)
ecrire('src/data/region_map/region_map_sections.json', S)

p = f'{JEU}/src/data/region_map/region_map_layout_kanto.h'
lignes = open(p).read().split('\n')
lignes[9] = lignes[9].replace('{MAPSEC_NONE, MAPSEC_NONE, MAPSEC_ROUTE_22', '{MAPSEC_MT_SILVER, MAPSEC_ROUTE_28, MAPSEC_ROUTE_22')
open(p, 'w').write('\n'.join(lignes))

p = f'{JEU}/src/region_map.c'
s = open(p).read()
if '[MAPSEC_ROUTE_28]' not in s:
    s = re.sub(r'(\n( *)\[MAPSEC_ROUTE_22\] = [^\n]*)',
               r'\1\n\2[MAPSEC_ROUTE_28] = {MAP_GROUP(MAP_ROUTE28), MAP_NUM(MAP_ROUTE28), HEAL_LOCATION_NONE},'
               r'\n\2[MAPSEC_MT_SILVER] = {MAP_GROUP(MAP_MT_SILVER_OUTSIDE), MAP_NUM(MAP_MT_SILVER_OUTSIDE), HEAL_LOCATION_MT_SILVER},', s, count=1)
    open(p, 'w').write(s)
print('Mont Argente complete')
