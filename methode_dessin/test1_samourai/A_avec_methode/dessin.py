#!/usr/bin/env python3
"""Jeune femme samourai - pixel art 64x96, suivant METHODE_PIXEL_ART.md.
Chaque etape est decrite en DONNEES puis tracee (R3) ; chaque etape sauve etape_XX_nom.png (x6)."""
import math, os
from PIL import Image, ImageDraw, ImageFont
import numpy as np

OUT = os.path.dirname(os.path.abspath(__file__))
W, Hc = 64, 96
S = 6  # agrandissement

# ---------------------------------------------------------------- ETAPE 0
INTENTION = [
    "ETAPE 0 - INTENTION",
    "Jeune femme samourai, mot cle : CALME (determinee).",
    "Vue 3/4 face, tournee vers la gauche de l'image. Toile 64x96, fond transparent.",
    "<= 24 couleurs. Semi-realiste : 6 tetes (H = 15 px, du y=4 au y=93).",
    "Lumiere : en haut a gauche, devant (cote ou regarde le visage).",
    "Forme dominante : TRIANGLE stable (hakama en A, diagonales du sabre).",
]

# ---------------------------------------------------------------- ETAPE 1
TOP, BOT = 4, 93          # haut du crane, plante des pieds (marges : chignon au-dessus, ombre dessous)
NHEADS = 6
HH = (BOT - TOP) / NHEADS  # ~14.8 px
REPERES = {  # repères mis a l'echelle 6 tetes (fractions de la hauteur)
    "menton": TOP + HH * 1.0,        # 18.8
    "epaules": TOP + HH * 1.3,       # 23
    "aisselles/poitrine": TOP + HH * 1.8,  # 30.7
    "coude/taille": TOP + HH * 2.45, # 40
    "entrejambe/poignets": TOP + HH * 3.0,  # 48.5 = moitie du corps
    "genoux": TOP + HH * 4.4,        # 69
    "chevilles": TOP + HH * 5.75,    # 89
    "pieds": BOT,
}
LARG_EPAULES = 1.3 * HH  # CONTROLE 1 : 1.0H etait trop etroit -> 6 tetes ~1.5H de face, ~1.3H en 3/4 (~19 px)

# ---------------------------------------------------------------- ETAPE 2
# poids sur la jambe PROCHE (gauche du perso = droite de l'image)
J = {
    'crane': (30, 11), 'cou_haut': (31, 18), 'cou_base': (31, 23),
    'ep_loin': (23, 24), 'ep_pres': (39, 26),  # CONTROLE 2 : ecartees de 2 px (epaules trop etroites)          # epaule proche plus basse
    'cd_loin': (16, 37), 'pg_loin': (27, 41.5), 'mn_loin': (30.5, 41.5),  # CONTROLE 5 : coude ecarte -> trou de fond   # main droite sur la poignee
    'cd_pres': (41, 41), 'pg_pres': (42, 52), 'mn_pres': (42, 59),   # bras le long du corps
    'bassin': (31, 46), 'hc_loin': (26, 47), 'hc_pres': (36, 45),    # hanche proche plus haute
    'gn_loin': (25, 69), 'ch_loin': (23, 89), 'pt_loin': (19, 92),
    'gn_pres': (34, 68), 'ch_pres': (32, 89), 'pt_pres': (28, 92),
}
OS_ = [('crane', 'cou_haut'), ('cou_haut', 'cou_base'), ('cou_base', 'ep_loin'), ('cou_base', 'ep_pres'),
       ('ep_loin', 'cd_loin'), ('cd_loin', 'pg_loin'), ('pg_loin', 'mn_loin'),
       ('ep_pres', 'cd_pres'), ('cd_pres', 'pg_pres'), ('pg_pres', 'mn_pres'),
       ('cou_base', 'bassin'), ('bassin', 'hc_loin'), ('bassin', 'hc_pres'),
       ('hc_loin', 'gn_loin'), ('gn_loin', 'ch_loin'), ('ch_loin', 'pt_loin'),
       ('hc_pres', 'gn_pres'), ('gn_pres', 'ch_pres'), ('ch_pres', 'pt_pres')]
LIGNE_ACTION = [(29, 4), (31, 15), (32, 24), (33.5, 36), (34, 47), (34, 60), (33.5, 75), (32, 89)]

# ---------------------------------------------------------------- ETAPE 3 volumes (centre, taille, inclinaison)
VOL = {
    'tete':    dict(t='ellipse', c=(30, 11.3), r=(6.2, 7.0)),  # CONTROLE 9 : ne deborde plus sous la machoire
    'cou':     dict(t='cyl', a=(31.5, 17), b=(31, 24), w=(4.5, 5)),
    # CONTROLE 3 : la boite du thorax laissait un trou a la taille -> oeuf effile vers la taille, incline
    'thorax':  dict(t='poly', p=[(23, 23.5), (31, 22.5), (39.5, 25.5), (38.5, 33), (36.5, 40), (27, 41), (25, 33)]),
    'bassin':  dict(t='box', c=(31.5, 45), s=(15, 9), ang=-7),     # incline en sens oppose
    'machoire': dict(t='poly', p=[(24.2, 12), (24.8, 16), (26.4, 18.2), (28.6, 18.9), (30.4, 18.3), (32.6, 16.8), (35, 14)]),
    'bras_loin':  dict(t='cyl', a=J['ep_loin'], b=J['cd_loin'], w=(4.5, 3.5)),
    'avb_loin':   dict(t='cyl', a=J['cd_loin'], b=J['pg_loin'], w=(3.5, 3)),
    'main_loin':  dict(t='box', c=(30.5, 41.5), s=(5, 4.5), ang=-20),
    'bras_pres':  dict(t='cyl', a=J['ep_pres'], b=J['cd_pres'], w=(5, 4)),
    'avb_pres':   dict(t='cyl', a=J['cd_pres'], b=J['pg_pres'], w=(4, 3)),
    'main_pres':  dict(t='box', c=(42.2, 55.5), s=(4, 7), ang=-3),
    'cuisse_loin': dict(t='cyl', a=J['hc_loin'], b=J['gn_loin'], w=(7, 5)),
    'mollet_loin': dict(t='cyl', a=J['gn_loin'], b=J['ch_loin'], w=(5, 3)),
    'pied_loin':   dict(t='poly', p=[(25, 88), (25, 93), (18, 93), (19, 91)]),
    'cuisse_pres': dict(t='cyl', a=J['hc_pres'], b=J['gn_pres'], w=(7.5, 5.5)),
    'mollet_pres': dict(t='cyl', a=J['gn_pres'], b=J['ch_pres'], w=(5.5, 3.5)),
    'pied_pres':   dict(t='poly', p=[(34, 88), (34, 93), (27, 93), (28, 91)]),
}
# repères du visage (Loomis) : axe tourne vers la gauche, yeux a mi-hauteur, nez au tiers inferieur
VISAGE = dict(axe_x=27, yeux_y=11.5, sourcils_y=10, nez_y=15, menton_y=19, oreille=(33, 12, 15))


