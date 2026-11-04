# Méthode de dessin de personnage en pixel art — règles obligatoires

Ce document oblige à dessiner comme un artiste : on construit d'abord, on détaille ensuite.
Il réunit la méthode classique du dessin de figure (Loomis, Vilppu, ligne d'action,
construction par volumes) et les règles du pixel art (silhouette, clusters, lignes propres,
rampes de couleurs, lumière).

## Règles générales (toujours valables)

- **R1. Ne jamais sauter une étape.** Chaque étape produit une image enregistrée
  (`etape_XX_nom.png`, agrandie ×6 au minimum). L'étape suivante commence seulement
  quand l'image a été **regardée** et validée avec sa grille de contrôle.
- **R2. Toujours du grand au petit.** D'abord la pose, ensuite les masses, puis la silhouette,
  la couleur, la lumière, et les détails en dernier. Un détail ne corrige jamais une erreur
  de construction : on revient à l'étape fautive.
- **R3. Décrire avant de dessiner.** Le squelette et les volumes sont d'abord écrits en
  données (coordonnées des articulations, centres et tailles des masses). Ensuite, on les
  trace. Pas de pixels « placés au feeling ».
- **R4. Regarder à deux tailles.** Chaque contrôle se fait à ×1 (taille réelle) **et** à
  l'agrandi. Ce qui ne se lit pas à ×1 n'existe pas.
- **R5. Corriger en boucle.** À chaque étape, on note au moins un défaut, on le corrige et on
  revérifie. On passe à la suite seulement quand il ne reste rien d'important.

## Étape 0 — Intention

Écrire en 3 à 5 lignes :
- qui est le personnage, son attitude et son émotion (un seul mot clé : « calme »,
  « menaçant », etc.) ;
- la vue (face, 3/4, profil), la taille de la toile et le nombre de couleurs ;
- le **style de proportions** : nombre de têtes de haut (2 à 3 pour du chibi, 4 à 5 pour un
  style RPG, 6 à 7,5 pour du semi-réaliste) ;
- la direction de la lumière (exemple : en haut à gauche, devant).

## Étape 1 — Grille des proportions

- Fixer la hauteur totale en pixels, en gardant 1 à 2 px de marge en haut et en bas.
- Hauteur de la tête : H = hauteur totale ÷ nombre de têtes. Tracer une ligne
  horizontale tous les H pixels.
