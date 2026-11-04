"""Planche des calques (E6) : chaque pièce seule à ×3, dans l'ordre d'empilement, puis l'assemblage."""
from PIL import Image
noms = ['etape00_construction', 'cadre', 'case', 'barre', 'onglet_rond_actif', 'onglet_losange_inactif',
        'onglet_croix_inactif', 'onglet_pic_inactif', 'bossette', 'logement', 'rubis', 'cimier', 'curseur']
k, m = 3, 6
ims = [Image.open(f'pieces/{n}.png').convert('RGBA') for n in noms]
W = sum(i.width * k + m for i in ims[:2]) + m
petits = ims[2:]
lignes, ligne, x = [], [], m
for i in petits:
    if x + i.width * k + m > W: lignes.append(ligne); ligne, x = [], m
    ligne.append(i); x += i.width * k + m
lignes.append(ligne)
H = 128 * k + 2 * m + sum(max(i.height for i in l) * k + m for l in lignes)
out = Image.new('RGBA', (W, H), (236, 234, 228, 255))
x = m
for i in ims[:2]:
    out.alpha_composite(i.resize((i.width * k, i.height * k), Image.NEAREST), (x, m)); x += i.width * k + m
y = 128 * k + 2 * m
for l in lignes:
    x = m
    for i in l:
        out.alpha_composite(i.resize((i.width * k, i.height * k), Image.NEAREST), (x, y)); x += i.width * k + m
    y += max(i.height for i in l) * k + m
out.save('calques.png')
