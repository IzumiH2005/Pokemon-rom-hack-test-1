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

La pointe (`pieces/pointe.txt`, 22x24) reprend le modèle 3D maison rendu avec three.js à 30° de plongée, à l'échelle du fût (rayon 10 px). Le cône à huit facettes, une arête vers l'avant, est aussi large que le fût et haut de 1,9 fois son rayon ; on en voit quatre facettes, de la plus claire à gauche à la plus sombre à droite. Il repose sur une bague fine de rayon 11 dont on voit à peine le rebord ; le bas de la bague suit un arc. `pieces/geo_pointe.py` calcule la silhouette et les facettes dans `pieces/pointe_geo.txt` ; `pointe.txt` en garde les quatorze premières rangées et trace à la main la base du cône et la bague.

`colonnes/c_couchee.txt` dessine une colonne tombée dans l'axe nord-sud, cassée en section ronde au sud. `colonnes/geo_couchee.py` l'écrit d'après un modèle three.js vu à 30° : le bout nord et les deux joints forment des arcs ∩ (flèche de 5 px, un quart de la largeur), et la face cassée, tournée vers la caméra, se voit presque ronde. Elle remplace les gros blocs effondrés de Platine (modèle 514), à côté de deux colonnes brisées debout. Les gravats (`colonnes/gravats.txt`) restent aux douze points de petit relief. `composer.py` (test16) pose le tout sur la carte.
