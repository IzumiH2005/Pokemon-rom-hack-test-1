import struct
from nitro import *
def s32(d,o): return struct.unpack_from('<i',d,o)[0]
def sx(v,b): v&=(1<<b)-1; return v-(1<<b) if v>>(b-1) else v
NPAR={0x10:1,0x11:0,0x12:1,0x13:1,0x14:1,0x15:0,0x16:16,0x17:12,0x18:16,0x19:12,0x1A:9,0x1B:3,0x1C:3,
      0x20:1,0x21:1,0x22:1,0x23:2,0x24:1,0x25:1,0x26:1,0x27:1,0x28:1,0x29:1,0x2A:1,0x2B:1,
      0x30:1,0x31:1,0x32:1,0x33:1,0x34:32,0x40:1,0x41:0,0x50:1,0x60:1,0x70:3,0x71:2,0x72:1,0x00:0}

def dl(d,o,n):
    """Exécute une display list GX ; renvoie des polygones [(sommets[(x,y,z)], uvs[(s,t)], cols)]"""
    end=o+n; polys=[]; cur=None; mode=0; v=[0,0,0]; uv=(0,0); col=(255,255,255)
    def emit(p):
        if cur is not None: cur.append((tuple(p),uv,col))
    while o+4<=end:
        cmds=d[o:o+4]; o+=4
        for c in cmds:
            if c not in NPAR: raise ValueError(hex(c))
            pr=[u32(d,o+4*i) for i in range(NPAR[c])]; o+=4*NPAR[c]
            if c==0x40:
                mode=pr[0]&3; cur=[]
            elif c==0x41:
                if cur: polys.append((mode,cur))
                cur=None
            elif c==0x22: uv=(sx(pr[0],16)/16,sx(pr[0]>>16,16)/16)
            elif c==0x20: col=((pr[0]&31)*8,((pr[0]>>5)&31)*8,((pr[0]>>10)&31)*8)
            elif c==0x23: v=[sx(pr[0],16)/4096,sx(pr[0]>>16,16)/4096,sx(pr[1],16)/4096]; emit(v)
            elif c==0x24: v=[sx(pr[0],10)/64,sx(pr[0]>>10,10)/64,sx(pr[0]>>20,10)/64]; emit(v)
            elif c==0x25: v=[sx(pr[0],16)/4096,sx(pr[0]>>16,16)/4096,v[2]]; emit(v)
            elif c==0x26: v=[sx(pr[0],16)/4096,v[1],sx(pr[0]>>16,16)/4096]; emit(v)
            elif c==0x27: v=[v[0],sx(pr[0],16)/4096,sx(pr[0]>>16,16)/4096]; emit(v)
            elif c==0x28: v=[v[0]+sx(pr[0],10)/4096,v[1]+sx(pr[0]>>10,10)/4096,v[2]+sx(pr[0]>>20,10)/4096]; emit(v)
    # triangulation
    tris=[]
    for mode,vs in polys:
        if mode==0: tris+= [vs[i:i+3] for i in range(0,len(vs)-2,3)]
        elif mode==1:
            for i in range(0,len(vs)-3,4): a,b,c_,e=vs[i:i+4]; tris+=[[a,b,c_],[a,c_,e]]
        elif mode==2: tris+=[vs[i:i+3] for i in range(len(vs)-2)]
        elif mode==3:
            for i in range(0,len(vs)-3,2): a,b,c_,e=vs[i:i+4]; tris+=[[a,b,e],[a,e,c_]]
    return tris

def modele(d):
    S=sections(d); m0=S[b'MDL0']
    out=[]
    for nm,o in dico(d,m0+8):
        m=m0+u32(d,o)
        ofsSbc,ofsMat,ofsShp=u32(d,m+4),u32(d,m+8),u32(d,m+12)
        posScale=s32(d,m+0x14+8)/4096
        # matériaux
        mb=m+ofsMat
        mats=[]
        for mn,mo in dico(d,mb+4):
            a=mb+u32(d,mo)
            tip=u32(d,a+0x14); flag=u16(d,a+0x1E); ow,oh=u16(d,a+0x20),u16(d,a+0x22)
            sc=(1,1)
            if flag&1 and not flag&2: sc=(s32(d,a+0x2C)/4096,s32(d,a+0x30)/4096)
            mats.append(dict(nom=mn,tip=tip,flag=flag,w=ow,h=oh,sc=sc,tex=None,pal=None,alpha=(u32(d,a+0xC)>>16)&31))
        for tn,to in dico(d,mb+u16(d,mb)):
            lo,n=u16(d,to),d[to+2]
            for i in range(n): mats[d[mb+lo+i]]['tex']=tn
        for pn,po in dico(d,mb+u16(d,mb+2)):
            lo,n=u16(d,po),d[po+2]
            for i in range(n): mats[d[mb+lo+i]]['pal']=pn
        # formes
        sb=m+ofsShp; shps=[]
        for sn,so in dico(d,sb):
            a=sb+u32(d,so)
            shps.append(dl(d,a+u32(d,a+8),u32(d,a+12)))
        # SBC : associe matériau -> forme
        o=m+ofsSbc; curmat=0; paires=[]
        while True:
            c=d[o]; op=c&0x1f
            if op==1: break
            if op==4: curmat=d[o+1]; o+=2
            elif op==5: paires.append((curmat,d[o+1])); o+=2
            elif op==0: o+=1
            elif op==2: o+=3
            elif op==3: o+=2
            elif op==6: o+=4+(1 if c in (0x26,0x46) else 2 if c==0x66 else 0)
            elif op in (7,8): o+=2
            elif op==9: n=d[o+2]; o+=3+3*n
            elif op==0xB: o+=1
            elif op in (0xC,0xD): o+=3
            else: raise ValueError(hex(c))
        out.append(dict(nom=nm,posScale=posScale,mats=mats,shps=shps,paires=paires))
    return out
