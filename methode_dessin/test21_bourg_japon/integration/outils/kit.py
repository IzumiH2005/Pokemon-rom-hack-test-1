# Pixel-art toolkit: palettes + a canvas that stores palette color names.
import math, hashlib
from PIL import Image

# Secondary palettes (slots 6..12). Every color is a multiple of 8 so it maps exactly to GBA 15-bit.
PALS = {
 6: ['_', (24,28,40),(48,56,80),(72,88,112),(104,120,144),(152,168,184),
     (48,28,20),(88,56,32),(128,82,46),(176,120,72),(240,240,224),(208,200,176),
     (40,56,120),(80,104,176),(240,192,72),(128,128,120)],
 7: ['_', (248,240,248),(248,200,216),(240,160,184),(216,120,152),(168,80,112),(104,48,80),
     (112,72,48),(64,36,24),(72,160,120),(40,112,88),
     (184,224,112),(136,192,96),(88,148,64),(40,88,40),(24,56,24)],
 8: ['_', (248,248,248),(232,72,48),(192,40,24),(128,24,16),(24,24,24),
     (208,208,200),(168,168,160),(120,120,112),(72,72,64),
     (168,216,240),(80,144,208),(48,92,152),(240,136,40),(248,224,88),(88,160,72)],
 9: ['_', (232,208,160),(208,176,128),(176,144,96),(128,96,64),
     (240,240,232),(216,216,208),(184,184,176),(144,144,136),
     (160,208,192),(112,192,160),(64,176,128),(40,128,96),(104,136,64),(152,152,144),(96,96,88)],
 10:['_', (24,28,40),(48,56,80),(72,88,112),(120,136,160),
     (232,88,64),(184,40,32),(112,24,16),(240,240,224),(200,192,168),
     (56,36,24),(120,76,44),(248,216,88),(192,144,40),(232,224,200),(16,16,24)],
 11:['_', (24,28,40),(48,56,80),(72,88,112),(104,120,144),(152,168,184),
     (48,28,20),(88,56,32),(128,82,46),(176,120,72),(240,240,224),(208,200,176),
     (120,32,40),(184,64,72),(240,192,72),(128,128,120)],
}
# Friendly names -> (palette, index)
N = {}
def _n(p, names):
    for i, nm in enumerate(names.split(), 1): N[nm] = (p, i)
_n(6, 'R0 R1 R2 R3 R4 W0 W1 W2 W3 PL PS NO0 NO1 LAMP GR')
_n(7, 'SW S1 S2 S3 S4 SO TL TD SH1 SH2 B1 B2 B3 B4 B5')
_n(8, 'WH V1 V2 V3 BK T1 T2 T3 T4 A1 A2 A3 KOI GLOW LILY')
_n(9, 'D1 D2 D3 D4 G1 G2 G3 G4 GC GD GE GK MOSS SS1 SS2')
_n(10,'K0 K1 K2 K3 Q1 Q2 Q3 KP KS KW1 KW2 AU1 AU2 ROPE KBK')
_n(11,'r0 r1 r2 r3 r4 w0 w1 w2 w3 pl ps NR0 NR1 lamp gr')

def rgb(name): p, i = N[name]; return PALS[p][i]

def noise(x, y, seed=0):
    h = hashlib.md5(f'{x},{y},{seed}'.encode()).digest()
    return h[0] / 255.0

class Canvas:
    def __init__(s, w, h, fill=None):
        s.w, s.h = w, h; s.p = [[fill] * w for _ in range(h)]
    def get(s, x, y):
        return s.p[y][x] if 0 <= x < s.w and 0 <= y < s.h else None
    def set(s, x, y, c):
        if 0 <= x < s.w and 0 <= y < s.h: s.p[y][x] = c
    def rect(s, x0, y0, x1, y1, c):  # inclusive
        for y in range(y0, y1 + 1):
            for x in range(x0, x1 + 1): s.set(x, y, c)
    def hline(s, x0, x1, y, c): s.rect(x0, y, x1, y, c)
    def vline(s, x, y0, y1, c): s.rect(x, y0, x, y1, c)
    def ellipse(s, cx, cy, rx, ry, c):
        for y in range(int(cy - ry) - 1, int(cy + ry) + 2):
            for x in range(int(cx - rx) - 1, int(cx + rx) + 2):
                if ((x + .5 - cx) / rx) ** 2 + ((y + .5 - cy) / ry) ** 2 <= 1: s.set(x, y, c)
    def outline(s, c, only=None):
        new = []
        for y in range(s.h):
            for x in range(s.w):
                if s.p[y][x] is not None and (only is None or s.p[y][x] in only):
                    for dx, dy in ((1,0),(-1,0),(0,1),(0,-1)):
                        if s.get(x+dx, y+dy) is None:
                            new.append((x, y)); break
        for x, y in new: s.p[y][x] = c
    def paste(s, o, ox, oy):
        for y in range(o.h):
            for x in range(o.w):
                if o.p[y][x] is not None: s.set(ox + x, oy + y, o.p[y][x])
    def mirror(s):
        c = Canvas(s.w, s.h); c.p = [row[::-1] for row in s.p]; return c
    def crop(s, x, y, w, h):
        c = Canvas(w, h); c.p = [row[x:x+w] for row in s.p[y:y+h]]; return c
    def png(s, path, scale=4, bg=(112,192,160)):
        im = Image.new('RGB', (s.w, s.h), bg); px = im.load()
        for y in range(s.h):
            for x in range(s.w):
                if s.p[y][x]: px[x, y] = rgb(s.p[y][x])
        im.resize((s.w * scale, s.h * scale), Image.NEAREST).save(path)
