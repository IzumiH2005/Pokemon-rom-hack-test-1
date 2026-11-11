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

## Tous les extérieurs

`outils/basculer_exterieurs.py <pokemonHnS> <jeu>` passe les dix villes et les Routes 1 à 22, 24 et
25 sur le décor HnS. Les portes suivent une table écrite à la main, les connexions reprennent celles
de HnS, et les PNJ de Rouge Feu se replacent seuls : case d'origine décalée si elle reste valide,
sinon place d'un PNJ HnS de même rôle. `outils/rapport_exterieurs.txt` liste ce que le script n'a
pas pu placer : portes de bâtiments absents du Kanto de HnS, panneaux sans support, déclencheurs
d'histoire retirés.

## Ce qui reste

- Zone de la Ligue : Route 23, Plateau Indigo, Routes 26 et 27, Route Victoire. La Route 22 mène
  encore à l'ancienne Route 23.
- Port de Carmin, extérieur du Mont Sélénite : cartes HnS sans équivalent, à créer.
- Intérieurs et donjons : encore en décor Rouge Feu.
- Lieux absents de HnS (Tour Pokémon, Manoir, Parc Safari, Centrale, Repaire Rocket, Sylphe, Océane) :
  à redessiner avec les tilesets HnS.
- Animations de porte de HnS non reprises.

## Intérieurs des villes et des routes

`outils/basculer_interieurs.py <pokemonHnS> <jeu>` se lance après `basculer_exterieurs.py`. Il associe chaque
intérieur de Rouge Feu à celui de Heart & Soul par les portes : deux portes posées sur la même case d'un extérieur
mènent au même bâtiment. Les étages sans porte sur l'extérieur sont listés dans `ETAGES`. Le résultat est écrit dans
`outils/paires_interieurs.json` (78 intérieurs).

Chaque intérieur reprend le décor et les portes de Heart & Soul. Les PNJ de Rouge Feu gardent leurs scripts et
prennent la place d'un PNJ de Heart & Soul de même rôle (infirmière, vendeur, dresseur, passant, objet), sinon la
case accessible la plus proche. `outils/tables.py` contient les tables écrites à la main : `PORTES` pour les
extérieurs et `PLACES` pour les scènes à placer case par case (Labo de Chen).

`outils/rapport_interieurs.txt` liste ce qui reste à reprendre : les étages des Centres Pokémon (Heart & Soul n'a
qu'un niveau), l'ascenseur du Centre Commercial, l'entrée du Repaire Rocket au Casino, les étages des postes de
garde et les déclencheurs retirés.
