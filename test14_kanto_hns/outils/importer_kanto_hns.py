#!/usr/bin/env python3
"""Importe les décors du Kanto de Pokémon Heart & Soul dans pokeemerald-expansion (build Rouge Feu).

Usage : python3 importer_kanto_hns.py <dossier pokemonHnS> <dossier du jeu>
À lancer après les scripts du test 13 (importer_hns.py, completer_mont_argente.py).

Le script n'ajoute que des décors : tilesets (préfixe hns_) et layouts (préfixe Hns_).
Aucune carte du jeu n'est modifiée. Une carte de Rouge Feu passe sur le décor Heart & Soul
quand son champ "layout" pointe vers LAYOUT_HNS_... (voir basculer_zone.py).
Le script peut être relancé : il ne duplique rien.
"""
import json, os, re, shutil, struct, sys

HNS, JEU = sys.argv[1], sys.argv[2]
MARQUE = '// --- Import Heart & Soul : Kanto ---'
DEJA = {'gTileset_Johto_General', 'gTileset_Johto_NorthEast', 'gTileset_MtSilverSnow', 'gTileset_Cave_Gray',
        'gTileset_Blackthorn', 'gTileset_MahoganyTown', 'gTileset_ViridianCity'}  # importés par le test 13

GROUPES_ENTIERS = ['gMapGroup_IndoorPallet', 'gMapGroup_IndoorViridian', 'gMapGroup_IndoorPewter',
                   'gMapGroup_IndoorCerulean', 'gMapGroup_IndoorVermilion', 'gMapGroup_IndoorLavender',
                   'gMapGroup_IndoorCeladon', 'gMapGroup_IndoorSaffron', 'gMapGroup_IndoorFuchsia',
                   'gMapGroup_IndoorCinnabar', 'gMapGroup_IndoorIndigo', 'gMapGroup_IndoorKantoRoutes']
DONJONS = ('VictoryRoadKanto', 'ViridianForest', 'MtMoon', 'RockTunnel', 'CeruleanCave', 'DiglettsCave',
           'SeafoamIslands', 'Route19_Cave', 'TohjoFalls')
EXCLUES = ('MtSilver', 'Route28')          # déjà importées par le test 13

# Cases redessinées après import : carte -> {(x, y): valeur de bloc}.
RETOUCHES = {'Route4': {(19, 5): 0x079 | 1 << 10}}   # fausse entrée de grotte hors d'atteinte, remplacée par la paroi

# Comportements de métatuile : mêmes numéros dans les deux moteurs, sauf ceux-ci.
COMPORTEMENTS = {0xEB: 0xC8, 0xEC: 0xC9, 0xEF: 0x64}
A_ZERO = ({0x1D, 0x1E, 0x1F, 0x23, 0x2C, 0x2D, 0xA1, 0xA2, 0xED, 0xEE, 0xFE, 0xFF}
          | set(range(0x54, 0x60)) | set(range(0xA3, 0xB0)) | set(range(0xC8, 0xCD)))
EAU = {0x10, 0x11, 0x12, 0x13, 0x15, 0x17, 0x18, 0x19, 0x1A, 0x2A, 0x50, 0x51, 0x52, 0x53}
ANIMS = {'InitTilesetAnim_JohtoGeneral': 'InitTilesetAnim_Hns_JohtoGeneral',
         'InitTilesetAnim_HoennGeneral': 'InitTilesetAnim_General',
         'InitTilesetAnim_Building': 'InitTilesetAnim_Building'}  # les autres animations ne sont pas reprises


def convertir_attributs(src, dst):
    d = open(src, 'rb').read()
    out = bytearray()
    for i in range(0, len(d) - 1, 2):
        v = struct.unpack_from('<H', d, i)[0]
        comp, couche = v & 0xFF, (v >> 12) & 3
        comp = COMPORTEMENTS.get(comp, 0 if comp in A_ZERO else comp)
        terrain = 1 if comp == 0x02 else 2 if comp in EAU else 0
        rencontre = 2 if comp in EAU else 1 if comp in (0x02, 0x08) else 0
        out += struct.pack('<I', comp | terrain << 9 | rencontre << 24 | couche << 29)
    open(dst, 'wb').write(out)


