# Test 14 : le Kanto de Heart & Soul dans Rouge Feu

Ce test remplace les décors de Kanto par ceux de Heart & Soul (HnS) et garde les PNJ, les scripts
et les dialogues de Rouge Feu. Le dépôt contient les scripts et cette note. Les tilesets et les
cartes de HnS restent hors du dépôt : les scripts les copient depuis un clone local de HnS.

## Ordre des scripts

1. `test13_mont_argente/outils/importer_hns.py` puis `completer_mont_argente.py`.
2. `outils/importer_kanto_hns.py <pokemonHnS> <jeu>` importe 55 tilesets et 170 layouts sous le
   préfixe `Hns_`. Aucune carte du jeu ne change à cette étape.
3. `outils/basculer_zone1.py <jeu>` passe Bourg Palette, la Route 1 et Jadielle sur le décor HnS.

`outils/layouts_kanto_hns.json` donne, pour chaque carte HnS, l'identifiant du layout importé.

## Zone 1 : ce qui a été vérifié en jeu

Les extérieurs HnS de cette zone dérivent des cartes de Rouge Feu, donc presque toutes les cases
coïncident. Jadielle demande cinq déplacements (porte, déclencheur et panneau de l'Arène, porte de
l'école). Deux panneaux « Astuces » manquent dans le décor HnS : le script recopie un bloc panneau.

Portes des maisons, du labo, du Centre et de l'école, raccords Bourg Palette / Route 1 / Jadielle,
script de Chen, Arène fermée et panneaux fonctionnent.

## Ce qui reste

- Les intérieurs de la zone gardent le décor de Rouge Feu. Ceux de HnS ont d'autres dimensions :
  chaque PNJ et chaque porte doit être replacé à la main.
- Route 2, Route 22 et Route 21 gardent leur ancien tileset, donc le raccord visuel avec la zone 1
  est faux tant qu'elles ne sont pas basculées.
- Les animations de porte de HnS ne sont pas reprises.
- Les autres villes ont été redessinées dans HnS (tailles et portes différentes). Les Routes 3, 5,
  18, 19, 20 et 24 sont identiques, les Routes 4, 9, 14, 15, 16 et 17 presque.
