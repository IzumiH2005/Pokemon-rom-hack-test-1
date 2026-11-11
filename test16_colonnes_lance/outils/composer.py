# Pose les colonnes dessinées à la main (methode_dessin/test22_colonnes_lance) sur le terrain
# rendu sans objets (rendu2.py ... --sans, puis couches.py), à la place des modèles de Platine.
# Usage : python3 composer.py <dossier_rendu_sans> <pokeplatinum> <dossier_dessins>
# Réécrit carte_bas.png et carte_haut.png dans <dossier_rendu_sans>.
import sys, struct
import numpy as np
from PIL import Image

REND, PLAT, DESS = sys.argv[1:4]

# modèle Platine -> dessin
DESSIN = {508: 'b100', 510: 'b84', 512: 'b70', 509: 'p104', 511: 'p88', 513: 'p72'}

# colonnes retirées à la demande (centre x, bas du socle) : elles s'entassaient avec leurs voisines
RETIREES = {(144, 601), (384, 601)}

# objets des quatre blocs (même lecture que rendu2.py)
props = []
for k, (cx, cy) in zip(range(375, 379), [(0, 0), (1, 0), (0, 1), (1, 1)]):
    d = open(f'{PLAT}/res/field/mapmodels/data/map_data_{k}.bin', 'rb').read()
    a, b = struct.unpack_from('<2I', d)
    for i in range(b // 48):
        v = struct.unpack_from('<i3i', d, 16 + a + i * 48)
        props.append((v[0], v[1] / 4096 + cx * 512, v[3] / 4096 + cy * 512))

bas = np.array(Image.open(f'{REND}/carte_bas.png').convert('RGB'))
haut = np.array(Image.open(f'{REND}/carte_haut.png').convert('RGBA'))
H, W = bas.shape[:2]

# Le terrain de Platine porte lui aussi huit colonnes et douze gravats (tout ce qui dépasse le
# sol de l'esplanade, hauteur 48). On les efface : bas_1.0_1.png donne le sol propre dessous.
sl = np.s_[160:160 + H, 240:240 + W]            # même découpe que couches.py
relief = np.load(f'{REND}/h_1.0_1.npy')[sl] > 48.5
sol = np.array(Image.open(f'{REND}/bas_1.0_1.png').convert('RGB'))[sl]
bas[relief] = sol[relief]
haut[relief, 3] = 0

# gravats : petites taches de relief, repérées par composantes connexes
vu = np.zeros_like(relief); gravats = []
for y0, x0 in zip(*np.nonzero(relief)):
    if vu[y0, x0]: continue
    pile, pts = [(y0, x0)], []
    vu[y0, x0] = True
    while pile:
        a, b = pile.pop(); pts.append((a, b))
        for c, d in ((a + 1, b), (a - 1, b), (a, b + 1), (a, b - 1)):
            if 0 <= c < H and 0 <= d < W and relief[c, d] and not vu[c, d]:
                vu[c, d] = True; pile.append((c, d))
    if len(pts) < 400:
        ys, xs = zip(*pts)
        gravats.append(((min(xs) + max(xs) + 1) // 2, max(ys)))

# colonnes du terrain : (centre x, bas du socle, dessin), relevés sur la carte de hauteur
TERRAIN = [(175, 223, 'b100'), (351, 223, 'p104'), (143, 255, 'p120'), (383, 255, 'b112'),
           (143, 335, 'b112'), (383, 335, 'p120'), (175, 431, 'p120'), (351, 431, 'b100')]

# Chaque élément : (image, x0, y0, bandes) ; une bande (y1, y2, pied) dit sur quelle rangée de
# pixels l'élément touche le sol. Au-dessus de la rangée de tuiles du pied, l'élément passe
# devant le joueur (couche haute) ; dans cette rangée, il reste au sol.
elems = []
for n, wx, wz in props:
    cx, pied = int(wx) + 16, int(wz) + 217          # centre et bas du socle, repère de la carte
    if (cx, pied) in RETIREES: continue
    if n in DESSIN:
        im = np.array(Image.open(f'{DESS}/{DESSIN[n]}.png').convert('RGBA'))
        h, w = im.shape[:2]
        elems.append((im, cx - w // 2, pied - h + 1, [(0, h - 1, pied)]))
    elif n == 514:
        # bloc effondré de Platine : deux colonnes brisées debout et une colonne couchée
        # nord-sud côté allée centrale (est pour le groupe ouest)
        x0, y0 = int(wx) - 24, int(wz) + 104
        ouest = wx < 256
        # à l'ouest, seule la première reste : la seconde masquait sa voisine
        for c, nom in ((x0 + 19, 'b84'),) if ouest else ((x0 + 21, 'b70'), (x0 + 61, 'b84')):
            im = np.array(Image.open(f'{DESS}/{nom}.png').convert('RGBA'))
            h, w = im.shape[:2]
            elems.append((im, c - w // 2, y0 + 61 - h + 1, [(0, h - 1, y0 + 61)]))
        im = np.array(Image.open(f'{DESS}/couchee.png').convert('RGBA'))
        xc = x0 + 59 if ouest else x0
        # une bande par rangée de tuiles : toute la colonne couchée reste au sol
        Y = y0 + 62
        bandes = [(a - Y, min(61, a + 15 - Y), a + 15) for a in range(Y // 16 * 16, Y + 62, 16)]
        bandes[0] = (0, bandes[0][1], bandes[0][2])
        elems.append((im, xc, y0 + 62, bandes))

for cx, pied, nom in TERRAIN:
    im = np.array(Image.open(f'{DESS}/{nom}.png').convert('RGBA'))
    h, w = im.shape[:2]
    elems.append((im, cx - w // 2, pied - h + 1, [(0, h - 1, pied)]))
g = np.array(Image.open(f'{DESS}/gravats.png').convert('RGBA'))
for i, (cx, pied) in enumerate(gravats):
    im = g[:, ::-1] if i % 2 else g                 # un tas sur deux en miroir
    h, w = im.shape[:2]
    elems.append((im, cx - w // 2, pied - h + 1, [(0, h - 1, pied)]))

# pas[ty, tx] : pixels d'éléments posés au sol dans la tuile ; sert aux collisions
pas = np.zeros((H // 16, W // 16), int)

# de l'arrière vers l'avant : un élément plus au sud recouvre les précédents
for im, x0, y0, bandes in sorted(elems, key=lambda e: e[3][0][2]):
    for y1, y2, pied in sorted(bandes, key=lambda b: b[2]):
        for y in range(y1, y2 + 1):
            Y = y0 + y
            if not 0 <= Y < H: continue
            devant = Y // 16 < pied // 16
            for x in range(im.shape[1]):
                X = x0 + x
                if im[y, x, 3] == 0 or not 0 <= X < W: continue
                if devant:
                    haut[Y, X] = im[y, x]
                else:
                    bas[Y, X] = im[y, x, :3]
                    haut[Y, X, 3] = 0
                    pas[Y // 16, X // 16] += 1

Image.fromarray(bas).save(f'{REND}/carte_bas.png')
np.save(f'{REND}/pas.npy', pas)
Image.fromarray(haut, 'RGBA').save(f'{REND}/carte_haut.png')
print(f'{len(elems)} objets posés')
