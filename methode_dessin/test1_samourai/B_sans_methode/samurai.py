"""Jeune femme samourai - pixel art 64x96, fond transparent, <=24 couleurs.
Construction : formes primitives (polygones) posées dans une grille d'index de palette,
puis patchs ASCII dessinés à la main pour le visage, les mains et les détails,
puis contour sélectif automatique."""
from PIL import Image, ImageDraw
import os

W, H = 64, 96
OUT = os.path.dirname(os.path.abspath(__file__))

PAL = {
    0: None,
    1: (27, 20, 36),      # contour
    2: (250, 222, 196),   # peau clair
    3: (232, 178, 142),   # peau
    4: (182, 116, 96),    # peau ombre
    5: (30, 22, 40),      # cheveux sombre
    6: (60, 44, 80),      # cheveux moyen
    7: (104, 84, 140),    # cheveux reflet
    8: (244, 240, 230),   # kimono blanc
    9: (198, 190, 206),   # kimono ombre
    10: (130, 120, 152),  # kimono ombre profonde
    11: (84, 96, 160),    # hakama reflet
    12: (52, 58, 112),    # hakama
    13: (32, 34, 72),     # hakama ombre
    14: (230, 88, 74),    # rouge clair
    15: (176, 44, 54),    # rouge
    16: (106, 24, 44),    # rouge ombre
    17: (92, 74, 100),    # laque reflet
    18: (46, 34, 52),     # laque
    19: (244, 204, 100),  # or clair
    20: (178, 126, 46),   # or
    21: (120, 74, 50),    # bois / semelle
}

G = [[0] * W for _ in range(H)]


def put(x, y, c):
    if 0 <= x < W and 0 <= y < H:
        G[y][x] = c


def mask_poly(pts):
    im = Image.new('L', (W, H), 0)
    ImageDraw.Draw(im).polygon(pts, fill=1, outline=1)
    return im


def poly(pts, c, only=None):
    """Remplit un polygone ; `only` = liste d'index sur lesquels peindre (ombres)."""
    im = mask_poly(pts)
    for y in range(H):
        for x in range(W):
            if im.getpixel((x, y)) and (only is None or G[y][x] in only):
                G[y][x] = c


def line(pts, c, only=None):
    im = Image.new('L', (W, H), 0)
    ImageDraw.Draw(im).line(pts, fill=1, width=1)
    for y in range(H):
        for x in range(W):
            if im.getpixel((x, y)) and (only is None or G[y][x] in only):
                G[y][x] = c


def patch(x0, y0, rows, key):
    for j, r in enumerate(rows):
        for i, ch in enumerate(r):
            if ch in key:
                put(x0 + i, y0 + j, key[ch])


KEY = {'o': 1, 'S': 2, 's': 3, 'd': 4, 'H': 5, 'h': 6, 'l': 7,
       'W': 8, 'w': 9, 'v': 10, 'B': 11, 'b': 12, 'n': 13,
       'R': 14, 'r': 15, 'q': 16, 'K': 17, 'k': 18, 'G': 19, 'g': 20, 'x': 21}

# ---------------------------------------------------------------- queue de cheval (arrière)
poly([(33, 7), (36, 3), (40, 3), (43, 6), (45, 11), (45, 19), (44, 26), (46, 33), (45, 37),
      (42, 33), (41, 25), (41, 16), (39, 10), (35, 9)], 6)
poly([(42, 6), (45, 11), (45, 19), (44, 26), (46, 33), (45, 37), (43, 30), (43, 15)], 5)
line([(36, 4), (40, 5), (42, 9), (42, 14)], 7)
line([(43, 18), (42, 27)], 7, only=[6])

# ---------------------------------------------------------------- hakama
HAK = [(21, 43), (39, 43), (42, 58), (45, 72), (48, 87), (46, 89), (33, 89), (31, 82), (29, 89),
       (15, 89), (13, 87), (16, 72), (19, 58)]
