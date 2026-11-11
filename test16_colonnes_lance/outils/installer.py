# Déclare dans le jeu le jeu de tuiles et la carte des Colonnes Lance produits par construire.py.
# Usage : python3 installer.py <jeu>     (relançable : chaque bloc est encadré par un marqueur)
import sys, json, re

JEU = sys.argv[1]
M = '// --- Colonnes Lance ---'

def bloc(chemin, texte, avant=None):
    s = open(chemin).read()
    s = re.sub(re.escape(M) + r'.*?' + re.escape(M) + r'\n', '', s, flags=re.S)
    b = f'{M}\n{texte}{M}\n'
    if avant:
        i = s.rindex(avant); s = s[:i] + b + s[i:]
    else:
        s += b
    open(chemin, 'w').write(s)

pals = lambda g: ''.join(f'    INCGFX_U16("data/tilesets/{g}/colonnes_lance/palettes/{i:02d}.pal", ".gbapal"),\n' for i in range(13))
gfx = meta = head = ''
for g, nom, sec in (('primary', 'ColonnesLance', 'FALSE'), ('secondary', 'ColonnesLanceSec', 'TRUE')):
    gfx += (f'const u32 gTilesetTiles_{nom}[] = INCGFX_U32("data/tilesets/{g}/colonnes_lance/tiles.png", ".4bpp.fastSmol");\n'
            f'const u16 gTilesetPalettes_{nom}[][16] =\n{{\n{pals(g)}}};\n\n')
    meta += (f'const u16 gMetatiles_{nom}[] = INCBIN_U16("data/tilesets/{g}/colonnes_lance/metatiles.bin");\n'
             f'const u16 gMetatileAttributes_{nom}[] = INCBIN_U16("data/tilesets/{g}/colonnes_lance/metatile_attributes.bin");\n')
    head += (f'const struct Tileset gTileset_{nom} =\n{{\n    .isCompressed = TRUE,\n    .isSecondary = {sec},\n'
             f'    .tiles = gTilesetTiles_{nom},\n    .palettes = gTilesetPalettes_{nom},\n'
             f'    .metatiles = gMetatiles_{nom},\n    .metatileAttributes = gMetatileAttributes_{nom},\n    .callback = NULL,\n}};\n\n')
bloc(f'{JEU}/src/data/tilesets/graphics.h', gfx)
bloc(f'{JEU}/src/data/tilesets/metatiles.h', meta)
bloc(f'{JEU}/src/data/tilesets/headers.h', head)
bloc(f'{JEU}/include/tilesets.h', 'extern const struct Tileset gTileset_ColonnesLance;\nextern const struct Tileset gTileset_ColonnesLanceSec;\n',
     avant='#endif //GUARD_tilesets_H')

# layout
j = json.load(open(f'{JEU}/data/layouts/layouts.json'))
j['layouts'] = [l for l in j['layouts'] if l.get('id') != 'LAYOUT_COLONNES_LANCE']
j['layouts'].append({'id': 'LAYOUT_COLONNES_LANCE', 'name': 'ColonnesLance_Layout', 'width': 34, 'height': 57,
                     'border_width': 2, 'border_height': 2,
                     'primary_tileset': 'gTileset_ColonnesLance', 'secondary_tileset': 'gTileset_ColonnesLanceSec',
                     'border_filepath': 'data/layouts/ColonnesLance/border.bin',
                     'blockdata_filepath': 'data/layouts/ColonnesLance/map.bin', 'layout_version': 'frlg'})
json.dump(j, open(f'{JEU}/data/layouts/layouts.json', 'w'), indent=2); open(f'{JEU}/data/layouts/layouts.json', 'a').write('\n')

# carte : inaccessible en jeu normal, sans PNJ ni warp
import os
d = f'{JEU}/data/maps/ColonnesLance'
os.makedirs(d, exist_ok=True)
carte = {'id': 'MAP_COLONNES_LANCE', 'name': 'ColonnesLance', 'layout': 'LAYOUT_COLONNES_LANCE',
         'music': 'MUS_RG_VICTORY_ROAD', 'region': 'REGION_KANTO', 'region_map_section': 'MAPSEC_NONE',
         'requires_flash': False, 'weather': 'WEATHER_NONE', 'map_type': 'MAP_TYPE_UNDERGROUND',
         'allow_cycling': False, 'allow_escaping': False, 'allow_running': True, 'show_map_name': False,
         'floor_number': 0, 'battle_scene': 'MAP_BATTLE_SCENE_NORMAL', 'connections': None,
         'object_events': [], 'warp_events': [], 'coord_events': [], 'bg_events': []}
json.dump(carte, open(f'{d}/map.json', 'w'), indent=2)
if not os.path.exists(f'{d}/scripts.inc'):
    open(f'{d}/scripts.inc', 'w').write('ColonnesLance_MapScripts::\n\t.byte 0\n')
g = json.load(open(f'{JEU}/data/maps/map_groups.json'))
grp = g['gMapGroup_SpecialArea_Frlg']
if 'ColonnesLance' not in grp: grp.append('ColonnesLance')
json.dump(g, open(f'{JEU}/data/maps/map_groups.json', 'w'), indent=2); open(f'{JEU}/data/maps/map_groups.json', 'a').write('\n')
es = f'{JEU}/data/event_scripts.s'
s = open(es).read()
inc = '\t.include "data/maps/ColonnesLance/scripts.inc"\n'
if inc not in s:
    i = s.index('\t.include "data/maps/MtSilver_Outside_Frlg/scripts.inc"\n')
    s = s[:i] + inc + s[i:]
    open(es, 'w').write(s)
print('installé')
