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
- **[T1]** une leçon du test 1.

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
    l'intention le demande.

## Étape 3 — Volumes (le mannequin)

Habiller le squelette de formes simples. Chaque forme est décrite en données, avec son
centre, sa taille et son inclinaison :
- **tête :** une boule pour le crâne, avec une « feuille » courbée pour le plan du
  visage [Z]. On coupe les côtés (plans de Loomis), puis on trace :
  - un axe vertical au milieu du visage, qui tourne avec la tête en 3/4 ;
  - les lignes de l'étape 3b.
- **cage thoracique :** un œuf ou une boîte inclinée ; **bassin :** une boîte, un bol ou un
  triangle [Z]. Ces deux masses s'inclinent en sens opposés en contrapposto.
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
- **mains :** un bloc pour la paume (≈ taille du visage, du menton au milieu du front), avec
  un pouce séparé. Les doigts sont groupés en mitaine si la taille est petite. Les
  cylindres des doigts s'emboîtent dans le cube de la paume [Z].
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

**Bilan [Z].** Noter **3 points réussis** puis **3 points à améliorer**. Les 3 points à
améliorer deviennent les objectifs du prochain dessin.

Corriger, puis refaire la planche.

---

## Résumé en une phrase

**Intention et références → proportions → pose → volumes → visage → vêtements et
cheveux → silhouette → contour → palette → ombres à la main → détails → nettoyage →
contrôle avec la référence.** Un calque par concept, du grand au petit. On ne pose pas un
pixel de détail tant que la structure n'est pas juste.