# ================================================================ outils
def up(img, s=S):
    return img.resize((img.width * s, img.height * s), Image.NEAREST)


def font(sz=12):
    try:
        return ImageFont.truetype("/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf", sz)
    except Exception:
        return ImageFont.load_default()


def guide_canvas(grid=True):
    """fond gris clair agrandi avec lignes des tetes"""
    im = Image.new('RGBA', (W * S, Hc * S), (236, 236, 232, 255))
    d = ImageDraw.Draw(im)
    if grid:
        for x in range(W):
            d.line([(x * S, 0), (x * S, Hc * S)], fill=(226, 226, 222, 255))
        for y in range(Hc):
            d.line([(0, y * S), (W * S, y * S)], fill=(226, 226, 222, 255))
        for i in range(NHEADS + 1):
            y = (TOP + HH * i) * S
            d.line([(0, y), (W * S, y)], fill=(90, 120, 200, 255), width=2)
            d.text((2, y + 1), f"{i}H", fill=(60, 80, 160, 255), font=font(11))
    return im, d


def P(pt):
    return (pt[0] * S + S / 2, pt[1] * S + S / 2)


def save(im, name):
    im.save(os.path.join(OUT, name))
    print("->", name)


def rot(p, c, ang):
    a = math.radians(ang)
    x, y = p[0] - c[0], p[1] - c[1]
    return (c[0] + x * math.cos(a) - y * math.sin(a), c[1] + x * math.sin(a) + y * math.cos(a))


def vol_poly(v, n=24):
    """contour (en px) d'un volume decrit en donnees"""
    t = v['t']
    if t == 'ellipse':
        (cx, cy), (rx, ry) = v['c'], v['r']
        return [(cx + rx * math.cos(2 * math.pi * i / n), cy + ry * math.sin(2 * math.pi * i / n)) for i in range(n)]
    if t == 'box':
        (cx, cy), (w, h) = v['c'], v['s']
        pts = [(cx - w / 2, cy - h / 2), (cx + w / 2, cy - h / 2), (cx + w / 2, cy + h / 2), (cx - w / 2, cy + h / 2)]
        return [rot(p, (cx, cy), v['ang']) for p in pts]
    if t == 'cyl':
        (ax, ay), (bx, by) = v['a'], v['b']
        dx, dy = bx - ax, by - ay
        L = math.hypot(dx, dy) or 1
        nx, ny = -dy / L, dx / L
        wa, wb = v['w'][0] / 2, v['w'][1] / 2
        return [(ax + nx * wa, ay + ny * wa), (bx + nx * wb, by + ny * wb), (bx - nx * wb, by - ny * wb), (ax - nx * wa, ay - ny * wa)]
    if t == 'poly':
        return v['p']


# ================================================================ etapes 0 a 3
def etape0():
    im = Image.new('RGBA', (W * S, Hc * S), (250, 248, 240, 255))
    d = ImageDraw.Draw(im)
    y = 20
    for i, l in enumerate(INTENTION):
        f = font(15 if i == 0 else 11)
        # retour a la ligne simple
        words, line = l.split(), ""
        for w_ in words:
            if d.textlength(line + " " + w_, font=f) > W * S - 30:
                d.text((14, y), line, fill=(30, 30, 50, 255), font=f); y += 18; line = w_
            else:
                line = (line + " " + w_).strip()
        d.text((14, y), line, fill=(30, 30, 50, 255), font=f); y += 26
    # fleche de lumiere
    d.line([(40, 470), (130, 540)], fill=(220, 160, 30, 255), width=4)
    d.ellipse([20, 450, 50, 480], fill=(250, 200, 60, 255))
    d.text((60, 545), "lumiere", fill=(150, 100, 20, 255), font=font(12))
    save(im, "etape_00_intention.png")


def etape1():
    im, d = guide_canvas()
    for k, y in REPERES.items():
        d.line([(0, y * S), (W * S, y * S)], fill=(220, 90, 60, 255), width=1)
        d.text((W * S - 150, y * S - 13), f"{k} y={y:.0f}", fill=(180, 60, 40, 255), font=font(10))
    cx = 31
    ex = LARG_EPAULES / 2
    d.line([((cx - ex) * S, REPERES['epaules'] * S), ((cx + ex) * S, REPERES['epaules'] * S)], fill=(40, 160, 80, 255), width=3)
    d.text(((cx - ex) * S, REPERES['epaules'] * S + 4), "epaules ~1.3H (3/4)", fill=(40, 130, 60, 255), font=font(10))
    d.line([(cx * S, TOP * S), (cx * S, BOT * S)], fill=(150, 150, 150, 255))
    save(im, "etape_01_grille.png")


