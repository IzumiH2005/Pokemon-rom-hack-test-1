# Sol — autotiles dessinés (remplacent le bruit procédural, contraire à R3)

Principe : un bloc 3×3 (48×48 : coins, bords, centre) + une planche de coins intérieurs (32×32).
`autotile.py` assemble chaque case 16×16 par quarts 8×8 selon 3 voisins (horizontal, vertical, diagonal),
d'où des motifs de période 8 sur les bords (raccord des quarts) et 16 au centre.
`herbe.py` remplit les `.` avec l'herbe primaire exacte du jeu (aperçus).

- terre : `forme.py` (marge 4, onde [0,0,1,1,2,1,1,0], rayon 4.5), `berge.py` (nord/ouest ombre d + rang c, sud/est clair a), cailloux posés à la main.
  - R5 : onde [0,0,1,1,1,1,0,0] = créneaux → onde en dégradé.
  - R5 : quart intérieur inversé dans l'aperçu → `autotile.quart_src` unique, partagé avec le chargeur.
- gravier : `gravier/gen.py` ; bordure de pierres taillées (4 px, une pierre / 8 px, coins arrondis), sillons droits période 4.
  - R5 : joints pleins = échelle ; pierres 4 px = corde pointillée ; onde en marches = planches.
- étang : pas d'herbe dans les cases (1 palette / tuile) ; pierres dessinées à la main (`etang/pieces.py`), 2 modèles alternés.
  - R5 : pierres identiques = mur de briques → 2e pierre ronde.
  - koï (2 sens) et nénuphar : pièces à poser sur le fond.
