from PIL import Image
H='0123456789abcdef'
PAL=[(115,197,164),(255,224,200),(240,182,152),(205,131,115),(123,70,66),
     (240,230,192),(210,188,132),(140,108,66),(238,198,84),(170,124,42),
     (56,192,184),(36,96,164),(54,46,70),(160,164,184),(248,248,248),(16,14,24)]
def load_txt(fn):
    rows=[l.rstrip('\n')[3:] for l in open(fn) if l[:2].strip().isdigit()]
    assert len(rows)==64 and all(len(r)==64 for r in rows),[len(r) for r in rows]
    return [[0 if c=='.' else H.index(c) for c in r] for r in rows]
def save_txt(g,fn):
    open(fn,'w').write(''.join('%2d '%y+''.join('.' if v==0 else H[v] for v in r)+'\n' for y,r in enumerate(g)))
def to_img(g):
    im=Image.new('P',(64,64)); flat=[c for p in PAL for c in p]
    im.putpalette(flat+[0]*(768-len(flat)))
    im.putdata([v for r in g for v in r]); return im
def prev(g,s=8,bg=(235,235,240)):
    im=to_img(g).convert('RGB'); px=im.load()
    for y in range(64):
        for x in range(64):
            if g[y][x]==0: px[x,y]=bg
    return im.resize((64*s,64*s),Image.NEAREST)
def write_pal(fn):
    open(fn,'w',newline='\r\n').write('JASC-PAL\n0100\n16\n'+''.join('%d %d %d\n'%c for c in PAL))
