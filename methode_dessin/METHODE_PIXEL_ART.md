# Méthode de pixel art — objets et personnages (v6)

On construit d'abord, on détaille ensuite. Cette méthode réunit le dessin classique
(construction par volumes, ligne d'action, anatomie) et les règles du pixel art
(silhouette, valeurs, clusters, lignes propres, rampes, lumière).

**Comment l'utiliser :**
- la **partie A** vaut pour tout : règles de travail, lisibilité, tailles, couleurs, lumière,
  matières, finition et contrôle ;
- la **partie B** donne les étapes de construction d'un **objet** ;
- la **partie C** donne les étapes de construction d'un **personnage** (anatomie, visage,
  cheveux) ; **C10** donne les règles par taille (8 à 128 px) ;
- un dessin suit B ou C pour la construction, puis le pipeline A5 pour les pixels ;
- la section **A4b** (simplifier) s'applique dès qu'une taille est imposée.

**Sources :** [Z] *Apprendre à tout dessiner avec Zephy* · [M] livre de dessin manga ·
[I] planches d'anatomie fournies · [C] planches sur les cheveux fournies ·
[R] recherches (Loomis, Bridgman, Proko, tutoriels d'anticrénelage, de matières et de
lisibilité d'icônes, simplification des formes) · [P] planches fournies (cheveux, œil, arche,
cristal, flamme, déclinaisons par taille, projections) · [T1]…[T4] leçons de nos propres tests.

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

## A4b. Simplifier les formes [R][P]

Simplifier, c'est **enlever et exagérer** : on retire ce qui ne se lit pas, et on grossit ce
qui fait reconnaître le sujet.

- **Enveloppe d'abord.** Une grande forme simple autour de tout le sujet (cercle, boîte,
  triangle, goutte). Elle donne les proportions et la silhouette avant le moindre détail.
- **Grand, moyen, petit.** Une forme domine (environ 70 % de l'image), une forme moyenne
  l'accompagne, et une petite zone porte le détail. Deux formes de même taille se battent.
  Exemples : le chapeau, le pied et l'anneau d'un champignon ; un grand cristal, un moyen
  et un petit, chacun avec un angle différent.
- **Langage de formes.** Rond = doux, gentil. Carré = solide, lourd. Triangle = rapide,
  dangereux. La forme dominante donne le caractère.
- **Sous-formes dans le même sens.** Une masse se découpe en sous-formes (langues d'une
  flamme, mèches, feuilles, plumes) qui suivent **un même mouvement**. Leur taille varie,
  pas leur direction générale.
- **Le plus petit détail nécessaire fixe la taille.** Se demander quel est le plus petit
  élément indispensable (les yeux, une serrure, une graine) et combien de pixels il lui
  faut. Choisir la taille à partir de là. Dans le doute, plus petit. Grossir la taille ne
  dispense pas de simplifier : on ne fait que repousser le problème.
- **Ce que chaque taille peut porter :**

| Taille | Ce qui tient |
|---|---|
| 8 px | la silhouette et 2 ou 3 masses de couleur, rien d'autre |
| 16 px | la catégorie (oiseau ou chat) et **un** détail d'identité |
| 32 px | une expression, l'équipement, 1 ou 2 détails |
| 48 à 64 px | la texture, plusieurs éléments, des détails hiérarchisés |

- **Redessiner à chaque taille, jamais réduire.** Une réduction garde des détails qui n'ont
  plus la place de se lire. On repart de la silhouette à la nouvelle taille.
- **Marqueurs d'identité.** Choisir 2 ou 3 marqueurs (une couleur, une forme forte, un
  accessoire) et les garder **à toutes les tailles**, quitte à les agrandir quand le reste
  rétrécit. Le reste disparaît avant eux.
- **Formes difficiles en marches nettes.** Une bosse molle ou une longue pente qui donne des
  escaliers irréguliers se redessine avec des cassures à 90° et 45°. Un arc fin et presque
  horizontal disparaît à petite taille : on l'épaissit ou on le supprime.
- **Chaque pixel fait double travail.** À petite taille, un pixel est une tache de peinture :
  il peut être à la fois contour, ombre et forme. Les formes deviennent des symboles (un œil
  = 1 px, une graine = 2 px).
