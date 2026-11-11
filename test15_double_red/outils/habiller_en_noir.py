#!/usr/bin/env python3
"""Double de Red : copie les sprites de Red et remplace les couleurs de sa tenue par du noir.

Usage : habiller_en_noir.py <jeu> <dossier de sortie>
Seules les palettes changent : le dessin reste celui de Red, pixel pour pixel.
Les images produites dérivent des sprites d'origine et ne sont pas versionnées ici.
"""
import os, sys
from PIL import Image

JEU, SORTIE = sys.argv[1], sys.argv[2]
SPRITES = ['graphics/object_events/pics/people/red/red_normal.png', 'graphics/object_events/pics/people/red/red_bike.png',
           'graphics/object_events/pics/people/red/red_surf.png', 'graphics/object_events/pics/people/red/red_item.png',
           'graphics/object_events/pics/people/red/red_fish.png', 'graphics/object_events/pics/people/red/red_surf_run.png',
           'graphics/object_events/pics/people/red/red_vs_seeker_bike.png',
           'graphics/trainers/front_pics/red.png', 'graphics/trainers/back_pics/red.png']
# couleur d'origine -> couleur du double. Le contour reste (0,0,0) : les noirs de la tenue sont donc un ton au-dessus.
TENUE = {
    # monde et dos (palette partagée)
    (255, 106, 74): (72, 72, 86), (197, 57, 57): (46, 46, 58), (106, 41, 41): (26, 26, 34),      # veste, casquette
    (65, 65, 213): (58, 58, 72), (57, 57, 123): (34, 34, 46), (115, 164, 197): (104, 104, 122),  # pantalon
    (238, 238, 255): (176, 176, 192), (180, 180, 213): (124, 124, 144),                          # blanc de la casquette
    (255, 222, 90): (190, 40, 48), (189, 156, 57): (122, 24, 36),                                # sac : seule touche rouge
    # portrait de face
    (255, 98, 90): (72, 72, 86), (197, 65, 65): (46, 46, 58),
    (123, 189, 222): (104, 104, 122), (82, 139, 180): (58, 58, 72), (49, 106, 139): (34, 34, 46), (24, 41, 82): (20, 20, 28),
    (213, 213, 222): (124, 124, 144), (255, 255, 255): (176, 176, 192),
    (255, 197, 90): (190, 40, 48), (189, 156, 90): (122, 24, 36),
}
os.makedirs(SORTIE, exist_ok=True)
for chemin in SPRITES:
    im = Image.open(f'{JEU}/{chemin}'); pal = im.getpalette()[:48]
    for i in range(1, 16):                                   # l'indice 0 est la transparence
        c = tuple(pal[i * 3:i * 3 + 3])
        if c in TENUE: pal[i * 3:i * 3 + 3] = TENUE[c]
    im.putpalette(pal + [0] * (768 - 48))
    nom = 'double_' + ('face.png' if 'front' in chemin else 'dos.png' if 'back' in chemin else os.path.basename(chemin)[4:])
    im.save(f'{SORTIE}/{nom}'); print(nom, im.size)
