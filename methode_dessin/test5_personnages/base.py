# Outils du test 5 (personnages) : réutilise le rendu du test 4.
import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'test4_objets_v4'))
from commun import rendre, vue
from outils import orphelins, angles_L, gris, chaine, grille_vide
from PIL import Image, ImageDraw, ImageOps

CLAIR, SOMBRE = (236, 232, 220, 255), (40, 44, 52, 255)

# Palette commune de « Lina », la dresseuse du test (15 couleurs + transparent).
PAL = {
    'O': (44, 26, 46),     # contour brun-violet (jamais noir)
    'E': (24, 16, 34),     # pupilles (seul ton presque noir)
    '1': (255, 226, 190),  # peau lumière (vers le jaune)
    '2': (240, 180, 146),  # peau base (pêche)
    '3': (200, 118, 116),  # peau ombre (vers le rose-violet)
    'a': (96, 168, 186),   # cheveux lumière
    'b': (52, 110, 142),   # cheveux base (bleu canard)
    'c': (34, 60, 98),     # cheveux ombre (vers le violet)
    'r': (250, 138, 76),   # veste lumière
    'q': (214, 78, 58),    # veste base
    'p': (140, 40, 64),    # veste ombre (vers le violet)
    'n': (74, 84, 128),    # short base
    'm': (46, 46, 86),     # short ombre
    'W': (244, 240, 226),  # blanc cassé
    'Y': (250, 206, 84),   # accent jaune (bandeau)
}

def verifier(G, nom):
    h = len(G); w = len(G[0])
    assert all(len(r) == w for r in G), [(i, len(r)) for i, r in enumerate(G) if len(r) != w]
    cols = sorted({c for r in G for c in r} - {'.'})
    print(nom, '%dx%d' % (w, h), len(cols), 'couleurs', ''.join(cols))
    o = [p for p in orphelins(G) if p[2] not in 'E']
    if o: print('  orphelins :', o[:12])

def planche(images, nom, k, fond=(255, 255, 255), gap=16):
    w = sum(im.width * k + gap for im in images); h = max(im.height for im in images) * k
    out = Image.new('RGB', (w, h), fond); x = 0
    for im in images:
        im2 = im.resize((im.width * k, im.height * k), Image.NEAREST)
        out.paste(im2, (x, h - im2.height), im2 if im2.mode == 'RGBA' else None); x += im2.width + gap
    out.save(nom); return out
