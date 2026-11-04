# lissage local : dans un rectangle, un pixel minoritaire prend la couleur majoritaire de ses 8 voisins
import sys
from collections import Counter
src,dst,x1,y1,x2,y2=sys.argv[1],sys.argv[2],*map(int,sys.argv[3:7])
G=[list(l.rstrip('\n')) for l in open(src) if l.strip()]
for _ in range(2):
  H=[r[:] for r in G]
  for y in range(max(1,y1),min(127,y2)):
    for x in range(max(1,x1),min(127,x2)):
      n=Counter(G[y+dy][x+dx] for dy in(-1,0,1) for dx in(-1,0,1) if dy or dx)
      c,k=n.most_common(1)[0]
      if n[G[y][x]]<=1 and k>=5: H[y][x]=c
  G=H
open(dst,'w').write('\n'.join(''.join(r) for r in G)+'\n')
