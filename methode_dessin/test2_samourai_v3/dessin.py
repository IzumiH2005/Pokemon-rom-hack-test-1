"""Samourai v3 - 128x192. Chaque piece = un polygone decide a la main (R3).
Les ombres sont aussi des formes decidees a la main (regle [T1]) : le script ne fait que remplir."""
from base import *
import numpy as np

# ---------------- palette (rampes : clair, moyen, ombre, ombre profonde, contour)
PAL = dict(
 peau=[(255,226,200),(242,196,166),(214,148,128),(170,100,100),(118,60,72)],
 blanc=[(252,250,244),(228,228,236),(186,186,210),(136,134,172),(80,76,116)],
 rouge=[(236,92,72),(198,52,56),(140,30,50),(100,20,42),(70,14,34)],
 indigo=[(98,112,178),(64,76,138),(44,50,104),(30,32,72),(18,18,44)],
 chev=[(128,102,160),(78,62,110),(50,38,78),(34,26,56),(22,16,38)],
 laque=[(124,112,146),(64,54,78),(40,34,52),(26,22,36),(14,12,22)],
 or_=[(250,214,120),(222,170,70),(160,108,40),(110,70,30),(70,44,24)],
 tsuka=[(110,120,150),(70,78,104),(46,50,72),(32,34,52),(18,18,30)],
 paille=[(236,214,160),(206,176,118),(160,128,84),(120,92,64),(80,60,44)],
 oeil=[(250,250,250),(110,84,140),(60,40,90),(34,22,52),(22,14,34)],
)
def col(m, i): return PAL[m][i] + (255,)

class Toile:
    def __init__(s):
        s.img = Image.new("RGBA", (W, H), (0, 0, 0, 0))
        s.mat = np.full((H, W), -1, int)       # id de piece par pixel (pour le contour)
        s.mats = []
    def piece(s, pts, m, i=1):
        """Remplit un polygone (forme decidee a la main) ; enregistre la piece."""
        mask = Image.new("L", (W, H), 0); ImageDraw.Draw(mask).polygon(pts, fill=255)
        a = np.array(mask) > 0
        s.mats.append(m); pid = len(s.mats) - 1
        s.mat[a] = pid
        s._paint(a, col(m, i)); return pid
    def forme(s, pts, m, i, dans=None):
        """Forme d'ombre/lumiere : polygone remplissant seulement la piece 'dans'."""
        mask = Image.new("L", (W, H), 0); ImageDraw.Draw(mask).polygon(pts, fill=255)
        a = np.array(mask) > 0
        if dans is not None: a &= dans
        s._paint(a, col(m, i)); return a
    def px(s, lst, m, i):
        for x, y in lst: s.img.putpixel((x, y), col(m, i))
    def _paint(s, a, c):
        arr = np.array(s.img); arr[a] = c; s.img = Image.fromarray(arr)

T = Toile()
A = {}  # masques des pieces
# ---- ordre de profondeur : du fond vers l'avant
# queue de cheval (derriere tout)
A['queue'] = T.piece([(72,7),(74,3),(79,1),(84,2),(88,6),(90,14),(91,26),(93,38),(96,48),(98,58),(98,66),
                      (95,73),(96,65),(94,61),(92,68),(91,60),(89,56),(87,62),(87,52),(85,42),(81,32),(78,22),(75,14)], 'chev')
# fourreau (saya) : sort de la hanche proche vers l'arriere, legere courbure
A['saya'] = T.piece([(78,93),(81,96),(92,108),(102,121),(110,133),(115,143),(113,146),(107,137),(99,125),(89,112),(77,100)], 'laque')
# hakama
A['hakama'] = T.piece([(47,82),(77,79),(80,92),(83,108),(86,124),(89,142),(92,160),(95,176),(91,179),(86,177),
                      (82,180),(77,178),(72,180),(66,178),(64,181),(58,179),(54,181),(48,179),(43,181),(38,178),
                      (34,180),(28,178),(31,160),(35,142),(39,124),(42,106),(45,92)], 'indigo')
