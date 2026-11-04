# Génère toutes les planches du test 5 (x1 et agrandies).
from base import *
import dresseur16 as d16, dresseur32 as d32, dresseur64 as d64, objets as ob, portrait as po
F = (236, 232, 220)

R = lambda G, p: rendre(G, dict(p, **{'#': (90, 90, 110)}))
planche([R(g, PAL) for g in (d16.FACE, d16.PAS_G, d16.PAS_D, d16.DOS, d16.PROFIL)], 'dresseur16.png', 8, fond=F)
planche([R(d16.FACE, PAL), R(d32.G, PAL), R(d64.G, d64.PAL64)], 'dresseurs_16_32_64.png', 5, fond=F)
planche([R(d64.dessiner(e), d64.PAL64) for e in (1, 2, 3, 99)], 'dresseur64_etapes.png', 4, fond=F)
planche([R(g, ob.PAL_O) for g in (ob.BAIE8, ob.BAIE16, ob.LANT16, ob.LANT32, ob.LANT64)], 'objets.png', 5, fond=F)
planche([R(g, po.PALP) for g in (po.P32, po.P48, po.P64)], 'portraits.png', 5, fond=F)
planche([R(po.portrait(64, e), po.PALP) for e in (1, 2, 99)], 'portrait64_etapes.png', 4, fond=F)
# contrôle à l'échelle 1 et 2 (taille réelle à l'écran)
imgs = [R(d16.FACE, PAL), R(d32.G, PAL), R(d64.G, d64.PAL64), R(ob.BAIE16, ob.PAL_O), R(ob.LANT32, ob.PAL_O),
        R(po.P32, po.PALP), R(po.P48, po.PALP), R(po.P64, po.PALP)]
planche(imgs, 'controle_x1.png', 1, fond=F, gap=4)
planche(imgs, 'controle_x2.png', 2, fond=F, gap=6)
