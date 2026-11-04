# Cape : bords, ourlet et crêtes de plis posés à la main ; ombrage entre crêtes (flanc éclairé à gauche).
# Usage : python3 c28_cape.py calque28_cape.txt
import sys, math
def interp(pts, v):
    for (a,va),(b,vb) in zip(pts,pts[1:]):
        if a<=v<=b:
            t=(v-a)/(b-a) if b!=a else 0; t=(1-math.cos(math.pi*t))/2
            return va+(vb-va)*t
    return None
GAUCHE=[(28,52),(40,56),(52,61),(64,66),(76,70),(120,70)]
DROITE=[(28,86),(38,92),(50,102),(58,106),(66,107),(74,109),(84,114),(96,120),(120,121)]
OURLET=[(70,86),(74,96),(81,89),(88,106),(96,93),(104,113),(110,100),(116,110),(121,98)]
# crêtes de plis (y, x) posées à la main : resserrées à l'épaule, ouvertes vers l'ourlet
CRETES=[[(28,74),(50,72),(75,75),(98,74)],
        [(28,79),(45,82),(70,86),(106,88)],
        [(28,84),(46,92),(66,100),(85,101),(113,104)],
        [(34,88),(54,103),(75,108),(100,114),(115,116)]]
def ourlet(x): return interp(OURLET,x)
G=[['.']*128 for _ in range(128)]
for y in range(28,120):
    xl=interp(GAUCHE,y); xr=interp(DROITE,y)
    cr=[interp(c,y) for c in CRETES]; cr=[c for c in cr if c is not None]
    for x in range(round(xl),round(xr)+1):
        h=ourlet(x)
        if h is None or y>h: continue
        # position entre crêtes
        gauche=[c for c in cr if c<=x]; droite=[c for c in cr if c>x]
        c0=gauche[-1] if gauche else None; c1=droite[0] if droite else None
        if c0 is None: ch='r' if x>=c1-1 else 'q'
        else:
            v=(c0+c1)/2 if c1 is not None else c0+6   # creux à mi-chemin
            if x<=v:   # flanc à l'ombre, juste après la crête (descend vite)
                g=(x-c0)/max(v-c0,1)
                ch='t' if g<0.1 else 's' if g<0.25 else 'r' if g<0.5 else 'q'
            else:      # flanc éclairé, remonte vers la crête suivante
                f=(x-v)/max(c1-v,1) if c1 is not None else 0
                ch='q' if f<0.15 else 'r' if f<0.35 else 's' if f<0.75 else 't'
        if y<33 and ch in 'ts': ch='r'   # ombre portée du col
        G[y][x]=ch
# balancement : les lambeaux se courbent vers la droite
H=[['.']*128 for _ in range(128)]
for y in range(128):
    d=round(max(0,(y-84)/26)**2*4)
    for x in range(128):
        if G[y][x]!='.' and x+d<128: H[y][x+d]=G[y][x]
G=H
# contour
O=[r[:] for r in G]
for y in range(128):
    for x in range(128):
        if G[y][x]=='.': continue
        for dx,dy in ((1,0),(-1,0),(0,1),(0,-1)):
            nx,ny=x+dx,y+dy
            if not(0<=nx<128 and 0<=ny<128) or G[ny][nx]=='.': O[y][x]='O'; break
open(sys.argv[1],'w').write('\n'.join(''.join(r) for r in O)+'\n')