# pieds (devant le bas du hakama)
A['zori_loin'] = T.piece([(29,184),(46,184),(47,186),(28,186)], 'paille')
A['zori_pres'] = T.piece([(47,185),(66,185),(67,187),(46,187)], 'paille')
A['pied_loin'] = T.piece([(36,178),(45,178),(46,182),(45,184),(33,184),(31,183),(32,181)], 'blanc')
A['pied_pres'] = T.piece([(54,179),(64,179),(66,183),(65,185),(51,185),(48,184),(50,182)], 'blanc')
# bras loin : avant-bras nu (brachio-radial haut dehors, flechisseurs plus bas dedans)
A['avb_loin'] = T.piece([(37,70),(43,70),(44,76),(45,82),(46,88),(46,94),(45,100),(45,104),(40,104),(39,100),
                        (37,95),(35,89),(34,83),(34,77)], 'peau')
A['main_loin'] = T.piece([(40,102),(45,102),(47,105),(48,110),(48,115),(47,119),(45,121),(43,121),(41,119),
                         (41,116),(40,112),(40,106)], 'peau')
A['pouce_loin'] = T.piece([(40,105),(38,107),(37,111),(38,114),(40,115),(41,112)], 'peau')
# haut du kimono avec manches relevees (tasuki)
A['kimono'] = T.piece([(55,37),(48,40),(43,42),(39,45),(37,50),(36,57),(35,64),(36,71),(44,72),(46,66),(47,60),
                      (48,70),(48,80),(76,78),(77,70),(77,60),(81,66),(86,73),(93,71),(92,63),(89,54),(86,48),
                      (81,44),(73,41),(65,37)], 'blanc')
A['tasuki_l'] = T.piece([(47,41),(50,41),(47,52),(47,57),(45,57),(45,52)], 'rouge')
A['tasuki_p'] = T.piece([(71,41),(74,41),(79,51),(80,57),(78,57),(76,51)], 'rouge')
# ceinture (obi) et sangle du hakama
A['obi'] = T.piece([(47,76),(76,73),(77,80),(47,83)], 'rouge')
A['himo'] = T.piece([(47,81),(77,78),(77,82),(47,85)], 'indigo', 3)
# bras proche : avant-bras nu, coude en pointe (olecrane)
A['avb_pres'] = T.piece([(86,70),(92,70),(95,74),(96,78),(95,82),(93,86),(90,89),(88,92),(82,92),(82,88),(83,83),
                        (84,78),(85,74)], 'peau')
# poignee (tsuka) devant le ventre, garde (tsuba), main qui tient le fourreau
A['tsuka'] = T.piece([(56,77),(59,75),(76,92),(73,95)], 'tsuka')
A['tsuba'] = T.piece([(72,97),(73,95),(78,90),(80,91),(79,93),(74,98)], 'or_')
A['main_pres'] = T.piece([(82,91),(87,91),(89,95),(89,100),(87,104),(84,106),(81,105),(80,102),(79,99),(77,97),
                         (78,95),(81,95)], 'peau')
A['kashira'] = T.piece([(55,77),(56,75),(58,74),(59,76),(57,78)], 'or_', 2)
# cou : part de derriere la machoire (sous l'oreille), penche vers l'avant
A['cou'] = T.piece([(57,32),(63,30),(66,29),(68,32),(68,38),(65,41),(56,41),(56,36)], 'peau')
# encolure en V (peau visible) : dessinee par-dessus le kimono
A['col_v'] = T.piece([(55,38),(66,38),(60,51)], 'peau')
# tete 3/4 gauche : front, creux de l'orbite, pommette, nez qui depasse, levres, menton ;
# machoire qui remonte vers l'oreille
A['tete'] = T.piece([(52,11),(56,8),(63,7),(69,9),(72,14),(73,20),(72,25),(69,28),(66,29),(64,30),(62,32),(58,33),
                    (55,33),(53,32),(52,30),(51,29),(51,28),(50,27),(49,26),(50,25),(50,23),(51,22),(51,21),
                    (50,20),(50,18),(51,14)], 'peau')