def etape2(name="etape_02_squelette.png"):
    im, d = guide_canvas()
    # ligne d'action (une seule courbe)
    pts = [P(p) for p in catmull(LIGNE_ACTION)]
    d.line(pts, fill=(230, 60, 160, 255), width=4)
    # lignes epaules / hanches
    d.line([P(J['ep_loin']), P(J['ep_pres'])], fill=(40, 160, 80, 255), width=3)
    d.line([P(J['hc_loin']), P(J['hc_pres'])], fill=(40, 160, 80, 255), width=3)
    for a, b in OS_:
        d.line([P(J[a]), P(J[b])], fill=(40, 40, 60, 255), width=3)
    for k, p in J.items():
        x, y = P(p)
        d.ellipse([x - 5, y - 5, x + 5, y + 5], fill=(240, 120, 40, 255))
    d.ellipse([P(J['crane'])[0] - 37, P(J['crane'])[1] - 45, P(J['crane'])[0] + 37, P(J['crane'])[1] + 45], outline=(40, 40, 60, 255), width=3)
    # ligne de gravite
    gx = P(J['cou_base'])[0]
    d.line([(gx, P(J['cou_base'])[1]), (gx, BOT * S)], fill=(60, 140, 230, 255), width=1)
    d.text((gx + 4, BOT * S - 30), "gravite", fill=(60, 140, 230, 255), font=font(10))
    save(im, name)
    return im


def catmull(pts, n=8):
    out = []
    pts = [pts[0]] + pts + [pts[-1]]
    for i in range(1, len(pts) - 2):
        p0, p1, p2, p3 = pts[i - 1], pts[i], pts[i + 1], pts[i + 2]
        for k in range(n):
            t = k / n
            out.append(tuple(0.5 * ((2 * p1[j]) + (-p0[j] + p2[j]) * t + (2 * p0[j] - 5 * p1[j] + 4 * p2[j] - p3[j]) * t * t
                                    + (-p0[j] + 3 * p1[j] - 3 * p2[j] + p3[j]) * t ** 3) for j in range(2)))
    out.append(pts[-2])
    return out


VOL_ORDRE = ['cuisse_loin', 'mollet_loin', 'pied_loin', 'bras_loin', 'cuisse_pres', 'mollet_pres', 'pied_pres',
             'bassin', 'thorax', 'cou', 'tete', 'machoire', 'bras_pres', 'avb_pres', 'main_pres', 'avb_loin', 'main_loin']


def etape3():
    im, d = guide_canvas()
    ov = Image.new('RGBA', im.size, (0, 0, 0, 0))
    od = ImageDraw.Draw(ov)
    cols = {'tete': (240, 190, 150), 'machoire': (240, 190, 150), 'cou': (230, 170, 140), 'thorax': (120, 170, 230), 'bassin': (120, 200, 160)}
    for k in VOL_ORDRE:
        v = VOL[k]
        poly = [P(p) for p in vol_poly(v)]
        c = cols.get(k, (230, 160, 120) if 'loin' not in k else (190, 140, 120))
        od.polygon(poly, fill=c + (255,), outline=(40, 40, 60, 255), width=2)
    im = Image.alpha_composite(im, ov)
    d = ImageDraw.Draw(im)
    # plans de Loomis
    t = VOL['tete']; (cx, cy), (rx, ry) = t['c'], t['r']
    d.line([P((VISAGE['axe_x'], 5)), P((VISAGE['axe_x'] - 0.5, 19))], fill=(200, 40, 40, 255), width=2)
    for k in ('sourcils_y', 'yeux_y', 'nez_y'):
        y = VISAGE[k]
        d.line([P((cx - rx + 0.5, y)), P((cx + rx - 0.5, y))], fill=(200, 40, 40, 255), width=1)
    ox, oy1, oy2 = VISAGE['oreille']
    d.rectangle([ox * S, oy1 * S, (ox + 1) * S, (oy2 + 1) * S], outline=(200, 40, 40, 255), width=2)
    d.ellipse([P((cx + 1.2, cy - 3.5))[0] - 18, P((cx + 1.2, cy - 3.5))[1] - 18, P((cx + 1.2, cy - 3.5))[0] + 18, P((cx + 1.2, cy - 3.5))[1] + 18], outline=(200, 40, 40, 255), width=1)
    # cote visible de la boite du thorax (3/4 : on voit le flanc droit de l'image)
    d.line([P((35, 24)), P((34, 40))], fill=(30, 60, 140, 255), width=2)
    save(im, "etape_03_volumes.png")


# ---------------------------------------------------------------- ETAPE 4 vetements / design (donnees)
# axe du sabre : saya vers l'arriere-bas (droite), tsuka vers l'avant-haut (gauche), meme droite
SABRE_DIR = (0.8, 0.6)  # CONTROLE 5 : plus incline, le kashira depasse au-dessus de l'avant-bras
TSUBA = (34, 44)
def le_long(t, base=TSUBA):
    return (base[0] + SABRE_DIR[0] * t, base[1] + SABRE_DIR[1] * t)

def bande(a, b, w):
    return vol_poly(dict(t='cyl', a=a, b=b, w=(w, w)))