def ajouter(chemin, texte):
    p = os.path.join(JEU, chemin)
    t = open(p).read()
    if MARQUE in t:
        t = t[:t.index(MARQUE)].rstrip('\n') + '\n'
    open(p, 'w').write(t + '\n' + MARQUE + '\n' + texte)


def inserer_avant(chemin, repere, texte):
    p = os.path.join(JEU, chemin)
    t = open(p).read()
    if MARQUE in t:
        a = t.index(MARQUE); b = t.index(MARQUE, a + 1) + len(MARQUE) + 1
        t = t[:a] + t[b:]
    i = t.rindex(repere)
    open(p, 'w').write(t[:i] + MARQUE + '\n' + texte + MARQUE + '\n' + t[i:])


def symbole(s):
    return 'gTileset_Hns_' + ''.join(x[:1].upper() + x[1:] for x in s[len('gTileset_'):].split('_'))


# 1. Cartes de Kanto dans Heart & Soul
G = json.load(open(f'{HNS}/data/maps/map_groups.json'))
villes = G['gMapGroup_TownsAndRoutes']
cartes = villes[villes.index('PalletTown'):]
for g in GROUPES_ENTIERS:
    cartes += G[g]
cartes += [m for m in G['gMapGroup_Dungeons'] if m.startswith(DONJONS)]
cartes = [m for m in cartes if not m.startswith(EXCLUES)]
cartes += [m for m in ('ReceptionGate',) if m not in cartes]   # portail de la Ligue, rangé hors de Kanto dans HnS

hl = {x['id']: x for x in json.load(open(f'{HNS}/data/layouts/layouts.json'))['layouts'] if x}
layouts = {}  # id HnS -> (carte, layout)
for m in cartes:
    lid = json.load(open(f'{HNS}/data/maps/{m}/map.json'))['layout']
    layouts.setdefault(lid, (m, hl[lid]))

# 2. Tilesets
entetes = open(f'{HNS}/src/data/tilesets/headers.h').read()
graphismes = open(f'{HNS}/src/data/tilesets/graphics.h').read()
metatuiles = open(f'{HNS}/src/data/tilesets/metatiles.h').read()
besoin = sorted({l[k] for _, l in layouts.values() for k in ('primary_tileset', 'secondary_tileset')} - DEJA)
gfx, meta, head, ext = [], [], [], []
for s in besoin:
    nom = s[len('gTileset_'):]
    bloc = re.search(r'const struct Tileset %s =\s*\{(.*?)\};' % s, entetes, re.S).group(1)
    champ = lambda c: re.search(r'\.%s = (\w+)' % c, bloc).group(1)
    chemin = lambda source, sym: re.search(r'\b%s\[\].*?"(data/tilesets/\w+/\w+)/' % sym, source, re.S).group(1)
    dm, da = chemin(metatuiles, champ('metatiles')), chemin(metatuiles, champ('metatileAttributes'))
    # gTileset_General (Parc Safari) n'a pas ses graphismes déclarés dans HnS : son dossier fait foi.
    declare = re.search(r'\b%s\[\]' % champ('tiles'), graphismes)
    dt, dp = (chemin(graphismes, champ('tiles')), chemin(graphismes, champ('palettes'))) if declare else (dm, dm)
    rappel = ANIMS.get(champ('callback'), 'NULL')
    typ, sym = ('secondary' if champ('isSecondary') == 'TRUE' else 'primary'), symbole(s)[len('gTileset_'):]
    rel = f'data/tilesets/{typ}/hns_{nom.lower()}'
    d = f'{JEU}/{rel}'
    os.makedirs(d + '/palettes', exist_ok=True)
    shutil.copy(f'{HNS}/{dt}/tiles.png', d)
    shutil.copy(f'{HNS}/{dm}/metatiles.bin', d)
    for i in range(13):
        shutil.copy(f'{HNS}/{dp}/palettes/{i:02d}.pal', d + '/palettes')
    convertir_attributs(f'{HNS}/{da}/metatile_attributes.bin', d + '/metatile_attributes.bin')
    gfx.append(f'const u32 gTilesetTiles_{sym}[] = INCGFX_U32("{rel}/tiles.png", ".4bpp.fastSmol");\n'
               f'const u16 gTilesetPalettes_{sym}[][16] =\n{{\n'
               + ''.join(f'    INCGFX_U16("{rel}/palettes/{i:02d}.pal", ".gbapal"),\n' for i in range(13)) + '};\n')
    meta.append(f'const u16 gMetatiles_{sym}[] = INCBIN_U16("{rel}/metatiles.bin");\n'
                f'const u16 gMetatileAttributes_{sym}[] = INCBIN_U16("{rel}/metatile_attributes.bin");\n')
    head.append(f'const struct Tileset gTileset_{sym} =\n{{\n    .isCompressed = TRUE,\n'
                f'    .isSecondary = {"FALSE" if typ == "primary" else "TRUE"},\n'
                f'    .tiles = gTilesetTiles_{sym},\n    .palettes = gTilesetPalettes_{sym},\n'
                f'    .metatiles = gMetatiles_{sym},\n    .metatileAttributes = gMetatileAttributes_{sym},\n'
                f'    .callback = {rappel},\n}};\n')
    ext.append(f'extern const struct Tileset gTileset_{sym};\n')

