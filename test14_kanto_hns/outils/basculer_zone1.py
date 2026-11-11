#!/usr/bin/env python3
"""Passe Bourg Palette, la Route 1 et Jadielle sur les décors Heart & Soul.

Usage : python3 basculer_zone1.py <dossier du jeu>      (après importer_kanto_hns.py)

Les PNJ, scripts et dialogues de Rouge Feu ne changent pas. Le script change le décor de chaque
carte et déplace les seuls événements dont la case a bougé. Il peut être relancé.
"""
import json, os, struct, sys

JEU = sys.argv[1]


def carte(nom):
    p = f'{JEU}/data/maps/{nom}_Frlg/map.json'
    return p, json.load(open(p))


def ecrire(p, j):
    json.dump(j, open(p, 'w'), indent=2, ensure_ascii=False); open(p, 'a').write('\n')


def deplacer(j, liste, cle, valeur, x, y):
    """Déplace l'événement dont le champ `cle` vaut `valeur`."""
    trouves = [e for e in j[liste] if e.get(cle) == valeur]
    assert len(trouves) == 1, (liste, cle, valeur, len(trouves))
    trouves[0]['x'], trouves[0]['y'] = x, y


def copier_bloc(layout, source, cible):
    """Recopie un bloc du décor (un panneau, par exemple) sur une autre case."""
    L = {x['id']: x for x in json.load(open(f'{JEU}/data/layouts/layouts.json'))['layouts'] if x}[layout]
    p = f'{JEU}/{L["blockdata_filepath"]}'
    d = bytearray(open(p, 'rb').read())
    lire = lambda c: struct.unpack_from('<H', d, 2 * (c[0] + c[1] * L['width']))[0]
    struct.pack_into('<H', d, 2 * (cible[0] + cible[1] * L['width']), lire(source))
    open(p, 'wb').write(d)


# Bourg Palette : mêmes cases qu'à l'origine. Le panneau « Astuces » n'existe pas dans le décor HnS.
p, j = carte('PalletTown')
j['layout'] = 'LAYOUT_HNS_PALLET_TOWN'
ecrire(p, j)
copier_bloc('LAYOUT_HNS_PALLET_TOWN', (9, 11), (5, 14))

# Route 1 : six colonnes d'arbres en plus à droite, aucune case utile ne bouge.
p, j = carte('Route1')
j['layout'] = 'LAYOUT_HNS_ROUTE1'
ecrire(p, j)

# Jadielle : la porte de l'Arène recule d'une case, l'école devient le grand bâtiment gris.
p, j = carte('ViridianCity')
j['layout'] = 'LAYOUT_HNS_VIRIDIAN_CITY'
deplacer(j, 'warp_events', 'dest_map', 'MAP_VIRIDIAN_CITY_GYM', 35, 10)
deplacer(j, 'warp_events', 'dest_map', 'MAP_VIRIDIAN_CITY_SCHOOL', 26, 19)
deplacer(j, 'coord_events', 'script', 'ViridianCity_EventScript_GymDoorLocked', 35, 11)
deplacer(j, 'bg_events', 'script', 'ViridianCity_EventScript_GymDoor', 35, 10)
deplacer(j, 'bg_events', 'script', 'ViridianCity_EventScript_GymSign', 37, 10)
ecrire(p, j)
copier_bloc('LAYOUT_HNS_VIRIDIAN_CITY', (20, 16), (23, 1))
print('Zone 1 basculee : PalletTown, Route1, ViridianCity')