DESIGN = [  # (nom, matiere, polygone) dans l'ordre arriere -> avant
    ('queue',      'hair', [(34, 3), (37, 1.2), (41, 1.6), (44, 4.5), (46.3, 10), (47.4, 17), (47, 24), (45.6, 30.5),
                            (44.6, 33), (43.8, 28), (44, 21), (43, 13), (40.6, 7.5), (37, 5.6)]),
    ('pied_loin',  'tabi', [(19.5, 89), (24.6, 89), (24.6, 93.4), (17.3, 93.4), (17.6, 91.5)]),
    ('pied_pres',  'tabi', [(28.4, 89), (33.6, 89), (33.6, 93.4), (26.3, 93.4), (26.6, 91.5)]),
    ('hakama',     'hak',  [(25, 40.5), (39.4, 39.6), (41.6, 46), (43.2, 60), (44.6, 76), (45.5, 89.6),
                            (39.5, 90.6), (34.6, 90.9), (33.2, 84), (31.2, 80.5), (29.7, 84), (28, 90.9),
                            (22, 90.7), (16.3, 90.2), (18.4, 76), (21, 60), (23.2, 47)]),
    ('cou',        'skin', vol_poly(VOL['cou'])),
    ('poitrine',   'skin', [(27.4, 21.4), (34.8, 21.4), (31, 28.4)]),
    # CONTROLE 6 : col croise en V (pan gauche par-dessus = 'y' vu de face)
    ('kimono',     'kim',  [(22.6, 24), (27.2, 21.6), (30.8, 27.6), (35, 21.6), (40.4, 25), (41.2, 31), (39.6, 40.5),
                            (25, 41), (23.5, 32)]),
    ('tete',       'skin', vol_poly(VOL['tete'], 32)),
    ('machoire',   'skin', VOL['machoire']['p']),
    ('cheveux',    'hair', [(24, 10.5), (23.6, 7), (25.2, 4.6), (28, 3.3), (32, 3), (35.2, 4), (37, 6.5), (37.4, 10),
                            (36.8, 14), (35.4, 17.2), (34, 17.4), (33.2, 14.6), (33, 10.4), (31.4, 8.2),
                            (29, 8.6), (27, 8), (25.6, 9.6)]),
    ('meche',      'hair', [(24.4, 7.6), (25.8, 8), (25.2, 12), (24.6, 15.4), (23.8, 15.6), (23.6, 11)]),
    ('lien',       'red',  [(33.4, 2.6), (36.2, 1.6), (37, 4.4), (34.6, 5.4)]),
    ('obi',        'red',  [(24.8, 38.2), (39.6, 37.4), (39.8, 41.2), (25, 42)]),
    ('saya',       'saya', bande(le_long(1), le_long(27), 2.6)),
    ('manche_pres','kim',  [(37.2, 25.2), (41.8, 25.4), (43.8, 31), (45.6, 39), (47, 45), (46.4, 48.4), (44.6, 49.2),
                            (39.6, 49.2), (38.2, 44), (38, 34)]),
    ('main_pres',  'skin', [(40.4, 48.6), (43.6, 48.6), (44.2, 53), (43.8, 58.6), (42.4, 60.2), (40.6, 59), (40.2, 54)]),
    ('tsuka',      'tsuka', bande(le_long(-13.4), le_long(-0.6), 2.8)),  # CONTROLE 8 : kashira visible au-dessus de l'avant-bras
    ('tsuba',      'gold', [(33, 42.2), (35, 42.6), (35.4, 46.2), (33.6, 46.4)]),
    ('manche_loin','kim',  [(24.2, 23.6), (20.6, 25), (17.4, 29.5), (15, 34.5), (13.8, 40), (14.4, 46), (16, 49),
                            (21.6, 49.2), (24, 46.6), (27.6, 43.6), (27.2, 40.2), (22, 37.6), (19.2, 35.4),
                            (20.4, 31), (22.6, 27.6), (24.6, 26)]),
    ('main_loin',  'skin', [(28.2, 39.8), (31.4, 39.4), (33.2, 40.8), (32.8, 43.6), (29.6, 44.2), (28, 43)]),  # CONTROLE 8 : poing reduit
]
ZDESIGN = {n: i + 1 for i, (n, _, _) in enumerate(DESIGN)}
MAT = {n: m for n, m, _ in DESIGN}


def raster(poly):
    im = Image.new('L', (W, Hc), 0)
    ImageDraw.Draw(im).polygon([(x - 0.0, y - 0.0) for x, y in poly], fill=1)
    return np.array(im, dtype=bool)


def regions():
    """carte des regions (indice z) a 1x"""
    lab = np.zeros((Hc, W), dtype=np.int16)
    for n, m, p in DESIGN:
        lab[raster(p)] = ZDESIGN[n]
    return lab


def etape4():
    im = Image.open(os.path.join(OUT, "etape_03_volumes.png")).convert('RGBA')
    im = Image.blend(Image.new('RGBA', im.size, (240, 240, 236, 255)), im, 0.35)
    d = ImageDraw.Draw(im)
    cols = {'hair': (40, 30, 60), 'kim': (90, 90, 140), 'hak': (30, 40, 120), 'red': (200, 30, 40), 'skin': (170, 90, 80),
            'saya': (20, 20, 20), 'tsuka': (60, 40, 80), 'gold': (190, 140, 30), 'tabi': (120, 120, 120)}
    for n, m, p in DESIGN:
        if n in ('tete', 'cou', 'machoire'):
            continue
        d.polygon([P(q) for q in p], outline=cols[m] + (255,), width=3)
    # plis : partent des points de tension (epaules, taille, genoux)
    for a, b in PLIS:
        d.line([P(a), P(b)], fill=(30, 40, 120, 255), width=1)
    save(im, "etape_04_vetements.png")


PLIS = [((28, 42), (22, 89)), ((31, 42), (27, 88)), ((34.5, 41.5), (37, 89)), ((37.5, 41), (41.5, 89)),
        ((31, 81), (31, 72)), ((39, 26), (45, 47)), ((17, 36), (16, 47))]


def etape5():
    lab = regions()
    sil = Image.new('RGBA', (W, Hc), (0, 0, 0, 0))
    a = np.zeros((Hc, W, 4), np.uint8)
    a[lab > 0] = (20, 18, 30, 255)
    sil = Image.fromarray(a)
    sheet = Image.new('RGBA', (W * S + W + 30, Hc * S), (250, 250, 250, 255))
    sheet.paste(up(sil), (0, 0), up(sil))
    sheet.paste(sil, (W * S + 15, 10), sil)
    save(sheet, "etape_05_silhouette.png")
    return lab