A['oreille'] = T.piece([(66,20),(68,19),(70,20),(70,25),(68,27),(66,26)], 'peau')
# cheveux tires en arriere : calotte + frange en meches + meche devant l'oreille
A['cheveux'] = T.piece([(51,15),(50,13),(50,10),(53,7),(58,5),(64,4),(69,4),(73,6),(76,9),(76,15),(75,21),
                       (74,26),(72,29),(70,30),(71,26),(71,20),(70,18),(66,18),(65,22),(64,22),(64,17),(62,14),
                       (59,13),(56,13),(53,14)], 'chev')
# deux meches libres sur le front (epaisseurs differentes, pointes fines)
A['meche_f1'] = T.piece([(53,13),(56,13),(55,16),(53,19),(54,16)], 'chev')
A['meche_f2'] = T.piece([(57,13),(59,13),(59,16),(58,18),(58,15)], 'chev')
A['meche'] = T.piece([(63,15),(66,16),(66,21),(65,25),(63,29),(64,24),(63,20)], 'chev')
A['lien'] = T.piece([(70,6),(73,3),(75,5),(72,9)], 'rouge')
A['ruban'] = T.piece([(74,7),(77,8),(79,13),(78,16),(76,11)], 'rouge', 2)
def V(n): return T.mat == A[n]
def ligne(p0, p1):
    """Pixels d'une ligne 1 px (Bresenham)."""
    (x0, y0), (x1, y1) = p0, p1; pts = []
    dx, dy = abs(x1-x0), -abs(y1-y0); sx, sy = (1 if x0 < x1 else -1), (1 if y0 < y1 else -1); e = dx + dy
    while True:
        pts.append((x0, y0))
        if (x0, y0) == (x1, y1): return pts
        e2 = 2*e
        if e2 >= dy: e += dy; x0 += sx
        if e2 <= dx: e += dx; y0 += sy
def trait(pts, m, i, dans=None):
    """Polyligne a la main, limitee a une piece visible."""
    for a, b in zip(pts, pts[1:]):
        for x, y in ligne(a, b):
            if dans is None or dans[y, x]: T.img.putpixel((x, y), col(m, i))
FLATS = T.img.copy()

