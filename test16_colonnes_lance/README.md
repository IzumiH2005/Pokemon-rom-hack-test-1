# Test 16 : les Colonnes Lance

La carte `MAP_COLONNES_LANCE` reprend le sommet du Mont Couronné de Platine, là où Red B se réveille, tente d'utiliser Dialga et Palkia puis affronte le Luka de son monde. Le joueur ne peut pas l'atteindre en jeu normal : aucun warp n'y mène, et seule une scène scriptée l'ouvrira plus tard.

Le dépôt ne contient que les scripts et cette note. Les modèles, textures, rendus et tuiles produits restent hors du dépôt.

## Source

La décompilation [pret/pokeplatinum](https://github.com/pret/pokeplatinum) fournit la carte. Un checkout partiel suffit :

```
res/field/mapmodels/   (map_data_375 à 378, map_texture_set_059.nsbtx)
res/field/props/       (prop_model_508 à 514 : colonnes debout, brisées, couchées)
```

Les Colonnes Lance occupent quatre blocs de 32x32 cases (375, 376, 377, 378). Chaque bloc porte son terrain 3D, sa grille de collisions et sa liste d'objets (les colonnes).

## Chaîne de fabrication

Les scripts de rendu lisent `/home/user/refs/pokeplatinum` en dur et écrivent dans le dossier courant.

1. `python3 rendu2.py 1.0 1` dessine le terrain et les colonnes en projection oblique (un pixel par unité, K=1 : chaque unité de hauteur remonte l'image d'un pixel). Il sort `rendu2_1.0_1.png` et `bas_1.0_1.png`, ce dernier ne gardant que ce qui reste au niveau du sol.
2. `python3 couches.py` découpe la zone utile (34x57 métatuiles) et sépare deux couches : `carte_bas.png` pour le sol, `carte_haut.png` pour les colonnes qui passent devant le joueur.
3. `python3 construire.py <dossier_rendu> <pokeplatinum> <jeu>` convertit les deux couches en tuiles GBA (couleurs 15 bits, palettes de 15 couleurs, tuiles dédoublonnées avec miroirs) et écrit la carte. Les collisions viennent du bit 15 de la grille Platine. Le palier et l'escalier nord, cachés derrière l'esplanade dans la vue GBA, restent fermés.
4. `python3 installer.py <jeu>` déclare le jeu de tuiles, le layout et la carte dans le jeu. On peut le relancer sans doublon.
5. Pour les colonnes dessinées à la main, on rend le terrain sans objets (`rendu2.py 1.0 1 --sans`), on lance `couches.py`, puis `python3 composer.py <dossier_rendu> <pokeplatinum> ../../methode_dessin/test22_colonnes_lance/colonnes`. Le script efface aussi les huit colonnes et les gravats que porte le terrain de Platine, puis pose les dessins de `test22` à leur place. Chaque dessin passe devant le joueur au-dessus de la rangée de tuiles de son pied.
6. `make firered` reconstruit la ROM, puis `python3 apercu.py` recompose la carte depuis les fichiers GBA pour vérifier le résultat.

`nitro.py` et `bmd.py` lisent les formats Nintendo DS (NSBTX, NSBMD : textures, matériaux, commandes de dessin).

## Résultat

Le jeu de tuiles compte 955 tuiles sur 1024, 5 palettes sur 13 et 550 métatuiles. La carte mesure 34x57 cases et joue la musique de la Route Victoire.

Pour tester, on place le joueur sur l'escalier sud en (16, 49) ou (16, 50). L'autel triangulaire se trouve au centre de l'esplanade.

## Limites

- Les colonnes viennent de `methode_dessin/test22_colonnes_lance` : six colonnes (trois pointues, trois brisées), deux tailles hautes pour le terrain, deux groupes de ruines et un tas de gravats, tous dessinés au pixel.
- La vue oblique écrase les reliefs : les colonnes debout couvrent jusqu'à quatre métatuiles vers le haut.
- Les lumières et le brouillard de Platine manquent.
- La scène elle-même (PNJ, Dialga, Palkia, combat) reste à écrire.
