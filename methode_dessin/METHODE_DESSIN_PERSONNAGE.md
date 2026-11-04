# Méthode de dessin de personnage en pixel art — règles obligatoires (v2)

Ce document oblige à dessiner comme un artiste : on construit d'abord, on détaille ensuite.
Il réunit la méthode classique du dessin de figure (Loomis, Vilppu, ligne d'action,
construction par volumes) et les règles du pixel art (silhouette, clusters, lignes propres,
rampes de couleurs, lumière).

**v2 :** ajout des règles tirées de deux livres de dessin et des leçons du test 1
(samouraï, avec méthode contre sans méthode).
Chaque règle nouvelle porte sa source :
- **[Z]** *Apprendre à tout dessiner avec Zephy* (Leber et Hollants) ;
- **[M]** le livre de dessin manga (Arienne Coudert) ;
- **[T1]** une leçon du test 1 ;
- **[I]** les 10 planches d'illustration fournies : canons à 7 et 8 têtes, tête de face
  et en 3/4, main en 6 étapes, torses en boîtes, torse en 4 étapes, écorchés
  simplifiés en couleur, visage pas à pas.

Les règles des livres sont adaptées au pixel art : un « trait épais » devient un contour
plus sombre, un « crayon 2B » devient un ton de la rampe, etc.

---

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
- **R6. Un calque par concept [Z].** Le dessin est un empilement de calques : un calque par
  étape (pose, proportions, volumes, visage, contour, couleurs, ombres, détails). On ne
  travaille qu'un concept à la fois. Le calque précédent reste visible **en transparence**
  sous le nouveau, comme un guide, puis il est masqué dans l'image finale.
- **R7. Une couleur par étape de construction [Z].** Les calques de construction se tracent
  dans des couleurs vives différentes : par exemple rouge pour la pose, bleu pour les
  repères de proportion, vert pour les volumes et le maillage. Ces couleurs ne doivent
  jamais apparaître dans l'image finale.
- **R8. Penser en rapports, jamais en mesures [Z].** On ne dit pas « le bras fait 14 px » au
  hasard. On écrit « l'avant-bras = 1 tête » ou « le torse = 2 fois la largeur du cou ».
  Les pixels sont calculés à partir des rapports.
- **R9. Refaire l'esquisse [Z].** La première version d'une pose ou d'un visage est rarement
  la bonne. Il faut produire **au moins 2 variantes** de la pose (étape 2) et du visage
  (étape 3b), puis garder la meilleure. Recommencer n'est pas un échec.
- **R10. Le moins de traits possible [M][Z].** Peu de lignes, longues et sûres. On fait une
  ligne par direction : à chaque changement de direction, un nouveau segment commence.
  Il y a trois types de lignes :
  - « I » (droite), pour la solidité et les premières esquisses ;
  - « C » (courbe), pour les volumes ;
  - « S » (ondulée), pour la fluidité, avec modération : cheveux, tissus.
  On commence en « I », on arrondit en « C », on finit par les « S ».
- **R11. Utiliser TOUTES ses connaissances d'anatomie [I].** Tu sais comment un corps est
  fait : os, articulations, muscles, amplitudes de mouvement, répartition du poids.
  Tu dois t'en servir à **chaque** étape, pas seulement au moment des détails.
  - Avant de tracer un membre, se demander : quel os est dessous, quelle articulation
    le relie, dans quel sens elle plie, quel muscle est étiré, lequel est contracté.
  - Une pose ou une forme impossible anatomiquement est une erreur, même si elle « a l'air
    bien » à ×1.
  - La section « Anatomie et articulations » ci-dessous est la liste minimale. Elle ne
    remplace pas ce que tu sais : elle t'oblige à le vérifier.

## Règles implicites (ce que les livres font sans le dire)

Ces règles ne sont pas écrites telles quelles dans les livres. Elles se voient dans
chaque exemple pas à pas, et elles sont aussi obligatoires.

- **I1. Esquisse claire d'abord, trait final sombre par-dessus [M][Z].** On n'appuie jamais
  dès le début. En pixel art, la construction se fait dans un ton clair et transparent. Le
  contour final se pose ensuite, en ton sombre, sur un calque séparé.
- **I2. Dessiner à travers les volumes [Z].** Chaque volume est tracé comme s'il était
  transparent, y compris ses parties cachées : le bras derrière le torse, l'arrière du
  crâne sous les cheveux. On efface ensuite ce qui est caché. Ainsi les membres se
  raccordent au bon endroit.
- **I3. Exagérer la pose par rapport à la référence [Z].** On amplifie toujours un peu la
  courbe de la ligne d'action et l'inclinaison des épaules et des hanches. Une pose fidèle
  mais molle est pire qu'une pose exagérée.
- **I4. Asymétrie plutôt que symétrie [Z].** Les formes symétriques sont statiques et raides.
  Il faut varier : une mèche plus longue, un pan de tissu qui pend d'un côté, une épaule
  plus haute. La symétrie stricte est réservée au visage vu de face.
- **I5. La cohérence prime sur la « vérité » [Z].** Plusieurs choix sont valables : volume
  cube ou sphère, ordre des épaisseurs de trait. Une fois un choix fait, on l'applique
  partout de la même façon.