def ombres():
    k = V('kimono')
    T.forme([(70,50),(77,52),(78,62),(77,79),(69,79),(71,70),(70,60)], 'blanc', 2, k)          # flanc proche (plan de cote)
    T.forme([(52,62),(58,64),(64,64),(70,62),(70,65),(64,67),(57,67),(52,65)], 'blanc', 2, k)   # sous la poitrine
    T.forme([(44,47),(48,43),(48,60),(46,66),(44,72),(42,72),(43,60)], 'blanc', 2, k)          # manche loin, cote interieur
    T.forme([(79,52),(86,56),(92,64),(93,71),(86,73),(81,66),(78,60)], 'blanc', 2, k)          # manche proche, dessous
    T.forme([(40,46),(46,41),(53,39),(50,42),(44,44),(41,49)], 'blanc', 0, k)                  # haut epaule loin
    T.forme([(72,41),(81,44),(87,49),(84,49),(78,46),(71,43)], 'blanc', 0, k)                  # haut epaule proche
    for f in [[(36,58),(40,57),(44,59)], [(36,65),(40,63),(43,64)], [(37,69),(41,68),(44,70)],      # plis du tasuki
              [(83,55),(87,58),(89,62)], [(84,63),(88,66),(91,67)]]:
        trait(f, 'blanc', 3, k)
    trait([(61,51),(57,63),(53,75)], 'blanc', 3, k)                                             # bord du pan croise
    trait([(60,52),(56,64),(52,75)], 'blanc', 2, k)
    for f in [[(58,77),(61,70)], [(66,76),(67,69)], [(72,76),(73,70)]]: trait(f, 'blanc', 2, k)  # plis rentres dans l'obi
    trait([(48,42),(46,52)], 'rouge', 0, V('tasuki_l')); trait([(72,42),(77,51)], 'rouge', 0, V('tasuki_p'))
    # hakama
    h = V('hakama')
    T.forme([(71,84),(77,82),(80,92),(84,110),(88,130),(92,150),(96,177),(85,179),(83,150),(79,120),(75,100)], 'indigo', 2, h)
    T.forme([(46,85),(77,82),(77,84),(46,88)], 'indigo', 2, h)                                  # ombre portee de la sangle
    for pl in [[(52,88),(48,120),(44,152),(43,178)], [(58,87),(56,128)], [(56,140),(54,179)],
               [(64,86),(64,118),(65,150),(66,178)], [(70,85),(73,126),(77,160),(77,178)], [(46,126),(39,170),(38,178)]]:
        trait(pl, 'indigo', 3, h)
    for hl in [[(51,96),(47,124),(44,146)], [(57,100),(55,124)], [(63,104),(63,124),(64,140)], [(69,100),(72,130),(75,150)]]:
        trait(hl, 'indigo', 0, h)                                                               # bord eclaire de chaque pli, plus court
    T.px([(43,179),(54,180),(66,179),(77,179),(38,178)], 'indigo', 3)                           # encoches de l'ourlet
    trait([(50,98),(47,118),(45,132)], 'indigo', 0, h)                                         # genou loin qui tend le tissu
    trait([(45,134),(42,140)], 'indigo', 0, h)
    trait([(47,140),(44,150),(43,160)], 'indigo', 2, h)                                        # tissu qui retombe sous le genou
    trait([(66,96),(67,118),(68,134)], 'indigo', 0, h)                                         # jambe d'appui, tendue
    T.forme([(68,100),(82,100),(84,108),(72,108)], 'indigo', 2, h)                              # ombre portee main + saya
    # peau : avant-bras loin (lumiere a gauche) : ombre propre a droite, brachio-radial eclaire en haut dehors
    b = V('avb_loin')
    T.forme([(42,72),(44,76),(46,84),(46,94),(45,104),(43,104),(43,96),(43,88),(42,80),(41,74)], 'peau', 2, b)
    T.forme([(34,70),(44,70),(44,72),(34,72)], 'peau', 2, b)                                    # ombre portee de la manche
    T.forme([(35,77),(37,74),(38,80),(38,88),(37,90),(35,86)], 'peau', 0, b)
    trait([(39,75),(40,84),(41,92)], 'peau', 2, b)                                              # separation brachio-radial / flechisseurs
    m = V('main_loin')
    T.forme([(46,103),(48,110),(48,115),(47,119),(45,121),(45,112)], 'peau', 2, m)             # tranche de la main, ombre
    trait([(41,111),(44,111),(47,112)], 'peau', 2, m)                                         # arc des jointures
    trait([(43,113),(43,119)], 'peau', 2, m); trait([(45,113),(46,118)], 'peau', 3, m)        # doigts plies
    T.px([(42,120),(43,121),(44,121)], 'peau', 2)                                             # bouts des doigts replies
    T.px([(42,104),(42,105),(43,106)], 'peau', 0)                                             # dos de la main eclaire
    pv = V('pouce_loin'); trait([(41,106),(41,113)], 'peau', 3, pv); T.px([(38,109),(38,110)], 'peau', 0)
    # pieds : separation du gros orteil, lanieres rouges, ombre du hakama
    T.px([(34,181),(34,182),(51,182),(51,183)], 'blanc', 3)
    T.px([(35,183),(36,182),(37,183),(52,184),(53,183),(54,184)], 'rouge', 1)
    T.forme([(30,178),(46,178),(46,180),(30,180)], 'blanc', 2, V('pied_loin'))
    T.forme([(48,179),(66,179),(66,181),(48,181)], 'blanc', 2, V('pied_pres'))
    for z in ('zori_loin', 'zori_pres'): T.forme([(20,186),(70,186),(70,190),(20,190)], 'paille', 2, V(z))
    # avant-bras proche : dessus eclaire, dessous dans l'ombre
    b = V('avb_pres')
    T.forme([(96,77),(96,81),(93,86),(90,89),(88,92),(85,92),(88,88),(92,83),(93,77)], 'peau', 2, b)   # dessous (ombre propre)
    T.forme([(86,70),(92,70),(92,72),(86,72)], 'peau', 2, b)                                        # ombre de la manche
    T.forme([(85,73),(88,73),(87,78),(85,82),(84,80)], 'peau', 0, b)                                 # masse des extenseurs eclairee
    trait([(89,75),(88,80),(86,86)], 'peau', 2, b)                                                   # separation des muscles
    m = V('main_pres')
    T.forme([(89,97),(89,100),(87,104),(84,106),(81,105),(84,103),(87,100)], 'peau', 2, m)          # doigts sous le fourreau
    trait([(88,97),(86,101),(83,103)], 'peau', 2, m)                                                 # arc des jointures
    T.px([(84,93),(85,94),(86,95)], 'peau', 0)                                                       # dos de la main
    T.px([(79,96),(80,97)], 'peau', 0)                                                               # pouce sur la garde
    # cou : dessous de la machoire et plan de cote dans l'ombre, sterno-cleido-mastoidien
    c = V('cou')
    T.forme([(56,32),(66,29),(68,32),(68,40),(64,41),(64,36),(60,34),(56,34)], 'peau', 2, c)
    trait([(64,34),(61,38),(60,40)], 'peau', 2, c)
    T.forme([(55,38),(66,38),(64,40),(57,40)], 'peau', 2, V('col_v'))                         # ombre portee du col
    # visage : majoritairement eclaire
    t = V('tete')
    T.px([(55,17),(56,14),(59,17),(52,15),(53,15)], 'peau', 2)                                  # ombre portee des meches / ligne des cheveux
    T.forme([(60,29),(65,27),(66,29),(63,31),(59,32)], 'peau', 2, t)                         # dessous de la machoire
    T.px([(52,23),(53,23),(51,24),(54,31),(53,30)], 'peau', 0)
    T.forme([(66,20),(70,20),(70,25),(68,27),(66,26)], 'peau', 1, V('oreille'))
    T.px([(67,21),(67,22),(68,23),(67,24),(67,25)], 'peau', 2)
    # cheveux tires vers le point d'attache G=(72,7) : meches qui convergent, reflet en arc decoupe
    hc = V('cheveux')
    T.forme([(64,4),(73,6),(76,9),(76,15),(75,21),(74,26),(72,29),(70,30),(71,20),(70,14),(68,10)], 'chev', 2, hc)  # arriere du crane
    T.forme([(71,22),(75,21),(74,26),(72,29),(70,30)], 'chev', 3, hc)                              # nuque, sous l'attache
    for x0, y0, x1, y1 in [(51,12,54,9),(54,12,58,8),(58,11,62,8),(62,10,66,8)]:                   # reflet : tirets dans le sens des meches
        trait([(x0,y0),(x1,y1)], 'chev', 0, hc)
    for f in [[(52,14),(60,10),(71,7)], [(56,13),(63,10),(71,8)], [(60,13),(66,11),(72,9)], [(63,16),(67,13),(72,10)]]:
        trait(f, 'chev', 2, hc)                                                                    # separations de meches vers G
    for n in ('meche_f1', 'meche_f2', 'meche'):
        m = V(n); T.forme([(50,10),(70,10),(70,30),(50,30)], 'chev', 2, m)
        T.forme([(50,10),(70,10),(70,17),(50,17)], 'chev', 1, m)                                    # racine claire, pointe sombre
    # queue : epaisse a l'attache, se separe en 3 pointes ; ombre et traits dans le sens des cheveux
    q = V('queue')
    T.forme([(86,4),(90,14),(91,26),(93,38),(96,48),(98,58),(98,66),(95,73),(92,60),(90,46),(88,30),(83,12)], 'chev', 2, q)
    T.forme([(92,36),(96,48),(98,58),(98,66),(96,62),(93,50)], 'chev', 3, q)
    T.forme([(74,4),(79,2),(84,3),(80,4),(76,6)], 'chev', 0, q)                                    # reflet sur la courbe du haut
    trait([(78,10),(80,20)], 'chev', 0, q); trait([(82,30),(85,38)], 'chev', 0, q)
    for f in [[(77,6),(81,22),(85,38),(88,50),(88,60)], [(82,5),(86,22),(89,36),(92,48),(93,62)],
              [(86,8),(89,24),(92,38),(95,50),(96,64)]]:
        trait(f, 'chev', 3, q)
    # fourreau, poignee, garde
    sv = V('saya'); trait([(80,95),(91,107),(101,119),(109,131),(114,142)], 'laque', 0, sv)
    tv = V('tsuka')
    for i in range(0, 20, 3):
        x, y = 58 + i * 0.85, 77 + i * 0.85
        T.px([(round(x), round(y))], 'tsuka', 0)
    T.px([(74,94),(75,95),(76,94)], 'or_', 3)

