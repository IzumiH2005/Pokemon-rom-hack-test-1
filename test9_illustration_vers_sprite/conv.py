# Convertit une illustration en sprite de dresseur GBA : 64x64, 15 couleurs + transparent.
import sys, numpy as np
from PIL import Image, ImageDraw, ImageEnhance, ImageFilter
src, out = sys.argv[1], sys.argv[2]
opts = dict(a.split('=') for a in sys.argv[3:])
SAT = float(opts.get('sat', 1.25)); CON = float(opts.get('con', 1.15))
OUTL = int(opts.get('outline', 1)); NCOL = 15; SHARP = int(opts.get('sharp', 1))

im = Image.open(src).convert('RGB')
W, H = im.size
# 1) masque : fond blanc relie au bord
thr = Image.fromarray(((np.asarray(im).min(2) > 232) * 255).astype('uint8'))
fl = thr.copy()
for x in range(0, W, 7):
    for y in (0, H - 1):
        if fl.getpixel((x, y)) == 255: ImageDraw.floodfill(fl, (x, y), 128)
for y in range(0, H, 7):
    for x in (0, W - 1):
        if fl.getpixel((x, y)) == 255: ImageDraw.floodfill(fl, (x, y), 128)
mask = (np.asarray(fl) != 128).astype('float32')
ys, xs = np.nonzero(mask); x0, x1, y0, y1 = xs.min(), xs.max(), ys.min(), ys.max()
# 2) carre, personnage en bas au centre
side = max(x1 - x0, y1 - y0) + 1
cx = (x0 + x1) // 2
bx0 = cx - side // 2; by0 = y1 + 1 - side
rgb = np.asarray(im).astype('float32') / 255
def crop(a):
    pad = np.zeros((side, side) + a.shape[2:], 'float32')
    sx0, sy0 = max(bx0, 0), max(by0, 0); sx1, sy1 = min(bx0 + side, W), min(by0 + side, H)
    pad[sy0 - by0:sy1 - by0, sx0 - bx0:sx1 - bx0] = a[sy0:sy1, sx0:sx1]
    return pad
m = crop(mask); c = crop(rgb * mask[..., None])
def down(a):
    return np.asarray(Image.fromarray(a).resize((64, 64), Image.BOX)) if a.ndim == 2 else \
        np.stack([np.asarray(Image.fromarray(a[..., k]).resize((64, 64), Image.BOX)) for k in range(3)], 2)
md = down(m); cd = down(c) / np.maximum(md[..., None], 1e-4)
alpha = md > 0.5
img = Image.fromarray((np.clip(cd, 0, 1) * 255).astype('uint8'))
img = ImageEnhance.Color(img).enhance(SAT); img = ImageEnhance.Contrast(img).enhance(CON)
if SHARP: img = img.filter(ImageFilter.UnsharpMask(1, 60, 2))
A = np.asarray(img).copy()
# 3) contour noir sur le bord du masque
ncol = NCOL
if OUTL:
    e = alpha & ~(np.roll(alpha, 1, 0) & np.roll(alpha, -1, 0) & np.roll(alpha, 1, 1) & np.roll(alpha, -1, 1))
    ncol -= 1
else:
    e = np.zeros_like(alpha)
# 4) quantification des pixels opaques : k-means, les pixels non rouges comptent plus
pix = A[alpha & ~e].astype('float64')
red = (pix[:, 0] > pix[:, 1] * 1.6) & (pix[:, 0] > pix[:, 2] * 1.6)
w = np.where(red, 1.0, float(opts.get('wchar', 3)))
q = Image.fromarray(pix.astype('uint8').reshape(1, -1, 3)).quantize(ncol, method=Image.Quantize.MEDIANCUT, dither=Image.Dither.NONE)
pal = np.array(q.getpalette()[:ncol * 3], 'float64').reshape(-1, 3)
for it in range(30):
    lab = ((pix[:, None] - pal[None]) ** 2).sum(-1).argmin(1)
    for k in range(ncol):
        sel = lab == k
        if sel.any(): pal[k] = (pix[sel] * w[sel, None]).sum(0) / w[sel].sum()
pal = pal.round().astype(int)
if 'pal' in opts:  # palette choisie a la main
    pal = np.array([[int(v) for v in l.split()] for l in open(opts['pal']) if l.strip()])
    ncol = len(pal)
dd = A[..., None, :].astype(int) - pal[None, None]
rm = (A[..., 0:1].astype(int) + pal[None, None, :, 0]) / 2
d = (2 + rm / 256) * dd[..., 0] ** 2 + 4 * dd[..., 1] ** 2 + (2 + (255 - rm) / 256) * dd[..., 2] ** 2; idx = d.argmin(-1) + 1
full = [(115, 197, 164)] + [tuple(p) for p in pal]
if OUTL:
    full.append((16, 16, 24)); idx[e] = len(full) - 1
idx[~alpha] = 0
while len(full) < 16: full.append((0, 0, 0))
o = Image.new('P', (64, 64)); o.putpalette(sum(full, ()) + (0,) * (768 - 48)); o.putdata(idx.flatten().tolist())
o.save(out)
open(out[:-4] + '.pal', 'w', newline='').write('JASC-PAL\r\n0100\r\n16\r\n' + ''.join('%d %d %d\r\n' % p for p in full))
