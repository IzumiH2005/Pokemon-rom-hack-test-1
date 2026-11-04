# Outil : tube émissif le long d'une ligne médiane décidée à la main (points x y rayon).
# Peint les couches halo u (r+1) > v (r) > w (r-1) > cœur x (r-2) ; ne décide aucune forme.
import sys
def tube(pts):
    out=[]
    for (x1,y1,r1),(x2,y2,r2) in zip(pts,pts[1:]):
        n=int(max(abs(x2-x1),abs(y2-y1))*3)+1
        for i in range(n+1):
            t=i/n; out.append((x1+(x2-x1)*t,y1+(y2-y1)*t,r1+(r2-r1)*t))
    return out
def peindre(G,pts,couches="uvwx"):
    s=tube(pts)
    for k,c in enumerate(couches):
        for x,y,r in s:
            rr=r+1-k
            if rr<0: continue
            for yy in range(int(y-rr)-1,int(y+rr)+2):
                for xx in range(int(x-rr)-1,int(x+rr)+2):
                    if (xx-x)**2+(yy-y)**2<=rr*rr+0.25 and 0<=xx<128 and 0<=yy<128:
                        G[yy][xx]=c
    # pointe : 1 px garanti au dernier point
    x,y,_=pts[-1]; G[round(y)][round(x)]=G[round(y)][round(x)] if G[round(y)][round(x)]!='.' else 'u'
def coeur(G,pts,seuil_w=0.4,seuil_x=1.1):
    # ligne de lumière centrale (cœur émissif) le long du brin
    for x,y,r in tube(pts):
        X,Y=round(x),round(y)
        if r>=seuil_x: G[Y][X]='x'
        elif r>=seuil_w and G[Y][X]!='x': G[Y][X]='w'
