# Méthode de pixel art — objets et personnages (v4)

On construit d'abord, on détaille ensuite. Cette méthode réunit le dessin classique
(construction par volumes, ligne d'action, anatomie) et les règles du pixel art
(silhouette, valeurs, clusters, lignes propres, rampes, lumière).

**Comment l'utiliser :**
- la **partie A** vaut pour tout : règles de travail, lisibilité, tailles, couleurs, lumière,
  matières, finition et contrôle ;
- la **partie B** donne les étapes de construction d'un **objet** ;
- la **partie C** donne les étapes de construction d'un **personnage** (anatomie, visage,
  cheveux) ;
- un dessin suit B ou C pour la construction, puis le pipeline A5 pour les pixels.

**Sources :** [Z] *Apprendre à tout dessiner avec Zephy* · [M] livre de dessin manga ·
[I] planches d'anatomie fournies · [C] planches sur les cheveux fournies ·
[R] recherches (Loomis, Bridgman, Proko, tutoriels d'anticrénelage, de matières et de
lisibilité d'icônes) · [T1]…[T3] leçons de nos propres tests.

---

# Partie A — Règles communes

## A1. Règles de travail

- **R1. Une étape = une image regardée.** Chaque étape produit `etape_XX_nom.png`. On
  la regarde **à ×1 et agrandie** avant de passer à la suite. Ce qui ne se lit pas à ×1
  n'existe pas.
- **R2. Du grand au petit.** Construction, puis silhouette, couleur, lumière, et les détails
  en dernier. Un détail ne corrige jamais une erreur de construction : on revient à
  l'étape fautive.
- **R3. Décider avant de tracer.** Volumes, articulations et formes d'ombre sont écrits en
  données (coordonnées, tailles), ou posés pixel par pixel. Un script peut **remplir** une
  forme décidée. Il ne **décide** jamais de la forme : pas d'ombre calculée par formule,
  ni de dégradé automatique [T1].
- **R4. Un calque par concept.** Construction dans des couleurs vives (rouge pour la pose ou
  les axes, bleu pour les repères, vert pour les volumes), qui n'apparaissent jamais dans
  l'image finale. Le contour final se pose ensuite en ton sombre.
- **R5. Corriger en boucle.** À chaque étape, noter au moins un défaut, le corriger,
  revérifier.
- **R6. Penser en rapports.** On écrit « le col = 1/3 de la largeur du ventre », pas
  « 4 px » au hasard. Les pixels se calculent à partir des rapports.
- **R7. Deux variantes.** Pour la forme principale (pose, visage, silhouette d'un objet),
  faire au moins 2 essais et garder le meilleur.
- **R8. Peu de traits.** Une ligne par direction : on commence en « I » (droite), on
  arrondit en « C », on finit par quelques « S ».
- **R9. Format imposé ou libre.** Si une taille est imposée (16, 32, 64…), suivre la table
  A3. Sinon, choisir un grand canevas (128 à 256 px pour un personnage) et dessiner comme
  un illustrateur : le pixel est l'outil, pas une excuse pour simplifier.

## A2. Lisibilité [R]

- **La silhouette d'abord.** Un objet ou un personnage doit être reconnaissable **en noir
  plein**. Si la silhouette ne dit pas ce que c'est, aucune couleur ne le sauvera.
- **La valeur fait le travail, pas la teinte.** En niveaux de gris, chaque matière ou
  pièce doit avoir sa propre valeur. Deux matières voisines de même valeur se fondent
  [T3 : le fer et le bois du coffre].
- **3 valeurs avant les nuances.** Poser seulement sombre, moyen et clair, et vérifier à ×1
  que le volume se lit déjà.
- **Budget de contraste.** Le plus fort contraste et le plus de détails vont au **point
  d'intérêt** (visage, mains ; garde d'une épée, gemme, serrure). Le reste est plus calme.
  Partout pareil = rien ne ressort.
- **Une seule couleur saturée (l'accent).** Les autres couleurs sont plus douces.
- **Pas de détail d'1 px isolé** à petite taille : il devient du bruit. Mieux vaut une forme
  de 2 à 3 px qu'un trait fin.
- **Formes intérieures par la valeur.** À petite taille, les formes intérieures se marquent
  par un changement de ton, pas par un trait de contour qui casserait la silhouette.
- **Tester en situation.** Sur fond clair **et** sur fond sombre, et dans le contexte du jeu
  (case d'inventaire, tuile de sol, à côté d'autres sprites).

## A3. Table par taille [R]

| | 16×16 | 32×32 | 64×64 | 128 px et plus |
|---|---|---|---|---|
| Tons par matière | 2 à 3 | 3 à 4 | 4 à 5 | 5 et plus |
| Couleurs au total | ≤ 8 | ≤ 16 | ≤ 24 | libre |
| Contour | 1 px, un ou deux tons sombres | 1 px, selout | 1 px, selout, contour cassé | 1 à 2 px, épaisseur variable |
| Anticrénelage (AA) | non | rare, à l'intérieur | sur les grandes courbes | oui, à la main |
| Texture | non | 1 ou 2 touches | par groupes de 2 ou 3 | oui |
| Décalage de teinte | faible : la valeur suffit | moyen | fort | fort |
| Idée de détail | 1 seule | 1 ou 2 | 3 ou 4, hiérarchisées | libre |

- **Petit format :** chaque pixel est une décision. On exagère la partie qui fait
  reconnaître l'objet et on supprime le reste.
- **Grand format :** on garde toutes les règles du dessin. Les clusters deviennent des
  coups de pinceau : chaque amas de couleur décrit un plan (facette, pli, reflet).

## A4. Règles implicites du dessin [Z][M][I]

- **Dessiner à travers les volumes.** Tracer aussi les parties cachées (l'arrière d'une
  sphère, le bras derrière le torse), puis effacer. Les raccords tombent juste.
- **Une ligne de centre par masse.** Elle tourne avec la masse et dit son orientation.
  Les lignes de construction dépassent un peu de la forme.
- **Asymétrie plutôt que symétrie.** La symétrie stricte est réservée à un visage de face
  ou à un objet manufacturé vu de face (et même là, la lumière la casse).
- **Cohérence.** Une fois un choix fait (volume, lumière, style de contour), on l'applique
  partout.
- **Les détails suivent la surface.** Plis, bandes, motifs, joints suivent la courbure du
  volume, grâce au maillage : un motif plat posé sur un cylindre détruit le volume.
- **Peu de détails dans la lumière.** Texture et détails vont dans les tons moyens et près
  du terminateur.
- **Les accents les plus sombres vont dans les creux** (dessous, aisselle, intérieur des
  cheveux, trou de serrure), jamais sur ce qui est devant.
- **Chevauchement net.** Une forme devant une autre coupe son contour. Pas de raccord en
  « T » lisse, et pas de tangentes (deux contours qui se touchent juste).

## A5. Pipeline pixel (pour objets et personnages)

### 5. Silhouette
- Remplir toute la forme d'une seule couleur sombre et la regarder à ×1.
- Lisible ? Reconnaissable ? Les espaces vides (entre bras et torse, entre lame et garde)
  ont-ils une forme claire ?
- Si non, on revient à la construction.

### 6. Contour (lignes « pixel-perfect »)
- **1 px d'épaisseur.** Les segments se touchent seulement en diagonale : pas d'angle en
  « L », pas de pixel doublé.
- **Courbes :** la longueur des segments change régulièrement (5-3-2-1-1, jamais
  5-2-1-2-1). Les plus longs vont en haut, en bas et sur les côtés de la courbe.
- **Diagonales :** segments égaux, ou motif régulier (2-1-2-1). Une diagonale 1:1 (pixel par
  pixel) est la plus nette.
- **Symétrie :** un objet symétrique a une **largeur impaire** s'il a un élément central
  (serrure, gemme, lame) : il lui faut une colonne de centre. Vérifier pixel par pixel
  que les deux côtés sont le miroir l'un de l'autre [T3].
- **Selout [R] :** le contour prend un ton plus sombre et plus saturé de la couleur qu'il
  entoure. Il est plus clair du côté de la lumière et plus sombre du côté de l'ombre.
  L'effet compte surtout dès 32 px.
- **Hiérarchie :** le contour extérieur est le plus sombre. Les lignes intérieures entre
  grandes masses sont en ton moyen-sombre. Les détails (plis, joints, coutures) sont juste
  un cran plus sombres que leur fond, et souvent **cassés** (interrompus).
- Pas de contour au contact du sol ni entre une main et l'objet tenu.
- Contour cassé et irrégulier pour la fourrure, les cheveux, l'herbe.

### 7. Palette et couleurs à plat
- **Palette d'abord :** poser les couleurs en carrés côte à côte et les ajuster avant de
  colorer.
- **Une rampe par matière**, triée par valeur (nombre de tons : table A3).
- **Décalage de teinte :**
  - lumière : plus claire, un peu moins saturée, la teinte tire vers le jaune ;
  - ombre : plus sombre, **plus saturée**, la teinte tire vers le rouge (couleurs chaudes)
    ou vers le bleu et le violet (couleurs froides) ;
  - jamais de noir ni de blanc purs pour ombrer ou éclairer, sauf l'éclat d'une surface
    brillante, qui peut être presque blanc.
- **Harmonie :** couleurs analogues (douces), complémentaires (une domine, l'autre est
  l'accent), ou triade. Chaudes = vitalité, froides = calme ou mystère.
- **Réutiliser** les tons d'une rampe dans une autre (l'ombre de l'or peut être le brun du
  bois) : la palette reste courte et cohérente.
- Remplir chaque zone avec le ton moyen, des grandes zones vers les petites.
- **Contrôle en gris :** chaque matière a sa valeur (A2).

### 8. Lumière et ombres (placées à la main)
- **Une seule source**, choisie à l'étape 0. Par défaut, en haut à gauche, devant.
- **Tracer d'abord le terminateur** (la limite lumière / ombre) sur chaque volume. Il suit
  le maillage. C'est une limite nette, qu'on valide avant de remplir.
- **Interdit : l'ombrage « coussin »** (des bandes sombres tout autour du bord). L'ombre se
  met du côté opposé à la lumière.
- **Les zones, avec une rampe de 5 tons (1 = le plus sombre) :**

| Zone | Où | Ton |
|---|---|---|
| Éclat | 1 à 3 px, surfaces brillantes seulement | 5 |
| Lumière directe | face tournée vers la source | 4 |
| Ton de base | demi-lumière | 3 |
| Ombre forte | bande étroite le long du terminateur, côté ombre | 1–2 |
| Ombre moyenne | le gros de l'ombre | 2 |
| Lumière réfléchie | fine bande au bord de l'ombre, côté sol | 2–3 |
| Ombre portée | sur le sol ou sur une autre pièce | 1–2 |
| Occlusion | creux où la lumière n'entre pas | 1 |

- **Ordre de pose :** ombre en aplat, ombre forte au terminateur, occlusion dans les creux,
  lumière, éclat.
- **Contraste :** tout ton de la zone éclairée est plus clair que tout ton de la zone
  d'ombre.
- **Nette ou douce :** les volumes anguleux (boîte, facette, pli marqué) ont une limite
  nette, en une marche. Les volumes ronds ont une limite adoucie par 1 ton
  intermédiaire, mais pas de dégradé large.
- **Interdit : le banding.** Deux limites de tons qui suivent le même escalier, ou des
  segments de même longueur, parallèles et alignés (même sans se toucher), font apparaître
  la grille. Décaler les limites et varier les longueurs.
- **Ombre portée au sol :** plus sombre au centre, plus claire vers l'extérieur. Pour une
  icône d'inventaire, elle est facultative.

### 8b. Matières [R][T3]

| Matière | Contraste | Éclat | Règle clé |
|---|---|---|---|
| Métal poli (lame, armure) | très fort | net, 1 à 2 px, presque blanc | bandes de reflet nettes qui suivent la forme ; l'ombre reprend la couleur de l'environnement (ciel bleuté en haut, sol chaud en bas) ; on peut passer du sombre au très clair sans transition |
| Métal mat (fer forgé) | moyen | petits points (rivets) | bord éclairé clair, bord opposé sombre, pour un ruban un peu bombé |
| Or | fort | blanc chaud | rampe brun → orange → jaune → crème ; l'ombre tire vers le brun-rouge, jamais vers le gris |
| Gemme taillée | très fort | 2×2 px presque blanc, plus 1 px en face | facettes à limites nettes ; la facette **opposée** à la lumière est souvent claire (la lumière traverse) ; couleurs très saturées |
| Verre | faible sur le verre lui-même | trait fin qui suit la courbe | on voit à travers : le contenu ou le fond reste visible ; un reflet en arc suit la forme |
| Liquide | moyen | à la surface | surface plus claire ; point lumineux au fond, du côté opposé à la lumière (la lumière traverse) |
| Bois | moyen | aucun | fibres et joints dans le sens du bois, par groupes de 2 ou 3 ; chanfrein clair sous chaque joint |
| Cuir | moyen | faible, large | coutures en pointillés réguliers ; bords usés plus clairs |
| Tissu | doux | aucun | plis depuis les points de tension ; limites douces |
| Peau | doux | très faible | ombre rouge-violet ou brun-rose ; jamais de tramage |
| Pierre | moyen | aucun | facettes, fissures cassées, tramage possible comme texture |
| Organique (champignon, plante) | moyen | doux, large | volumes ronds ; petites taches ou nervures qui suivent le maillage ; lumière réfléchie colorée dessous |

### 9. Détails (en dernier)
- **Règle du tiers :** la texture et les détails couvrent environ 1/3 de la surface. Les
  2/3 restants sont calmes : l'œil complète.
- **Par 2 ou 3 :** un détail se répète en petits groupes (rivets, plis, mèches, fibres),
  jamais sur toute la surface. Varier la taille, l'inclinaison et l'espacement.
- **Raconter :** un ou deux détails qui disent quelque chose (une entaille, une étiquette,
  une usure).
- Finir par quelques accents du ton le plus sombre, seulement dans les creux.

### 10. Nettoyage
- **Orphelins :** un pixel seul d'une couleur. Le garder seulement s'il est voulu (éclat,
  rivet). Sinon, le supprimer ou le grouper en amas de 2 à 3 px.
- **Anticrénelage (AA) [R] :**
  - d'abord se demander s'il est nécessaire, souvent non. Pas d'AA sous 32 px ;
  - la valeur du pixel d'AA dépend de la part du pixel que la ligne couvrirait : beaucoup
    couvert → proche du trait, peu couvert → proche du fond ;
  - pas de moyenne des deux couleurs (boue) : prendre un ton de la palette de valeur proche ;
  - plus le segment est long, plus la rangée d'AA est longue ;
  - l'AA reste **à l'intérieur** du contour extérieur, car le fond du jeu change ;
  - jamais d'AA automatique sur chaque angle.
- Supprimer tous les pixels de construction.
- Chaque pixel doit mériter sa place.

### 11. Contrôle final (obligatoire)
Produire une planche avec l'image à ×1, ×2 et agrandie, sur fond clair et sur fond sombre,
retournée en miroir, en silhouette noire, en niveaux de gris, et **en situation** (case
d'inventaire, tuile, à côté d'un autre sprite du même jeu).

Questions communes :
1. La silhouette se reconnaît-elle seule ?
2. Les matières se séparent-elles en gris ?
3. Le volume se lit-il, et la lumière vient-elle d'une seule source ?
4. Le point d'intérêt a-t-il le plus fort contraste ?
5. Reste-t-il des orphelins, du banding, de l'ombrage coussin, des « L » dans le contour ?
6. L'objectif de l'étape 0 est-il atteint ?

Puis les questions propres à l'objet (B5) ou au personnage (C8).

**Bilan :** 3 points réussis, 3 points à améliorer. Les 3 points à améliorer deviennent les
objectifs du dessin suivant.

---

# Partie B — Objets

## B0. Intention
Écrire en 3 à 5 lignes :
- **ce que c'est et à quoi ça sert** dans le jeu : icône d'inventaire, objet posé au sol,
  élément d'interface ;
- la **taille** (celle de la tuile ou de la case) et le nombre de couleurs (table A3) ;
- la **vue**, la même pour tout le set : de face ou de profil pour une icône, ou inclinée
  vers l'avant pour un jeu vu de dessus ;
- la lumière : en haut à gauche, comme les autres objets du jeu ;
- la matière principale et **l'accent** (la seule couleur saturée).

## B1. Cadre et placement
- Garder 1 px de marge. L'objet remplit la case : une case vide autour rend l'icône faible.
- **Objets longs** (épée, bâton, flèche) : sur la **diagonale** de la case, pointe en haut
  à droite. La diagonale 1:1 donne le contour le plus propre et la plus grande longueur.
- Centrer **visuellement** (le centre de masse), pas seulement le cadre englobant.
- Fixer les rapports clés en données : par exemple col = 1/3 du ventre, poignée = 1/4 de la
  longueur d'une épée.

## B2. Volumes
- Décomposer l'objet en **formes primitives** : sphère, cylindre, cône, boîte, disque.
- Tracer pour chaque volume : son axe, une ligne de maillage, et le **terminateur** pour la
  lumière choisie.
- Une boîte vue un peu d'en haut montre son dessus (plus clair) et sa face avant.
- Un objet plat (lame, bouclier) a quand même une épaisseur : un biseau ou un bord de 1 px
  qui accroche la lumière.

## B3. Forme iconique
- **Exagérer ce qui fait reconnaître l'objet :** la garde d'une épée, le bouchon d'une
  potion, le chapeau d'un champignon, la serrure d'un coffre. Simplifier le reste.
- Comparer avec 2 ou 3 icônes du même objet que l'on connaît : quelle partie la rend
  lisible ?
- Faire 2 silhouettes (R7) et garder la plus claire à ×1.

## B4. Matière et lumière
- Choisir la rampe de chaque matière (A5 étape 7) et sa règle (tableau 8b).
- Placer le **point d'intérêt** : c'est là que vont l'éclat et le plus fort contraste.

## B5. Contrôle propre aux objets
- L'objet se reconnaît-il en 1 seconde dans une case d'inventaire ?
- Va-t-il avec les autres objets du set (même vue, même lumière, même épaisseur de
  contour, même densité de détail) ?
- Les éléments centraux sont-ils vraiment centrés (largeur impaire) ?
- Les matières se distinguent-elles en gris ?

---

# Partie C — Personnages

Construction d'un personnage, puis pipeline A5. L'anatomie (C9) s'applique à **chaque**
étape, pas seulement aux détails.

## C0. Intention
- Qui est le personnage, son attitude, un mot clé d'émotion (« calme », « menaçant »).
- La vue (face, 3/4, profil), la taille, le nombre de couleurs.
- Le style : nombre de têtes de haut (2 à 3 pour un chibi, 4 à 5 en RPG, 6 à 8 en
  semi-réaliste), et le style du visage (manga, RPG simple, semi-réaliste).
- 2 à 3 références, avec pour chacune **ce qu'on lui prend**. On combine, on ne copie pas.
- Un objectif prioritaire (la pose, le visage, la lumière…).

## C1. Proportions
- Hauteur totale avec 1 à 2 px de marge. Tête H = hauteur ÷ nombre de têtes. Dessiner à
  côté une **colonne de têtes** et lire les repères dessus.

  | Repère | Canon 7 têtes | Canon 8 têtes |
  |---|---|---|
  | Menton | 1 | 1 |
  | Épaules | ≈ 1,3 | ≈ 1,3 |
  | Tétons, aisselles | ≈ 2 | 2 |
  | Bas de la cage, coudes | ≈ 2,6 à 3 | 3 (nombril) |
  | Entrejambe, poignets | ≈ 3,7 à 4 | 4 (moitié) |
  | Bout des doigts | ≈ 4,6 (mi-cuisse) | ≈ 4,8 à 5 |
  | Genoux | ≈ 5,2 | ≈ 5,8 à 6 |
  | Chevilles | ≈ 6,7 | ≈ 7,6 |
  | Plante des pieds | 7 | 8 |

- Le canon de 8 têtes allonge surtout les jambes.
- Valable pour tous les styles : le pubis est au milieu du corps ; coudes au bas de la
  cage ; poignets au pubis ; genoux au milieu des jambes.
- Chibi de 3 têtes : 1 tête, 1 torse, 1 jambe ; les bras ont la longueur du torse.
- Largeurs : épaules d'homme ≈ 2 à 2,3 H, de femme ≈ 1,8 à 2 H.
- **Contrôle :** les bras ne sont pas trop courts (erreur la plus fréquente) ; les espaces
  vides (bras / torse, entre les jambes) ont une forme plausible.

## C2. Pose : ligne d'action et squelette
- **Une seule courbe** pour la ligne d'action (en C ou en S), jamais droite.
- Le torse est un rectangle déformable : ligne des épaules en haut, ligne du bassin en bas.
  En mouvement, elles s'inclinent : un côté est étiré, l'autre pincé.
- Placer les articulations **en données**, puis les relier en fil de fer.
- **Contrapposto :** côté de la jambe d'appui, la hanche monte et l'épaule descend. La
  cheville d'appui est sous la base du cou (ligne de gravité).
- En 3/4, le côté éloigné est plus étroit.
- 2 variantes (R7), puis **exagérer** la meilleure : une pose fidèle mais molle est pire
  qu'une pose exagérée.
- **Contrôle :** la pose tient debout ; chaque articulation plie dans son sens (C9-A) ; pas
  de pieds joints au garde-à-vous sauf si l'intention le demande [T1] ; les deux côtés
  évitent la symétrie et les parallèles.

## C3. Volumes (le mannequin)
Ordre obligatoire :
1. tête (sphère + plan du visage) et ligne de centre ;
2. cage thoracique (œuf ou boîte) et bassin (bol ou boîte), qui tournent et s'inclinent
   séparément, chacun avec sa croix de centre ;
3. **cercles d'articulations** : épaules (qui débordent de la cage), coudes, poignets,
   hanches, genoux (rotule devant), chevilles ;
4. cylindres effilés entre les cercles (cuisse plus large que le mollet, bras plus large
   que l'avant-bras ; l'avant-bras est en forme de bouteille) ;
5. cou en cylindre, qui part de l'arrière du crâne et entre dans le torse vers l'avant ;
6. mains en blocs, pieds en cales (≈ 1 tête de long).

Puis :
- **maillage :** une ligne verticale et une horizontale sur chaque masse, comme une ficelle
  nouée autour ; elles guident les détails et les ombres ;
- **cube, sphère ou cylindre :** le cube donne de la solidité, la sphère de la douceur.
  C'est un choix de style, à garder cohérent ;
- **angle difficile :** dessiner d'abord une boîte en perspective, puis placer les volumes
  dedans.

**Main (dès qu'elle dépasse 6 px) :**
1. paume en trapèze, plus large aux jointures qu'au poignet ;
2. 4 jointures sur un **arc** (le majeur le plus haut) ;
3. doigts en 3 phalanges de plus en plus courtes ; majeur le plus long, puis annulaire et
   index, puis auriculaire ;
4. pouce qui part **du côté du poignet**, relié par une masse charnue ; 2 phalanges
   visibles ; son bout arrive vers la base de l'index ;
5. contour qui enveloppe les cercles, articulations un peu gonflées ;
6. trait plus marqué dans l'ombre et aux superpositions.

## C4. Tête et visage
**Forme :** femme = menton plus haut, mâchoire ronde, cou fin ; homme = mâchoire anguleuse,
cou presque aussi large que la mâchoire ; personne âgée = visage plus long. Vérifier la
longueur du cou : un cou nu trop long était le principal défaut du test 1.

**De face :**
1. cercle du crâne et ligne de centre jusqu'au menton ;
2. mâchoire : deux lignes presque verticales puis en angle ; menton en petit segment plat ;
3. lignes horizontales : yeux à mi-hauteur de la tête (un peu plus bas en manga), bas du
   nez au bas du cercle, bouche au tiers entre nez et menton ;
4. yeux en amandes séparés d'une largeur d'œil ; paupière du haut plus épaisse ;
5. nez ≈ écart entre les yeux ; coins de la bouche à l'aplomb des pupilles ;
6. oreilles de la ligne des sourcils au bas du nez ;
7. cou depuis l'intérieur de la mâchoire, avec le V des sterno-cléido-mastoïdiens.

**En 3/4 (Loomis) :** sphère, puis cercle aplati sur le côté (l'oreille juste derrière
et sous son centre) ; ligne de centre **courbe** ; plan du visage en bloc sous la sphère ;
mâchoire depuis l'arrière du cercle latéral ; le côté éloigné est raccourci (œil du fond
plus étroit).

**Guides obligatoires :** ligne de centre, ligne des yeux, ligne du nez, ligne de la
bouche. Sans elles, la symétrie dérive.

**Placement selon le style :**
- semi-réaliste : 3 tiers égaux (cheveux → sourcils → bas du nez → menton) ;
- manga : yeux sous le milieu de la tête, nez entre ce milieu et le menton, oreilles en
  « C » entre la ligne des yeux et celle du nez.

**Yeux :** femme ≈ 1/6 de la hauteur de la tête, homme ≈ 1/8 ; largeur ≈ 1/4. Iris ovale,
pupille ≈ 1/4 de l'iris, haut de l'iris plus sombre ; reflet au même endroit sur les deux
yeux.

**Expressions :**

| Émotion | Sourcils | Yeux | Bouche |
|---|---|---|---|
| Colère | vers le nez | — | — |
| Tristesse, peur | vers les oreilles | peur : petites pupilles | — |
| Détermination | baissés | mi-clos | — |
| Surprise | levés | grands ouverts | — |
| Calme | — | — | petite |

**En pixels :**
- tête de 6 px ou moins : 1 px sombre par œil, pas de nez ;
- tête de 7 à 12 px : yeux de 1×2 ou 2×2 px, nez en 1 px d'ombre ;
- au-delà : on applique les rapports ci-dessus.

**Attrait [T1] :** le visage est **majoritairement dans la lumière**. Pas de visage coupé en
deux moitiés claire et sombre (effet masque), sauf intention dramatique.

## C5. Vêtements et design
- Les vêtements épousent les volumes, puis s'en écartent selon le tissu. Les plis partent
  des points de tension (épaules, coudes, taille, genoux).
- **Langage de formes :** rond = doux, carré = solide, triangle = dynamique ou dangereux.
  Une forme dominante.
- **Hiérarchie :** primaires (torse, jupe, cape, masse de cheveux), puis secondaires
  (manches, ceinture, col), puis tertiaires (boutons, bijoux). Varier les tailles, garder
  des zones calmes.

## C6. Cheveux [M][C]
**Construction :**
- Dessiner d'abord **la tête chauve**, puis une enveloppe de volume un peu plus grande que
  le crâne. Des cheveux tirés ou attachés épousent le crâne, à 1 ou 2 px.
- **Ligne des cheveux en premier.** Chez un adulte : cheveux → haut des yeux = yeux → nez.
  Un enfant a un front plus grand ; un front d'enfant sur un adulte le fait paraître
  dégarni. Formes : arrondie, en M, plate. Une ligne qui recule part du M et finit en arc.
- **Point d'attache** (queue, chignon) : toutes les mèches tirées vont vers lui en suivant
  le crâne. Queue haute : l'attache se voit. Queue basse : les cheveux pendent vers elle.
  Couettes : derrière les oreilles, à la même hauteur, alignées avec les yeux.

**Mèches :**
- Des mèches et touffes, jamais des fils. Épaisseurs et longueurs variées.
- Une pointe finit sur **1 px**.
- Cheveux en pointes : les plus longues à l'arrière ; leur hauteur suit un demi-cercle
  autour du crâne.
- Ondulé : des « S ». Bouclé : des demi-cercles plus petits vers les racines et les pointes.
  Spirales : un cône qui se vrille. Tresse : 3 bandes, des « Y », puis arrondir.
- Cheveux longs : plus fins en haut, plus gonflés en bas ; ils suivent les épaules et la
  poitrine, ne tombent jamais tout droit.
- Frange : épaisseurs variées. Mèches de côté : elles partent entre les yeux et les
  oreilles. Raie : placée par rapport aux yeux.
- Quelques mèches libres pour faire naturel.

**Couleur :**
- Clairs : surtout des ombres. Moyens : tons moyens et ombres franches. Foncés : masse
  sombre, reflet facultatif.
- **Reflet en arc** qui suit le crâne, découpé en tirets dans le sens des mèches.
- L'ombre suit le sens des cheveux. Ombre portée de 1 px sous la frange. Arrière du crâne,
  nuque et dessous de l'attache dans l'ombre.

**Contrôle :** ligne des cheveux à la bonne hauteur ; mèches vers le point d'attache ;
pointes à 1 px ; reflet en arc ; pointes visibles, pas cachées derrière un bras [T2].

## C7. Astuces de figure [R]
- Le geste d'abord, l'anatomie par-dessus : si les muscles cassent la ligne d'action, on
  redessine les muscles, pas la pose.
- Sur un membre, un côté plutôt droit et l'autre courbe, puis ça s'inverse. Deux côtés
  courbes = saucisse molle.
- Lignes de rythme qui se croisent : une courbe d'un côté se continue plus bas de l'autre
  côté.
- Un bras tendu n'est jamais parfaitement droit.
- Les petits traits d'ombre suivent le sens des fibres du muscle.
- À partir de 64 px de haut, ombrer par **plans musculaires** : chaque grand muscle est une
  facette, claire si tournée vers la lumière.

## C8. Contrôle propre aux personnages
1. La pose exprime-t-elle l'intention ? Les proportions suivent-elles la colonne de têtes ?
2. Le visage est-il attirant et majoritairement éclairé ? Se lit-il à ×1, comme les mains ?
3. Chaque articulation est-elle plausible ? Le deltoïde dépasse-t-il la cage ? Le cou
   part-il de derrière la mâchoire ? Le pouce part-il du poignet ?
4. Peut-on nommer les muscles qui font le contour de chaque membre (C9-I) ? Reste-t-il un
   bras « tube » ou un torse « rectangle » ?
5. Les cheveux passent-ils le contrôle C6 ?
6. À côté de la référence, le dessin tient-il la comparaison ?

## C9. Anatomie de référence [I]
Simplifier la **forme**, jamais l'anatomie : chaque muscle visible se voit (bosse, plan,
creux) ou pousse le contour ou le vêtement.

### A. Articulations

| Articulation | Type | Mouvement | Erreur interdite |
|---|---|---|---|
| Épaule | rotule | tous les sens ; bras levé au-dessus de l'horizontale = l'omoplate et la clavicule montent | bras levé avec l'épaule restée basse |
| Coude | charnière | plie seulement vers l'avant, ~145° | coude plié en arrière ou sur le côté |
| Avant-bras | rotation | c'est l'avant-bras qui tourne la paume, pas le coude | paume retournée sans torsion |
| Poignet | ellipsoïde | beaucoup vers l'avant, moins vers l'arrière, peu sur les côtés | main à 90° sur le côté |
| Hanche | rotule emboîtée | avant beaucoup, arrière ~20°, côté ~45° | jambe en arrière très haut sans bascule du bassin |
| Genou | charnière | plie seulement vers l'arrière ; la rotule reste devant | genou plié vers l'avant |
| Cheville | charnière | haut ~20°, bas ~45° | pied à angle droit en pointe |
| Cou | 7 vertèbres | tourne ~80° de chaque côté | tête tournée à 180° |
| Taille | colonne souple | la cage et le bassin bougent l'un par rapport à l'autre | torse d'un seul bloc dans une pose dynamique |

### B. Longueurs
- Un os ne change jamais de longueur : en raccourci il paraît plus court, mais ses deux
  articulations gardent leur distance en 3D.
- Bras : épaule → coude ≈ coude → poignet. Main ≈ longueur du visage.
- Jambe : hanche → genou ≈ genou → cheville. Pied ≈ 1 tête.
- Bras le long du corps : coude à la taille, poignet à l'entrejambe, doigts à mi-cuisse.

### C. Raccords
- **Épaule :** le deltoïde couvre la tête de l'humérus et dépasse la cage ; le pectoral
  passe dessous ; les trapèzes descendent en pente du cou à l'épaule.
- **Hanche :** la jambe s'attache sur le côté du bassin ; la cuisse part en diagonale vers
  l'intérieur du genou.
- **Cou :** il part de derrière la mâchoire et sous les oreilles ; la nuque commence plus
  haut que la gorge.
- **Coude, genou, poignet, cheville :** plus étroits et osseux ; les muscles gonflent
  au-dessus et en dessous.

### D. Rythme du contour
Les bosses d'un membre ne sont jamais face à face à la même hauteur :
- cuisse : bombée haut dehors, bas dedans (vaste interne en goutte au-dessus du genou) ;
- mollet : haut dehors, plus bas dedans ;
- bras : deltoïde en haut dehors ; triceps derrière, plus haut que le biceps devant ;
- avant-bras : large près du coude (le brachio-radial part du bras), fin au poignet.

### E. Torse
- Cage = œuf plus haut que large, avec l'arc costal en V renversé. Bassin = bol plus petit.
  Entre les deux, la taille, souple.
- Face : pectoraux, grand droit (6 à 8 blocs), obliques, dentelé. Dos : trapèze en losange,
  grand dorsal en V, fessiers.
- La poitrine est posée **sur** la cage et suit son maillage.

### F. Homme / femme

| | Homme | Femme |
|---|---|---|
| Épaules | ≈ 2 à 2,3 têtes | ≈ 1,8 à 2 têtes, plus tombantes |
| Taille | peu marquée | marquée (sablier) |
| Bassin | étroit, plus haut | plus large ; hanches ≈ épaules |
| Cuisses | droites | plus en diagonale vers les genoux |
| Cou | ≈ largeur de la mâchoire | fin |
| Avant-bras | épais | plus fins, tendons moins marqués [T2] |

### G. Poids
- La ligne de gravité tombe du creux du cou sur le pied d'appui.
- Côté qui porte : hanche haute, jambe tendue, cuisse contractée. Côté libre : genou fléchi.
- Un objet lourd tenu d'une main fait pencher le torse du côté opposé.

### I. Carte des muscles

| Zone | Muscles | Ce qu'ils font au dessin |
|---|---|---|
| Cou | sterno-cléido-mastoïdien, trapèze | V de derrière l'oreille au creux du cou ; pente cou → épaule |
| Épaule | deltoïde | bosse qui dépasse de la cage ; finit en pointe au tiers du bras |
| Poitrine | grand pectoral | éventail du sternum, entre sous le deltoïde |
| Dos | trapèze, grand dorsal, érecteurs | V du dos ; deux colonnes le long de la colonne |
| Flanc | dentelé, obliques | dents sous l'aisselle ; bourrelet au-dessus du bassin |
| Bras | biceps, triceps | biceps rond devant ; triceps en fer à cheval, plus long, derrière |
| Avant-bras | brachio-radial, fléchisseurs, extenseurs | bosse en haut et dehors ; tendons vers le poignet |
| Cuisse | quadriceps, couturier, adducteurs | couturier en diagonale ; vaste interne juste au-dessus du genou |
| Jambe | jumeaux, soléaire, tibia | mollet plus haut dedans ; tibia presque droit devant |
| Cheville | malléoles | interne haute, externe basse |

- Un muscle **contracté** est plus court et plus rond ; un muscle **étiré** est plus long et
  plus plat. Dans chaque pose, un côté est pincé et l'autre étiré.
- Les muscles s'emboîtent comme des coins, jamais posés côte à côte comme des saucisses.

---

## Résumé

**Objet :** intention et usage → cadre (diagonale pour les objets longs) → volumes et
terminateur → forme iconique → silhouette → contour → palette → lumière selon la matière →
détails → nettoyage → contrôle en situation.

**Personnage :** intention et références → proportions → pose → volumes → visage →
vêtements → cheveux → silhouette → contour → palette → ombres à la main → détails →
nettoyage → contrôle avec la référence.

Un concept à la fois, du grand au petit. Aucun pixel de détail tant que la structure n'est
pas juste.
