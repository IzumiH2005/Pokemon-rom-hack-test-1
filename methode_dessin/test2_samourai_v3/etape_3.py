from base import *
from etapes_1_2 import J, OS
import math
g, d = guide()
VERT = (0, 150, 70, 255)
def cyl(a, b, ra, rb, c=VERT):
    (x1, y1), (x2, y2) = J[a] if isinstance(a, str) else a, J[b] if isinstance(b, str) else b
    ang = math.atan2(y2 - y1, x2 - x1); nx, ny = -math.sin(ang), math.cos(ang)
    pts = [(x1 + nx*ra, y1 + ny*ra), (x2 + nx*rb, y2 + ny*rb), (x2 - nx*rb, y2 - ny*rb), (x1 - nx*ra, y1 - ny*ra)]
    d.polygon([P(*p) for p in pts], outline=c, width=2)
def circ(c, r, col=(0, 60, 200, 255)):
    x, y = J[c] if isinstance(c, str) else c
    d.ellipse([P(x - r, y - r), P(x + r, y + r)], outline=col, width=2)
for a, b in OS: d.line([P(*J[a]), P(*J[b])], fill=(220, 80, 80, 120), width=1)
# tete : sphere + plan lateral + croix du visage (Loomis 3/4)
d.ellipse([P(49, 8), P(71, 31)], outline=VERT, width=2)
d.ellipse([P(60, 13), P(69, 27)], outline=VERT, width=1)                      # plan lateral (cercle)
d.line([P(53, 9), P(51, 20), P(52, 28), P(55, 34)], fill=(230, 40, 40, 255), width=2)  # ligne centrale courbe
d.line([P(50, 20), P(68, 21)], fill=(230, 40, 40, 255), width=1)              # sourcils
d.line([P(50, 27), P(67, 27)], fill=(230, 40, 40, 255), width=1)              # nez
d.polygon([P(51, 27), P(57, 27), P(60, 31), P(55, 34), P(52, 32)], outline=VERT, width=1)  # bloc machoire
# cou : cylindre qui part de derriere la machoire, penche vers l'avant
cyl((62, 28), (60, 41), 5.5, 7)
# cage (oeuf) et bassin (bol) : deux masses separees
d.ellipse([P(46, 42), P(77, 72)], outline=VERT, width=2)
d.line([P(57, 42), P(55, 58), P(58, 72)], fill=(230, 40, 40, 255), width=1)  # ligne centrale cage
d.polygon([P(47, 82), P(76, 79), P(78, 94), P(63, 103), P(48, 98)], outline=VERT, width=2)
# epaules : spheres du deltoide qui depassent de la cage
circ("ep_loin", 6); circ("ep_pres", 7)
# bras
cyl("ep_loin", "coude_loin", 5.5, 4); circ("coude_loin", 3.5); cyl("coude_loin", "poig_loin", 4.5, 2.6); circ("poig_loin", 2.5)
cyl("ep_pres", "coude_pres", 6, 4.3); circ("coude_pres", 3.8); cyl("coude_pres", "poig_pres", 5, 3); circ("poig_pres", 2.8)
# mains : paume trapeze
d.polygon([P(41, 103), P(46, 103), P(48, 113), P(42, 114)], outline=VERT, width=2)
d.polygon([P(76, 89), P(80, 94), P(74, 100), P(70, 95)], outline=VERT, width=2)
# jambes (sous le hakama, mais construites quand meme)
circ("hanche_loin", 6); circ("hanche_pres", 6)
cyl("hanche_loin", "genou_loin", 8, 5); circ("genou_loin", 4.5); cyl("genou_loin", "chev_loin", 5, 2.6); circ("chev_loin", 2.5)
cyl("hanche_pres", "genou_pres", 8.5, 5.5); circ("genou_pres", 5); cyl("genou_pres", "chev_pres", 5.5, 2.8); circ("chev_pres", 2.6)
d.polygon([P(45, 177), P(31, 183), P(32, 186), P(46, 186)], outline=VERT, width=2)
d.polygon([P(64, 177), P(50, 184), P(51, 187), P(66, 187)], outline=VERT, width=2)
on_bg(g).save(f"{OUT}/etape_03_volumes.png")