poly(HAK, 12)
# grand pan d'ombre côté droit
poly([(36, 43), (39, 43), (42, 58), (45, 72), (48, 87), (46, 89), (42, 89), (40, 70), (38, 55)], 13)
# bord éclairé côté gauche
poly([(21, 43), (22, 43), (18, 62), (15, 80), (14, 89), (13, 87), (16, 72), (19, 58)], 11)
# plis : arête claire + creux sombre, même pente
for (x0, y0), (x1, y1) in [((25, 45), (18, 88)), ((28, 46), (24, 88)), ((31, 46), (30, 80)),
                           ((34, 46), (37, 88)), ((37, 52), (42, 88))]:
    line([(x0 - 1, y0), (x1 - 1, y1)], 11, only=[12])
    line([(x0, y0), (x1, y1)], 13)
line([(31, 80), (31, 84)], 13)
# ourlet
line([(15, 88), (29, 88)], 13, only=[12, 11])
line([(33, 88), (46, 88)], 13, only=[12])
# himo (lien du hakama) + noeud
line([(21, 43), (39, 43)], 11)
line([(21, 44), (39, 44)], 12)
patch(26, 43, ["bBb.", "Bbnb", ".bn.", ".bb."], KEY)

# ---------------------------------------------------------------- pieds (tabi + zori)
patch(15, 89, [
    "..wWWWw.",
    ".wWWWWWw",
    "WWrWWWwv",
    "xxxxxxxx",
], KEY)
patch(32, 89, [
    "...wWWWw..",
    "..wWWWWWw.",
    ".WWrWWWWwv",
    "xxxxxxxxxx",
], KEY)

# ---------------------------------------------------------------- torse (kimono blanc)
poly([(22, 24), (26, 22), (32, 22), (37, 24), (39, 27), (38, 40), (22, 40), (21, 28)], 8)
poly([(33, 24), (37, 24), (39, 27), (38, 40), (34, 40), (35, 31)], 9)
line([(37, 30), (37, 40)], 10)
# peau du décolleté
poly([(27, 22), (31, 22), (29, 27)], 3)
put(30, 22, 4); put(30, 23, 4)
# col : sous-col rouge (juban) + revers blancs
line([(26, 22), (29, 28)], 15)
line([(32, 22), (29, 28)], 15)
line([(31, 23), (30, 25)], 14)
line([(33, 23), (25, 39)], 10)      # bord du revers supérieur
line([(26, 23), (29, 31)], 9)
line([(24, 30), (24, 37)], 9)       # pli de poitrine

# ---------------------------------------------------------------- saya (fourreau)
poly([(36, 42), (38, 41), (59, 57), (58, 60), (35, 44)], 18)
line([(38, 42), (58, 57)], 17)
line([(36, 44), (57, 60)], 1)
poly([(56, 56), (59, 57), (59, 60), (56, 59)], 20)  # kojiri
put(57, 57, 19)
# sageo (cordon) qui pend
line([(38, 44), (39, 47), (41, 48), (42, 46)], 15)
put(39, 46, 14); put(40, 47, 14)

# ---------------------------------------------------------------- obi
poly([(22, 39), (38, 39), (38, 43), (22, 43)], 15)
line([(22, 39), (38, 39)], 14)
line([(34, 40), (38, 40)], 16, only=[15])
line([(22, 42), (38, 42)], 16)
put(37, 41, 16)

# ---------------------------------------------------------------- bras droit (côté gauche image)
# haut du bras + grande manche qui pend
poly([(22, 24), (19, 26), (17, 31), (15, 38), (14, 44), (16, 48), (21, 49), (26, 47), (28, 42),
      (24, 36), (24, 29)], 8)
line([(24, 28), (23, 34)], 9)              # aisselle
line([(19, 28), (17, 35)], 9, only=[8])    # ombre externe douce
# avant-bras qui traverse vers la poignée
poly([(18, 35), (23, 34), (29, 36), (29, 40), (23, 40), (18, 39)], 8)
line([(23, 33), (28, 35)], 9)              # bord supérieur sur le torse
# manche sous l'avant-bras
poly([(15, 41), (19, 41), (24, 41), (28, 42), (26, 47), (21, 49), (16, 48), (14, 44)], 9)
line([(18, 40), (28, 41)], 10)             # pli sous l'avant-bras
poly([(26, 42), (28, 42), (27, 46), (25, 47)], 10)   # ouverture de manche
line([(16, 48), (21, 49), (25, 47)], 10)
line([(17, 43), (20, 47)], 10)

