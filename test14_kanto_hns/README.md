# Test 14 : le Kanto de Heart & Soul dans Rouge Feu

Ce test remplace les décors de Kanto par ceux de Heart & Soul (HnS) et garde les PNJ, les scripts
et les dialogues de Rouge Feu. Le dépôt contient les scripts et cette note. Les tilesets et les
cartes de HnS restent hors du dépôt : les scripts les copient depuis un clone local de HnS.

## Ordre des scripts

1. `test13_mont_argente/outils/importer_hns.py` puis `completer_mont_argente.py`.
2. `outils/importer_kanto_hns.py <pokemonHnS> <jeu>` importe 55 tilesets et 170 layouts sous le
   préfixe `Hns_`. Aucune carte du jeu ne change à cette étape.
3. `outils/basculer_zone1.py <jeu>` passe Bourg Palette, la Route 1 et Jadielle sur le décor HnS.
4. `outils/creer_cartes.py <pokemonHnS> <jeu>` crée vides les cartes absentes de Rouge Feu.
5. `outils/basculer_exterieurs.py` puis `outils/basculer_interieurs.py`, avec les deux mêmes arguments.

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

## Zone de la Ligue et donjons redessinés

`basculer_interieurs.py` traite aussi les cartes de la table `PAIRES_FIXES` (`outils/tables.py`) : le Portail de la
Ligue, la Route Victoire, la Route 23, le Plateau Indigo, son Centre, les salles du Conseil, la Forêt de Jade et ses
postes, le Mont Sélénite, la Cave Taupiqueur et la Grotte. Le total passe à 100 cartes.

Le trajet suit Heart & Soul : Route 22, Portail, Route Victoire (trois niveaux), Route 23, Plateau Indigo. Les quatre
membres du Conseil de Rouge Feu occupent les salles de Clément, Koga, Aldo et Marion. Le Portail mène aussi à la
Route 28 et au Mont Argenté.

Points ouverts, listés dans `outils/rapport_interieurs.txt` : les contrôles de badges de la Route 23 sont retirés,
l'entrée de la Cave Taupiqueur côté Route 11 n'a plus de sortie de son côté.

## Donjons restants et cartes nouvelles

`creer_cartes.py` se lance après `importer_kanto_hns.py` et avant les deux bascules. Il crée vides les treize cartes de
Heart & Soul sans équivalent dans Rouge Feu (table `NOUVELLES`) : l'extérieur et la boutique du Mont Sélénite,
l'arrière-salle de la Centrale, les Routes 26 et 27 avec leurs maisons, les Chutes Tohjo, la grotte de la Route 19 et
la salle du Dojo. Aucun personnage d'Or et Argent n'y est importé.

Le lot bascule aussi la Caverne Azurée (trois niveaux), les Îles Écume, la Centrale et les quatre accès des
souterrains des Routes 5 à 8. L'Arène d'Auguste quitte Cramois'Île pour les Îles Écume, comme dans Heart & Soul.

Trois règles s'ajoutent à `basculer_interieurs.py`. Les étages sans équivalent (table `FUSIONS`) cèdent leurs
dresseurs et leurs objets à l'étage conservé : B2F et B3F des Îles Écume, B1F et B2F du Mont Sélénite. Les rochers
à pousser, les rochers à briser et les arbustes à couper restent seulement là où Heart & Soul en pose un. Les
commandes `setmetatile` des scripts sont mises en commentaire, car elles redessineraient l'ancien décor.

Huit entrées ont été vérifiées en jeu : Caverne Azurée, Arène des Îles Écume, Centrale, souterrain de la Route 5,
boutique du Mont Sélénite, Portail vers la Route 26, Chutes Tohjo, maison de la Route 26.

