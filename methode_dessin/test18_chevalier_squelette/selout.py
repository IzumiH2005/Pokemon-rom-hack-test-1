# Contour sélectif (étape A6-I) : côté lumière (haut-gauche) seulement, le trait extérieur
# prend une teinte sombre du matériau qu'il borde au lieu du quasi-noir O.
import sys
G=[list(l.rstrip('\n')) for l in open(sys.argv[1]) if l.strip()]
H,W=len(G),len(G[0]); out=[r[:] for r in G]
TEINTE={**{c:'a' for c in 'def'},**{c:'h' for c in 'jlm'},**{c:'r' for c in 'st'}}
for y in range(H):
    for x in range(W):
        if G[y][x]!='O': continue
        vide_hg = (x>0 and G[y][x-1]=='.') or (y>0 and G[y-1][x]=='.')
        if not vide_hg: continue
        voisin=[G[y][x+1] if x+1<W else '.', G[y+1][x] if y+1<H else '.']
        for v in voisin:
            if v in TEINTE: out[y][x]=TEINTE[v]; break
open(sys.argv[2],'w').write('\n'.join(''.join(r) for r in out)+'\n')
