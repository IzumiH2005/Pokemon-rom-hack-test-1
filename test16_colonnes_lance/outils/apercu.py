# aperçu : reconstruit la carte depuis les fichiers GBA + collisions en rouge
import struct, numpy as np
from PIL import Image
G='/home/user/pokeemeraude-expansion/data/tilesets/'
J=G+'primary/colonnes_lance/'
L='/home/user/pokeemeraude-expansion/data/layouts/ColonnesLance/'
t1=np.array(Image.open(J+'tiles.png')); t2=np.array(Image.open(G+'secondary/colonnes_lance/tiles.png'))
t1=np.vstack([t1,np.zeros((640//16*8-t1.shape[0],128),np.uint8)]); ti=np.vstack([t1,t2])
pals=[]
for i in range(13):
    l=open(J+f'palettes/{i:02d}.pal').read().splitlines()[3:19]
    pals.append([tuple(map(int,x.split())) for x in l])
mt=open(J+'metatiles.bin','rb').read()
blk=open(L+'map.bin','rb').read()
W,H=34,57
out=np.zeros((H*16,W*16,3),np.uint8); col=np.zeros((H*16,W*16),bool)
def tile(e):
    n=e&0x3ff; a=ti[(n//16)*8:(n//16)*8+8,(n%16)*8:(n%16)*8+8]
    if e>>10&1: a=a[:,::-1]
    if e>>11&1: a=a[::-1]
    return a, e>>12
for i in range(W*H):
    v=struct.unpack_from('<H',blk,2*i)[0]; m=v&0x3ff; x,y=i%W,i//W
    E=struct.unpack_from('<8H',mt,16*m)
    for L_ in (0,1):
        for k in range(4):
            a,p=tile(E[L_*4+k]); ox,oy=x*16+(k%2)*8,y*16+(k//2)*8
            P=np.array(pals[p],np.uint8); msk=a>0
            out[oy:oy+8,ox:ox+8][msk]=P[a[msk]]
    if v>>10&3: col[y*16:y*16+16,x*16:x*16+16]=True
Image.fromarray(out).save('apercu_gba.png')
o=out.copy().astype(float); o[col]=o[col]*0.55+np.array([255,0,0])*0.45
c=np.zeros((H*16,W*16*2+16,3),np.uint8); c[:,:W*16]=out; c[:,W*16+16:]=o.astype(np.uint8); Image.fromarray(c).save('apercu_double.png')