# ---------------------------------------------------------------- katana : tsuka + tsuba
poly([(22, 31), (24, 30), (36, 39), (35, 42)], 18)
for k in range(0, 13, 2):
    put(23 + k, 31 + (k * 3) // 4, 8)
for k in range(1, 13, 2):
    put(23 + k, 32 + (k * 3) // 4, 17)
patch(21, 29, [".g.", "gGg", ".gg"], KEY)     # kashira
poly([(35, 39), (37, 38), (38, 41), (37, 44), (35, 44), (34, 42)], 20)
put(36, 39, 19); put(35, 40, 19); put(37, 43, 18)

# main droite sur la poignée (poing, pouce par-dessus)
patch(29, 34, [
    "..sS..",
    ".sSSs.",
    "sSSSSs",
    "sSSssd",
    "dsdsd.",
    ".dd...",
], KEY)

# ---------------------------------------------------------------- bras gauche (côté droit image)
poly([(36, 24), (40, 25), (42, 29), (43, 37), (46, 46), (45, 50), (39, 50), (37, 44), (36, 34)], 8)
poly([(40, 27), (42, 29), (43, 37), (46, 46), (45, 50), (42, 49), (41, 38)], 9)
line([(36, 28), (37, 46)], 10)             # séparation bras / torse
line([(40, 49), (45, 49)], 10)
line([(44, 42), (45, 47)], 10)
put(39, 47, 10); put(38, 47, 10)            # ouverture de manche
# main gauche
patch(38, 48, [
    ".ss..",
    "sSSs.",
    "sSSsd",
    "sSssd",
    ".Ssdd",
    ".sd.d",
    "..d..",
], KEY)

# ---------------------------------------------------------------- cou
poly([(27, 20), (30, 20), (30, 23), (27, 23)], 3)
line([(30, 20), (30, 23)], 4)

# ---------------------------------------------------------------- tête (patch dessiné à la main)
HEAD = [
    "......ooooo......",   # y7
    "....ooHhhhhoo....",
    "...oHhhlllhhhoo..",
    "..oHhllhhhhhhhHo.",
    "..oHhlhhhhhhhhHHo",
    ".oHhHhhhhhhhhhHHo",
    ".ohHShHSShhhhHHHo",
    ".oSHSSHHHShhhhHHo",   # sourcils
    ".oSoSSoooohshhHHo",   # cils
    ".oShSSolWShdhhHHo",   # yeux
    "oSSSsSSSSshdhhHHo",   # nez
    ".oSsSSSSSshshhHo.",
    ".oSdsSSSSsdhhHo..",   # bouche
    "..oSSSSSsddhHo...",
    "...ossssddohho...",
    "....oooddddoo....",
]
patch(20, 7, HEAD, KEY)
for p in [(26, 9), (27, 9), (28, 8), (24, 11), (25, 10)]:
    put(*p, 7)
for p in [(29, 10), (30, 9), (31, 9), (27, 11), (28, 11)]:
    put(*p, 5)

# ---------------------------------------------------------------- lien rouge de la queue
patch(33, 6, ["rR", "qr"], KEY)

# ---------------------------------------------------------------- ombres portées finales
line([(17, 50), (22, 51), (26, 49)], 13, only=[11, 12])
line([(18, 51), (22, 52)], 13, only=[11, 12])
for x in (17, 22, 28, 35, 40):
    put(x, 87, 11) if G[87][x] in (12,) else None

# ---------------------------------------------------------------- contour automatique
def outline():
    add = []
    for y in range(H):
        for x in range(W):
            if G[y][x] == 0:
                for dx, dy in ((1, 0), (-1, 0), (0, 1), (0, -1)):
                    nx, ny = x + dx, y + dy
                    if 0 <= nx < W and 0 <= ny < H and G[ny][nx] not in (0, 1):
                        add.append((x, y))
                        break
    for x, y in add:
        G[y][x] = 1


outline()


def save():
    img = Image.new('RGBA', (W, H), (0, 0, 0, 0))
    used = set()
    for y in range(H):
        for x in range(W):
            c = G[y][x]
            if c:
                img.putpixel((x, y), PAL[c] + (255,))
                used.add(c)
    img.save(os.path.join(OUT, 'final.png'))
    img.resize((W * 6, H * 6), Image.NEAREST).save(os.path.join(OUT, 'final_x6.png'))
    print('couleurs utilisées :', len(used))


save()
