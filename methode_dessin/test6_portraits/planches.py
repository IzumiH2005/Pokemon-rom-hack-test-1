# Planches du test 6 : avant/après, tailles, expressions, étapes, contrôle à x1.
import sys
from PIL import Image
from portrait import *
sys.path.insert(0, '../test5_personnages')
import portrait as _p6
F = (232, 230, 222)

def rang(ims, nom, k, gap=20):
    ims = [i.resize((i.width * k, i.height * k), Image.NEAREST) for i in ims]
    W = sum(i.width for i in ims) + gap * (len(ims) + 1); H = max(i.height for i in ims) + 2 * gap
    s = Image.new('RGB', (W, H), F); x = gap
    for i in ims: s.paste(i, (x, H - gap - i.height), i); x += i.width + gap
    s.save(nom)

tailles = [png(portrait(S), PAL, None) for S in (48, 64, 96)]
rang(tailles, 'portraits.png', 5)
rang(tailles, 'portraits_x1.png', 1, gap=8)
rang([png(portrait(96, expr=e), PAL, None) for e in ('sourire', 'clin', 'surprise')], 'expressions96.png', 4)
rang([png(portrait(96, 1), PAL, None), png(portrait(96, 2), PAL, None), png(portrait(96), PAL, None)], 'etapes96.png', 4)
# avant (test 5, 64 px) / après (test 6, 64 px)
import importlib.util
spec = importlib.util.spec_from_file_location('ancien', '../test5_personnages/portrait.py')
sys.path.insert(0, '../test5_personnages'); anc = importlib.util.module_from_spec(spec); spec.loader.exec_module(anc)
from commun import rendre
rang([rendre(anc.P64, anc.PALP), png(portrait(64), PAL, None)], 'avant_apres64.png', 6)