Points ouverts : les énigmes à
interrupteurs (Carmin, Route Victoire, Arène d'Auguste) sont désactivées, la maison de la Route 27 et la grotte de
la Route 19 n'ont pas d'accès.

## Parc Safari et port de Carmin

Le Parc Safari prend les quatre zones de Heart & Soul : Beach pour le centre, Brush à l'ouest, Mountain au nord et
Cave à l'est. Les objets et les scripts de Rouge Feu sont replacés sur le nouveau décor. Les occupants des maisons
de repos et de la Maison Secrète attendent dehors, dans leur zone (table `HABITANTS`), car ces maisons n'existent
pas dans Heart & Soul. L'entrée garde son guichet, placé à gauche du couloir : les pas et les regards du script
sont réécrits par la table `REMPLACEMENTS`.

Le port suit le trajet de Heart & Soul. La jetée de Carmin mène à `VermilionCity_PortOutside`, carte nouvelle, puis
au hall du port, qui remplace l'ancien quai de l'Océane. Le marin et le contrôle du billet quittent Carmin pour le
hall (table `TRANSFERTS`). Le bout de la passerelle n'est pas une case de porte, donc un déclencheur fait monter à
bord (`SCRIPTS_AJOUTES`, `DECLENCHEURS_AJOUTES`). Le ferry des îles Sevii accoste au même quai (`src/seagallop.c`).

Vérifié en jeu : paiement à l'entrée du Safari, arrivée dans la zone, retour et sortie ; jetée de Carmin, hall du
port, refus sans billet, embarquement avec le billet, retour à quai et sortie vers la jetée.

La scène du départ de l'Océane a été jouée en jeu : le navire quitte le quai puis le joueur ressort sur la jetée.
L'arrivée du ferry des îles Sevii reste à jouer en jeu.

## Dernière passe : scènes et portes perdues

Le Mont Sélénite retrouve la scène des fossiles. Miguel, les deux fossiles et le déclencheur passent du B2F de
Rouge Feu à la salle équivalente du 1F de Heart & Soul (`TRANSFERTS`), et une retouche de décor ouvre le passage.
L'Arène d'Auguste garde la grotte de Heart & Soul mais s'ouvre sur Cramois'Île, avec le verrou de la Clé Secrète
et la scène de Léo ; l'échelle des Îles Écume mène chez Artikodin (`PORTES_FORCEES`).

Plusieurs bâtiments de Rouge Feu n'avaient pas de porte dans le décor importé. Une porte est dessinée sur une
façade libre (`RETOUCHES`) et reliée par `PORTES` : maison du Gardien et maison 3 à Parmanie, une maison et le
Fan Club à Safran, les maisons 4 et 5 à Azuria, la salle des lots, l'hôtel et une maison à Céladopole. Chacune a
été vérifiée en jeu, à l'entrée et à la sortie.

Les postes à étage de Rouge Feu n'ont qu'un niveau dans Heart & Soul : les occupants de l'étage des Routes 15, 16
et 18 descendent au rez-de-chaussée (`HABITANTS`, `PLACES`).

Scènes vérifiées en jeu : guide d'Argenta, garde du poste de Safran, rival de la Route 22 (déclencheurs en place),
premier garde de badge de la Route 23, départ de l'Océane. Sur la Route 23, les gardes se tiennent après la Route
Victoire, car Heart & Soul place la route entre la grotte et le Plateau Indigo.

Le rapport des extérieurs ne liste plus les déclencheurs et panneaux reposés à la main par l'étape des intérieurs.

Points ouverts : bureau du Safari sans bâtiment, étage des Centres Pokémon sans accès, ascenseur du Grand Magasin,
étages fusionnés des Îles Écume et du Mont Sélénite, énigmes à interrupteurs désactivées, Repaire Rocket reporté.

## Audit des collisions et des PNJ

`audit_cartes.py` relit chaque carte importée et signale les PNJ posés sur une case bloquée, les portes qui
tombent dans un mur et les cases franchissables sur une tuile d'ordinaire bloquante (façade, barrière, rocher).
Lancé depuis le dossier du jeu, après les deux imports : `python3 audit_cartes.py .` (`LISTE=1` détaille les tuiles).

Les trous repérés sont bouchés par la table `COLLISIONS` de `tables.py`, que `basculer_exterieurs.py` applique en
dernier : rocher de la Route 2, mur à lampes des entrées du Souterrain, coins de toits et de rochers sur les Routes
3 à 7, 21 et 23, quai de Carmin, Chutes Tohjo, comptoirs des postes. Le garde du badge Cascade monte en tête du
couloir de la Route 23 avec ses déclencheurs, Crissy quitte le plateau fleuri fermé de la Route 4, et les
occupants de la maison de repos du Safari Ouest attendent sur le chemin près du gardien.

L'audit passe de 34 à 14 signalements. Les 14 restants sont voulus : vendeurs et gardes derrière un comptoir,
glace et lave des Îles Écume, passage au-dessus d'un escalier au Safari Est, mur invisible de l'arène de Koga,
navires jamais affichés. Route 2, Safari Ouest et Souterrain ont été vérifiés en jeu.
