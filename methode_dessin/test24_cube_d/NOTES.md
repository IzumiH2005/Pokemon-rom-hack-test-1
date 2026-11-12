# Test 24 — Le Dé (Cube D)

Résultat : `de_64.png` (image plein écran de la scène 6), `de_icone_24.png` (icône du
sac, redessinée), `de_x8.png` (les deux agrandis), `planche_64.png` et `planche_24.png`
(contrôle A5-11), `situation_x3.png` (écran GBA). Intention et rapports : `INTENTION.md`.
`build.sh` reconstruit toutes les étapes depuis les fichiers de commandes.

## Ce que le dessin raconte
- Six faces comme les six places de l'équipe ; on en voit trois, qui se touchent au même
  coin comme sur un vrai dé (1, 2 et 3).
- Face 1 à gauche, allumée en **jaune** : Pikachu. Un seul gros point, le plus clair de
  l'image : c'est le point d'intérêt.
- Face 2 à droite, allumée en **orange** : Dracaufeu.
- Face 3 en haut, **éteinte** : trois creux gris. Elle tient lieu des quatre faces
  grises.
- Corps en pierre grise lisse, arêtes arrondies, chaque face porte un panneau serti. Une
  face « s'allume » : seul son panneau change, le corps reste gris.

## Méthode suivie (64×64)
1. `c00` construction : arêtes en fil de fer isométrique 2:1, panneaux, places des points.
   Défaut : panneau du dessus à 12/28 de l'arête au lieu de 20/28 → corrigé.
2. `c01` silhouette en noir plein (hexagone net), puis `c02` trois valeurs : dessus clair,
   gauche moyen, droite sombre. Le volume se lit à ×1 avant toute couleur.
3. Contour (`contour.py`), puis `c04` panneaux à plat.
4. `c05` rainure 1 px et bande sombre 2 px de largeur fixe : ombrage inversé des panneaux
   émissifs (C15-D), creux du dessus à paroi haute sombre et lèvre basse claire (leçon T15).
5. `c06` points posés en pièces écrites à la main (`pieces/`) : cœur presque blanc et halo
   pour les faces allumées, creux pour la face éteinte.
   Défaut : creux de 3 rangées lus comme des taches → 4 rangées ; points extérieurs collés
   au bord du panneau → décalés d'1 px vers le centre.
6. `c07` arêtes arrondies : reflets 2 px sur les bords du dessus, arête gauche claire,
   bas des côtés dans l'ombre, sommets gauche et droit coupés.

## Icône 24×24
Redessinée depuis la silhouette (A4b), sans panneau serti : à cette taille la face entière
prend la couleur. Marqueurs gardés : coin du cube, points de dé, jaune à gauche, orange à
droite. 16 couleurs au plus (table A3).

## Défauts restants
- Sur fond sombre, le contour côté droit se fond (B5). Le Dé est montré sur fond sombre :
  un liseré de rebond sur l'arête droite l'aiderait, à essayer si l'image paraît lourde
  en jeu.
- La lumière des panneaux ne déborde pas encore sur le gris voisin (C15-D). Je l'ai
  laissée de côté pour garder le corps lisible.
