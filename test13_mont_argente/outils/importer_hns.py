#!/usr/bin/env python3
"""Importe la Route 28 et le Mont Argenté de Pokémon Heart & Soul dans pokeemerald-expansion (build Rouge Feu).

Usage : python3 importer_hns.py <dossier pokemonHnS> <dossier du jeu>

Ce que fait le script :
- copie 7 tilesets (préfixe hns_) et convertit leurs attributs du format Émeraude (16 bits)
  au format Rouge Feu (32 bits) ;
- copie 11 cartes (layouts) et crée leurs map.json sans PNJ ni scripts, en gardant les warps
  et les connexions entre cartes importées ;
- déclare tilesets, animations d'eau, cartes, groupe de cartes et noms de lieux.
Le script peut être relancé : il ne duplique rien.
"""
import json, os, shutil, struct, sys

HNS, JEU = sys.argv[1], sys.argv[2]
MARQUE = '// --- Import Heart & Soul : Mont Argente ---'

# dossier HnS -> (type, nouveau dossier, suffixe de symbole, symbole HnS)
TILESETS = [
    ('primary',   'johto_general',    'Hns_JohtoGeneral',   'gTileset_Johto_General'),
    ('primary',   'johto_north_east', 'Hns_JohtoNorthEast', 'gTileset_Johto_NorthEast'),
    ('secondary', 'mt_silver_snow',   'Hns_MtSilverSnow',   'gTileset_MtSilverSnow'),
    ('secondary', 'cave_gray',        'Hns_CaveGray',       'gTileset_Cave_Gray'),
    ('secondary', 'blackthorn',       'Hns_Blackthorn',     'gTileset_Blackthorn'),
    ('secondary', 'mahogany_town',    'Hns_MahoganyTown',   'gTileset_MahoganyTown'),
    ('secondary', 'viridian_city',    'Hns_ViridianCity',   'gTileset_ViridianCity'),
]
SYMBOLE = {t[3]: 'gTileset_' + t[2] for t in TILESETS}

# carte HnS -> (musique, section de carte)
CARTES = {
    'Route28':                   ('MUS_RG_ROUTE11',      'MAPSEC_ROUTE_28'),
    'MtSilver_Outside':          ('MUS_RG_ROUTE11',      'MAPSEC_MT_SILVER'),
    'MtSilver_1F_WaterfallRoom': ('MUS_RG_VICTORY_ROAD', 'MAPSEC_MT_SILVER'),
    'MtSilver_1F_ItemRoom':      ('MUS_RG_VICTORY_ROAD', 'MAPSEC_MT_SILVER'),
    'MtSilver_1F_MoltresRoom':   ('MUS_RG_VICTORY_ROAD', 'MAPSEC_MT_SILVER'),
    'MtSilver_2F':               ('MUS_RG_VICTORY_ROAD', 'MAPSEC_MT_SILVER'),
    'MtSilver_3F':               ('MUS_RG_VICTORY_ROAD', 'MAPSEC_MT_SILVER'),
    'MtSilver_MountainSide':     ('MUS_RG_VICTORY_ROAD', 'MAPSEC_MT_SILVER'),
    'MtSilver_Snow':             ('MUS_RG_VICTORY_ROAD', 'MAPSEC_MT_SILVER'),
    'MtSilver_SummitDay':        ('MUS_NONE',            'MAPSEC_MT_SILVER'),
    'MtSilver_SummitNight':      ('MUS_NONE',            'MAPSEC_MT_SILVER'),
}
GROUPE = 'gMapGroup_MtSilver_Frlg'

# comportements HnS absents de notre moteur -> MB_NORMAL
COMPORTEMENTS_INCONNUS = {0x1E, 0x23, 0xA1, 0xFE, 0xFF}
EAU = {0x10, 0x11, 0x12, 0x13, 0x15, 0x17, 0x18, 0x19, 0x1A, 0x2A, 0x50, 0x51, 0x52, 0x53}


def convertir_attributs(src, dst):
    """Émeraude : u16 = comportement (bits 0-7) + couche (bits 12-15).
    Rouge Feu : u32 = comportement (0-8), terrain (9-13), rencontre (24-26), couche (29-30)."""
    d = open(src, 'rb').read()
    out = bytearray()
    for i in range(0, len(d), 2):
        v = struct.unpack_from('<H', d, i)[0]
        comp, couche = v & 0xFF, (v >> 12) & 3
        if comp in COMPORTEMENTS_INCONNUS:
            comp = 0
        terrain = 1 if comp == 0x02 else 2 if comp in EAU else 0
        rencontre = 2 if comp in EAU else 1 if comp in (0x02, 0x08) else 0
        out += struct.pack('<I', comp | terrain << 9 | rencontre << 24 | couche << 29)
    open(dst, 'wb').write(out)


def ajouter(chemin, texte, marque=MARQUE):
    p = os.path.join(JEU, chemin)
    t = open(p).read()
    if marque in t:
        t = t[:t.index(marque)].rstrip('\n') + '\n'
    open(p, 'w').write(t + '\n' + marque + '\n' + texte)


