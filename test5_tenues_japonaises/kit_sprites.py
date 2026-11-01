from PIL import Image
R='/home/user/pokeemeraude-expansion/graphics/object_events/'
O='/tmp/claude-0/-home-user-Pokemon-rom-hack-test-1/1e190316-06ac-53a7-95a3-788b4028550e/scratchpad/ow/orig/people/'
H='0123456789abcdef'
def pal(name):
    L=open(R+'palettes/'+name+'.pal').read().split('\n')[3:19]
    return [tuple(map(int,l.split())) for l in L]
def load(png):
    im=Image.open(O+png+'.png'); px=im.load()
    return [[[px[f*16+x,y] for x in range(16)] for y in range(32)] for f in range(im.size[0]//16)], im
def apply(frame, start, rows, remap=None, upto=None):
    fr=[r[:] for r in frame]
    if remap:
        for y in range(upto if upto is not None else start):
            fr[y]=[remap.get(v,v) for v in fr[y]]
    for i,row in enumerate(rows):
        y=start+i
        assert len(row)==16,(row,len(row))
        for x,ch in enumerate(row):
            if ch=='?': continue
            fr[y][x]=0 if ch=='.' else H.index(ch)
    for y in range(start+len(rows),32): fr[y]=[0]*16
    return fr
def shift(fr):
    return [[0]*16]+[r[:] for r in fr[:31]]
def build(C):
    frames,im=load(C['src'])
    rm=C.get('remap')
    st={}
    for d,fi in (('down',0),('up',1),('left',2)):
        s,rows=C[d]
        st[d]=apply(frames[fi],s,rows,rm)
    out=[st['down'],st['up'],st['left']]
    for d in ('down','up','left'):
        for alt in C[d+'_w']:
            w=shift(st[d])
            for i,row in enumerate(alt):
                y=32-len(alt)+i
                for x,ch in enumerate(row):
                    if ch=='?': continue
                    w[y][x]=0 if ch=='.' else H.index(ch)
            out.append(w)
    new=Image.new('P',im.size,0); new.putpalette(im.getpalette())
    px=new.load()
    for f,fr in enumerate(out):
        for y in range(32):
            for x in range(16): px[f*16+x,y]=fr[y][x]
    return new
def preview(img,p,scale=5,bg=(200,230,200)):
    out=Image.new('RGB',img.size); px=img.load(); o=out.load()
    for y in range(img.size[1]):
        for x in range(img.size[0]):
            v=px[x,y]; o[x,y]=bg if v==0 else p[v]
    return out.resize((img.size[0]*scale,img.size[1]*scale),Image.NEAREST)
