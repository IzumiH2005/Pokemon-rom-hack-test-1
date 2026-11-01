from PIL import Image
H='0123456789abcdef'
PAL=[(115,197,164),(255,224,200),(246,190,156),(214,146,120),(123,65,65),
     (238,228,190),(206,186,132),(128,100,64),(236,196,82),(168,122,40),
     (52,190,182),(30,96,156),(58,48,72),(184,190,206),(248,248,248),(16,14,24)]
def grid(rows,start):
    g=[[0]*16 for _ in range(32)]
    for i,r in enumerate(rows):
        assert len(r)==16,(start+i,r,len(r))
        for x,ch in enumerate(r): g[start+i][x]=0 if ch in '.' else H.index(ch)
    return g
def shift(g): return [[0]*16]+[r[:] for r in g[:31]]
def over(g,rows,start):
    g=[r[:] for r in g]
    for i,r in enumerate(rows):
        assert len(r)==16,(start+i,r,len(r))
        for x,ch in enumerate(r):
            if ch=='?': continue
            g[start+i][x]=0 if ch=='.' else H.index(ch)
    return g
def sheet(frames):
    im=Image.new('P',(16*len(frames),32),0)
    flat=[]
    for c in PAL: flat+=list(c)
    im.putpalette(flat+[0]*(768-len(flat)))
    px=im.load()
    for f,g in enumerate(frames):
        for y in range(32):
            for x in range(16): px[f*16+x,y]=g[y][x]
    return im
def preview(im,scale=8,bg=(200,230,200),crop=None):
    im=im.convert('RGB') if crop is None else im.crop(crop).convert('RGB')
    px=im.load()
    for y in range(im.size[1]):
        for x in range(im.size[0]):
            if px[x,y]==PAL[0]: px[x,y]=bg
    return im.resize((im.size[0]*scale,im.size[1]*scale),Image.NEAREST)
