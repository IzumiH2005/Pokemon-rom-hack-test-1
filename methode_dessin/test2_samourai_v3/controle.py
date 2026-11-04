"""Etape 11 : tableau de controle + comparaison avec le test 1."""
from base import *
from PIL import ImageOps, ImageDraw
im = Image.open('travail.png').convert('RGBA')
im.save('final.png'); up(on_bg(im), 4).save('final_x4.png')
fond = on_bg(im).convert('RGB')
sil = Image.new('RGB', im.size, BG); sil.paste((20,20,20), mask=im.split()[3])
vues = [('x1', fond), ('miroir', ImageOps.mirror(fond)), ('silhouette', sil), ('gris', ImageOps.grayscale(fond).convert('RGB'))]
S2 = 3; pad = 12
board = Image.new('RGB', (pad + len(vues) * (W*S2 + pad), H*S2 + 2*pad + 14), (250,250,250))
d = ImageDraw.Draw(board)
for i, (n, v) in enumerate(vues):
    x = pad + i * (W*S2 + pad); board.paste(v.resize((W*S2, H*S2), Image.NEAREST), (x, pad + 14)); d.text((x, 2), n, fill=(0,0,0))
board.paste(fond, (board.width - W - 4, board.height - H - 4))   # vraie taille en coin
board.save('etape_11_controle.png')
# comparaison a la meme hauteur affichee (576 px)
refs = [('test 1 A (avec methode v1)', '../test1_samourai/A_avec_methode/final.png'),
        ('test 1 B (sans methode)', '../test1_samourai/B_sans_methode/final.png'),
        ('test 2 (methode v3)', 'final.png')]
HT = 576; ims = []
for n, f in refs:
    r = Image.open(f).convert('RGBA'); k = HT // r.height
    ims.append((n, on_bg(r).convert('RGB').resize((r.width*k, r.height*k), Image.NEAREST)))
cw = sum(i.width for _, i in ims) + pad * (len(ims) + 1)
comp = Image.new('RGB', (cw, HT + 2*pad + 14), (250,250,250)); d = ImageDraw.Draw(comp); x = pad
for n, i in ims:
    comp.paste(i, (x, pad + 14)); d.text((x, 2), n, fill=(0,0,0)); x += i.width + pad
comp.save('comparaison_test1_test2.png')
