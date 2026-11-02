# Image complète de la carte (512x512, palette de la carte) -> tuiles map.png + map.bin
# Garde l'ordre des tuiles d'origine et ajoute les nouvelles à la fin (max 256 : fond affine 8bpp).
import sys
from PIL import Image
full=Image.open(sys.argv[1]); old=Image.open(sys.argv[2]); n_old=int(sys.argv[3])
def tb(im,x,y): return im.crop((x,y,x+8,y+8)).tobytes()
tiles=[tb(old,(i%16)*8,(i//16)*8) for i in range(n_old)]
idx={}
for i,t in enumerate(tiles): idx.setdefault(t,i)
out=bytearray()
for ty in range(64):
    for tx in range(64):
        t=tb(full,tx*8,ty*8)
        if t not in idx:
            idx[t]=len(tiles); tiles.append(t)
        out.append(idx[t])
assert len(tiles)<=256, len(tiles)
rows=(len(tiles)+15)//16
im=Image.new('P',(128,rows*8)); im.putpalette(old.getpalette())
for i,t in enumerate(tiles):
    im.paste(Image.frombytes('P',(8,8),t),((i%16)*8,(i//16)*8))
im.save(sys.argv[4]); open(sys.argv[5],'wb').write(out)
print('tuiles:',len(tiles))
