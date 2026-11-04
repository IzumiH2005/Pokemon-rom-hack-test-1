"""Conversion automatique illustration -> base TxT (128 par défaut) à retoucher.

Usage : python3 conv.py carre.png dossier_sortie [nb_couleurs] [taille]
Étapes : voile retiré, médiane + accentuation, réduction k-centroïde,
traits sombres extraits à part et reposés, palette k-means pondérée
(+ 2 rouges fixes), pixels isolés nettoyés. Sort auto.txt et palette.json.
"""
import sys, numpy as np
from PIL import Image, ImageFilter
SRC,O=sys.argv[1],sys.argv[2]
N=int(sys.argv[3]) if len(sys.argv)>3 else 14
T=int(sys.argv[4]) if len(sys.argv)>4 else 128
im=Image.open(SRC).convert('RGB')
I=np.asarray(im).astype(float)/255
# 1. enlever le voile (dark channel prior)
dark=np.asarray(Image.fromarray((I.min(2)*255).astype(np.uint8)).filter(ImageFilter.MinFilter(15))).astype(float)/255
A=np.array([0.98,0.97,0.98])
t=np.clip(1-0.45*dark/0.98,0.45,1)[...,None]
J=np.clip((I-A)/t+A,0,1)
# 2. niveaux + contraste local
lo,hi=np.percentile(J,1),np.percentile(J,99.5)
J=np.clip((J-lo)/(hi-lo),0,1)**0.95
pre=Image.fromarray((J*255).astype(np.uint8)).filter(ImageFilter.MedianFilter(7 if T<=128 else 5)).filter(ImageFilter.UnsharpMask(4,50,3))
pre.save(f'{O}/pre.png')
P=np.asarray(pre).astype(float)
# 3. réduction k-centroïde : couleur dominante de chaque case, traits sombres préservés
H=P.shape[0];out=np.zeros((T,T,3))
e=np.linspace(0,H,T+1).astype(int)
for y in range(T):
  for x in range(T):
    b=P[e[y]:e[y+1],e[x]:e[x+1]].reshape(-1,3)
    c=b[np.linspace(0,len(b)-1,3).astype(int)].copy()
    for _ in range(6):
      d=((b[:,None]-c[None])**2).sum(2);l=d.argmin(1)
      for k in range(3):
        if (l==k).any(): c[k]=b[l==k].mean(0)
    cnt=np.bincount(l,minlength=3);lum=c@[.3,.59,.11]
    k=cnt.argmax();kd=lum.argmin()
    if cnt[kd]>=0.3*len(b) and lum[k]-lum[kd]>70: k=kd
    out[y,x]=c[k]
Image.fromarray(out.astype(np.uint8)).save(f'{O}/kc.png')
# 3b. traits : pixels nettement plus sombres que leur voisinage dans l'original
g=np.asarray(im.convert('L')).astype(float)
gb=np.asarray(im.convert('L').filter(ImageFilter.GaussianBlur(5))).astype(float)
ln=((gb-g)>22)&(g<75)
LM=np.zeros((T,T),bool)
for y in range(T):
  for x in range(T):
    LM[y,x]=ln[e[y]:e[y+1],e[x]:e[x+1]].mean()>0.10
np.save(f'{O}/LM.npy',LM)
# 4. palette de N couleurs (k-means), fond à part
px=out.reshape(-1,3);bg=(px.min(1)>200)|((px[:,2]>px[:,0]+15)&(px.mean(1)>150))
fg=px[~bg];rng=np.random.default_rng(1)
K=N-3
U,W=np.unique((fg//8)*8+4,axis=0,return_counts=True);W=W**0.5
c=U[rng.choice(len(U),K,replace=False,p=W/W.sum())].astype(float)
for _ in range(50):
  l=((U[:,None]-c[None])**2).sum(2).argmin(1)
  for k in range(K):
    m=l==k
    if m.any(): c[k]=(U[m]*W[m,None]).sum(0)/W[m].sum()
lab=np.full(len(px),N-1);lab[~bg]=((fg[:,None]-c[None])**2).sum(2).argmin(1)
pal=np.vstack([c,[[196,58,60],[255,96,72],[250,250,253]]]).astype(np.uint8)
L=lab.reshape(T,T)
# 5. nettoyage : pixel isolé dont les 4 voisins sont d'accord
for _ in range(2):
  M=L.copy()
  for y in range(1,T-1):
    for x in range(1,T-1):
      n=[L[y-1,x],L[y+1,x],L[y,x-1],L[y,x+1]]
      if L[y,x] not in n and n.count(n[0])>=3: M[y,x]=n[0]
  L=M
np.save(f'{O}/L.npy',L);np.save(f'{O}/pal.npy',pal)
lum=pal.astype(float)@[.3,.59,.11];kd=int(lum.argmin())
# poser les traits, sauf sur le fond
L[LM&(L!=N-1)]=kd
res=Image.fromarray(pal[L])
res.save(f'{O}/auto.png')
z=res.resize((512,512),Image.NEAREST);ref=im.resize((512,512),Image.LANCZOS)
c2=Image.new('RGB',(1032,512),'white');c2.paste(ref,(0,0));c2.paste(z,(520,0));c2.save(f'{O}/cmp.png')
print('ok',len(np.unique(L)))

# export texte : lettres triées du plus sombre au plus clair, '.' = fond
import json
order=np.argsort(pal[:K].astype(float)@[.3,.59,.11])
let={int(k):'abcdefghijk'[i] for i,k in enumerate(order)}
let[K]='o';let[K+1]='p';let[N-1]='.'
json.dump({let[k]:'#%02x%02x%02x'%tuple(int(v) for v in pal[k]) for k in let if let[k]!='.'},open(f'{O}/palette.json','w'),indent=0)
open(f'{O}/auto.txt','w').write('\n'.join(''.join(let[int(v)] for v in r) for r in L)+'\n')
