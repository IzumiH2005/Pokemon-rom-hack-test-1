# Empile les calques dans l'ordre (le '.' laisse voir le calque du dessous).
import sys
ordre = ["calque00_fond.txt","calque12_habit.txt","calque11_cheveux.txt","calque10_peau.txt",
         "calque31_bas.txt","calque20_contour.txt","calque21_meches.txt","calque22_boucles.txt",
         "calque23_tresse.txt","calque24_ombres.txt","calque30_yeux.txt"]
import os
img = [['.']*128 for _ in range(128)]
for c in ordre:
    if not os.path.exists(c): continue
    for y,l in enumerate(open(c).read().split('\n')[:128]):
        for x,ch in enumerate(l[:128]):
            if ch != '.': img[y][x] = ch
open(sys.argv[1],'w').write('\n'.join(''.join(r) for r in img)+'\n')