def contours():
    """Selout : bord exterieur en ton 4 (ton 3 cote lumiere = haut/gauche) ;
    bord interieur seulement quand le contraste entre deux pieces est faible."""
    arr = np.array(T.img); mat = T.mat
    lum = lambda c: 0.3*c[0] + 0.59*c[1] + 0.11*c[2]
    out = arr.copy()
    for y in range(H):
        for x in range(W):
            p = mat[y, x]
            if p < 0: continue
            m = T.mats[p]
            for dx, dy in ((1,0),(-1,0),(0,1),(0,-1)):
                nx, ny = x+dx, y+dy
                q = mat[ny, nx] if 0 <= nx < W and 0 <= ny < H else -1
                if q == p: continue
                if q < 0:
                    out[y, x] = col(m, 3 if (dx < 0 or dy < 0) else 4); break
                if q < p and T.mats[q] != m and abs(lum(PAL[m][1]) - lum(PAL[T.mats[q]][1])) < 60:
                    out[y, x] = col(m, 3); break
    T.img = Image.fromarray(out)

def visage():
    """Traits du visage, places pixel par pixel (apres le contour)."""
    D, IR, IC, BL = col('oeil', 4), col('oeil', 2), col('oeil', 1), col('oeil', 0)
    put = lambda pts, c: [T.img.putpixel(p, c) for p in pts]
    put([(56,19),(57,19),(58,19),(59,19),(60,20)], col('chev', 3))       # sourcil proche
    put([(52,19),(53,19),(54,19)], col('chev', 3))                        # sourcil loin (raccourci)
    put([(56,21),(57,21),(58,21),(59,21),(60,21),(61,21),(61,22),(62,21)], D)  # paupiere haute + cil
    put([(57,22)], BL); put([(58,22),(57,23),(58,23)], IR); put([(57,24),(58,24)], IC)  # iris (regard a gauche)
    put([(56,22),(59,22),(60,22),(56,23),(59,23)], BL); put([(60,23),(56,24),(59,24)], col('peau', 1))
    put([(57,25),(58,25)], col('peau', 2))                                # paupiere basse
    put([(52,21),(53,21),(54,21)], D)                                     # oeil loin
    put([(52,22),(52,23)], IR); put([(53,22)], BL); put([(53,23)], IC); put([(52,24),(53,24)], col('peau', 2))
    put([(52,27)], col('peau', 2))                                        # narine / ombre du nez
    put([(52,29),(53,29)], col('peau', 3)); put([(54,29)], col('peau', 2))  # bouche
    put([(55,27),(56,27),(57,27),(56,26)], (240,172,156,255))             # joue
if __name__ == "__main__":
    on_bg(up(FLATS)).save(f"{OUT}/etape_07_couleurs_plates.png")
    ombres(); on_bg(up(T.img)).save(f"{OUT}/etape_08_lumiere.png")
    contours(); on_bg(up(T.img)).save(f"{OUT}/etape_06b_contour.png")
    visage()
    T.img.save(f"{OUT}/travail.png")
