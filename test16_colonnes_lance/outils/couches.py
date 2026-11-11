import numpy as np
from PIL import Image
X0,Y0,MW,MH,DY=15,3,34,57,7
full=np.array(Image.open('rendu2_1.0_1.png')).astype(int)
low=np.array(Image.open('bas_1.0_1.png')).astype(int)
h=np.load('h_1.0_1.npy')
H,W=h.shape
Yp=np.arange(H)[:,None]+np.zeros((1,W))
foot=np.floor((Yp+h-160)/16); disp=np.floor(Yp/16)-7
top=(h>48.5)&(foot>disp)
sl=np.s_[(Y0+DY)*16:(Y0+DY+MH)*16, X0*16:(X0+MW)*16]
bas=np.where(top[...,None],low,full)[sl]
haut=np.where(top[...,None],full,0)[sl]; mh=top[sl]
Image.fromarray(bas.astype(np.uint8)).save('carte_bas.png')
a=np.dstack([haut,mh*255]).astype(np.uint8); Image.fromarray(a,'RGBA').save('carte_haut.png')
c=(bas>>3)
print('couleurs bas',len(np.unique(c.reshape(-1,3),axis=0)),'haut',len(np.unique((haut>>3)[mh].reshape(-1,3),axis=0)))
