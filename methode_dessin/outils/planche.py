"""Planche de contrôle (A5-11, règle 25).

Usage : python3 planche.py in.png out.png [situation.png]
Rangée 1 : ×1 et ×2 sur fond clair et sombre, miroir, silhouette, gris.
Rangée 2 : agrandi ×4 ; et l'image « en situation » si on la donne.
"""
import sys
from PIL import Image, ImageOps

CLAIR, SOMBRE = (236, 234, 228, 255), (34, 30, 44, 255)


def sur(im, fond, k=1, marge=4):
    W, H = im.size
    f = Image.new('RGBA', (W * k + 2 * marge, H * k + 2 * marge), fond)
    f.alpha_composite(im.resize((W * k, H * k), Image.NEAREST), (marge, marge))
    return f


src, dst = sys.argv[1], sys.argv[2]
im = Image.open(src).convert('RGBA')
a = im.split()[3]
silh = Image.new('RGBA', im.size, (20, 16, 24, 255)); silh.putalpha(a)
gris = ImageOps.grayscale(im.convert('RGB')).convert('RGBA'); gris.putalpha(a)
miroir = ImageOps.mirror(im)

r1 = [sur(im, CLAIR), sur(im, SOMBRE), sur(im, CLAIR, 2), sur(im, SOMBRE, 2),
      sur(miroir, CLAIR, 2), sur(silh, CLAIR, 2), sur(gris, CLAIR, 2)]
r2 = [sur(im, CLAIR, 4)]
if len(sys.argv) > 3:
    r2.append(sur(Image.open(sys.argv[3]).convert('RGBA'), CLAIR, 2))
r2.append(sur(gris, CLAIR, 4))

W = max(sum(p.width for p in r1), sum(p.width for p in r2)) + 8 * 8
H = max(p.height for p in r1) + max(p.height for p in r2) + 24
out = Image.new('RGBA', (W, H), (200, 196, 190, 255))
x = 8
for p in r1:
    out.alpha_composite(p, (x, 8)); x += p.width + 8
x, y = 8, max(p.height for p in r1) + 16
for p in r2:
    out.alpha_composite(p, (x, y)); x += p.width + 8
out.convert('RGB').save(dst)
