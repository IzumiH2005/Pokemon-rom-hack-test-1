#!/usr/bin/env python3
"""Mini atelier de pixel art pour sprites de dresseur GBA (64x64, 16 couleurs).
Etat : work.txt (64 lignes de 64 chiffres hex, '.'=transparent) + pal.txt.
  studio.py ed "<cmds>"     modifie (separateur ';'), sauvegarde l'historique, puis rend la vue
  studio.py view [zone] [ref]  rend view.png
  studio.py undo            revient a l'etape precedente
Commandes d'edition :
  p x y c            un pixel
  r y x0 chaine      une ligne de pixels a partir de x0 (espace ou '_' = ne pas toucher)
  f x0 y0 x1 y1 c    rectangle plein (bornes incluses)
  rep x0 y0 x1 y1 ab remplace la couleur a par b dans le rectangle
  map x0 y0 x1 y1 ab:cd:...  plusieurs remplacements a->b simultanes
Zones (vue) : x0,y0,x1,y1 ; ref : cle de REFS ou x0,y0,x1,y1 dans ref_a.png
"""
import sys, os, glob, shutil
from PIL import Image, ImageDraw, ImageFont
D = os.path.dirname(os.path.abspath(__file__))
H = '0123456789abcdef'
FONT = ImageFont.truetype('/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf', 10)
FONTB = ImageFont.truetype('/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf', 13)
BG = (32, 32, 40); FG = (230, 230, 230); PAPER = (226, 226, 234)
REFS = {  # zones de la reference (ref_a.png) pour chaque partie du corps
    'tete': (260, 20, 480, 240), 'buste': (180, 180, 560, 560), 'jambes': (190, 480, 560, 1300),
    'tout': (150, 0, 600, 1308), 'mains': (170, 380, 570, 720)}

def load_pal():
    return [tuple(int(v) for v in l.split()) for l in open(os.path.join(D, 'pal.txt')) if l.strip()]
def load(fn='work.txt'):
    return [list(l.rstrip('\n')) for l in open(os.path.join(D, fn))][:64]
def save(g, fn='work.txt'):
    open(os.path.join(D, fn), 'w').write('\n'.join(''.join(r) for r in g) + '\n')
def rgb(g, pal, bg=PAPER):
    im = Image.new('RGB', (64, 64), bg); px = im.load()
    for y in range(64):
        for x in range(64):
            c = g[y][x]
            if c not in '.0': px[x, y] = pal[H.index(c)]
    return im

def zoom_grid(g, pal, box, s, diff=None):
    x0, y0, x1, y1 = box; w, h = x1 - x0 + 1, y1 - y0 + 1
    im = rgb(g, pal).crop((x0, y0, x1 + 1, y1 + 1)).resize((w * s, h * s), Image.NEAREST)
    m = 16; out = Image.new('RGB', (w * s + m, h * s + m), BG); out.paste(im, (m, m)); d = ImageDraw.Draw(out)
    for i in range(w + 1):
        X = m + i * s; d.line((X, m, X, m + h * s), fill=(0, 0, 0) if (x0 + i) % 8 else (255, 60, 60), width=1)
    for j in range(h + 1):
        Y = m + j * s; d.line((m, Y, m + w * s, Y), fill=(0, 0, 0) if (y0 + j) % 8 else (255, 60, 60), width=1)
    for i in range(w):
        if (x0 + i) % 2 == 0: d.text((m + i * s + 1, 2), str((x0 + i) % 100), font=FONT, fill=FG)
    for j in range(h):
        if (y0 + j) % 2 == 0: d.text((0, m + j * s + 2), str(y0 + j), font=FONT, fill=FG)
    if diff:
        for (x, y) in diff:
            if x0 <= x <= x1 and y0 <= y <= y1:
                X, Y = m + (x - x0) * s, m + (y - y0) * s
                d.rectangle((X + 1, Y + 1, X + s - 1, Y + s - 1), outline=(255, 0, 255))
    return out

def battle(g, pal):
    bg = Image.new('RGB', (128, 96), (232, 248, 208)); d = ImageDraw.Draw(bg)
    d.ellipse((14, 62, 114, 90), fill=(200, 232, 160), outline=(176, 208, 120))
    sp = rgb(g, pal, bg=(1, 2, 3)); m = Image.new('L', (64, 64), 0); mp = m.load(); sx = sp.load()
    for y in range(64):
        for x in range(64):
            if sx[x, y] != (1, 2, 3): mp[x, y] = 255
    bg.paste(sp, (32, 12), m); return bg.resize((256, 192), Image.NEAREST)