# ---------------------------------------------------------------- PALETTE (etape 7, decalage de teinte, <=24)
PAL = {
    'OUT': (28, 20, 40),                                   # contour le plus sombre (pas noir pur)
    's0': (112, 56, 72), 's1': (178, 106, 116), 's2': (228, 162, 136), 's3': (248, 206, 172),   # peau
    'h1': (46, 38, 70), 'h2': (72, 62, 102), 'h3': (112, 102, 146),                          # cheveux / laque
    'k0': (92, 92, 132), 'k1': (158, 162, 198), 'k2': (212, 212, 222), 'k3': (244, 238, 218), # kimono blanc
    'a1': (32, 34, 72), 'a2': (48, 54, 100), 'a3': (78, 88, 140),  # hakama indigo (CONTROLE 7 : plus sombre, moins sature)
    'r0': (112, 22, 48), 'r1': (204, 48, 56), 'r2': (240, 104, 72),  # ACCENT rouge (CONTROLE 7 : valeur > hakama)
    'g0': (128, 86, 40), 'g1': (212, 166, 70), 'g2': (248, 222, 132),                        # or (tsuba)
    'SOL': (28, 20, 40, 90),                                                                 # ombre au sol
}
RAMPE = {  # matiere -> (contour, ombre, base, lumiere)
    'skin': ('s0', 's1', 's2', 's3'), 'hair': ('OUT', 'h1', 'h2', 'h3'), 'kim': ('k0', 'k1', 'k2', 'k3'),
    'tabi': ('k0', 'k1', 'k2', 'k3'), 'hak': ('OUT', 'a1', 'a2', 'a3'), 'red': ('r0', 'r0', 'r1', 'r2'),
    'saya': ('OUT', 'OUT', 'h1', 'h3'), 'tsuka': ('OUT', 'h1', 'a1', 'a2'), 'gold': ('g0', 'g0', 'g1', 'g2'),
}
# paires (avant, arriere) qui recoivent une ligne interieure (contraste insuffisant ou chevauchement)
LIGNES_INT = {('manche_pres', 'kimono'), ('manche_pres', 'hakama'), ('manche_pres', 'obi'), ('manche_pres', 'saya'),
              ('manche_loin', 'kimono'), ('manche_loin', 'hakama'), ('manche_loin', 'obi'),
              ('main_loin', 'manche_loin'), ('main_loin', 'obi'), ('main_loin', 'kimono'), ('main_loin', 'tsuka'),
              ('main_pres', 'manche_pres'), ('main_pres', 'hakama'),
              ('kimono', 'cou'), ('queue', 'cheveux'), ('cheveux', 'queue'),
              ('pied_loin', 'hakama'), ('pied_pres', 'hakama'), ('obi', 'kimono'), ('obi', 'hakama'),
              ('kimono', 'queue'), ('manche_pres', 'queue'), ('tsuka', 'obi'), ('tsuka', 'kimono'), ('tsuka', 'manche_loin'),
              ('tsuba', 'obi'), ('tsuba', 'hakama'), ('saya', 'hakama'), ('saya', 'obi'), ('lien', 'cheveux'), ('lien', 'queue'),
              ('kimono', 'poitrine')}  # CONTROLE 6 : plus de ligne cheveux/peau (effet casque)
NOMS = {v: k for k, v in ZDESIGN.items()}
N4 = [(-1, 0), (1, 0), (0, -1), (0, 1)]


def voisins(lab, x, y, d=N4):
    for dx, dy in d:
        xx, yy = x + dx, y + dy
        yield dx, dy, (lab[yy, xx] if 0 <= xx < W and 0 <= yy < Hc else 0)


def contour(lab):
    """renvoie {(x,y): 'ext'|'int'} ; contour 1 px puis suppression des angles en L"""
    line = {}
    for y in range(Hc):
        for x in range(W):
            z = lab[y, x]
            if not z:
                continue
            for dx, dy, zz in voisins(lab, x, y):
                if zz == 0:
                    line[(x, y)] = 'ext'; break
                if zz < z and (NOMS[z], NOMS[zz]) in LIGNES_INT:
                    line.setdefault((x, y), 'int')
    return line


def supprime_L(lab, line):
    """pixel-perfect : un pixel de contour qui forme un coin en L avec deux voisins de contour
    (un horizontal, un vertical) est retire ; coin convexe exterieur -> devient fond."""
    changed = True; n = 0
    while changed:
        changed = False
        for (x, y), kind in list(line.items()):
            if kind != 'ext':
                continue
            h = [(x + d, y) for d in (-1, 1) if line.get((x + d, y)) == 'ext']
            v = [(x, y + d) for d in (-1, 1) if line.get((x, y + d)) == 'ext']
            if len(h) == 1 and len(v) == 1:
                # coin : les deux autres voisins orthogonaux
                ox, oy = 2 * x - h[0][0], 2 * y - v[0][1]
                o1 = lab[y, ox] if 0 <= ox < W else 0
                o2 = lab[oy, x] if 0 <= oy < Hc else 0
                if o1 == 0 and o2 == 0:  # coin convexe : on arrondit
                    del line[(x, y)]; lab[y, x] = 0; changed = True; n += 1
    return n


def compte_L(line):
    n = 0
    for (x, y) in line:
        h = sum((x + d, y) in line for d in (-1, 1)); v = sum((x, y + d) in line for d in (-1, 1))
        dg = sum((x + a, y + b) in line for a in (-1, 1) for b in (-1, 1))
        if h == 1 and v == 1 and dg == 0:
            n += 1
    return n


def couleur_contour(lab, x, y, kind):
    m = MAT[NOMS[lab[y, x]]]
    r = RAMPE[m]
    if kind == 'ext':
        # cote lumiere (fond a gauche / en haut) : contour plus clair (selout)
        lit = any(zz == 0 and (dx < 0 or dy < 0) for dx, dy, zz in voisins(lab, x, y))
        return r[1] if lit and m not in ('hak', 'hair', 'saya') else r[0]
    return r[0] if m not in ('kim', 'tabi', 'skin') else r[1] if m == 'kim' else r[0]


def to_img(cv):
    a = np.zeros((Hc, W, 4), np.uint8)
    for y in range(Hc):
        for x in range(W):
            k = cv[y][x]
            if k:
                c = PAL[k]
                a[y, x] = c if len(c) == 4 else c + (255,)
    return Image.fromarray(a, 'RGBA')


def etape6():
    lab = regions()
    nL = supprime_L(lab, line := contour(lab))
    line = contour(lab)  # recalcul apres arrondi
    nL += supprime_L(lab, line)
    cv = [[None] * W for _ in range(Hc)]
    for (x, y), kind in line.items():
        cv[y][x] = couleur_contour(lab, x, y, kind)
    img = to_img(cv)
    bg = Image.new('RGBA', (W, Hc), (255, 255, 255, 255))
    bg = Image.alpha_composite(bg, img)
    save(up(bg), "etape_06_contour.png")
    print("   coins L arrondis:", nL, " L restants:", compte_L({k for k, v in line.items() if v == 'ext'}))
    return lab, line