garde = lambda blocs: '#if IS_FRLG\n' + '\n'.join(blocs) + '#endif // IS_FRLG\n'
ajouter('src/data/tilesets/graphics.h', garde(gfx))
ajouter('src/data/tilesets/metatiles.h', garde(meta))
ajouter('src/data/tilesets/headers.h', garde(head))
inserer_avant('include/tilesets.h', '#endif', ''.join(ext) + '\n')

# 3. Layouts
p = f'{JEU}/data/layouts/layouts.json'
L = json.load(open(p))
table = {}
for lid, (carte, h) in layouts.items():
    nouvel_id = 'LAYOUT_HNS_' + lid[len('LAYOUT_'):]
    nom = 'Hns_' + h['name'][:-len('_Layout')]
    d = f'data/layouts/{nom}'
    os.makedirs(f'{JEU}/{d}', exist_ok=True)
    shutil.copy(f'{HNS}/{h["blockdata_filepath"]}', f'{JEU}/{d}/map.bin')
    shutil.copy(f'{HNS}/{h["border_filepath"]}', f'{JEU}/{d}/border.bin')
    for (x, y), v in RETOUCHES.get(carte, {}).items():
        with open(f'{JEU}/{d}/map.bin', 'r+b') as f:
            f.seek(2 * (x + y * h['width'])); f.write(struct.pack('<H', v))
    entree = {'id': nouvel_id, 'name': nom + '_Layout', 'width': h['width'], 'height': h['height'],
              'border_width': 2, 'border_height': 2,
              'primary_tileset': symbole(h['primary_tileset']), 'secondary_tileset': symbole(h['secondary_tileset']),
              'border_filepath': d + '/border.bin', 'blockdata_filepath': d + '/map.bin', 'layout_version': 'frlg'}
    L['layouts'] = [x for x in L['layouts'] if not (x and x.get('id') == nouvel_id)] + [entree]
    table[carte] = nouvel_id
json.dump(L, open(p, 'w'), indent=2, ensure_ascii=False); open(p, 'a').write('\n')

# table carte HnS -> layout, pour les scripts de bascule
ici = os.path.dirname(os.path.abspath(__file__))
complet = {m: 'LAYOUT_HNS_' + json.load(open(f'{HNS}/data/maps/{m}/map.json'))['layout'][len('LAYOUT_'):] for m in cartes}
json.dump(complet, open(f'{ici}/layouts_kanto_hns.json', 'w'), indent=1, sort_keys=True)
print('Import termine :', len(besoin), 'tilesets,', len(layouts), 'layouts,', len(cartes), 'cartes de Kanto')