- **Formes qui riment.** Les variantes d'un même objet ou d'un même set reprennent les mêmes
  formes (même courbe de chapeau, même angle de garde) : différentes, mais de la même
  famille.
- **Vide utile.** Les espaces vides (entre les cristaux, sous l'arche, entre les langues de
  feu) ont eux-mêmes une forme claire. Un vide informe est une erreur de silhouette.

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
- **Ordre selon la forme [P] :** objet dur ou taillé (cristal, arme, meuble) : trait propre
  d'abord, puis couleur. Forme molle ou organique (cheveux, flamme, feuillage) : masse de
  couleur d'abord, sous-formes, puis contour posé **à la fin** autour de la forme trouvée.
- **Épaisseur de trait [P] :** le trait le plus épais va en haut et à l'extérieur (paupière
  du haut, dessus d'un chapeau). Les traits du bas et de l'intérieur sont plus fins ou
  cassés.
- **Lignes secondaires en couleur [P] :** pli de paupière, bas de l'œil, joints fins : un ton
  coloré plus clair que le contour, jamais la couleur du contour.
- **Couleur du contour :** le ton le plus sombre du set, chaud ou froid, mais pas le noir
  pur. Le même pour tous les objets d'un set (le brun-bordeaux d'une carotte, d'un pain et
  d'un bol).

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
- **Palette en chaîne [P] :** les rampes se relient en une seule suite de teintes voisines
  (bleu → cyan → vert pâle → crème → rose → rouge → violet → sombre). Chaque couleur sert
  à plusieurs endroits (le cyan du blanc de l'œil, le crème du reflet de l'iris).
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
- **Un ton par face [P] :** sur un volume à faces planes (bloc, cristal, arche), chaque face
  a **un seul ton** selon son orientation : dessus = le plus clair, face tournée vers la
  lumière = clair, face avant = moyen, dessous et intérieur = sombre.