def gris(img):
    g = img.convert('LA').convert('RGBA')
    g.putalpha(img.getchannel('A'))
    return g


def cote_a_cote(imgs, fond=(250, 250, 250, 255), s=S):
    w = sum(i.width * s for i in imgs) + 10 * (len(imgs) - 1)
    sh = Image.new('RGBA', (w, Hc * s), fond)
    x = 0
    for i in imgs:
        u = up(i, s); sh.paste(u, (x, 0), u); x += u.width + 10
    return sh


def aplats(lab, line):
    cv = [[None] * W for _ in range(Hc)]
    for y in range(Hc):
        for x in range(W):
            if lab[y, x]:
                cv[y][x] = RAMPE[MAT[NOMS[lab[y, x]]]][2]
    for (x, y), kind in line.items():
        cv[y][x] = couleur_contour(lab, x, y, kind)
    return cv


def etape7(lab, line):
    cv = aplats(lab, line)
    img = to_img(cv)
    save(cote_a_cote([img, gris(img)]), "etape_07_couleurs_plates.png")
    return cv

# ---------------------------------------------------------------- ETAPE 8 lumiere (donnees)
LUM = (-0.55, -0.62, 0.56)  # haut-gauche, devant
_n = math.sqrt(sum(c * c for c in LUM)); LUM = tuple(c / _n for c in LUM)
# modele de volume par region : ('sphere', centre, rayons, seuil_ombre, seuil_lumiere)
#                               ('cyl', seuil_ombre u, seuil_lumiere u, part haute eclairee 0..1)
OMBRAGE = {
    'tete': ('sphere', (30.5, 12), (6.5, 8), 0.22, 0.83), 'machoire': ('sphere', (30.5, 12), (6.5, 8), 0.22, 0.83),
    'cheveux': ('sphere', (31, 9.5), (7, 7.5), 0.30, 0.86), 'meche': ('cyl', 0.99, 0.0, 0),
    'queue': ('cyl', 0.52, 0.3, 0.55), 'lien': ('cyl', 0.6, 0.3, 1),
    'kimono': ('cyl', 0.70, 0.22, 0.45), 'manche_loin': ('cyl', 0.66, 0.34, 0.55), 'manche_pres': ('cyl', 0.56, 0.0, 0),  # CONTROLE 11 : trainee claire parasite sur l'epaule
    'hakama': ('cyl', 0.64, 0.12, 0.4), 'obi': ('cyl', 0.74, 0.3, 1), 'poitrine': ('cyl', 0.99, 0, 0),  # CONTROLE 9 hakama : la bande claire suivait tout le contour (banding)
    'main_pres': ('cyl', 0.55, 0.3, 0.5), 'main_loin': ('cyl', 0.75, 0.4, 0.5),
    'pied_loin': ('cyl', 0.7, 0.3, 1), 'pied_pres': ('cyl', 0.7, 0.3, 1),
    'saya': ('cyl', 0.99, 0, 0), 'tsuka': ('cyl', 0.99, 0, 0), 'tsuba': ('cyl', 0.6, 0.3, 0.6), 'cou': ('cyl', 0.0, 0, 0),
}


def ombrer(lab, line, cv):
    masques = {n: raster(p) for n, m, p in DESIGN}
    ext = {}
    for n, mk in masques.items():  # etendue NON masquee de chaque volume (pour suivre la forme reelle)
        ys, xs = np.nonzero(mk)
        rows = {}
        for y, x in zip(ys, xs):
            a, b = rows.get(y, (99, -1)); rows[y] = (min(a, x), max(b, x))
        ext[n] = (rows, ys.min(), ys.max())
    for y in range(Hc):
        for x in range(W):
            z = lab[y, x]
            if not z or (x, y) in line:
                continue
            n = NOMS[z]; r = RAMPE[MAT[n]]; o = OMBRAGE[n]
            t = 2
            if o[0] == 'sphere':
                (cx, cy), (rx, ry), ts, tl = o[1:]
                nx, ny = (x - cx) / rx, (y - cy) / ry
                q = nx * nx + ny * ny
                if q > 1: nx, ny, q = nx / math.sqrt(q), ny / math.sqrt(q), 1
                nz = math.sqrt(1 - q)
                d = nx * LUM[0] + ny * LUM[1] + nz * LUM[2]
                t = 1 if d < ts else 3 if d > tl else 2
            else:
                ts, tl, haut = o[1:]
                rows, y0, y1 = ext[n]
                a, b = rows[y]
                u = (x - a) / max(1, b - a)
                f = (y - y0) / max(1, y1 - y0)
                ts_y = ts + 0.06 * math.sin(y * 0.9 + x * 0.0)  # terminateur legerement ondule (anti-banding)
                tl_y = tl * max(0.0, 1 - f / haut) if haut else 0
                t = 1 if u > ts_y else 3 if u < tl_y else 2
            cv[y][x] = r[t]
    ombres_portees(lab, line, cv)