def inserer_avant(chemin, repere, texte):
    p = os.path.join(JEU, chemin)
    t = open(p).read()
    if MARQUE in t:
        a = t.index(MARQUE); b = t.index(MARQUE, a + 1) + len(MARQUE) + 1
        t = t[:a] + t[b:]
    i = t.rindex(repere)
    open(p, 'w').write(t[:i] + MARQUE + '\n' + texte + MARQUE + '\n' + t[i:])


# 1. Tilesets
gfx, meta, head, ext = [], [], [], []
for typ, nom, sym, _ in TILESETS:
    s = f'{HNS}/data/tilesets/{typ}/{nom}'
    rel = f'data/tilesets/{typ}/hns_{nom}'
    d = f'{JEU}/{rel}'
    os.makedirs(d + '/palettes', exist_ok=True)
    shutil.copy(s + '/tiles.png', d)
    shutil.copy(s + '/metatiles.bin', d)
    for i in range(13):
        shutil.copy(f'{s}/palettes/{i:02d}.pal', d + '/palettes')
    convertir_attributs(s + '/metatile_attributes.bin', d + '/metatile_attributes.bin')
    if nom == 'johto_general':
        shutil.copytree(s + '/anim', d + '/anim', dirs_exist_ok=True)
    gfx.append(f'const u32 gTilesetTiles_{sym}[] = INCGFX_U32("{rel}/tiles.png", ".4bpp.fastSmol");\n'
               f'const u16 gTilesetPalettes_{sym}[][16] =\n{{\n'
               + ''.join(f'    INCGFX_U16("{rel}/palettes/{i:02d}.pal", ".gbapal"),\n' for i in range(13)) + '};\n')
    meta.append(f'const u16 gMetatiles_{sym}[] = INCBIN_U16("{rel}/metatiles.bin");\n'
                f'const u16 gMetatileAttributes_{sym}[] = INCBIN_U16("{rel}/metatile_attributes.bin");\n')
    head.append(f'const struct Tileset gTileset_{sym} =\n{{\n    .isCompressed = TRUE,\n'
                f'    .isSecondary = {"FALSE" if typ == "primary" else "TRUE"},\n'
                f'    .tiles = gTilesetTiles_{sym},\n    .palettes = gTilesetPalettes_{sym},\n'
                f'    .metatiles = gMetatiles_{sym},\n    .metatileAttributes = gMetatileAttributes_{sym},\n'
                f'    .callback = {"InitTilesetAnim_Hns_JohtoGeneral" if typ == "primary" else "NULL"},\n}};\n')
    ext.append(f'extern const struct Tileset gTileset_{sym};\n')

garde = lambda blocs: '#if IS_FRLG\n' + '\n'.join(blocs) + '#endif // IS_FRLG\n'
ajouter('src/data/tilesets/graphics.h', garde(gfx))
ajouter('src/data/tilesets/metatiles.h', garde(meta))
ajouter('src/data/tilesets/headers.h', garde(head))
inserer_avant('include/tilesets.h', '#endif', ''.join(ext) + '\n')
inserer_avant('include/tileset_anims.h', '#endif', 'void InitTilesetAnim_Hns_JohtoGeneral(void);\n\n')

A = 'data/tilesets/primary/hns_johto_general/anim'
anim = '#if IS_FRLG\n'
for nom, dossier, n in (('Flower', 'flower', 5), ('SandWatersEdge', 'sandwatersedge', 8), ('Water', 'water_current_landwatersedge', 8)):
    for i in range(n):
        anim += f'static const u16 sTilesetAnims_Hns_{nom}_Frame{i}[] = INCBIN_U16("{A}/{dossier}/{i}.4bpp");\n'
    anim += f'static const u16 *const sTilesetAnims_Hns_{nom}[] = {{\n' + ''.join(f'    sTilesetAnims_Hns_{nom}_Frame{i},\n' for i in range(n)) + '};\n\n'
anim += '''static void TilesetAnim_Hns_JohtoGeneral(u16 timer)
{
    if (timer % 8 == 0)
        AppendTilesetAnimToBuffer(sTilesetAnims_Hns_SandWatersEdge[(timer / 8) % ARRAY_COUNT(sTilesetAnims_Hns_SandWatersEdge)], (u16 *)(BG_VRAM + TILE_OFFSET_4BPP(416)), 18 * TILE_SIZE_4BPP);
    if (timer % 16 == 2)
        AppendTilesetAnimToBuffer(sTilesetAnims_Hns_Flower[(timer / 16) % ARRAY_COUNT(sTilesetAnims_Hns_Flower)], (u16 *)(BG_VRAM + TILE_OFFSET_4BPP(508)), 4 * TILE_SIZE_4BPP);
    // La cascade commence a la tuile 34 de chaque image de la planche d'eau.
    if (timer % 16 == 3)
        AppendTilesetAnimToBuffer(sTilesetAnims_Hns_Water[(timer / 16) % ARRAY_COUNT(sTilesetAnims_Hns_Water)] + 34 * (TILE_SIZE_4BPP / 2), (u16 *)(BG_VRAM + TILE_OFFSET_4BPP(450)), 12 * TILE_SIZE_4BPP);
}

void InitTilesetAnim_Hns_JohtoGeneral(void)
{
    sPrimaryTilesetAnimCounter = 0;
    sPrimaryTilesetAnimCounterMax = 256;
    sPrimaryTilesetAnimCallback = TilesetAnim_Hns_JohtoGeneral;
}
#endif // IS_FRLG
'''
ajouter('src/tileset_anims.c', anim)

