# Test 23 : colonne brisée, seconde version

La première série (test22) restait plate : un fût vu de face posé sur un rectangle. Cette version dessine la colonne vue un peu de dessus, comme les décors de Rouge Feu.

- La dalle carrée montre son dessus et sa face avant.
- Le tore du pied est une ellipse (rapport 0,4) dont on voit le dessus et le bourrelet arrondi.
- Les joints des tambours suivent le même arc que le pied.
- La cassure montre sa surface vue de dessus, avec un éclat qui reste debout à gauche et une marche dans la pierre.
- Le fût porte des cannelures nettes : un creux sombre, une arête claire, et un ombrage de cylindre éclairé en haut à gauche.
- Les ombres tirent vers le violet gris, les lumières vers la crème chaude.
- Piqûres, fissures et éclats cassent la régularité de la pierre.
- L'ombre portée tombe en bas à droite.

Étapes : `etapes/c03.txt` (volumes et ombrage), puis `etapes/c04.txt` (usure). Pièces : `fut.txt`, `tore.txt`, `cassure.txt`.

## Passage au style Platine

La colonne reprend la gamme crème olive du sol de Platine (#eee6c5 à #736a41, contour #4f4628), sans violet ni noir. Le fût porte de grandes facettes plates au lieu de cannelures. Le dessus de la cassure montre des fissures en étoile autour d'un point d'impact, et les joints côté ombre passent en brun clair pour adoucir le contour.

## Série complète

`assembler.sh nom type hauteur "joints"` monte une colonne à partir des pièces de `pieces/` : la base (dalle, tore, ombre) en bas, le fût répété, le pied, puis le sommet. Le type `brise` pose `cassure.txt`, `brise2` pose `cassure2.txt` (cassure en biais, haute à gauche) et `pointe` pose `pieces/pointe.txt`, qui porte la lame et le collier. Les fichiers `colonnes/d_*.txt` ajoutent l'usure propre à chaque colonne.

La pointe (`pieces/pointe.txt`, 22x25) est vue légèrement de haut et fait /\ : pointe centrée, côté gauche clair, facette avant moyenne, côté droit sombre. `pieces/geo_pointe.py` calcule la lame d'après un modèle 3D maison rendu avec three.js à 30° de plongée (cône à huit facettes, hauteur 1,9 fois le rayon, un peu plus étroit que le collier). L'entrée de la lame dans le collier et la lèvre sont tracées à la main.

`colonnes/c_couchee.txt` dessine une colonne tombée dans l'axe nord-sud, cassée en section ronde au sud. Elle remplace les gros blocs effondrés de Platine (modèle 514), à côté de deux colonnes brisées debout. Les gravats (`colonnes/gravats.txt`) restent aux douze points de petit relief. `composer.py` (test16) pose le tout sur la carte.