def ombres_portees(lab, line, cv):
    def nm(x, y):
        return NOMS.get(int(lab[y, x])) if 0 <= x < W and 0 <= y < Hc and lab[y, x] else None

    def setr(x, y, t):
        if (x, y) not in line and lab[y, x]:
            cv[y][x] = RAMPE[MAT[nm(x, y)]][t]
    for y in range(Hc):
        for x in range(W):
            n = nm(x, y)
            if not n:
                continue
            au_dessus = [nm(x, y - k) for k in (1, 2)]
            if n in ('tete', 'machoire') and au_dessus[0] in ('cheveux', 'meche'):
                setr(x, y, 1)                      # sous la frange
            if n == 'cou' and not (nm(x - 1, y) is not None and nm(x - 2, y) is None and y >= 20):
                setr(x, y, 1)                      # sous le menton (le bord gauche reste eclaire, CONTROLE 9)
            if n == 'poitrine' and y <= 23:
                setr(x, y, 1)
            if n == 'hakama' and ('obi' in au_dessus or 'tsuba' in au_dessus[:1] or 'main_loin' in au_dessus):
                setr(x, y, 1)                      # sous l'obi / la main
            if n in ('hakama', 'obi', 'kimono') and nm(x - 1, y) in ('manche_loin',) or (n == 'hakama' and nm(x - 1, y - 1) == 'manche_loin'):
                setr(x, y, 1)                      # la manche gauche porte son ombre vers la droite
            if n in ('hakama', 'saya') and nm(x - 1, y) in ('main_pres', 'manche_pres'):
                setr(x, y, 1)
            if n == 'hakama' and nm(x, y - 1) in ('manche_pres', 'manche_loin'):
                setr(x, y, 1)
            if n == 'kimono' and nm(x, y - 1) == 'poitrine':
                pass
            if n == 'obi' and nm(x - 1, y) in ('main_loin', 'tsuka'):
                setr(x, y, 1)


def ombre_sol(cv):
    for x in range(14, 49):
        for y in (93, 94):
            e = ((x - 31) / 17.5) ** 2 + ((y - 93.6) / 1.4) ** 2
            if e <= 1 and cv[y][x] is None:
                cv[y][x] = 'SOL'


def etape8(lab, line, cv):
    cv = [row[:] for row in cv]
    ombrer(lab, line, cv)
    ombre_sol(cv)
    img = to_img(cv)
    save(cote_a_cote([img, gris(img)]), "etape_08_lumiere.png")
    return cv

# ---------------------------------------------------------------- ETAPE 9 details (donnees, en dernier)
DETAILS_VISAGE = {
    # yeux sur la ligne y=11 (etape 3), ecart = un oeil ; regard vers la gauche (iris a gauche)
    (26, 11): 'OUT', (27, 11): 'OUT', (27, 12): 'h1',                 # oeil du fond, plus etroit
    (30, 11): 'OUT', (31, 11): 'OUT', (30, 12): 'h1', (31, 12): 'k2',  # oeil proche
    (30, 10): 'h1', (31, 10): 'h1',                                    # sourcil (meche groupee de la frange)
    (28, 13): 's3', (29, 14): 's1',                                    # arete du nez eclairee, ombre portee du nez a droite
    (28, 16): 's0', (29, 16): 's1',                                    # bouche fermee, calme
    (33, 12): 's2', (33, 13): 's1', (33, 14): 's1',                    # oreille entre yeux et nez
    (27, 9): 'h2', (28, 9): 's1', (31, 9): 'h2', (32, 9): 'h1',        # pointes de frange (triangles)
}
DETAILS_MAINS = {
    # poing sur la tsuka : rangee des phalanges eclairee, doigts marques par 1 px sombre
    (29, 40): 's3', (30, 40): 's3', (31, 40): 's2',
    (29, 42): 's1', (31, 42): 's1', (32, 41): 's1', (32, 42): 's1',
    # main proche (mitaine) : pouce devant (gauche) separe par 1 px
    (42, 53): 's1', (42, 54): 's1', (41, 52): 's3', (41, 53): 's3', (44, 52): 's1', (44, 53): 's1', (43, 57): 's1',
}


def tracer(a, b):
    """segment de Bresenham (lignes pixel-perfect)"""
    (x0, y0), (x1, y1) = (round(a[0]), round(a[1])), (round(b[0]), round(b[1]))
    dx, dy = abs(x1 - x0), -abs(y1 - y0); sx = 1 if x0 < x1 else -1; sy = 1 if y0 < y1 else -1
    err = dx + dy; pts = []
    while True:
        pts.append((x0, y0))
        if (x0, y0) == (x1, y1): break
        e2 = 2 * err
        if e2 >= dy: err += dy; x0 += sx
        if e2 <= dx: err += dx; y0 += sy
    return pts


PLIS_HAKAMA = [((28, 47), (23, 88)), ((31, 46), (28, 79)), ((35, 46), (37, 88)), ((38, 46), (41, 88))]
PLIS_KIMONO = [((30, 28), (27, 37)),            # bord du pan croise (le 'y')
               ((40, 30), (44, 46)), ((18, 38), (17, 46)), ((25, 30), (24, 37))]


def details(lab, line, cv):
    def nm(x, y):
        return NOMS.get(int(lab[y, x])) if lab[y, x] else None

    def put(x, y, k, seulement=None, interieur=True):
        if not lab[y, x] or (interieur and (x, y) in line):
            return
        if seulement and nm(x, y) not in seulement:
            return
        cv[y][x] = k
    for (x, y), k in DETAILS_VISAGE.items():
        put(x, y, k, interieur=False)
    for (x, y), k in DETAILS_MAINS.items():
        put(x, y, k)
    # plis du hakama : ligne d'ombre + lumiere sur la crete (seulement dans le haut, cote lumiere)
    for i, (a, b) in enumerate(PLIS_HAKAMA):
        pts = tracer(a, b)
        for j, (x, y) in enumerate(pts):
            put(x, y, 'a1', {'hakama'})
            if i < 2 and j < len(pts) * 0.55 and j % 9 < 6:
                put(x - 1, y, 'a3', {'hakama'})
    for a, b in PLIS_KIMONO:
        for (x, y) in tracer(a, b):
            put(x, y, 'k1', {'kimono', 'manche_pres', 'manche_loin'})
    # ombre portee de la tete sur le col (lumiere en haut a gauche -> ombre en bas a droite)
    for x in range(32, 36):
        for y in range(22, 25 + (x < 34)):
            put(x, y, 'k1', {'kimono'})
    # saya laquee : deux reflets nets sur l'arete haute
    for t in list(range(6, 11)) + list(range(17, 20)):
        x, y = le_long(t)
        put(round(x + 0.3), round(y - 0.9), 'h3', {'saya'}, interieur=False)
    # tsuka : tressage (losanges clairs) et kashira dore
    for t in (-12.5, -10.5, -8.5):
        x, y = le_long(t); put(round(x), round(y), 'k1', {'tsuka'})
    x, y = le_long(-13.6); put(round(x), round(y), 'g1', {'tsuka'}, interieur=False)
    # tsuba : reflet
    put(33, 43, 'g2', {'tsuba'}, interieur=False)
    # pieds : semelle de zori sombre, tabi eclaire en haut a gauche, lanière
    for n_ in ('pied_loin', 'pied_pres'):
        ys, xs = np.nonzero(lab == ZDESIGN[n_])
        for x, y in zip(xs, ys):
            if y == ys.max() - 1 and (x, y) not in line:
                cv[y][x] = 'h1'
        put(xs.min() + 2, ys.min() + 1, 'h1')  # lanière (hanao)
    # queue de cheval : meche separee (ligne sombre) + reflet groupe dans la courbe
    for (x, y) in tracer((45, 17), (45, 29)):
        put(x, y, 'h1', {'queue'})
    for (x, y) in [(41, 4), (42, 5), (43, 6), (42, 4)]:
        put(x, y, 'h3', {'queue'})


