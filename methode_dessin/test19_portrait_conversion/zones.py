# Étape 2 : zones posées à la main (polygones en coordonnées 128), chaque zone a sa rampe.
# La valeur (clair/sombre) vient de l'illustration, étirée zone par zone ; la teinte vient de la rampe.
# Usage : python3 zones.py reduit128.png brouillon.txt
import sys
from PIL import Image, ImageDraw
im = Image.open(sys.argv[1]).convert('RGB'); px = im.load()
def masque(polys):
    m = Image.new('L', (128, 128), 0); d = ImageDraw.Draw(m)
    for p in polys: d.polygon(p, fill=255)
    return m.load()
VISAGE = masque([[(43,29),(78,29),(83,40),(84,52),(83,66),(80,77),(74,85),(66,90),(60,91),(53,88),(47,82),(43,74),(41,62),(40,44)],
                 [(32,57),(37,56),(39,72),(35,74),(32,68)]])
COU    = masque([[(46,82),(53,88),(60,92),(70,88),(78,80),(80,96),(85,110),(80,122),(70,128),(50,128),(40,118),(42,100)]])
HABIT  = masque([[(18,118),(40,111),(50,128),(18,128)],[(84,108),(100,104),(110,116),(112,128),(74,128)]])
RAMPES = {'cheveux': 'Oabcde', 'peau': 'ghijkl', 'habit': 'Oqrst'}
lum = lambda c: 0.3*c[0] + 0.59*c[1] + 0.11*c[2]
def fond(c): return lum(c) > 215 and max(c) - min(c) < 40
def zone(x, y):
    c = px[x, y]
    if fond(c): return None
    sat = c[0] - c[2]
    if (VISAGE[x, y] or COU[x, y]) and sat > 24 and lum(c) > 42: return 'peau'
    if HABIT[x, y] and sat > 8: return 'habit'
    return 'cheveux'
Z = [[zone(x, y) for x in range(128)] for y in range(128)]
# seuils de valeur choisis à la main par zone (luminance de l'illustration -> cran de rampe)
SEUILS = {'cheveux': [30, 52, 88, 130, 999], 'peau': [50, 64, 84, 120, 175], 'habit': [25, 40, 55, 75]}
G = []
for y in range(128):
    l = ''
    for x in range(128):
        z = Z[y][x]
        if z is None: l += '.'; continue
        v = lum(px[x, y]); i = sum(v >= s for s in SEUILS[z])
        l += RAMPES[z][i]
    G.append(l)
open(sys.argv[2], 'w').write('\n'.join(G) + '\n')
