# Empile : fond, puis aplats découpés par la silhouette ('2' = fond), puis les
# calques peints par-dessus dans l'ordre donné ('.' = transparent). Ne décide aucune forme.
import sys
def L(f): return [l.rstrip('\n') for l in open(f) if l.strip()]
sil, fond, plats = L('silhouette.txt'), L('calque00_fond.txt'), L('calque10_plats.txt')
G=[[fond[y][x] if sil[y][x]=='2' else plats[y][x] for x in range(128)] for y in range(128)]
for f in sys.argv[2:]:
    for y,l in enumerate(L(f)):
        for x,c in enumerate(l):
            if c!='.': G[y][x]= fond[y][x] if c=='2' else c
open(sys.argv[1],'w').write('\n'.join(''.join(r) for r in G)+'\n')
