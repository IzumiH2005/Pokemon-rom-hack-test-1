# Planches d'étapes et planche de contrôle final (étape 11) du test 4.
from PIL import Image, ImageDraw, ImageOps
from outils import *
import gemme, epee, champignon as ch

CLAIR, SOMBRE = (236, 232, 220, 255), (40, 44, 52, 255)

def planche(images, nom, k, titre_h=0):
    w = sum(im.width * k + 16 for im in images); h = max(im.height for im in images) * k
    out = Image.new('RGB', (w, h), (255, 255, 255)); x = 0
    for im in images:
        out.paste(im.resize((im.width * k, im.height * k), Image.NEAREST), (x, 0)); x += im.width * k + 16
    out.save(nom)

def etapes_gemme():
    G = gemme.G
    contour = [''.join(c if c == 'O' else '.' for c in r) for r in G]
    aplat = [''.join('O' if c == 'O' else ('3' if c != '.' else '.') for c in r) for r in G]
    ims = [rendre(gemme.SIL, {'#': (30, 30, 40)}, fond=CLAIR), rendre(contour, gemme.PAL, fond=CLAIR),
           rendre(aplat, gemme.PAL, fond=CLAIR), rendre(G, gemme.PAL, fond=CLAIR)]
    planche(ims, 'etapes_gemme.png', 12)

def etapes_epee():
    m = epee.construire(); G = epee.colorer(m)
    sil = [''.join('#' if c != '.' else '.' for c in r) for r in G]
    contour = [''.join(c if c in 'Oo' else '.' for c in r) for r in G]
    base = {'lame': '3', 'garde': 'q', 'poignee': 'l', 'pommeau': 'q'}
    aplat = [list(r) for r in contour]
    for (x, y), v in m.items(): aplat[y][x] = base[v]
    for (x, y) in [(9, 20), (10, 20), (9, 21), (10, 21)]: aplat[y][x] = 'h'
    pal = dict(epee.PAL, **{'#': (30, 30, 40)})
    ims = [rendre(sil, pal, fond=CLAIR), rendre(contour, pal, fond=CLAIR),
           rendre(chaine(aplat), pal, fond=CLAIR), rendre(G, pal, fond=CLAIR)]
    planche(ims, 'etapes_epee.png', 8)

def construction_champi():
    """Étape 2 : volumes et terminateur en couleurs de construction (absentes de l'image finale)."""
    k = 8; im = Image.new('RGB', (64 * k, 64 * k), (236, 232, 220)); d = ImageDraw.Draw(im)
    def ell(e, col, w=2):
        cx, cy, rx, ry = e; d.ellipse([(cx - rx + .5) * k, (cy - ry + .5) * k, (cx + rx + .5) * k, (cy + ry + .5) * k], outline=col, width=w)
    for i in range(65):
        d.line([(i * k, 0), (i * k, 64 * k)], fill=(222, 218, 206)); d.line([(0, i * k), (64 * k, i * k)], fill=(222, 218, 206))
    vert, bleu, rouge = (40, 160, 70), (40, 90, 220), (220, 40, 40)
    ell(ch.CHAPEAU_DOME, vert); ell(ch.CHAPEAU_BORD, vert); ell(ch.BULBE, vert); ell(ch.OMBRE, vert, 1)
    ell(ch.BEBE_CHAPEAU, vert); ell(ch.BEBE_BORD, vert)
    for y, x0, x1 in (ch.PIED[0], ch.PIED[-1]): d.line([(x0 * k, y * k), ((x1 + 1) * k, y * k)], fill=vert, width=2)
    d.line([(24 * k, 33 * k), (24 * k, 52 * k)], fill=vert, width=2); d.line([(41 * k, 33 * k), (41 * k, 52 * k)], fill=vert, width=2)
    ell(ch.CH_LUM, bleu); ell(ch.CH_DEMI, bleu); ell(ch.CH_ECLAT, bleu); ell(ch.OMBRE_SOUS_CHAPEAU, bleu, 1)
    d.line([(32.5 * k, 6 * k), (32.5 * k, 58 * k)], fill=rouge, width=2)          # axe de symétrie
    d.line([(4 * k, 4 * k), (14 * k, 12 * k)], fill=(240, 170, 0), width=4)       # direction de la lumière
    d.polygon([(14 * k, 12 * k), (10 * k, 12 * k), (13 * k, 9 * k)], fill=(240, 170, 0))
    for e in ch.TACHES: ell(e, (160, 60, 200), 1)
    im.save('etape_02_champi_volumes.png')

