# Rendu des 4 blocs des Colonnes Lance + colonnes posées, en projection oblique (K) façon GBA.
import struct, sys, numpy as np
from bmd import *
from PIL import Image
R='/home/user/refs/pokeplatinum/res/field/'
def jeu(d):
    T=tex0(d,sections(d)[b'TEX0']); return d,T,{t['nom']:t for t in T['texs']},{p['nom']:p for p in T['pals']}
SET=jeu(open(R+'mapmodels/texture_sets/map_texture_set_059.nsbtx','rb').read())
cache={}
def texture(J,mt):
    d,T,TX,PL=J; t0=mt['tip']>>29&1; k=(id(d),mt['tex'],mt['pal'],t0)
    if k not in cache:
        t=TX.get(mt['tex']); p=PL.get(mt['pal'])
        if t: t=dict(t,t0=t['t0']|t0)
        cache[k]=np.array(decode(d,T,t,p)).astype(np.float32) if t and (p or t['fmt']==7) else None
    return cache[k]
K=float(sys.argv[1]) if len(sys.argv)>1 else 0.0
PX=int(sys.argv[2]) if len(sys.argv)>2 else 1
MARGE=160
W=64*16*PX; H=(64*16+MARGE)*PX
img=np.zeros((H,W,3),np.float32); img[:]=(30,30,40); zb=np.full((H,W),-1e9,np.float32)
idb=np.full((H,W),-1,np.int32)
hb=np.full((H,W),-1e9,np.float32)
low=img.copy(); zl=np.full((H,W),-1e9,np.float32)
def wrap(q,n,rep,flip):
    q=np.floor(q).astype(int)
    if not rep: return np.clip(q,0,n-1)
    if flip:
        r=np.mod(q,2*n); return np.where(r<n,r,2*n-1-r)
    return np.mod(q,n)
def dessine(mo,J,ox,oz,oy=0,obj=-1):
    s=mo['posScale']
    for mi,si in mo['paires']:
        mt=mo['mats'][mi]; tx=texture(J,mt)
        if tx is None: tx=texture(SET,mt)
        for tri in mo['shps'][si]:
            P=np.array([v for v,_,_ in tri])*s
            if obj>=0 and P[:,1].max()<1.5: continue   # semelle plate d'un accessoire, cachée en jeu
            P[:,0]+=ox; P[:,2]+=oz; P[:,1]+=oy
            UV=np.array([u for _,u,_ in tri])
            X=(P[:,0]+256)*PX
            Y=(P[:,2]+256-P[:,1]*K+MARGE)*PX
            Z=P[:,1]+P[:,2]*K
            x0,x1=int(max(0,np.floor(X.min()))),int(min(W-1,np.ceil(X.max())))
            y0,y1=int(max(0,np.floor(Y.min()))),int(min(H-1,np.ceil(Y.max())))
            if x1<x0 or y1<y0: continue
            den=(Y[1]-Y[2])*(X[0]-X[2])+(X[2]-X[1])*(Y[0]-Y[2])
            if abs(den)<1e-9: continue
            gx,gy=np.meshgrid(np.arange(x0,x1+1)+.5,np.arange(y0,y1+1)+.5)
            l0=((Y[1]-Y[2])*(gx-X[2])+(X[2]-X[1])*(gy-Y[2]))/den
            l1=((Y[2]-Y[0])*(gx-X[2])+(X[0]-X[2])*(gy-Y[2]))/den
            l2=1-l0-l1
            m=(l0>=-1e-4)&(l1>=-1e-4)&(l2>=-1e-4)
            if not m.any(): continue
            z=l0*Z[0]+l1*Z[1]+l2*Z[2]
            hh=l0*P[0,1]+l1*P[1,1]+l2*P[2,1]
            if tx is None:
                c_=np.zeros(z.shape+(3,))+[200,0,200]; al=np.ones(z.shape)
            else:
                th,tw=tx.shape[:2]
                u=(l0*UV[0,0]+l1*UV[1,0]+l2*UV[2,0])*mt['sc'][0]
                v=(l0*UV[0,1]+l1*UV[1,1]+l2*UV[2,1])*mt['sc'][1]
                tip=mt['tip']
                ui=wrap(u,tw,tip>>16&1,tip>>18&1); vi=wrap(v,th,tip>>17&1,tip>>19&1)
                smp=tx[vi,ui]; c_=smp[...,:3]; al=smp[...,3]/255
            m&=al>0.5
            ml=m&(hh<=48.5); sl=zl[y0:y1+1,x0:x1+1]; ml&=z>=sl-1e-3
            sl[ml]=z[ml]; low[y0:y1+1,x0:x1+1][ml]=c_[ml]
            sub=zb[y0:y1+1,x0:x1+1]; m&=z>=sub-1e-3
            sub[m]=z[m]; img[y0:y1+1,x0:x1+1][m]=c_[m]; idb[y0:y1+1,x0:x1+1][m]=obj; hb[y0:y1+1,x0:x1+1][m]=hh[m]
props=[]
for k,(cx,cy) in zip(range(375,379),[(0,0),(1,0),(0,1),(1,1)]):
    d=open(R+f'mapmodels/data/map_data_{k}.bin','rb').read()
    a,b,c,e=struct.unpack_from('<4I',d)
    for mo in modele(d[16+a+b:16+a+b+c]): dessine(mo,SET,cx*512,cy*512)
    for i in range(b//48):
        v=struct.unpack_from('<i3i',d,16+a+i*48)
        props.append((v[0],v[1]/4096+cx*512,v[3]/4096+cy*512,v[2]/4096))
if '--sans' not in sys.argv:
  for i,(n,x,z,y) in enumerate(props):
    pd=open(R+f'props/models/prop_model_{n}.nsbmd','rb').read()
    J=jeu(pd)
    for mo in modele(pd): dessine(mo,J,x,z,y,i)
Image.fromarray(img.clip(0,255).astype(np.uint8)).save(f'rendu2_{K}_{PX}.png')
np.save(f'idb_{K}_{PX}.npy',idb); np.save(f'h_{K}_{PX}.npy',hb)
Image.fromarray(low.clip(0,255).astype(np.uint8)).save(f'bas_{K}_{PX}.png')
print(props)
