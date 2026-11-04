# Planche des étapes : 8 vignettes cumulatives (squelette puis chaque groupe d'armure).
# Usage : python3 etapes.py  (après assembler.py et selout.py)
import json
from PIL import Image, ImageDraw
from assembler import ORDRE
pal = json.load(open('palette.json'))
GROUPES = [('1 squelette', ['calque14_jambes', 'calque12_bassin', 'calque11_tronc', 'calque13_bras', 'calque10_crane']),
           ('2 heaume + panache', ['calque21_panache', 'calque20_heaume']),
           ('3 gorgerin + plastron', ['calque22_gorgerin', 'calque23_plastron']),
           ('4 epauliere + gantelet', ['calque24_epauliere', 'calque25_gantelet']),
           ('5 ceinture + jambiere', ['calque26_ceinture', 'calque27_jambiere']),
           ('6 cape', ['calque28_cape']),
           ('7 epee', ['calque29_epee', 'calque29c_pommeau']),
           ('8 effets + contour', None)]
def rendu(G, k=3):
    im = Image.new('RGB', (128, 128), (150, 150, 160))
    for y, r in enumerate(G):
        for x, c in enumerate(r):
            if c != '.': im.putpixel((x, y), tuple(int(pal[c][j:j+2], 16) for j in (1, 3, 5)))
    return im.resize((128 * k, 128 * k), Image.NEAREST)
lire = lambda n: [l.rstrip('\n') for l in open(n + '.txt') if l.strip()]
actifs, vignettes = set(), []
for titre, cal in GROUPES:
    if cal is None: G = lire('chevalier_final')
    else:
        actifs |= set(cal); G = [['.'] * 128 for _ in range(128)]
        for n in ORDRE:
            if n in actifs:
                for y, l in enumerate(lire(n)):
                    for x, c in enumerate(l):
                        if c != '.': G[y][x] = c
    vignettes.append((titre, rendu(G)))
W = 128 * 3 + 10
out = Image.new('RGB', (4 * W + 10, 2 * (128 * 3 + 30) + 10), (34, 34, 44)); d = ImageDraw.Draw(out)
for i, (t, im) in enumerate(vignettes):
    x, y = 10 + (i % 4) * W, 10 + (i // 4) * (128 * 3 + 30)
    d.text((x, y), t, fill=(235, 235, 235)); out.paste(im, (x, y + 18))
out.save('etapes_chevalier.png')
