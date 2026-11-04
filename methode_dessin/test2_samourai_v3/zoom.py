import sys
from base import *
from PIL import Image
f, x0, y0, x1, y1, s = sys.argv[1], *map(int, sys.argv[2:7])
im = Image.open(f).convert("RGBA")
if im.width > W: im = im.resize((W, H), Image.NEAREST)
c = on_bg(im.crop((x0, y0, x1, y1))).resize(((x1-x0)*s, (y1-y0)*s), Image.NEAREST)
d = ImageDraw.Draw(c)
for x in range(x0, x1):
    if x % 10 == 0: d.line([((x-x0)*s, 0), ((x-x0)*s, c.height)], fill=(255, 0, 255, 90)); d.text(((x-x0)*s+1, 1), str(x), fill=(200, 0, 200))
for y in range(y0, y1):
    if y % 10 == 0: d.line([(0, (y-y0)*s), (c.width, (y-y0)*s)], fill=(255, 0, 255, 90)); d.text((1, (y-y0)*s+1), str(y), fill=(200, 0, 200))
c.save(sys.argv[7])