# 2. Layouts
hl = {x['name']: x for x in json.load(open(f'{HNS}/data/layouts/layouts.json'))['layouts'] if x}
p = f'{JEU}/data/layouts/layouts.json'
L = json.load(open(p))
ids_carte = {}
for nom in CARTES:
    h = hl[nom + '_Layout']
    hm = json.load(open(f'{HNS}/data/maps/{nom}/map.json'))
    ids_carte[hm['id']] = nom
    d = f'data/layouts/{nom}_Frlg'
    os.makedirs(f'{JEU}/{d}', exist_ok=True)
    shutil.copy(f'{HNS}/{h["blockdata_filepath"]}', f'{JEU}/{d}/map.bin')
    shutil.copy(f'{HNS}/{h["border_filepath"]}', f'{JEU}/{d}/border.bin')
    entree = {'id': h['id'], 'name': nom + '_Frlg_Layout', 'width': h['width'], 'height': h['height'],
              'border_width': 2, 'border_height': 2,
              'primary_tileset': SYMBOLE[h['primary_tileset']], 'secondary_tileset': SYMBOLE[h['secondary_tileset']],
              'border_filepath': d + '/border.bin', 'blockdata_filepath': d + '/map.bin', 'layout_version': 'frlg'}
    L['layouts'] = [x for x in L['layouts'] if not (x and x.get('id') == h['id'])] + [entree]
json.dump(L, open(p, 'w'), indent=2, ensure_ascii=False); open(p, 'a').write('\n')

# 3. Cartes
for nom, (musique, mapsec) in CARTES.items():
    h = json.load(open(f'{HNS}/data/maps/{nom}/map.json'))
    sommet = 'Summit' in nom
    grotte = h['map_type'] == 'MAP_TYPE_UNDERGROUND'
    conns = [c for c in (h['connections'] or []) if c['map'] in ids_carte]
    m = {'id': h['id'], 'name': nom + '_Frlg', 'layout': h['layout'], 'music': musique,
         'region': 'REGION_KANTO', 'region_map_section': mapsec, 'requires_flash': False,
         'weather': h['weather'] if h['weather'] == 'WEATHER_SNOW' else ('WEATHER_NONE' if grotte else 'WEATHER_SUNNY'),
         'map_type': 'MAP_TYPE_UNDERGROUND' if grotte else 'MAP_TYPE_ROUTE',
         'allow_cycling': not sommet, 'allow_escaping': grotte, 'allow_running': True,
         'show_map_name': not sommet, 'floor_number': 0, 'battle_scene': 'MAP_BATTLE_SCENE_NORMAL',
         'connections': conns or None, 'object_events': [],
         # les warps vers des cartes non importees (Centre Pokemon, maison, poste) pointent sur eux-memes
         'warp_events': [w if w['dest_map'] in ids_carte else dict(w, dest_map=h['id'], dest_warp_id=str(i))
                         for i, w in enumerate(h['warp_events'])],
         'coord_events': [], 'bg_events': []}
    d = f'{JEU}/data/maps/{nom}_Frlg'
    os.makedirs(d, exist_ok=True)
    json.dump(m, open(d + '/map.json', 'w'), indent=2, ensure_ascii=False); open(d + '/map.json', 'a').write('\n')
    if not os.path.exists(d + '/scripts.inc'):
        open(d + '/scripts.inc', 'w').write(f'{nom}_Frlg_MapScripts::\n\t.byte 0\n')

p = f'{JEU}/data/maps/map_groups.json'
G = json.load(open(p))
if GROUPE not in G['group_order']:
    G['group_order'].append(GROUPE)
G[GROUPE] = [n + '_Frlg' for n in CARTES]
json.dump(G, open(p, 'w'), indent=2, ensure_ascii=False); open(p, 'a').write('\n')

ajouter('data/event_scripts.s', '.if IS_FRLG\n' + ''.join(f'\t.include "data/maps/{n}_Frlg/scripts.inc"\n' for n in CARTES) + '.endif\n', marque='@ --- Import Heart & Soul : Mont Argente ---')

# 4. Noms de lieux
p = f'{JEU}/src/data/region_map/region_map_sections.json'
S = json.load(open(p))
for i, n in (('MAPSEC_ROUTE_28', 'ROUTE 28'), ('MAPSEC_MT_SILVER', 'MONT ARGENTE')):
    if not any(x['id'] == i for x in S['map_sections']):
        S['map_sections'].append({'id': i, 'name': n})
json.dump(S, open(p, 'w'), indent=2, ensure_ascii=False); open(p, 'a').write('\n')
print('Import termine :', len(TILESETS), 'tilesets,', len(CARTES), 'cartes')