- Repères pour un adulte de 7 à 7,5 têtes (à mettre à l'échelle selon le style) :
  - menton à 1 H ;
  - tétons et aisselles vers 2 H ;
  - nombril et coude vers 3 H ;
  - entrejambe et poignets vers 3,5 à 4 H, ce qui fait la moitié du corps ;
  - genoux vers 5 à 5,5 H ;
  - pieds à 7 à 7,5 H.
- Largeurs :
  - épaules d'homme ≈ 2 à 2,3 H, de femme ≈ 1,8 à 2 H ;
  - hanches de femme ≈ largeur des épaules, d'homme un peu moins.
- Pour un chibi de 3 têtes : 1 tête, 1 torse, 1 jambe. Les bras ont la longueur du torse.
  Le coude arrive à la taille, et le bout des doigts juste sous l'entrejambe.
- **Contrôle :** les repères tombent sur les bonnes lignes, et les bras ne sont ni trop
  courts (erreur la plus fréquente) ni trop longs.

## Étape 2 — Ligne d'action et squelette

- Tracer d'abord **une seule courbe** pour la ligne d'action, qui suit la colonne de la tête
  au bassin et à la jambe d'appui. Elle doit être courbe (en C ou en S), jamais
  parfaitement droite, sinon la pose est raide.
- Placer les articulations **en données** :
  - tête ;
  - cou, puis épaule gauche et droite ;
  - coudes, poignets, mains ;
  - centre du bassin, hanches gauche et droite ;
  - genoux, chevilles, pointes de pieds.
- Relier les articulations en « bonhomme fil de fer ». Ajouter la ligne des épaules et la
  ligne des hanches.
- **Équilibre et contrapposto :**
  - si le poids repose sur une jambe, la hanche de ce côté **monte** et l'épaule du même côté
    **descend**, si bien que les deux lignes s'inclinent en sens opposés ;
  - la cheville d'appui est à la verticale de la base du cou (ligne de gravité).
- **Raccourcis en 3/4 :** le côté le plus éloigné est plus étroit. L'épaule, la hanche et
  l'œil du fond se rapprochent de l'axe central.
- **Contrôle :**
  - la pose tient debout sans tomber ;
  - les longueurs des os sont symétriques à gauche et à droite (sauf raccourci voulu) ;
  - la pose exprime l'intention de l'étape 0.

## Étape 3 — Volumes (le mannequin)

Habiller le squelette de formes simples. Chaque forme est décrite en données, avec son
centre, sa taille et son inclinaison :
- **tête :** une boule. On coupe les côtés (plans de Loomis), puis on trace :
  - un axe vertical au milieu du visage, qui tourne avec la tête en 3/4 ;
  - une ligne des yeux à **la moitié de la hauteur de la tête** ;
  - la ligne du nez au tiers inférieur du visage ;
  - les oreilles entre la ligne des yeux et celle du nez.
- **cage thoracique :** un œuf ou une boîte inclinée ; **bassin :** une boîte ou un bol.
  Ces deux masses s'inclinent en sens opposés en contrapposto.
- **cou :** un cylindre, qui part de l'arrière du crâne et entre dans le torse vers l'avant.
- **membres :** des cylindres effilés. La cuisse est plus large que le mollet, le bras plus
  large que l'avant-bras.
- **mains :** un bloc pour la paume (≈ taille du visage, du menton au milieu du front), avec
  un pouce séparé. Les doigts sont groupés en mitaine si la taille est petite.
- **pieds :** une cale ou un triangle, aussi long qu'une tête environ.
- **Contrôle :**
  - les masses se chevauchent correctement, l'avant passant devant l'arrière ;
  - le volume est cohérent avec la vue (3/4 : on voit un côté de la boîte du torse).

## Étape 4 — Vêtements et design par-dessus le mannequin

- Les vêtements **épousent** les volumes, puis s'en écartent selon le tissu. Les plis partent
  des points de tension (épaules, coudes, taille, genoux) et suivent des cylindres ou des
  cônes.
- **Langage de formes :**
  - rond = doux ou gentil ;
  - carré = solide ou stable ;
  - triangle = dynamique ou dangereux.
  Choisir une forme dominante.
- Varier les tailles : grandes, moyennes et petites formes, avec des zones calmes.
  Un grand élément vaut mieux que beaucoup de petits.

## Étape 5 — Silhouette

- Remplir tout le personnage d'une **seule couleur unie**.
- **Contrôle :**
  - la silhouette remplie en noir reste lisible : on comprend la pose et l'accessoire ;
  - les bras ou l'objet tenu se détachent du corps, avec des « trous » de fond lisibles ;
  - c'est lisible à ×1.
  Sinon, revenir à l'étape 2 ou 4 et modifier la pose.

## Étape 6 — Contour propre (lignes « pixel-perfect »)

- Le contour fait 1 px d'épaisseur. Les segments se touchent **seulement en diagonale** :
  pas d'angles en « L » ni de pixels doublés.
- **Courbes :** la longueur des segments change régulièrement, par exemple 5-3-2-1-1, et
  jamais 5-2-1-2-1. Les plus longs segments vont en haut, en bas et sur les côtés d'une
  courbe.
- **Diagonales droites :** tous les segments ont la même longueur, ou suivent un motif
  régulier (2-1-2-1).
- Les lignes intérieures se tracent seulement où le contraste manque (tête contre cou,
  bras devant le torse). On peut juste les suggérer.
- Ne pas tracer de contour au point de contact avec le sol ou entre la main et l'objet tenu.
- Le contour n'est pas noir pur. **Selout :** chaque partie du contour prend une teinte plus
  sombre de la couleur qu'elle entoure, avec un contour plus clair du côté de la lumière.

## Étape 7 — Couleurs à plat

- Une **rampe** par matière (peau, cheveux, tissu 1, tissu 2, métal), de 3 à 5 tons triés
  par luminosité.
- **Décalage de teinte :**
  - les ombres vont vers le froid (bleu ou violet) ;
  - les lumières vont vers le chaud (jaune ou orange) ;
  - jamais de noir ou de blanc pur dans une rampe ;
  - l'ombre de la peau est un violet ou brun-rose désaturé, pas un marron gris.
- Peu de couleurs. **Un seul accent saturé**, comme une ceinture ou un foulard, attire l'œil.
- Remplir chaque zone avec le ton moyen de sa rampe.
- **Contrôle en niveaux de gris :** les grandes zones se distinguent par leur valeur, pas
  seulement par leur teinte.

## Étape 8 — Lumière et ombres

- Une **seule source de lumière**, celle de l'étape 0. Chaque ombre doit pouvoir dire d'où
  vient la lumière.
- **Interdit : l'ombrage « coussin »,** c'est-à-dire des bandes plus sombres le long du bord,
  tout autour. L'ombre se met du côté opposé à la lumière, en suivant le **volume de
  l'étape 3**.
- Zones dans l'ordre :
  1. ton de base ;
  2. ombre propre, avec une limite d'ombre nette (le « terminateur ») ;
  3. ombres portées, très nettes (sous le menton, la frange, les bras, les plis) ;
  4. lumière ;
  5. reflet, petit et seulement sur les surfaces brillantes.
- **Interdit : le banding,** c'est-à-dire deux bandes de tons qui suivent exactement le même
  escalier de pixels. Décaler les limites.
- Ajouter une ombre portée au sol, sous les pieds.
- Tramage (dithering) : seulement s'il sert aussi de texture.

## Étape 9 — Détails (en dernier)

- **Visage :**
  - les yeux sont sur la ligne de l'étape 3 ;
  - l'écart entre les yeux vaut un œil ;
  - à petite taille, l'œil se fait en 1 à 2 px sombres, avec un pixel de blanc ou un reflet
    seulement si on a la place ;
  - pas de pupilles ni de dents trop petites, qui deviennent du bruit.
- **Mains :** la forme de mitaine de l'étape 3, avec un pouce lisible. Les doigts sont
  indiqués par 1 px sombre si on a la place.
- Cheveux en **mèches groupées** (gros clusters), pas en fils.
- Choisir quelques points forts pour la lumière et supprimer les autres.

## Étape 10 — Nettoyage

- **Pixels orphelins :** un pixel isolé d'une couleur, sans voisins de la même couleur. Pour
  chacun, se demander s'il est nécessaire. Sinon, le supprimer ou le grouper en un amas de
  2 à 3 px.
- **Clusters :** des amas de tons clairs et voulus. Le moins de petits amas possible.
- **Anticrénelage (AA) :** à la main et avec parcimonie, seulement sur les grands escaliers
  des courbes importantes. Trop d'AA rend l'image floue.
- Chaque pixel doit « mériter sa place ».

## Étape 11 — Contrôle final (obligatoire)

Produire une planche avec :
- l'image à ×1 et à ×6 ;
- l'image retournée horizontalement, pour faire ressortir les défauts d'anatomie ;
- la silhouette en noir ;
- la version en niveaux de gris.

Répondre honnêtement :
1. La pose exprime-t-elle l'intention ?
2. Les proportions respectent-elles la grille (bras, tête, jambes) ?
3. Le volume se lit-il, et la lumière est-elle cohérente ?
4. Le visage et les mains sont-ils lisibles à ×1 ?
5. Reste-t-il des orphelins, du banding, de l'ombrage coussin, des contours en « L » ?

Corriger, puis refaire la planche.

## Résumé en une phrase

**Pose → squelette → volumes → silhouette → contour → couleurs → lumière → détails →
nettoyage → contrôle.** On ne pose pas un pixel de détail tant que la structure n'est pas
juste.
