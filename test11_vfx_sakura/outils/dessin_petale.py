import sys
from PIL import Image
PAL=[(115,197,164),(150,40,90),(232,104,152),(255,170,204),(255,236,244),(204,72,132),(255,204,226)]+[(0,0,0)]*9
F0="""................
................
................
................
.........55.55..
........544631..
.......5466331..
......54663321..
......5463321...
......533221....
......522211....
.......1111.....
................
................
................
................"""
f0=[[0 if c=='.' else int(c) for c in r] for r in F0.split('\n')]
assert len(f0)==16 and all(len(r)==16 for r in f0)
CX,CY=9.0,7.5
def squash(src,s,back=False):
    out=[[0]*16 for _ in range(16)]
    for y in range(16):
        for x in range(16):
            p=((x+.5-CX)+(y+.5-CY))/2   # composante perpendiculaire a l'axe
            k=p*(1/s-1)
            sx,sy=int(round(x+.5+k-.5)),int(round(y+.5+k-.5))
            if 0<=sx<16 and 0<=sy<16: out[y][x]=src[sy][sx]
    # contours recalculés
    filled=[[c!=0 for c in r] for r in out]
    for y in range(16):
        for x in range(16):
            if not filled[y][x]: continue
            def e(a,b): return not(0<=a<16 and 0<=b<16) or not filled[b][a]
            if e(x+1,y) or e(x,y+1): out[y][x]=1
            elif e(x-1,y) or e(x,y-1): out[y][x]=5
            elif back: out[y][x]={4:3,6:3,3:2,2:5}.get(out[y][x],out[y][x])
    return out
f1=squash(f0,0.72); f2=squash(f0,0.4); f3=squash(f0,0.72,True)
fr=[f0,f1,f2,f3]
for g in fr: print('\n'.join(''.join('.' if c==0 else str(c) for c in r) for r in g)); print()
im=Image.new('P',(16,64)); im.putpalette([v for c in PAL for v in c]+[0]*(768-48)); px=im.load()
for f,g in enumerate(fr):
    for y in range(16):
        for x in range(16): px[x,f*16+y]=g[y][x]
im.save(sys.argv[1])
Z=12; v=Image.new('RGB',(4*(16*Z+8)+8+280, 16*Z+16),(40,40,48))
b=Image.new('RGB',(64,48),(240,200,215))
for f in range(4):
    c=im.crop((0,f*16,16,f*16+16)); m=Image.new('L',(16,16)); m.putdata([0 if p==0 else 255 for p in c.get_flattened_data()])
    bg=Image.new('RGB',(16,16),(232,248,208)); bg.paste(c.convert('RGB'),(0,0),m)
    v.paste(bg.resize((16*Z,16*Z),Image.NEAREST),(8+f*(16*Z+8),8))
    b.paste(c.convert('RGB'),(f*16,8),m); b.paste(c.convert('RGB').transpose(Image.FLIP_LEFT_RIGHT),(f*16,26),m.transpose(Image.FLIP_LEFT_RIGHT))
v.paste(b.resize((256,192),Image.NEAREST),(4*(16*Z+8)+16,8))
v.save(sys.argv[2])