def view(box=None, ref=None):
    pal = load_pal(); g = load()
    box = box or (0, 0, 63, 63)
    w, h = box[2] - box[0] + 1, box[3] - box[1] + 1
    s = max(6, min(26, 640 // max(w, h)))
    hist = sorted(glob.glob(os.path.join(D, 'hist', '*.txt')))
    diff = None
    if len(hist) >= 2:
        p = load(os.path.relpath(hist[-2], D)); diff = [(x, y) for y in range(64) for x in range(64) if p[y][x] != g[y][x]]
    z = zoom_grid(g, pal, box, s, diff)
    bs = max(3, s // 2); base = rgb(load('base.txt'), load_pal_base()).crop((box[0], box[1], box[2] + 1, box[3] + 1)).resize((w * bs, h * bs), Image.NEAREST)
    full = rgb(g, pal).resize((192, 192), Image.NEAREST)
    one = rgb(g, pal)
    bat = battle(g, pal)
    rb = REFS.get(ref, None) if ref else REFS['tout']
    if ref and ref not in REFS: rb = tuple(int(v) for v in ref.split(','))
    r = Image.open(os.path.join(D, 'ref_a.png')).convert('RGB').crop(rb)
    rh = z.height; r = r.resize((max(1, r.width * rh // r.height), rh), Image.LANCZOS)
    if r.width > 520: r = r.resize((520, r.height * 520 // r.width), Image.LANCZOS)
    W = r.width + z.width + 30 + max(256, base.width)
    Hh = max(z.height, r.height) + 40 + 200
    out = Image.new('RGB', (W, Hh), BG); d = ImageDraw.Draw(out)
    d.text((10, 6), 'Reference', font=FONTB, fill=FG); out.paste(r, (10, 26))
    X = r.width + 20; d.text((X, 6), 'Travail %s (zoom x%d, magenta = modifie)' % (str(box), s), font=FONTB, fill=FG); out.paste(z, (X, 26))
    X2 = X + z.width + 10
    d.text((X2, 6), 'Base (Pierre Rochard)', font=FONTB, fill=FG); out.paste(base, (X2, 26))
    Y = max(z.height, r.height) + 34
    out.paste(full, (10, Y)); out.paste(one, (212, Y)); out.paste(bat, (290, Y))
    pw = 18
    for i, c in enumerate(pal):
        d.rectangle((560 + (i % 8) * 34, Y + (i // 8) * 40, 560 + (i % 8) * 34 + pw, Y + (i // 8) * 40 + pw), fill=c, outline=(255, 255, 255))
        d.text((560 + (i % 8) * 34 + 4, Y + (i // 8) * 40 + 20), H[i], font=FONTB, fill=FG)
    out.save(os.path.join(D, 'view.png'))

def load_pal_base():
    return [tuple(int(v) for v in l.split()) for l in open(os.path.join(D, 'pal_base.txt')) if l.strip()]

def snapshot(g):
    os.makedirs(os.path.join(D, 'hist'), exist_ok=True)
    n = len(glob.glob(os.path.join(D, 'hist', '*.txt')))
    save(g, 'hist/%03d.txt' % n)

def ed(cmds):
    g = load()
    for c in cmds.split(';'):
        t = c.split()
        if not t: continue
        op = t[0]
        if op == 'p': g[int(t[2])][int(t[1])] = t[3]
        elif op == 'r':
            y, x0 = int(t[1]), int(t[2]); s = c.split(None, 3)[3]
            for i, ch in enumerate(s):
                if ch not in ' _': g[y][x0 + i] = ch
        elif op == 'f':
            x0, y0, x1, y1 = map(int, t[1:5])
            for y in range(y0, y1 + 1):
                for x in range(x0, x1 + 1): g[y][x] = t[5]
        elif op in ('rep', 'map'):
            x0, y0, x1, y1 = map(int, t[1:5]); M = dict((p[0], p[1]) for p in t[5].split(':'))
            for y in range(y0, y1 + 1):
                for x in range(x0, x1 + 1):
                    if g[y][x] in M: g[y][x] = M[g[y][x]]
        else: raise SystemExit('commande inconnue: ' + c)
    save(g); snapshot(g)

if __name__ == '__main__':
    a = sys.argv[1:]
    if a[0] == 'ed':
        ed(a[1]); a = ['view'] + a[2:]
    if a[0] == 'undo':
        hs = sorted(glob.glob(os.path.join(D, 'hist', '*.txt')))
        os.remove(hs[-1]); shutil.copy(hs[-2], os.path.join(D, 'work.txt')); a = ['view'] + a[1:]
    if a[0] == 'view':
        box = tuple(int(v) for v in a[1].split(',')) if len(a) > 1 and a[1] != '-' else None
        view(box, a[2] if len(a) > 2 else None)
