import struct
from PIL import Image
def u8(d,o): return d[o]
def u16(d,o): return struct.unpack_from('<H',d,o)[0]
def u32(d,o): return struct.unpack_from('<I',d,o)[0]

def dico(d,o):
    """Dictionnaire 3D Nitro : renvoie [(nom, offset_donnee)]"""
    n=d[o+1]
    p=o+u16(d,o+6)                      # saute le bloc inconnu
    ent=u16(d,p); dsz=u16(d,p+2)
    data=p+4
    names=p+dsz
    out=[]
    for i in range(n):
        nm=d[names+16*i:names+16*i+16].split(b'\0')[0].decode('latin1')
        out.append((nm,data+ent*i))
    return out

def sections(d):
    n=u16(d,0xE)
    return {d[u32(d,0x10+4*i):u32(d,0x10+4*i)+4]:u32(d,0x10+4*i) for i in range(n)}

def rgb555(c):
    return ((c&31)*255//31,((c>>5)&31)*255//31,((c>>10)&31)*255//31)

def tex0(d,b):
    texsz=u16(d,b+0xC)<<3; texinfo=u16(d,b+0xE); texdata=u32(d,b+0x14)
    ctexdata=u32(d,b+0x24); ctexinfo=u32(d,b+0x28)
    palinfo=u32(d,b+0x34); paldata=u32(d,b+0x38)
    texs=[]
    for nm,o in dico(d,b+texinfo):
        p=u32(d,o)
        texs.append(dict(nom=nm,off=(p&0xffff)<<3,w=8<<((p>>20)&7),h=8<<((p>>23)&7),fmt=(p>>26)&7,t0=(p>>29)&1,param=p))
    pals=[]
    for nm,o in dico(d,b+palinfo):
        pals.append(dict(nom=nm,off=u16(d,o)<<3))
    return dict(base=b,texdata=b+texdata,ctexdata=b+ctexdata,ctexinfo=b+ctexinfo,paldata=b+paldata,texs=texs,pals=pals)

def decode(d,T,t,pal):
    w,h,f=t['w'],t['h'],t['fmt']
    P=T['paldata']+pal['off']
    def col(i): return rgb555(u16(d,P+2*i))
    img=Image.new('RGBA',(w,h))
    px=img.load()
    if f==5:
        base=T['ctexdata']+t['off']
        ib=T['ctexinfo']+t['off']//2
        bw=w//4
        for by in range(h//4):
            for bx in range(bw):
                k=by*bw+bx
                bits=u32(d,base+4*k); info=u16(d,ib+2*k)
                po=P+((info&0x3fff)<<2); mode=info>>14
                c=[rgb555(u16(d,po+2*i)) for i in range(4)]
                a=[255]*4
                if mode==0: a[3]=0
                elif mode==1:
                    c[2]=tuple((c[0][j]+c[1][j])//2 for j in range(3)); a[3]=0
                elif mode==3:
                    c[2]=tuple((5*c[0][j]+3*c[1][j])//8 for j in range(3)); c[3]=tuple((3*c[0][j]+5*c[1][j])//8 for j in range(3))
                for yy in range(4):
                    for xx in range(4):
                        v=(bits>>(2*(yy*4+xx)))&3
                        px[bx*4+xx,by*4+yy]=c[v]+(a[v],)
        return img
    base=T['texdata']+t['off']
    for y in range(h):
        for x in range(w):
            i=y*w+x
            if f==1:
                v=d[base+i]; c=col(v&31); a=(v>>5)*255//7; px[x,y]=c+(a,)
            elif f==6:
                v=d[base+i]; c=col(v&7); a=(v>>3)*255//31; px[x,y]=c+(a,)
            elif f==2:
                v=(d[base+i//4]>>(2*(i%4)))&3; px[x,y]=col(v)+(0 if (v==0 and t['t0']) else 255,)
            elif f==3:
                v=(d[base+i//2]>>(4*(i%2)))&15; px[x,y]=col(v)+(0 if (v==0 and t['t0']) else 255,)
            elif f==4:
                v=d[base+i]; px[x,y]=col(v)+(0 if (v==0 and t['t0']) else 255,)
            elif f==7:
                v=u16(d,base+2*i); px[x,y]=rgb555(v)+((255 if v&0x8000 else 0),)
    return img
