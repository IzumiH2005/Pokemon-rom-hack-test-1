# Render a map layout (or a whole tileset's metatiles) to PNG using the real game data.
import sys, struct, json, os
from PIL import Image
ROOT='/home/user/pokeemeraude-expansion'
def pal(path):
    L=open(path).read().split('\n')[3:19]
    return [tuple(int(x)//8*8 for x in l.split()) for l in L]  # GBA 15-bit
def tiles(path):
    im=Image.open(path); w,h=im.size; px=im.load(); out=[]
    for ty in range(h//8):
        for tx in range(w//8):
            out.append([[px[tx*8+x,ty*8+y]&15 for x in range(8)] for y in range(8)])
    return out
def u16s(path):
    d=open(path,'rb').read(); return list(struct.unpack('<%dH'%(len(d)//2),d))
class TS:
    def __init__(s,prim,sec):
        P=ROOT+'/data/tilesets/primary/'+prim; S=ROOT+'/data/tilesets/secondary/'+sec
        s.pals=[pal(f'{P}/palettes/{i:02d}.pal') for i in range(6)]+[pal(f'{S}/palettes/{i:02d}.pal') for i in range(6,13)]
        s.tiles=tiles(P+'/tiles.png'); s.tiles+= [[[0]*8]*8]*(512-len(s.tiles)); s.tiles+=tiles(S+'/tiles.png')
        s.mt=u16s(P+'/metatiles.bin'); s.mt+=[0]*(512*8-len(s.mt)); s.mt+=u16s(S+'/metatiles.bin')
    def draw(s,img,mid,ox,oy):
        px=img.load()
        for layer in (0,1):
            for q in range(4):
                if (mid*8+layer*4+q)>=len(s.mt): return
                e=s.mt[mid*8+layer*4+q]; t=e&0x3ff; hf=e>>10&1; vf=e>>11&1; p=e>>12
                tile=s.tiles[t] if t<len(s.tiles) else [[0]*8]*8
                bx=ox+(q%2)*8; by=oy+(q//2)*8
                for y in range(8):
                    for x in range(8):
                        c=tile[7-y if vf else y][7-x if hf else x]
                        if c==0 and layer==1: continue
                        col=s.pals[p][c] if c else s.pals[0][0]
                        px[bx+x,by+y]=col
def render_layout(name,out,scale=1,grid=False):
    L=[l for l in json.load(open(ROOT+'/data/layouts/layouts.json'))['layouts'] if l.get('name')==name][0]
    def tsdir(n):
        import re
        g=open(ROOT+'/src/data/tilesets/graphics.h').read()+open(ROOT+'/src/graphics.c').read()
        base=n.replace('gTileset_','')
        m=re.search(r'gTilesetTiles_%s\[\] = INCGFX_U32\("data/tilesets/(\w+)/(\w+)/'%base,g); return m.group(2)
    ts=TS(tsdir(L['primary_tileset']),tsdir(L['secondary_tileset']))
    w,h=L['width'],L['height']; blocks=u16s(ROOT+'/'+L['blockdata_filepath'])
    img=Image.new('RGB',(w*16,h*16))
    for i,b in enumerate(blocks): ts.draw(img,b&0x3ff,(i%w)*16,(i//w)*16)
    if scale>1: img=img.resize((w*16*scale,h*16*scale),Image.NEAREST)
    img.save(out)
def render_tileset(prim,sec,out,start=512,count=None,cols=8,scale=2):
    from PIL import ImageDraw
    ts=TS(prim,sec); n=count or (len(ts.mt)//8-start)
    rows=(n+cols-1)//cols; img=Image.new('RGB',(cols*16,rows*16),(255,0,255))
    for i in range(n): ts.draw(img,start+i,(i%cols)*16,(i//cols)*16)
    img=img.resize((cols*16*scale,rows*16*scale),Image.NEAREST); d=ImageDraw.Draw(img)
    for i in range(n): d.text(((i%cols)*16*scale+1,(i//cols)*16*scale),'%X'%(start+i),fill=(255,0,0))
    img.save(out)
if __name__=='__main__':
    if sys.argv[1]=='layout': render_layout(sys.argv[2],sys.argv[3],int(sys.argv[4]) if len(sys.argv)>4 else 1)
    else: render_tileset(sys.argv[2],sys.argv[3],sys.argv[4],int(sys.argv[5],0) if len(sys.argv)>5 else 512, int(sys.argv[6]) if len(sys.argv)>6 else None)
