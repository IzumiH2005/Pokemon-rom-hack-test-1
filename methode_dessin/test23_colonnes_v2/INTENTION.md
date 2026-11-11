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

`assembler.sh nom type hauteur "joints"` monte une colonne à partir des pièces de `pieces/` : la base (dalle, tore, ombre) en bas, le fût répété, le pied, puis le sommet. Le type `brise` pose `cassure.txt`, `brise2` pose `cassure2.txt` (cassure en biais, haute à gauche) et `pointe` pose la pointe à facettes et son collier. Les fichiers `colonnes/d_*.txt` ajoutent l'usure propre à chaque colonne.

Les ruines (`c_ruine_g`, `c_ruine_d`) assemblent deux blocs dressés à coins cassés (`blocA`, `blocB`, faits de `bloc.txt` et des coins) et trois cubes. `c_souche.txt` dessine une colonne brisée au ras du socle, sur un anneau rond (`pieces/anneau.txt`) ; elle remplace les gravats aux douze points de petit relief. La pointe (`pieces/pointe.txt`, 30 rangées) est un éclat asymétrique : un grand plan clair à gauche, tourné vers le haut, et une face sombre à droite. `composer.py` (test16) pose le tout sur la carte.
