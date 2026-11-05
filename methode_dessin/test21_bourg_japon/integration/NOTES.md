# Intégration dans la ROM

`outils/assets.py` lit les grilles de lettres finales (maison, labo, sanctuaire, torii, sakura, lanterne,
bambou, sol, panneau, plaque, rocher, pétales) et les range dans les palettes GBA 6 à 11 :

| Slot | Contenu |
|---|---|
| 6 | maison, labo, lanterne, panneau, plaque (+ portes) |
| 11 | maison rouge (noren R/r) |
| 10 | sanctuaire, torii |
| 7 | sakura, bambou, pétales |
| 9 | terre, gravier (herbe = mêmes couleurs que l'herbe primaire) |
| 8 | étang, koï, lys, rocher |

`outils/build.py` compose le Bourg et la Route 101, assemble les sols par autotile (`sol/autotile.py`),
exporte tuiles, métatuiles, cartes et animations de porte (porte1/2/3). Collisions : objet bloquant =
couche NORMAL (le perso passe devant), débord marchable (haut de toit, poutre du torii) = couche COVERED.
`outils/check.py` vérifie que PNJ, warps et panneaux restent accessibles et qu'aucune case bloquante
ne passe par-dessus la tête du joueur.

Résultat : 338 tuiles, 182 métatuiles. `planche_carte.png` = Bourg, Route 101, captures émulateur.