def etape9(lab, line, cv):
    cv = [row[:] for row in cv]
    details(lab, line, cv)
    img = to_img(cv)
    save(cote_a_cote([img, gris(img)]), "etape_09_details.png")
    return cv

# ---------------------------------------------------------------- ETAPE 10 nettoyage
N8 = [(a, b) for a in (-1, 0, 1) for b in (-1, 0, 1) if (a, b) != (0, 0)]
# orphelins voulus (chacun "merite sa place") : yeux, bouche, nez, reflets choisis, kashira, laniere
ORPHELINS_VOULUS = set(DETAILS_VISAGE) | {(33, 43)}


def orphelins(cv):
    out = []
    for y in range(Hc):
        for x in range(W):
            k = cv[y][x]
            if not k or k == 'SOL':
                continue
            if not any(0 <= x + a < W and 0 <= y + b < Hc and cv[y + b][x + a] == k for a, b in N8):
                out.append((x, y))
    return out


def nettoyer(lab, line, cv):
    cv = [row[:] for row in cv]
    avant = orphelins(cv)
    garde, corr = [], []
    for (x, y) in avant:
        if (x, y) in ORPHELINS_VOULUS or cv[y][x] in ('g1', 'g2', 'h3'):  # reflets / or choisis
            garde.append((x, y)); continue
        # remplace par la couleur majoritaire des 4 voisins de la meme region
        cnt = {}
        for dx, dy in N4:
            xx, yy = x + dx, y + dy
            if 0 <= xx < W and 0 <= yy < Hc and cv[yy][xx] and lab[yy, xx] == lab[y, x]:
                cnt[cv[yy][xx]] = cnt.get(cv[yy][xx], 0) + 1
        if cnt:
            cv[y][x] = max(cnt, key=cnt.get); corr.append((x, y))
        else:
            garde.append((x, y))
    return cv, avant, garde, corr


def etape10(lab, line, cv):
    cv2, avant, garde, corr = nettoyer(lab, line, cv)
    img_av = to_img(cv); img_ap = to_img(cv2)
    mark = up(img_av).copy(); d = ImageDraw.Draw(mark)
    for (x, y) in corr:
        d.rectangle([x * S, y * S, x * S + S - 1, y * S + S - 1], outline=(255, 0, 0, 255), width=2)
    for (x, y) in garde:
        d.rectangle([x * S, y * S, x * S + S - 1, y * S + S - 1], outline=(0, 170, 0, 255), width=2)
    sheet = Image.new('RGBA', (W * S * 2 + 10, Hc * S), (250, 250, 250, 255))
    sheet.paste(mark, (0, 0), mark); u = up(img_ap); sheet.paste(u, (W * S + 10, 0), u)
    save(sheet, "etape_10_nettoyage.png")
    print(f"   orphelins: {len(avant)}  corriges: {len(corr)}  gardes (voulus): {len(garde)}")
    return cv2

# ---------------------------------------------------------------- ETAPE 11 controle final
def couleurs(img):
    a = np.array(img); m = a[..., 3] > 0
    return len({tuple(p) for p in a[m]})


def etape11(cv, nom="planche_controle.png"):
    img = to_img(cv)
    img.save(os.path.join(OUT, "final.png")); up(img).save(os.path.join(OUT, "final_x6.png"))
    flip = img.transpose(Image.FLIP_LEFT_RIGHT)
    sil = img.copy(); a = np.array(sil); a[a[..., 3] > 0] = (0, 0, 0, 255)
    a[(np.array(img)[..., 3] > 0) & (np.array(img)[..., 3] < 255)] = (0, 0, 0, 0)  # pas l'ombre au sol
    sil = Image.fromarray(a)
    g = gris(img)
    pan = [up(img), up(flip), up(sil), up(g)]
    sw = sum(p.width for p in pan) + 10 * 5 + W + 20
    sheet = Image.new('RGBA', (sw, Hc * S + 40), (246, 244, 238, 255))
    d = ImageDraw.Draw(sheet)
    x = 10
    sheet.paste(img, (x, 30), img); d.text((x, 8), "x1", fill=(0, 0, 0, 255), font=font(12))
    sheet.paste(sil, (x, 140), sil); sheet.paste(g, (x, 250), g)
    x += W + 20
    for lbl, p in zip(["x6", "miroir", "silhouette", "gris"], pan):
        sheet.paste(p, (x, 30), p); d.text((x, 8), lbl, fill=(0, 0, 0, 255), font=font(12)); x += p.width + 10
    save(sheet, nom)
    print("   couleurs utilisees:", couleurs(img), " orphelins restants:", len(orphelins(cv)))

#PART8
if __name__ == '__main__':
    import sys
    upto = int(sys.argv[1]) if len(sys.argv) > 1 else 99
    etape0(); etape1(); etape2(); etape3(); etape4(); etape5(); lab, line = etape6(); cv = etape7(lab, line); cv = etape8(lab, line, cv); cv = etape9(lab, line, cv); cv = etape10(lab, line, cv); etape11(cv)