- **I6. Les détails suivent la surface [Z].** Plis, motifs, ceinture, bandeau, rayures :
  tout suit la courbure du volume (le maillage de l'étape 3). Un motif plat posé sur un
  cylindre détruit le volume.
- **I7. Moins de détails dans la lumière [Z].** Les zones éclairées montrent peu de texture.
  Les détails et la texture vont surtout dans les tons moyens et près du terminateur.
- **I8. Les accents les plus sombres vont dans les creux et au fond [Z].** Les petites
  touches de ton le plus sombre (« aplats noirs ») se mettent seulement dans les
  creux : aisselle, entre les doigts, sous le menton, intérieur des cheveux, plis profonds.
  On les met aussi sur les éléments de l'arrière-plan, jamais sur ce qui est devant.
- **I9. Observer la référence à chaque étape [Z].** On revient à la référence à chaque
  étape et pas seulement au début. Le regard alterne sans cesse entre la référence et le
  dessin.
- **I10. Les articulations sont dessinées comme des formes [I].** Dans toutes les planches,
  épaules, coudes, poignets, hanches, genoux et chevilles sont des **cercles ou
  disques**, posés avant les segments. Les membres sont des cylindres tendus **entre**
  ces cercles.
- **I11. Une ligne de centre traverse chaque masse [I].** Tête, cage, bassin, et même
  chaque doigt reçoivent une ligne médiane. Elle tourne avec la masse et dit son
  orientation.
- **I12. Les lignes de construction dépassent [I].** Les lignes des épaules, des yeux et
  du maillage débordent un peu de la forme. Elles appartiennent au volume entier, pas au
  seul contour visible.

## Anatomie et articulations — logique obligatoire [I] (R11)

Ces règles s'appliquent dès l'étape 2. On les revérifie à l'étape 11.

### A. Types d'articulations et sens de pliage

| Articulation | Type | Ce qu'elle peut faire | Erreur interdite |
|---|---|---|---|
| Épaule | rotule (boule) | tourne dans tous les sens ; le bras levé au-dessus de l'horizontale **entraîne l'omoplate et la clavicule**, donc l'épaule monte | bras levé avec une épaule restée basse et plate |
| Coude | charnière | plie **seulement vers l'avant**, jusqu'à ~145° ; tendu, il est presque droit | coude plié vers l'arrière ou sur le côté |
| Avant-bras | rotation (radius autour du cubitus) | la main tourne paume en haut / en bas ; c'est l'avant-bras qui tourne, pas le coude | paume retournée sans torsion des muscles de l'avant-bras |
| Poignet | ellipsoïde | plie vers l'avant (beaucoup), vers l'arrière (moins), un peu sur les côtés | main pliée à 90° sur le côté |
| Hanche | rotule, plus emboîtée que l'épaule | jambe en avant (beaucoup), en arrière (peu, ~20°), sur le côté (~45°) | jambe en arrière très haut sans bascule du bassin |
| Genou | charnière | plie **seulement vers l'arrière** ; la rotule reste devant et monte quand on s'accroupit | genou plié vers l'avant, rotule qui disparaît |
| Cheville | charnière + un peu de rotation | pied vers le haut (~20°), vers le bas (~45°) | pied à angle droit en position pointée |
| Cou | colonne de 7 vertèbres | penche, tourne (~80° de chaque côté), se plie en avant plus qu'en arrière | tête tournée à 180°, cou cassé à angle vif |
| Taille (colonne lombaire) | flexible | la cage et le bassin tournent et s'inclinent **l'un par rapport à l'autre** | torse rigide d'un seul bloc dans une pose dynamique |

### B. Longueurs et raccourcis

- La longueur d'un os **ne change jamais** : en 3/4 ou en raccourci, il paraît plus court
  mais ses deux articulations restent à la même distance en 3D. Écrire les longueurs en
  données une fois, puis seulement les projeter.
- Bras : épaule→coude ≈ coude→poignet (le bras est légèrement plus long). La main fait à
  peu près la longueur du visage (menton → racine des cheveux) [I].
- Jambe : hanche→genou ≈ genou→cheville. Le pied fait ≈ 1 tête de long.
- Bras le long du corps [I] : coude au niveau de la taille (bas de la cage), poignet au
  niveau de l'entrejambe, bout des doigts vers le milieu de la cuisse.
- Les deux côtés du corps ont les **mêmes longueurs**. Un bras plus court qu'un autre doit
  s'expliquer par un raccourci.

### C. Comment un membre se raccorde

- **Épaule [I] :** le deltoïde est une coque qui couvre la tête de l'humérus et **dépasse la
  cage** sur le côté. Le pectoral passe **sous** le deltoïde et s'accroche au bras. Les
  trapèzes descendent en pente du cou à l'épaule : le cou n'entre jamais à angle droit
  dans des épaules horizontales.
- **Hanche [I] :** la jambe s'attache sur le **côté** du bassin, pas en dessous. La cuisse
  part en diagonale de l'extérieur de la hanche vers l'intérieur du genou ; le sartorius
  suit cette diagonale.
- **Cou [I] :** il part de **derrière** la mâchoire et sous les oreilles ; les deux
  sterno-cléido-mastoïdiens forment un V de derrière les oreilles au creux du sternum.
  La nuque commence plus haut que la gorge (sous l'arrière du crâne).
- **Coude et genou [I] :** à l'articulation, le membre est plus étroit et plus « osseux » ;
  les muscles gonflent au-dessus et en dessous.

### D. Rythme du contour (muscles décalés) [I]

- Les bosses musculaires d'un membre ne sont **jamais face à face** à la même hauteur. Elles
  alternent :
  - **cuisse :** l'extérieur est bombé haut (vaste externe) et l'intérieur bombé bas, juste
    au-dessus du genou (vaste interne, en goutte) ;
  - **mollet :** l'extérieur est bombé **haut** et l'intérieur bombé **plus bas** ;
  - **bras :** le deltoïde est en haut et dehors, le biceps devant et le triceps derrière,
    plus haut que le biceps ;
  - **avant-bras :** il est large et musclé près du coude (brachioradial, la « dent » qui
    part du bras et passe le coude), fin et plat près du poignet.
- Résultat : le contour d'un membre est une suite de courbes « C » alternées, en léger S,
  jamais deux parenthèses symétriques ().

### E. Torse : deux masses et une liaison souple [I]

- **Cage thoracique = un œuf** (ou une boîte), plus haut que large. Son bas forme une arche
  en V renversé (arc costal) au milieu.
- **Bassin = un bol ou une boîte** plus petit, sous un espace libre : la taille, où il n'y
  a que des muscles (abdominaux, obliques).
- Les deux masses **tournent, se penchent et s'inclinent séparément**. Chacune a sa propre
  ligne de centre et sa croix de maillage. La ligne de centre du torse devient une
  courbe en S quand le corps se tord.
- Les sphères des épaules se posent aux coins hauts et extérieurs de la cage.
- Muscles de face : pectoraux (deux plaques sous les clavicules), grand droit de
  l'abdomen (6 à 8 blocs qui rétrécissent vers le bas, jusqu'au pubis), obliques sur les
  côtés, dentelé sous l'aisselle. De dos : trapèze en losange, grand dorsal en V jusqu'à la
  taille, fessiers (moyen en haut et sur le côté, grand en bas).
- **Poitrine :** elle est posée **sur** la cage et suit son orientation et son maillage. Le
  haut part sous la clavicule. Elle n'est jamais collée à plat devant une cage vue de
  profil.

### F. Différences homme / femme (même anatomie, formes différentes) [I][Z]

| | Homme | Femme |
|---|---|---|
| Épaules | ≈ 2 à 2,3 têtes, deltoïdes larges | ≈ 1,8 à 2 têtes, plus tombantes |
| Cage | grande, pectoraux en plaques | plus petite et courte |
| Taille | peu marquée (rectangle) | marquée (sablier) |
| Bassin | étroit, plus haut | plus large, plus bas ; hanches ≈ largeur des épaules |
| Cuisses | droites | partent plus en diagonale vers les genoux, plus d'écart en haut |
| Cou | épais, ≈ largeur de la mâchoire | fin |
| Bras au repos | à peine écartés | coudes plus près de la taille |

### G. Poids et équilibre

- La ligne de gravité part du creux du cou et tombe sur le pied d'appui, ou entre les deux
  pieds si le poids est réparti.
- Le côté qui porte : hanche haute, jambe tendue, muscles de la cuisse contractés (plus
  ronds). Le côté libre : genou un peu fléchi, hanche basse.
- Un objet lourd tenu d'une main fait pencher le torse **du côté opposé** pour compenser.

### H. Pixel art : comment appliquer l'anatomie à petite taille

- Même si une articulation fait 1 px, sa **position** vient des données anatomiques, et la
  direction du pliage doit être juste.
- **À partir de 32 px de haut :** marquer le coude et le genou par un pixel de rétrécissement
  ou un changement de pente du contour. Marquer le deltoïde par une petite bosse qui
  dépasse de la cage.
- **À partir de 64 px :** appliquer le rythme décalé (D) au contour des membres.
- Au-delà, ajouter les plans musculaires (E) dans l'ombrage, comme des facettes, à la
  manière des écorchés simplifiés.

---

## Étape 0 — Intention

Écrire en 3 à 5 lignes :
- qui est le personnage, son attitude et son émotion (un seul mot clé : « calme »,
  « menaçant », etc.) ;
- la vue (face, 3/4, profil), la taille de la toile et le nombre de couleurs ;
- le **style de proportions** : nombre de têtes de haut (2 à 3 pour du chibi, 4 à 5 pour un
  style RPG, 6 à 7,5 pour du semi-réaliste) ;
- le **style du visage** [M][T1] : manga (grands yeux bas, nez minimal), RPG simple
  ou semi-réaliste. Ce choix fixe les règles de l'étape 3b ;
- la direction de la lumière (exemple : en haut à gauche, devant).

Ajouts v2 :
- **Références [Z][T1].** Lister 2 à 3 références, pas une seule : pose, costume, style
  d'un artiste qu'on admire. Le personnage est un « patchwork » : on combine plusieurs
  sources, on ne copie pas une image. Écrire pour chacune **ce qu'on lui prend**.
- **Un sujet + un thème [Z].** Exemple : « samouraï » + « hiver ». Le thème décide des
  accessoires et de la palette.
- **Un objectif par dessin [Z].** Écrire l'aspect qu'on veut réussir en priorité (la pose,
  le visage, la lumière…). Le contrôle final le vérifie en premier.

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
- **Repères par rapports, valables pour tous les styles [Z] :**
  - le **pubis est le milieu du corps** ;
  - le haut du corps se divise en **3 parts égales** : tête, cage thoracique, bassin ;
  - les jambes font **le double** de cette part ;
  - les genoux sont au milieu des jambes ;
  - les **coudes** sont au niveau du bas de la cage thoracique ;
  - les **poignets** sont au niveau du pubis.
- **Colonne de têtes [I].** Comme sur les planches, dessiner à gauche du personnage une
  pile de cercles de hauteur H : 7 pour un canon réaliste, 8 pour un canon héroïque
  ou de mode. Chaque repère se lit sur cette colonne.

  | Repère | Canon 7 têtes [I] | Canon 8 têtes [I] |
  |---|---|---|
  | Menton | 1 | 1 |
  | Ligne des épaules | ≈ 1,3 | ≈ 1,3 |
  | Tétons, aisselles | ≈ 2 | 2 |
  | Bas de la cage, coudes | ≈ 2,6 à 3 | 3 (nombril) |
  | Haut du bassin | ≈ 3,2 | ≈ 3,4 |
  | Entrejambe, poignets | ≈ 3,7 à 4 | 4 (moitié exacte) |
  | Bout des doigts | ≈ 4,6 (mi-cuisse) | ≈ 4,8 à 5 |
  | Genoux (centre de la rotule) | ≈ 5,2 | ≈ 5,8 à 6 |
  | Chevilles | ≈ 6,7 | ≈ 7,6 |
  | Plante des pieds | 7 | 8 |

  Le canon de 8 têtes allonge surtout **les jambes**. La tête et le torse gardent presque
  les mêmes repères.
- **Cadre et repères [Z].** Tracer le rectangle qui contient le personnage, puis marquer
  sur ses bords les repères de hauteur et de largeur (deux couleurs, cf. R7).
  Chaque grande masse se place d'abord comme un rectangle dans ce cadre.
- **Contrôle :**
  - les repères tombent sur les bonnes lignes ;
  - les bras ne sont ni trop courts (erreur la plus fréquente) ni trop longs ;
  - **espaces négatifs [Z]** : les vides entre le bras et le torse et entre les jambes ont
    une forme et une taille plausibles. Un vide trop petit ou mal formé révèle une
    proportion fausse.

## Étape 2 — Ligne d'action et squelette

- Tracer d'abord **une seule courbe** pour la ligne d'action, qui suit la colonne de la tête
  au bassin et à la jambe d'appui. Elle doit être courbe (en C ou en S), jamais
  parfaitement droite, sinon la pose est raide.
- **Le torse est un rectangle déformable [Z].** Son bord haut est la ligne des épaules, son
  bord bas la ligne du bassin. Dans une pose statique de face, ces lignes sont
  parallèles. Dans une pose en mouvement, elles s'inclinent : un côté est **étiré** (celui
  de la ligne d'action), l'autre est **plié**.
- Placer les articulations **en données** :
  - tête ;
  - cou, puis épaule gauche et droite ;
  - coudes, poignets, mains ;
  - centre du bassin, hanches gauche et droite ;
  - genoux, chevilles, pointes de pieds.
- Relier les articulations en « bonhomme fil de fer ». Ajouter la ligne des épaules et la
  ligne des hanches.
- **Les membres se tracent en lignes « S » fluides [Z].** Les membres ne sont jamais des
  bâtons droits. On marque les coudes et les genoux par une petite courbe.
  À ce stade, la dynamique passe avant l'exactitude des longueurs.
- **Équilibre et contrapposto :**
  - si le poids repose sur une jambe, la hanche de ce côté **monte** et l'épaule du même côté
    **descend**, si bien que les deux lignes s'inclinent en sens opposés ;
  - la cheville d'appui est à la verticale de la base du cou (ligne de gravité).
- **Raccourcis en 3/4 :** le côté le plus éloigné est plus étroit. L'épaule, la hanche et
  l'œil du fond se rapprochent de l'axe central.
- **Faire au moins 2 variantes (R9), puis exagérer la meilleure (I3).**
- **Contrôle :**
  - la pose tient debout sans tomber ;
  - les longueurs des os sont symétriques à gauche et à droite (sauf raccourci voulu) ;
  - la pose exprime l'intention de l'étape 0 ;
  - [T1] les pieds ne sont pas joints et alignés comme au garde-à-vous, sauf si
    l'intention le demande ;
  - [I] chaque articulation plie dans son sens et reste dans son amplitude (tableau A) ;
  - les longueurs d'os en données n'ont pas changé (B) ;
  - la ligne de gravité tombe sur l'appui (G).

## Étape 3 — Volumes (le mannequin)

Habiller le squelette de formes simples. Chaque forme est décrite en données, avec son
centre, sa taille et son inclinaison :
- **tête :** une boule pour le crâne, avec une « feuille » courbée pour le plan du
  visage [Z]. On coupe les côtés (plans de Loomis), puis on trace :
  - un axe vertical au milieu du visage, qui tourne avec la tête en 3/4 ;
  - les lignes de l'étape 3b.
- **cage thoracique :** un œuf ou une boîte inclinée ; **bassin :** une boîte, un bol ou un
  triangle [Z]. Ces deux masses s'inclinent en sens opposés en contrapposto.
- **Torse en 3 passes [I] :**
  1. deux **boîtes**, la cage et le bassin, chacune avec sa croix de centre ; on fixe leur
     rotation et leur inclinaison séparément ;
  2. on arrondit : œuf pour la cage, avec l'arc costal en V renversé en bas, sphères des
     épaules aux coins hauts, bol du bassin ;
  3. anatomie : clavicules, pectoraux ou poitrine, ligne médiane, nombril, obliques,
     tracés sur le maillage des deux masses.
- **Torse dessiné d'un geste [I]** (variante pour les poses vivantes) :
  1. une forme en trapèze effilé : ligne des épaules, ligne de centre **courbe**, ligne de
     taille ;
  2. cylindre du cou, sphère de l'épaule, triangle du sternum ;
  3. ellipses de maillage sur la cage, puis le bassin ; cercle du coude **sur la ligne de
     taille**, cercle du poignet ;
  4. formes finales sur le maillage.
- **cou :** un cylindre, qui part de l'arrière du crâne et entre dans le torse vers l'avant.
- **membres :** des cylindres effilés. La cuisse est plus large que le mollet, le bras plus
  large que l'avant-bras. Formes simplifiées [Z] :
  - épaule = trapèze, bras = rectangle ;
  - avant-bras = quille, en forme de bouteille ;
  - main = triangle ;
  - même découpage pour la jambe : cuisse, genou, jambe, pied.
- **muscles du torse [Z] :** trapèzes = triangle du cou aux épaules ; pectoraux sur le haut de
  la cage ; abdominaux jusqu'au pubis. On change la morphologie en changeant **la taille**
  des formes : un sablier donne une taille fine, un rectangle donne un corps robuste.
  L'anatomie, elle, ne change pas.
- **Mannequin articulé [I].** Ordre obligatoire, comme sur les planches de canon :
  1. tête (ovale) et ligne de centre ;
  2. barre des épaules et cage (forme à bas arrondi) ;
  3. bassin en triangle pointe en bas, ou en slip ;
  4. **cercles d'articulations** : épaules, coudes, poignets, hanches, genoux,
     chevilles ;
  5. cylindres entre les cercles ;
  6. mains en blocs, pieds en cales.
  Les cercles des épaules débordent de la cage, et les rotules sont des disques posés
  devant le genou.
- **mains :** un bloc pour la paume (≈ taille du visage, du menton au milieu du front), avec
  un pouce séparé. Les doigts sont groupés en mitaine si la taille est petite. Les
  cylindres des doigts s'emboîtent dans le cube de la paume [Z].
- **Main en 6 étapes [I]** (obligatoire dès que la main dépasse 6 px) :
  1. **Paume :** un trapèze légèrement bombé, plus large du côté des jointures que du côté
     du poignet.
  2. **Jointures :** 4 cercles posés sur un **arc**, pas sur une ligne droite. Le majeur est
     le plus haut. L'arc se creuse quand la main se ferme.
  3. **Doigts :** chaque doigt fait 3 phalanges, en cercles et cylindres, de plus en plus
     courtes vers le bout. Le majeur est le plus long, puis l'annulaire et l'index (presque
     égaux), puis l'auriculaire, qui arrive à la dernière articulation de l'annulaire.
     Les doigts pliés suivent l'arc des jointures et convergent légèrement.
  4. **Pouce :** il part du **côté du poignet**, pas du bord de la paume. Une masse
     triangulaire charnue (l'éminence thénar) le relie à la paume. Il n'a que 2
     phalanges visibles, et son bout arrive à peu près à la base de l'index.
  5. **Contour :** il enveloppe les cercles, avec des articulations légèrement gonflées et
     les segments entre elles un peu plus fins.
  6. **Trait final :** plus épais sur les bords dans l'ombre et aux superpositions, fin
     ailleurs. Les bouts des doigts sont arrondis et carrés, et on marque l'ongle s'il y a
     la place.
- **pieds :** une cale ou un triangle, aussi long qu'une tête environ.
- **Choix des volumes [Z].** Le cube donne de la solidité, la sphère de la douceur, le
  cylindre est entre les deux. C'est un choix de style, à garder cohérent (I5).
  Ensuite, les volumes de base peuvent être déformés : sphère aplatie, cylindre courbé,
  cône anguleux.
- **Maillage [Z].** Sur le calque des volumes, tracer 1 ligne verticale et 1 ligne
  horizontale de contour sur chaque masse (comme une ficelle nouée autour). Les ellipses
  penchent avec l'inclinaison de la masse. Ces lignes guideront le placement des détails
  (I6) et la limite des ombres (étape 8).
- **Angle difficile [Z].** Pour une plongée, une contre-plongée ou un objet complexe (arme,
  sac), dessiner d'abord une **boîte** en perspective, puis placer les volumes dedans.
  Pour trouver le milieu d'une face, tracer une croix entre ses coins.
- **Contrôle :**
  - les masses se chevauchent correctement, l'avant passant devant l'arrière ;
  - le volume est cohérent avec la vue (3/4 : on voit un côté de la boîte du torse) ;
  - les parties cachées ont été dessinées à travers (I2).

## Étape 3b — Tête et visage (nouvelle étape) [M][Z][T1]

Le test 1 a montré que la méthode v1 donnait un visage moins attirant que le dessin libre.
Cette étape construit le visage **avant** la couleur, sur son propre calque, à ×6 au moins.

**Forme de tête [M][Z].** Choisir d'abord la forme qui correspond au personnage : ovale,
rectangle, goutte inversée…
- **Femme :** ligne du menton plus haute, mâchoire ronde, menton légèrement pointu, cou
  fin.
- **Homme :** mâchoire anguleuse, cou presque aussi large que la mâchoire.
- **Personne âgée :** visage plus long et plus étroit.
- Cou : deux lignes qui descendent de la mâchoire. [T1] Vérifier sa longueur : un cou nu
  trop long a été le principal défaut du test 1.

**Construction de face, pas à pas [I]** :
1. Tracer un cercle pour le crâne et une ligne verticale de centre, qui descend sous le
   cercle jusqu'au menton.
2. **Mâchoire :** deux lignes descendent des côtés du cercle, à peu près verticales puis
   en angle vers le menton. Le menton est un petit segment plat, pas une pointe, sauf en
   manga très stylisé. Il se trouve à environ 1/2 à 2/3 du diamètre du cercle sous celui-ci.
3. **Lignes horizontales :**
   - les sourcils, juste au-dessus du milieu de la hauteur totale ;
   - les **yeux à mi-hauteur de la tête complète** (crâne + mâchoire), sauf en manga, où
     ils sont un peu plus bas ;
   - le **bas du nez au bas du cercle** ;
   - la bouche au tiers entre le nez et le menton.
4. **Yeux :** des amandes posées sur leur ligne, séparées d'**une largeur d'œil**. La
   paupière supérieure est plus épaisse et plus sombre que l'inférieure. Le coin extérieur
   est un peu plus haut ou au même niveau que le coin intérieur.
5. **Sourcils :** ils suivent l'arcade et commencent au-dessus du coin intérieur de l'œil.
6. **Nez puis bouche :** la largeur du nez ≈ l'écart entre les yeux ; les coins de la
   bouche sont à l'aplomb des pupilles ou un peu en dedans.
7. **Oreilles :** de la ligne des sourcils (ou des yeux) jusqu'au bas du nez, collées aux
   côtés du cercle, là où il rencontre la mâchoire.
8. **Cou :** il part de l'intérieur de la mâchoire, un peu en retrait de ses angles. Deux
   lignes diagonales (les sterno-cléido-mastoïdiens) vont de derrière les oreilles au creux
   du sternum. Les trapèzes descendent en pente vers les épaules.
9. Les cheveux en dernier, **au-dessus** du cercle (masse plus grande que le crâne).

**Construction en 3/4 (méthode Loomis) [I] :**
1. Sphère du crâne.
2. **On coupe le côté :** un cercle aplati (plan latéral) se dessine sur le côté de la
   sphère tournée. Le centre de ce cercle est l'endroit où la tête pivote ; l'oreille
   se place juste derrière et en dessous de ce centre.
3. **Ligne des sourcils :** elle fait le tour de la sphère en suivant le maillage. Elle
   passe sur le haut du cercle latéral.
4. **Ligne de centre :** elle est **courbe**. Elle suit l'avant de la sphère, puis descend
   devant pour former le plan du visage (front, arête du nez, menton).
5. **Plan du visage :** sous la sphère, un bloc qui va de l'arcade au menton. Sa face
   avant est plate, et ses côtés reculent vers les oreilles.
6. **Mâchoire :** de l'arrière du cercle latéral, sous l'oreille, une ligne descend à l'angle
   de la mâchoire, puis repart vers le menton.
7. Le cou part **sous et derrière** la mâchoire. La ligne de la nuque part de la base du
   crâne, plus haut et plus en arrière que la gorge.
8. Le côté éloigné du visage est raccourci : l'œil du fond est plus étroit, et l'arcade et
   la pommette peuvent couper son contour.

**Guides obligatoires [M].** Tracer toujours :
- la ligne verticale du centre du visage ;
- la ligne des yeux ;
- la ligne du nez ;
- la ligne de la bouche.
Sans ces lignes, la symétrie des yeux dérive.

**Placement — style semi-réaliste [Z] :**
- le visage se divise en 3 tiers : racine des cheveux → sourcils → bas du nez → menton ;
- faire varier les tiers change la morphologie (front court, menton long…) ;
- les oreilles vont entre la ligne des sourcils et le bas du nez ;
- **l'entonnoir :** une forme d'entonnoir, du milieu des oreilles aux coins du menton,
  contient les sourcils, les yeux, le nez et la bouche ; les coins de la bouche s'alignent
  sur ses bords ;
- **le trapèze :** un petit trapèze entre les sourcils fixe l'écart entre eux.

**Placement — style manga [M] :**
- les yeux sont **sous** la ligne de milieu de la tête ;
- le nez est entre cette ligne et le menton ;
- la lèvre inférieure est à mi-chemin entre le nez et le menton ;
- le nez, les pommettes et les lobes d'oreilles sont à la même hauteur ;
- les oreilles sont des « C » allongés, entre la ligne des yeux et celle du nez (plus bas
  que sur un vrai visage).

**Yeux [M] :**
- **Femme :** hauteur de l'œil ≈ 1/6 de la hauteur de la tête, largeur ≈ 1/4 de la
  largeur de la tête.
- **Homme :** hauteur ≈ 1/8 de la tête, largeur ≈ 1/4. L'œil est plus étroit et plus plat.
- Les yeux ne sont jamais rapprochés (écart ≥ 1 œil).
- Les deux yeux gardent la même taille et le même alignement dans toutes les vues.
- Iris ovale. Pupille ≈ 1/4 de l'iris.
- **Reflets :**
  - un reflet ≈ 1/10 de l'iris dans le coin haut, **au même endroit sur les deux yeux** ;
  - un 2e reflet, deux fois plus petit, en bas du côté opposé.
- **Le haut de l'iris est plus sombre que le bas** (ombre des cils).

**Nez [M] :**
- de face : un point ou un petit trait ;
- en 3/4 : deux petites courbes ;
- de profil : petit et pointu.

**Expressions [M].** Choisir l'expression qui correspond au mot clé de l'étape 0.

| Émotion | Sourcils | Yeux / pupilles | Bouche |
|---|---|---|---|
| Colère | inclinés vers le nez | — | — |
| Tristesse, peur | inclinés vers les oreilles | peur : petites pupilles | — |
| Détermination | baissés | mi-clos | — |
| Surprise | levés | grands ouverts | — |
| Timidité | — | pupilles vers le bas | — |
| Calme, sérieux | — | — | petite |

**Adaptation pixel art :**
- **Tête de 6 px de haut ou moins :** 1 px sombre par œil, pas de nez, la bouche seulement
  si l'expression l'exige.
- **Tête de 7 à 12 px :** yeux de 1×2 ou 2×2 px, avec 1 px de reflet seulement si l'œil
  fait 2 px de large ; le nez est 1 px de ton d'ombre.
- **Tête de plus de 12 px :** on applique les rapports manga ou semi-réalistes ci-dessus.

**Règle d'attrait [T1] :**
- Le visage doit être **majoritairement dans la lumière.**
- Interdit : couper le visage en deux moitiés, l'une claire et l'autre sombre (effet
  « masque »), sauf intention dramatique écrite à l'étape 0.
- Pour un personnage de jeu, la lumière vient de l'avant, en 3/4.

**Contrôle :**
- comparer le visage, côte à côte, avec la référence de style choisie à l'étape 0 ;
- se demander : est-il aussi attirant ? L'expression se lit-elle à ×1 ?
- produire 2 variantes (R9) et garder la meilleure.

## Étape 4 — Vêtements, cheveux et design par-dessus le mannequin

- Les vêtements **épousent** les volumes, puis s'en écartent selon le tissu. Les plis partent
  des points de tension (épaules, coudes, taille, genoux) et suivent des cylindres ou des
  cônes.
- **Langage de formes :**
  - rond = doux ou gentil ;
  - carré = solide ou stable ;
  - triangle = dynamique ou dangereux.
  Choisir une forme dominante.
- **Hiérarchie des formes [Z].** Classer chaque forme en trois niveaux :
  - **primaires** : torse, jupe, cape, masse de cheveux ;
  - **secondaires** : manches, ceinture, col ;
  - **tertiaires** : boutons, bijoux, coutures.
  Elles se dessinent dans cet ordre, et chaque niveau se place d'abord comme une forme
  plate (rectangle, triangle) sur le volume, avant de recevoir son épaisseur.
- Varier les tailles : grandes, moyennes et petites formes, avec des zones calmes.
  Un grand élément vaut mieux que beaucoup de petits.
- **Formes dynamiques [Z].** Une fois placées, les formes géométriques deviennent
  asymétriques et irrégulières (I4).
- **Cheveux [M] :**
  - les cheveux se dessinent en **mèches et touffes**, jamais en fils ;
  - on les découpe en 4 zones : devant (frange), côtés, arrière, dessus ;
  - la masse de cheveux est **un peu plus grande que le crâne** : jamais collée à la boule de
    l'étape 3 ;
  - 3 à 5 mèches de frange suffisent pour une coiffure simple ;
  - une mèche qui contraste (direction ou couleur) donne du caractère ;
  - on superpose les mèches puis on efface les lignes cachées.
- **Contrôle :** les plis et motifs suivent le maillage (I6), et on lit les trois niveaux de
  formes.

## Étape 5 — Silhouette

- Remplir tout le personnage d'une **seule couleur unie**.
- **Contrôle :**
  - la silhouette remplie en noir reste lisible : on comprend la pose et l'accessoire ;
  - les bras ou l'objet tenu se détachent du corps, avec des « trous » de fond lisibles ;
  - c'est lisible à ×1.
  Sinon, revenir à l'étape 2 ou 4 et modifier la pose.
- **Espaces négatifs [Z] :** les trous de fond ont des formes variées. Deux trous identiques
  côte à côte signalent une pose raide.

## Étape 6 — Contour propre (lignes « pixel-perfect »)

- Le contour fait 1 px d'épaisseur. Les segments se touchent **seulement en diagonale** :
  pas d'angles en « L » ni de pixels doublés.
- **Courbes :** la longueur des segments change régulièrement, par exemple 5-3-2-1-1, et
  jamais 5-2-1-2-1. Les plus longs segments vont en haut, en bas et sur les côtés d'une
  courbe.
- **Diagonales droites :** tous les segments ont la même longueur, ou suivent un motif
  régulier (2-1-2-1).
- **Hiérarchie des traits [Z][M].** Il y a trois « épaisseurs », qui deviennent trois tons
  en pixel art :
  - **traits principaux** : contour extérieur de la silhouette, en ton le plus sombre
    (selout sombre) ;
  - **traits secondaires** : lignes intérieures entre grandes masses (bras devant le torse,
    tête contre cou), en ton moyen-sombre de la matière ;
  - **traits de détail** : plis, coutures, cils, en ton juste un cran plus sombre que le
    fond, ou en simple différence de teinte.
  Les détails ne sont jamais aussi forts que la silhouette.
- Les lignes intérieures se tracent seulement où le contraste manque (tête contre cou,
  bras devant le torse). On peut juste les suggérer.
- Ne pas tracer de contour au point de contact avec le sol ou entre la main et l'objet tenu.
- **Contours cassés [Z].** On interrompt le contour pour la racine des cheveux, la barbe, la
  fourrure et le bord des sourcils. Sur ces bords, il est fait de petites pointes
  irrégulières, pas d'une ligne continue.
- Le contour n'est pas noir pur. **Selout :** chaque partie du contour prend une teinte plus
  sombre de la couleur qu'elle entoure, avec un contour plus clair du côté de la lumière.
  [Z] Cette teinte est **plus saturée** et un peu plus sombre que la couleur principale :
  par exemple vert foncé pour une plante, brun-rouge pour la peau.

## Étape 7 — Couleurs à plat

- **Palette d'abord [Z].** Avant de colorer, choisir 5 à 6 couleurs de référence. Les poser
  en carrés côte à côte sur une planche de test, puis ajuster jusqu'à ce qu'elles
  s'accordent.
- **Formule d'harmonie [Z].** En choisir une :
  - **analogues** : teintes voisines, résultat doux ;
  - **complémentaires** : teintes opposées ; l'une domine, l'autre sert d'accent ;
  - **double complémentaire** : deux paires opposées, plus riche ;
  - **triade** : trois teintes à intervalles égaux sur le cercle, dynamique.
- **Les teintes varient, mais la valeur et la saturation restent proches [Z]** entre les
  couleurs principales. Seul l'accent saturé y fait exception.
- Une **rampe** par matière (peau, cheveux, tissu 1, tissu 2, métal), de 3 à 5 tons triés
  par luminosité.
- **Décalage de teinte (affiné) [Z] :**
  - **lumière :** une teinte voisine vers le jaune, **plus claire et moins saturée** ;
  - **ombre :** une teinte voisine de l'autre côté du cercle (vers le rouge pour les
    chauds, vers le bleu ou le violet pour les froids), **plus sombre et plus saturée** ;
  - si on change seulement la valeur, le résultat est terne. Il faut changer les trois :
    teinte, valeur et saturation ;
  - jamais de noir ou de blanc pur pour ombrer ou éclairer ;
  - l'ombre de la peau est un rouge-violet ou brun-rose, pas un marron gris.
- Peu de couleurs. **Un seul accent saturé**, comme une ceinture ou un foulard, attire l'œil.
- Couleurs chaudes = vitalité, couleurs froides = calme ou mystère [Z]. Choisir la
  dominante selon l'intention de l'étape 0.
- Remplir chaque zone avec le ton moyen de sa rampe. Commencer par les grandes zones et
  finir par les petites [M].
- **Contrôle en niveaux de gris :** les grandes zones se distinguent par leur valeur, pas
  seulement par leur teinte.

## Étape 8 — Lumière et ombres (placées à la main)

**Règle v2 [T1] :** les zones d'ombre se dessinent **à la main, comme des formes**. On
décide de leurs pixels en regardant le volume. Il est interdit de les calculer par une
formule, par exemple une distance au centre ou un dégradé automatique : au test 1, cela
a produit du banding et un visage en masque. Un script peut remplir une forme déjà
décidée, mais il ne décide pas de la forme.

- Une **seule source de lumière**, celle de l'étape 0. Chaque ombre doit pouvoir dire d'où
  vient la lumière.
- **Ligne de séparation d'abord [Z].** Sur chaque masse, tracer la limite entre la zone
  éclairée et la zone d'ombre. Elle suit la courbure du volume, comme une ligne du
  maillage. C'est une limite **nette**, pas un dégradé. La valider avant de remplir.
- **Interdit : l'ombrage « coussin »,** c'est-à-dire des bandes plus sombres le long du bord,
  tout autour. L'ombre se met du côté opposé à la lumière, en suivant le **volume de
  l'étape 3**.
- **Les 8 zones, traduites en rampe [Z].** Avec une rampe de 5 tons, du plus sombre (1) au
  plus clair (5) :

| Zone (livre) | En pixel art | Ton |
|---|---|---|
| Lumière vive (directe) | zone face à la lumière | 4 |
| Lumière atténuée (tons moyens) | ton de base | 3 |
| Éclat (reflet de la source) | 1 à 3 px, surfaces brillantes seulement | 5 |
| Ombre forte (« ombre de forme ») | bande étroite le long du terminateur, côté ombre | 1–2 |
| Ombre moyenne | le gros de la zone d'ombre | 2 |
| Ombre légère (lumière réfléchie) | fine bande au bord de l'ombre, côté sol | 2–3 |
| Ombre portée | sur le sol ou sur une autre partie du corps | 1–2 |
| Ombre profonde (occlusion) | creux où la lumière n'entre pas | 1 |

- **Ordre de pose [Z] :**
  1. ombre légère, en aplat sur toute la zone d'ombre ;
  2. ombre moyenne ;
  3. ombre forte au terminateur ;
  4. ombre profonde dans les creux ;
  5. lumière ;
  6. éclat.
- **Règle de contraste [Z] :** tout ton de la zone éclairée est **plus clair** que tout ton de
  la zone d'ombre. Ce n'est ni trop contrasté (tout noir et blanc), ni trop uniforme (plat).
- **Nette ou douce [Z] :**
  - volumes anguleux (boîte, pli marqué, rebord) → limite **nette**, en une marche de
    rampe ;
  - volumes ronds (tête, joue, bras) → limite **adoucie** par 1 ton intermédiaire ou
    quelques pixels de transition, mais pas de dégradé large ;
  - les ombres douces sont plutôt grandes, et les ombres nettes plutôt petites ;
  - un pli léger donne une ombre diffuse, un pli marqué une ombre nette.
- **Où l'ombre va presque toujours sur un personnage [M] :**
  - sous le menton, sur le cou ;
  - sous la lèvre inférieure ;
  - sur le côté du nez opposé à la lumière ;
  - près des paupières et en haut de l'iris ;
  - à l'intérieur et à l'arrière de la masse de cheveux ;
  - sous la frange, sur le front.
- **Ombrer par plans musculaires [I].** Sur un corps visible (bras nus, torse, jambes) et
  à partir de 64 px de haut, chaque grand muscle est un **plan à facettes**, comme dans les
  écorchés simplifiés.
  - Le plan tourné vers la lumière prend le ton clair, celui qui s'en détourne le ton
    d'ombre.
  - Les limites suivent les séparations entre muscles : deltoïde et biceps, pectoral et
    deltoïde, les blocs des abdominaux, vaste interne et rotule.
  - Un vêtement moulant garde ces plans, en plus doux.
- **Style manga [M] :** du cel shading, c'est-à-dire des aplats nets et pas de dégradés. On
  garde des zones blanches ou très claires pour les reflets : le bandeau de lumière sur
  les cheveux, les reflets des yeux.
- **Interdit : le banding,** c'est-à-dire deux bandes de tons qui suivent exactement le même
  escalier de pixels. Décaler les limites.
- Ajouter une ombre portée au sol, sous les pieds : plus sombre au centre, plus claire vers
  l'extérieur [Z].
- Tramage (dithering) : seulement s'il sert aussi de texture.

## Étape 9 — Détails (en dernier)

- **Visage :**
  - les éléments sont placés sur les lignes de l'étape 3b ;
  - à petite taille, l'œil se fait en 1 à 2 px sombres, avec un pixel de blanc ou un reflet
    seulement si on a la place ;
  - pas de pupilles ni de dents trop petites, qui deviennent du bruit.
- **Mains :** la forme de mitaine de l'étape 3, avec un pouce lisible. Les doigts sont
  indiqués par 1 px sombre si on a la place.
- Cheveux en **mèches groupées** (gros clusters), pas en fils.
- Choisir quelques points forts pour la lumière et supprimer les autres.
- **Règle du tiers [Z].** Les détails de texture occupent environ **1/3** de la surface
  du personnage. Les **2/3** restants sont calmes : l'œil complète tout seul.
- **Grouper par 2 ou 3 [Z].** Un détail se répète en petits groupes de 2 ou 3 (plis,
  mèches, coutures), jamais sur une surface entière.
- **Textures [Z].** Repérer d'abord si la texture est :
  - **répétitive** (fourrure, herbe, tricot) : un seul motif simplifié, répété ;
  - **multiple** (bois, métal, cuir usé) : plusieurs motifs variés.
  Tester le motif sur un petit carré avant de l'appliquer. Faire varier sa taille, son
  inclinaison, son épaisseur et son espacement, pour éviter un rendu mécanique. Ne pas
  texturer tout le contour : garder des bords lisses là où la matière est courte.
- **Accents sombres [Z].** Finir par quelques touches du ton le plus sombre, seulement dans
  les creux et à l'arrière (I8).
- **Raconter [Z].** Un ou deux détails d'environnement ou d'accessoire qui racontent quelque
  chose, comme une entaille sur le fourreau ou de la neige sur les épaules. On choisit
  peu de détails, mais ils doivent dire quelque chose.

## Étape 10 — Nettoyage

- **Pixels orphelins :** un pixel isolé d'une couleur, sans voisins de la même couleur. Pour
  chacun, se demander s'il est nécessaire. Sinon, le supprimer ou le grouper en un amas de
  2 à 3 px.
- **Clusters :** des amas de tons clairs et voulus. Le moins de petits amas possible.
- **Anticrénelage (AA) :** à la main et avec parcimonie, seulement sur les grands escaliers
  des courbes importantes. Trop d'AA rend l'image floue.
- Supprimer tous les pixels des calques de construction (couleurs vives de R7).
- Chaque pixel doit « mériter sa place ».

## Étape 11 — Contrôle final (obligatoire)

Produire une planche avec :
- l'image à ×1 et à ×6 ;
- l'image retournée horizontalement, pour faire ressortir les défauts d'anatomie ;
- la silhouette en noir ;
- la version en niveaux de gris ;
- **la référence de style à côté, à la même échelle [T1].**

Répondre honnêtement :
1. La pose exprime-t-elle l'intention ?
2. Les proportions respectent-elles la grille (bras, tête, jambes, cou) ?
3. Le volume se lit-il, et la lumière est-elle cohérente ?
4. Le visage est-il attirant et majoritairement éclairé ? Se lit-il à ×1, comme les
   mains ?
5. Reste-t-il des orphelins, du banding, de l'ombrage coussin, des contours en « L » ?
6. L'objectif principal de l'étape 0 est-il atteint ?
7. À côté de la référence, le dessin tient-il la comparaison ? Sinon, quelle étape est en
   cause ?
8. **Anatomie (R11)** :
   - Chaque articulation est-elle plausible : sens de pliage, amplitude ?
   - Le deltoïde dépasse-t-il la cage ? Le cou part-il de derrière la mâchoire ?
   - Le pouce part-il du poignet, et les jointures suivent-elles un arc ?
   - Les bosses des membres sont-elles décalées ?
   - La cage et le bassin sont-ils deux masses distinctes ?

**Bilan [Z].** Noter **3 points réussis** puis **3 points à améliorer**. Les 3 points à
améliorer deviennent les objectifs du prochain dessin.

Corriger, puis refaire la planche.

---

## Résumé en une phrase

**Intention et références → proportions → pose → volumes → visage → vêtements et
cheveux → silhouette → contour → palette → ombres à la main → détails → nettoyage →
contrôle avec la référence.** Un calque par concept, du grand au petit. On ne pose pas un
pixel de détail tant que la structure n'est pas juste.
