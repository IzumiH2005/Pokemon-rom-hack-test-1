"""Etats de porte 16x32 decoupes dans un sprite final.
usage: portes.py dossier final.txt x0 y0 ix0 iy0 ix1 iy1 [xbord]
(x0,y0) = coin de la colonne de porte ; (ix..,iy..) = vantail interieur (coord. absolues)
xbord = colonne ou s'arrete le vantail glisse (mi-ouvert)."""
import sys,subprocess
d,f,x0,y0,a,b,c,e=sys.argv[1],sys.argv[2],*map(int,sys.argv[3:9])
xb=int(sys.argv[9]) if len(sys.argv)>9 else (a+c)//2
g=[list(l.rstrip('\n')) for l in open(f"{d}/{f}")]
crop=[r[x0:x0+16] for r in g[y0:y0+32]]
half=[r[:] for r in crop]; opn=[r[:] for r in crop]
for y in range(b,e+1):
    for x in range(a,c+1):
        v='O' if y<e else 'A'
        opn[y-y0][x-x0]=v
        if x>xb: half[y-y0][x-x0]=v
    half[y-y0][xb-x0]='t'
for n,rows in (("porte1_fermee",crop),("porte2_mi",half),("porte3_ouverte",opn)):
    open(f"{d}/{n}.txt","w").write("\n".join("".join(r) for r in rows)+"\n")
    subprocess.run(["python3","/home/user/Pokemon-rom-hack-test-1/methode_dessin/outils/px.py",f"{d}/{n}.txt","8",f"{d}/palette.json"])