- **Creux inversés [P] :** dans un creux (alvéole de gaufre, trou, intérieur d'une arche),
  l'ombre est sur la paroi **du côté de la lumière** et la paroi opposée est éclairée.
  C'est l'inverse d'une bosse.
- **Ombre d'un surplomb :** ce qui avance projette une ombre sur ce qui est dessous. La
  paupière assombrit le haut de l'iris et du blanc de l'œil ; la frange, le haut du front ;
  le chapeau, le haut du pied.
- **Deuxième lumière (contre-jour) [P], facultative :** une lumière plus faible, d'une
  teinte contrastée (souvent froide : violet, bleu), arrive de l'arrière. Elle pose une
  bande de 1 px sur les bords **opposés** à la lumière principale, jamais sur tout le
  contour. Elle détache le sujet du fond.
- **Objet qui émet de la lumière [P] (feu, magie, lampe) :** on ombre à l'envers. Le cœur
  est le plus clair (presque blanc), entouré de couches de plus en plus sombres ; les
  bords et les pointes sont les plus sombres. Le cœur est décalé vers la source (la base
  d'une flamme). Pas de contour sombre autour.

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
| Pierre taillée (blocs, arche) | moyen | aucun | un ton par face ; joints **perpendiculaires** au bord (rayons sur un arc) ; mousse sur le dessus et dans les fentes |
| Cristal | très fort | 1 à 2 px blancs sur les arêtes et les pointes | prismes à pointe ; un ton par facette ; contour coloré (rouge sombre pour un cristal rouge) ; contre-jour froid possible |
| Feu, magie | — | le cœur entier | ombrage inversé (8) ; langues dans le même sens ; étincelles détachées |
| Nourriture cuite (pain, gaufre) | moyen | petits points sur les bosses | rampe chaude crème → orange → brun ; dessus brillant, côtés plus sombres ; motifs (graines, alvéoles) qui suivent la surface |
| Organique (champignon, plante) | moyen | doux, large | volumes ronds ; petites taches ou nervures qui suivent le maillage ; lumière réfléchie colorée dessous |

### 8c. Variation de couleur (après les valeurs) [P]
Une fois les valeurs justes, on varie les **teintes sans changer les valeurs** (contrôle en
gris : l'image ne doit pas bouger) :
- ombres vers le violet ou le bleu, lumières vers le jaune (rappel de l'étape 7) ;
- le long d'une forme longue, la teinte glisse : cheveux chauds en haut, rosés aux pointes ;
  flamme orange au centre, magenta aux bords, cœur blanc-cyan ;
- 1 ou 2 facettes d'une autre teinte sur un cristal ou une gemme.

### 9. Détails (en dernier)
- **Règle du tiers :** la texture et les détails couvrent environ 1/3 de la surface. Les
  2/3 restants sont calmes : l'œil complète.
- **Par 2 ou 3 :** un détail se répète en petits groupes (rivets, plis, mèches, fibres),
  jamais sur toute la surface. Varier la taille, l'inclinaison et l'espacement.
- **Raconter :** un ou deux détails qui disent quelque chose (une entaille, une étiquette,
  une usure).
- Finir par quelques accents du ton le plus sombre, seulement dans les creux.
- **Les motifs suivent la forme [P] :** joints en rayons sur un arc, stries courbes sur un
  cylindre (carotte), grille raccourcie par la perspective (gaufre), graines orientées
  selon la surface (pain).
- **La nature décide où vont les détails [P] :** mousse et poussière sur les dessus et dans
  les fentes ; herbe qui cache la base et ancre l'objet au sol ; usure sur les arêtes.
- **Particules [P] (étincelles, vapeur, éclats) :** 1 ou 2 px, par groupes de 2 ou 3,
  détachées de l'objet, de plus en plus petites en s'éloignant. Elles restent rares.
- **Éclats aux arêtes :** sur une surface taillée, l'éclat va là où deux faces se
  rencontrent et sur les pointes.

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
6. Y a-t-il une forme dominante, une moyenne et une petite (A4b) ? Les marqueurs d'identité
   se voient-ils à ×1 ?
7. L'objectif de l'étape 0 est-il atteint ?

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
- la **projection**, la même pour tout le set (tableau B0b) ;
- la lumière : en haut à gauche, comme les autres objets du jeu ;
- la matière principale et **l'accent** (la seule couleur saturée).

## B0b. Projection [P]

| Projection | On voit | Usage |
|---|---|---|
| De face (jeu de plateforme) | la face avant seule | icônes, jeux de côté |
| Vue de dessus « 3/4 » | le dessus **et** la face avant, pas les côtés | RPG vus de dessus, comme les jeux Pokémon : bâtiments, objets posés |
| De dessus pur | le dessus seul | cartes, toits |
| Isométrique | le dessus et deux côtés | lignes en pente 2:1 (2 px de côté pour 1 de haut) |
| Dimétrique 45° | le dessus en losange et deux côtés | carte tournée de 45° |
| Oblique | la face avant et un côté fuyant | décor, effet de profondeur simple |

- Une seule projection par jeu. Un objet en 3/4 à côté d'un objet de face casse le monde.
- Pour ce hack (moteur GBA vu de dessus) : objets du monde en **vue 3/4 de dessus**,
  icônes d'inventaire de face ou légèrement inclinées, toutes de la même façon.

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
- **Extrusion [P] :** pour donner de l'épaisseur à une forme (arche, anneau, roue) : tracer
  la face, la **dupliquer et la décaler** dans la direction de la profondeur, tracer la
  forme intérieure, couper ce qui est caché, puis ajouter les bouts de face intérieure
  visibles. On colore ensuite face par face (8).
- **Couches empilées [P] (burger, gâteau, pile) :** toutes les couches ont la même
  inclinaison d'ellipse. Leurs valeurs alternent (clair, sombre, clair) pour qu'elles se
  séparent même en gris.

## B3. Forme iconique
- **Exagérer ce qui fait reconnaître l'objet :** la garde d'une épée, le bouchon d'une
  potion, le chapeau d'un champignon, la serrure d'un coffre. Simplifier le reste.
- Comparer avec 2 ou 3 icônes du même objet que l'on connaît : quelle partie la rend
  lisible ?
- Faire 2 silhouettes (R7) et garder la plus claire à ×1.

## B4. Matière et lumière
- Choisir la rampe de chaque matière (A5 étape 7) et sa règle (tableau 8b).
- Placer le **point d'intérêt** : c'est là que vont l'éclat et le plus fort contraste.

## B4b. Décliner un objet en plusieurs tailles [R][P]
Exemple : une carotte en 8, 16 et 32 px.
- **8 px :** silhouette, 2 tons, feuillage en un seul amas.
- **16 px :** un éclat, 1 ou 2 stries, contour sombre.
- **32 px :** stries courbes qui suivent le cylindre, 4 tons, éclat allongé, feuillage en
  2 ou 3 lobes.
- Même angle, même couleur de contour, mêmes marqueurs à toutes les tailles. Le nombre
  d'idées augmente avec la taille (A3), mais l'identité ne change pas.

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
- au-delà : on applique les rapports ci-dessus ;
- détail par taille (yeux, expressions, format GBA) : **C10**.

**Œil en grand (dès 32 px de tête) [P], dans l'ordre :**
1. trait : paupière du haut épaisse (2 à 3 px) avec un cil qui part au coin extérieur ;
   pli de paupière séparé au-dessus ; paupière du bas fine et cassée ;
2. iris en aplat sombre ; blanc de l'œil **jamais blanc** : bleu clair ou gris, plus
   sombre sous la paupière ;
3. iris sombre en haut (ombre de la paupière), clair en bas, avec un fin arc lumineux en
   bas (la lumière traverse) ;
4. pupille, puis reflet de 1 à 2 px presque blanc, du côté de la lumière ;
5. paupière du haut doublée à l'intérieur d'un ton coloré (son ombre sur l'œil) ;
6. pli et paupière du bas éclaircis en ton de peau rosé (lignes secondaires en couleur) ;
7. une touche de couleur froide en haut de l'iris pour la profondeur.

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

**Ordre de pose en pixels [P] :**
1. la masse entière en un aplat, comme un casque ;
2. la lumière sur la masse entière (un anneau de reflet qui suit le crâne, l'ombre sous la
   masse et à la raie) ;
3. découpage en grandes mèches, qui suivent toutes le même mouvement ;
4. contour posé autour des mèches, pointes ouvertes ;
5. chaque mèche reçoit sa propre lumière et sa propre ombre ;
6. variation de couleur (8c) : chaud en haut, rosé ou violet vers les pointes et dans les
   ombres ;
7. le reflet en arc se casse en tirets dans le sens des mèches.

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

## C10. Personnages en pixel art, taille par taille [R]
Plus le personnage est petit, plus on **exagère** la tête et les yeux et plus on
**supprime** (nez, bouche, doigts, cou). On choisit la taille d'après ce qu'il faut lire :
à 16 px, une direction et une coiffure ; à 32 px, une expression ; à 64 px, un visage.

### A. Table par hauteur du personnage

| Hauteur | Têtes | Tête / hauteur | Yeux | Nez, bouche | Bras, mains | Couleurs |
|---|---|---|---|---|---|---|
| 8 px | 1 à 1,5 | ≈ 60 % | 1 px chacun | aucun | aucun ou 1 px | 3 à 4 |
| 16 px | 2 à 3 | 45 à 60 % | 1×1 ou 1×2 | aucun | bras 1 px, main = 1 px de peau | 5 à 8 |
| 20 à 24 px | 1,6 à 2,5 | 50 à 62 % | 1×2 | bouche rare (1 px) | bras 1 à 2 px | 8 à 13 |
| 32 px | 2,5 à 4 | 40 à 50 % | 2×2 avec 1 px de reflet | nez = 1 px d'ombre, bouche 1 à 2 px | main = bloc 2×2, pouce 1 px | 10 à 14 |
| 48 px | 4 à 5 | 30 à 40 % | 3×2 à 3×3 : paupière, iris, pupille, reflet | nez par l'ombre, bouche 2 à 3 px | moufle + pouce | 12 à 16 |
| 64 px | 5 à 6 | 25 à 35 % | 4×3 et plus, avec blanc de l'œil | nez en plan d'ombre, lèvre du bas par son ombre | doigts en 2 masses | 14 à 20 |
| 96 px et plus (portrait) | réaliste | — | recette « œil en grand » (C4) | narine, lèvres | doigts séparés | 16 (portrait GBA) |

- Style « héroïque » : tête sous 35 % ; c'est alors une capuche, une cape ou une arme qui
  porte la silhouette.
- Les yeux 2×2 avec reflet n'apparaissent qu'au-dessus de 16×24 ; en dessous, un reflet
  blanc rend le regard fou.
- Le blanc de l'œil n'existe qu'à partir de 3 px de large.

### B. Format Pokémon GBA (notre ROM)
- **Sprite de dresseur sur la carte :** cellule 16×32 ; le personnage occupe ≈ 14×20 px,
  pieds sur la dernière rangée, vide au-dessus. Tête ≈ 60 % de la hauteur (≈ 1,6 tête),
  yeux 1×2 sombres, **pas de bouche ni de nez**, 13 à 14 couleurs.
- **Palette :** 16 couleurs dont l'index 0 transparent → 15 utiles. Répartition type :
  contour 1, peau 3, cheveux 3, vêtement principal 3, vêtement secondaire 2 à 3, yeux et
  détail 1 à 2, blanc 1.
- **Portrait ou sprite de combat :** 5 tons de peau, 9 pour le reste ; contour = la couleur
  la plus sombre. Palette sûre : 3 couleurs × 3 tons ; un objet sombre prend 2 tons +
  contour, un objet clair jusqu'à 5 ; les cheveux peuvent prendre un 4e ton.

### C. Placer le visage aux petites tailles
1. **La frange fixe la ligne des yeux** : les yeux se collent sous les cheveux, sur la
   moitié basse de la tête. Yeux bas et écartés = jeune et mignon ; plus hauts et serrés =
   plus âgé ou plus dur.
2. **Écart :** à 16 px, 2 px de peau entre les yeux (1 px fait loucher, 3 px élargit la
   face). Sous les yeux, 1 à 2 rangées de peau, puis le menton.
3. **Pas de cou** sous 32 px : la tête repose sur les épaules.
4. **3/4 :** tout le visage glisse vers le côté regardé ; l'œil du fond fait 1 px de moins
   ou touche le bord du visage ; dès 32 px, le nez est 1 px qui dépasse du contour.
5. **Profil :** un seul œil, 1 px en retrait du bord du visage ; l'oreille en 1 à 2 px de
   peau plus sombre au milieu de la tête.
6. **Dos :** aucun trait, les cheveux couvrent la tête ; on garde la même hauteur de tête.

### D. Recettes d'yeux, pixel par pixel
- **1×1 :** le ton le plus sombre de la palette (pas forcément noir).
- **1×2 vertical (standard GBA) :** 2 px sombres ; variante : haut sombre, bas couleur de
  l'iris.
- **2×2 :** rangée du haut sombre (paupière) ; en bas, 1 px d'iris + 1 px de reflet clair
  du côté de la lumière.
- **3×3 :** rangée du haut = paupière sombre qui déborde de 1 px vers l'extérieur (le cil) ;
  au milieu, pupille + iris + reflet ; en bas, 1 px d'iris clair ou de blanc bleuté.
- **4×4 et plus :** recette « œil en grand » de C4.
- **Partout :** les deux yeux ont la même forme (sauf en 3/4), le reflet est **du même côté**
  sur les deux, et le noir pur est réservé aux pupilles.
- **Sourcils :** à 16 px, la frange les remplace ; dès 24 à 32 px, un trait de 2 à 3 px dans
  le ton sombre des cheveux, assez haut (plus haut = plus doux).

### E. Expressions au pixel
On ne touche **qu'aux sourcils, aux yeux et à la bouche** ; le reste de la tête est
recopié à l'identique, sinon l'animation tremble.

| Émotion | 16 px (yeux seuls) | 32 px et plus |
|---|---|---|
| Joie | yeux en ligne de 2×1 ou en « ^ » | bouche ouverte, joues 1 px rosé |
| Colère | yeux 1×1 + 1 px d'ombre au coin intérieur haut | sourcils en V, yeux plus petits |
| Tristesse | yeux 1 px plus bas | intérieur des sourcils levé, bouche courbée vers le bas |
| Surprise | yeux 2×2 | yeux agrandis, bouche ronde sombre |
| Fatigue, ennui | yeux 2×1 horizontaux | paupière à mi-hauteur de l'iris |

### F. Couleurs du personnage
- **3 tons par partie**, 6 à 12 couleurs pour un petit personnage. Une teinte dominante pour
  le personnage, une couleur d'accent.
- **Peau :** base pêche ; ombre vers le rose ou le rouge-violet ; ombre profonde vers le
  violet-bleu ; lumière vers le jaune. ≈ 20° de décalage de teinte par cran, **dans le même
  sens pour toutes les rampes**.
- **Contour :** jamais noir ; un brun-rouge ou violet très sombre. Contour extérieur plus
  sombre que le contour intérieur. Contre la peau, le trait prend l'ombre de la peau ou
  disparaît (selout).
- **Séparation :** membres proches plus clairs, membres éloignés plus sombres.
- **Lumière :** une direction fixe pour tout le projet ; le visage reste majoritairement
  éclairé (C4).

### G. Vue de dessus 3/4 (jeu type Pokémon)
- On voit le **haut des épaules** ; le torse passe un peu sous la tête.
- Sprite 1 tuile de large × 2 de haut ; les pieds sont toujours sur la même rangée.
- **Directions :** face d'abord, puis dos, puis profil ; l'autre profil = miroir, sauf
  détail asymétrique (sac, mèche, arme) qu'on redessine.
- Même hauteur et même épaisseur de membres dans toutes les directions : on fait tourner
  le personnage pour vérifier.
- Hauteurs fixes par type : enfant < femme < homme ; une personne âgée un peu voûtée.
- Deux personnages peuvent se chevaucher en hauteur, jamais en largeur.

### H. Animation
- Mannequin en aplats d'abord ; costume et équipement sur des calques séparés.
- **Marche :** pas, passage, autre pas, passage (3 images uniques) ; le corps monte de 1 px
  aux passages ; les pieds ne glissent pas ; 100 à 150 ms par image. Plus fluide : 6 images.
- **Attente :** respiration de 1 px (tête et épaules) ; on tient les poses extrêmes plus
  longtemps ; cheveux et reflets bougent par petits pas réguliers.
- Le rebond de tête est asymétrique (il monte plus vite qu'il ne descend).

### I. Mains, cheveux, identité
- **Mains :** grossies volontairement ; on les dessine avant de régler les chevauchements.
- **Cheveux en petit :** une masse unique, 2 à 3 mèches finissant en pointe de 1 px, un
  reflet en bande cassée (jamais une rangée régulière). La coiffure est le premier marqueur
  d'identité.
- **Identité :** une forme forte (coiffure, chapeau, cape), une couleur dominante, une
  asymétrie voulue. Silhouettes types : guerrier large, mage en trapèze (robe), archer fin,
  soigneur en tons pastel.
- **Test :** en noir uni, à ×1, on reconnaît le personnage et sa direction.

### J. Procédure
1. Taille et rôle → lire la table A (part de la tête, yeux, couleurs).
2. Mannequin en aplats : tête, torse, membres proches, membres éloignés, ligne de sol.
3. **Le visage tout de suite** : il fixe l'échelle (ligne des yeux, recette D).
4. Coiffure et vêtements, puis test de la silhouette noire.
5. Palette (F), contour et selout, lumière.
6. Expressions, directions, animation.
7. Contrôle K.

### K. Contrôle et erreurs fréquentes
1. La tête et les yeux respectent-ils la table A ? Pas de nez ni de bouche à 16 px ?
2. Les yeux sont-ils sous la frange, bien espacés, reflets du même côté ?
3. Courbes : au plus 2 longueurs de pente, pas d'écart de plus de 1 entre pentes voisines,
   un angle vif finit sur 1 px.
4. Anticrénelage : 1 à 2 px par coin au plus, jamais sur le contour extérieur d'un sprite
   de jeu.
5. Pas de banding, pas de pillow shading, pas de pixel orphelin sur le visage.
6. Lisible à ×1, en noir uni, et dans toutes les directions ?
7. Budget de couleurs tenu (15 + transparent sur GBA) ?

---

## Résumé

**Objet :** intention, usage et projection → cadre (diagonale pour les objets longs) →
volumes et terminateur → simplification (A4b) → forme iconique → silhouette → contour →
palette → lumière selon la matière → variation de couleur → détails → nettoyage → contrôle en situation.

**Personnage :** intention et références → proportions → pose → volumes → visage →
vêtements → cheveux → table par taille (C10) → silhouette → contour → palette → ombres à la main → détails →
nettoyage → contrôle avec la référence.

Un concept à la fois, du grand au petit. Aucun pixel de détail tant que la structure n'est
pas juste.