def etapes_champi():
    pal = dict(ch.PAL, **{'#': (30, 30, 40)})
    ims = [rendre(ch.dessiner(e), pal, fond=CLAIR) for e in (5, 6, 7, 8, 99)]
    planche(ims, 'etapes_champi.png', 4)

def controle():
    objets = [('gemme', gemme.G, gemme.PAL), ('epee', epee.colorer(epee.construire()), epee.PAL),
              ('champi', ch.dessiner(), ch.PAL)]
    lignes = []
    for nom, G, pal in objets:
        w = len(G[0]); k = {16: 4, 32: 2, 64: 1}[w]
        x1c = rendre(G, pal, fond=CLAIR); x1s = rendre(G, pal, fond=SOMBRE)
        vues = [x1c, rendre(G, pal, k=2, fond=CLAIR), rendre(G, pal, k=4 * k, fond=SOMBRE),
                gris(rendre(G, pal, k=4 * k, fond=CLAIR)),
                ImageOps.mirror(rendre(G, pal, k=4 * k, fond=CLAIR)),
                rendre([''.join('#' if c not in '.S' else '.' for c in r) for r in G], {'#': (20, 20, 28)}, k=4 * k, fond=CLAIR)]
        rendre(G, pal, nom='%s_%d.png' % (nom, w)); rendre(G, pal, nom='%s_%d_x8.png' % (nom, w), k=8 if w < 64 else 6)
        lignes.append(vues)
    # mise en situation : inventaire (gemme, épée, potion du test 3) et champignon sur une tuile d'herbe
    inv = Image.new('RGB', (3 * 40 + 8, 48), (58, 48, 66)); di = ImageDraw.Draw(inv)
    pot = Image.open('../test3_objets/potion_16.png').convert('RGBA')
    gem = rendre(gemme.G, gemme.PAL); sw = rendre(epee.colorer(epee.construire()), epee.PAL)
    for i, (im, s) in enumerate(((gem, 2), (sw, 1), (pot, 2))):
        x0 = 4 + i * 40; di.rectangle([x0, 4, x0 + 36, 40], fill=(92, 78, 104), outline=(150, 132, 160))
        im2 = im.resize((im.width * s, im.height * s), Image.NEAREST); inv.paste(im2, (x0 + 2, 6), im2)
    herbe = Image.new('RGB', (96, 80), (88, 146, 70)); dh = ImageDraw.Draw(herbe)
    for (x, y) in [(6, 10), (40, 6), (70, 18), (14, 60), (84, 66), (60, 70), (24, 34), (88, 40)]:
        dh.line([(x, y), (x + 1, y - 2)], fill=(122, 180, 84)); dh.line([(x + 2, y), (x + 3, y - 3)], fill=(122, 180, 84))
    champi = rendre(ch.dessiner(), ch.PAL); herbe.paste(champi, (16, 8), champi)
    # assemblage
    k_aff = 2
    W = 1500; H = sum(max(v.height for v in l) * 1 + 24 for l in lignes) + 200
    out = Image.new('RGB', (W, H), (255, 255, 255)); y = 0
    for vues in lignes:
        x = 0
        for v in vues: out.paste(v.convert('RGB') if v.mode != 'RGBA' else v, (x, y), v if v.mode == 'RGBA' else None); x += v.width + 16
        y += max(v.height for v in vues) + 24
    inv3 = inv.resize((inv.width * 3, inv.height * 3), Image.NEAREST); out.paste(inv3, (0, y))
    out.paste(herbe, (inv3.width + 30, y)); h2 = herbe.resize((192, 160), Image.NEAREST); out.paste(h2, (inv3.width + 30 + 96 + 20, y))
    out = out.crop((0, 0, W, y + max(inv3.height, 160) + 4)); out.save('etape_11_controle.png')

if __name__ == '__main__':
    vue(gemme.SIL, {'#': (30, 30, 40)}, 'etape_05_gemme_silhouette.png')
    etapes_gemme(); etapes_epee(); construction_champi(); etapes_champi(); controle()
