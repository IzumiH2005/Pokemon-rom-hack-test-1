"""Vérifie que le trait du template est toujours là (hors yeux recolorés et calques posés dessus)."""
import sys
G=[l.rstrip() for l in open(sys.argv[1])];T=[l.rstrip() for l in open('etape01_template.txt')]
bad=[(x,y,G[y][x]) for y in range(35) for x in range(24) if T[y][x]=='O' and G[y][x] in 'sSlr']
print(sys.argv[1], 'trait du template intact' if not bad else f'trait écrasé par la peau : {bad}')
