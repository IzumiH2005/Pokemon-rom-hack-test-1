"""Apercu : remplit les '.' d'une grille par l'herbe primaire (meme motif que le jeu) -> png xK."""
import sys, json
from PIL import Image
prim = Image.open('/home/user/pokeemeraude-expansion/data/tilesets/primary/general/tiles.png').load()
def herbe(x, y):
    t = [[2, 3], [3, 2]][(y % 16) // 8][(x % 16) // 8]
    v = prim[(t % 16) * 8 + x % 8, (t // 16) * 8 + y % 8] & 15
    return {0xd: 'h', 0xe: 'i', 0xc: 'g'}.get(v, 'h')
src, dst, k = sys.argv[1], sys.argv[2], int(sys.argv[3])
pal = json.load(open(sys.argv[4] if len(sys.argv) > 4 else 'sol/palette.json'))
G = [l.rstrip('\n') for l in open(src) if l.strip()]
im = Image.new('RGB', (len(G[0]), len(G)))
for y, r in enumerate(G):
    for x, c in enumerate(r):
        c = herbe(x, y) if c == '.' else c
        im.putpixel((x, y), tuple(int(pal[c][i:i+2], 16) for i in (1, 3, 5)))
im.resize((im.width * k, im.height * k), Image.NEAREST).save(dst)
