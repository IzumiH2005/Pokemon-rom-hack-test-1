# Planche de construction : têtes chauves (Loomis + proportions anime) à 0°, 25° et 45°.
import numpy as np
from PIL import Image, ImageDraw
from vec import masque
from tete import Tete
PEAU = {'1': (255, 236, 218), '2': (250, 204, 178), '3': (230, 146, 146), '4': (150, 66, 96), 'O': (30, 26, 56)}

def chauve(lacet, S=96):
    T = Tete(50, 36, 24, lacet=lacet)
    G = np.full((S, S), '.', dtype='<U1')
    cou = masque(T.cou(98), S); G[cou] = '2'
    vis = masque(T.contour(), S); G[vis] = '1'
    cote = masque(T.plan_cote(1), S) & vis; G[cote] = '2'                 # plan de côté à l'ombre
    # ombre du menton sur le cou : le contour du visage décalé vers le bas
    sous = np.zeros_like(vis)
    for d in range(1, 5): sous |= np.roll(vis, d, 0)
    G[cou & ~vis & sous] = '3'
    G[vis & ~np.roll(vis, -1, 0) & cou] = '4'                              # trait chaud du menton
    ore = masque(T.oreille(1), S)
    if T.tourne((.86, 0, -.12))[2] > -.2:                                   # oreille proche
        G[ore & (G != '.')] = '2'
        bord = ore & ~(np.roll(ore, 1, 0) & np.roll(ore, -1, 0) & np.roll(ore, 1, 1) & np.roll(ore, -1, 1))
        G[bord & (G != '.')] = '4'
    plein = G != '.'
    tour = plein & ~(np.roll(plein, 1, 0) & np.roll(plein, -1, 0) & np.roll(plein, 1, 1) & np.roll(plein, -1, 1))
    G[tour] = 'O'
    return T, G

def image(lacet, guides, k=4, S=96):
    T, G = chauve(lacet, S)
    im = np.full((S, S, 3), 236, np.uint8)
    for c, rgb in PEAU.items(): im[G == c] = rgb
    img = Image.fromarray(im).resize((S * k, S * k), Image.NEAREST)
    if guides:
        d = ImageDraw.Draw(img); s = S / 100 * k
        col = {'cercle': (120, 120, 120), 'axe': (40, 110, 220), 'sourcils': (130, 130, 130), 'yeux': (220, 40, 40),
               'nez': (30, 150, 60), 'bouche': (210, 120, 0)}
        for nom, c in T.guides().items():
            vis = [(p[0] * s, p[1] * s) for p in c if p[2] > -.02 or nom.startswith('mach') or nom == 'cercle']
            if len(vis) > 1: d.line(vis, fill=col.get(nom, (150, 0, 150)), width=2)
        for sgn in (-1, 1):
            (x, y), f = T.regard(sgn)
            d.ellipse([(x - 7 * f) * s, (y - 4) * s, (x + 7 * f) * s, (y + 5) * s], outline=(220, 40, 40), width=2)
    return img

if __name__ == '__main__':
    W = Image.new('RGB', (3 * 384, 2 * 384), (255, 255, 255))
    for i, a in enumerate((0, 25, 45)):
        W.paste(image(a, True), (i * 384, 0)); W.paste(image(a, False), (i * 384, 384))
    W.save('construction_tete.png')
