# Dresseuse Lina, sprite de carte 16x32 (format Emerald). Personnage ≈ 14x21, tête ≈ 60 %.
# Yeux 1x2 sous la frange, 2 px d'écart, pas de nez ni de bouche. Lumière en haut à gauche.
from base import *

FACE = [
"................",
"................",
"................",
"................",
"................",
"................",
"................",
"................",
"................",
"................",
"................",
".....OOOOOO.....",
"...OOaaabbbOO...",
"..OaaabbbbbbcO..",
"..OYYYYYYYYYYO..",
".ObbabbbbbbbbcO.",
".Obcb1bbbb1bbcO.",
".Obc11111111ccO.",
".Obc11E11E12ccO.",
".Obc11E11E22ccO.",
".Obc11111122ccO.",
".OccO222222OccO.",
"..OOOO3WW3OOOO..",
"...OrqqWWqqqpO..",
"..OrOrqqqqqpOpO.",
"..O2OrqqqqqpO3O.",
"..OOOqqYYqqpOOO.",
"....OnnnnnnmO...",
"....OnnmOnnmO...",
"....O22O.O23O...",
"...OmmmO.OmmmO..",
"...OOOOO.OOOOO..",
]

HAUT = FACE[:11]
DOS = HAUT + [
".....OOOOOO.....",
"...OOaaabbbOO...",
"..OaaabbbbbbcO..",
"..OYYYYYYYYYYO..",
".ObbabbbbbbbbcO.",
".ObabbbbbbbbbcO.",
".ObbbbbbbbbbbcO.",
".ObbbbbbbbbbbcO.",
".ObcbbbbbbbbccO.",
".OccbbbbbbbcccO.",
".OcccbbbbbcccO..".replace('O..', 'cO.')[:16],
"..OOOcccccccOO..",
"...OOOqqqqqOO...",
"..OrOrqqqqqpOpO.",
"..O2OrqqqqqpO3O.",
"..OOOqqqqqqpOOO.",
"....OnnnnnnmO...",
"....OnnmOnnmO...",
"....O22O.O33O...",
"...OmmmO.OmmmO..",
"...OOOOO.OOOOO..",
]
PROFIL = HAUT + [
"......OOOOO.....",
"....OOaaabbOO...",
"...OaabbbbbbcO..",
"...OYYYYYYYYYO..",
"..ObabbbbbbbbcO.",
"..Obb1bbbbbbbcO.",
"..O111bbbbbbbcO.",
"..O1E12bbbbbccO.",
"..O1E12cbbbbccO.",
"..O1122cbbbbccO.",
"..OO222OcccccO..",
"....OO3OOOOOO...",
".....OrqqqpO....",
".....OrqqqpO....",
".....O2qqqpO....",
".....OqYYqpO....",
".....OnnnnmO....",
".....OnnnnmO....",
".....OO22OO.....",
".....OmmmmO.....",
".....OOOOOO.....",
]
def pas(G, gauche):
    """Image de pas : une jambe levée d'1 px, le corps monte d'1 px aux passages (ici on garde le corps)."""
    g = [list(r) for r in G]
    if gauche:  # jambe gauche (côté écran) levée : on remonte la colonne 4..7 des 3 dernières rangées
        for y in (29, 30): g[y][3:8] = list(G[y + 1][3:8])
        g[31][3:8] = list('.....')
    else:
        for y in (29, 30): g[y][9:14] = list(G[y + 1][9:14])
        g[31][9:14] = list('.....')
    return chaine(g)
PAS_G = pas(FACE, True); PAS_D = pas(FACE, False)
