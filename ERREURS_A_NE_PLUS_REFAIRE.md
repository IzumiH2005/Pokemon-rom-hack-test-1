# Erreurs à ne plus refaire

## 1. Orientation du joueur à l'arrivée sur une carte

**Erreur :** au début du jeu, Red arrivait aux Colonnes Lances tourné vers le bas, dos à l'escalier et à l'autel où il doit aller.

**Cause :** un warp sans porte (`WARP_ID_NONE`) pose le joueur dans la direction par défaut, c'est-à-dire vers le bas. Personne n'avait choisi l'orientation.

**Règle :** à chaque arrivée scriptée (nouvelle partie, téléportation, warp de cinématique), on fixe l'orientation du joueur vers ce qu'il vient voir ou vers là où il doit aller. On le fait dans `MAP_SCRIPT_ON_WARP_INTO_MAP_TABLE` avec `turnobject OBJ_EVENT_ID_PLAYER, DIR_...`, avant le fondu. Sinon, le joueur se retourne à l'écran.

**Vérification :** sur la première capture après l'arrivée, le joueur regarde dans la bonne direction.

## 2. `waitstate` placé après un `msgbox`

**Erreur :** après les cris de Dialga et Palkia, le jeu se figeait et plus rien ne répondait.

**Cause :** `special ShakeCamera` réveille le script quand la secousse finit. Le `msgbox` venait juste après, puis `waitstate`. Si le joueur lisait lentement, la secousse finissait pendant le texte : le réveil passait dans le vide, et `waitstate` attendait ensuite un réveil qui ne viendrait plus. Les tests automatiques appuyaient vite sur A et ne voyaient pas le bug.

**Règle :** `waitstate` vient juste après le `special` qui réveille le script, jamais après un texte ou un autre ordre qui attend le joueur. Les tests de scène se font aussi en lisant lentement (A toutes les 2 à 3 secondes).

## 3. Orientation au Mont Argenté (récidive de l'erreur 1)

**Erreur :** à l'arrivée sur le Mont Argenté, Red regardait dans la mauvaise direction.

**Cause :** la règle 1 n'avait été appliquée qu'aux Colonnes Lances. La nouvelle carte de la scène n'avait pas d'orientation fixée.

**Règle :** la règle 1 vaut pour chaque carte où une scène fait arriver le joueur. À chaque nouvelle scène, on vérifie la première capture après le fondu.

## 4. Message de début de tour terminé par `end2`

**Erreur :** Red B annonçait « Je l'avais prévu » puis n'attaquait pas. Un seul des deux camps agissait par tour.

**Cause :** le message de début de tour finissait par `end2`. Cette commande règle l'action en cours sur « fin de tour » : le moteur sautait la première attaque du tour.

**Règle :** un message lancé au milieu d'un tour passe par `BattleScriptPushCursorAndCallback` avec un script qui finit par `end3`. `end2` sert seulement aux scripts qui terminent vraiment l'action.

## 5. Tester une IA contre elle-même

**Erreur :** la simulation faisait combattre l'IA de Red B contre une IA de même niveau. Les deux camps changeaient de Pokémon à chaque tour et le combat ne finissait jamais.

**Règle :** on mesure l'IA de Red B contre l'IA des dresseurs ordinaires. Un changement de Pokémon coûte un tour : l'IA ne change que si le gain est net, et jamais deux fois de suite sans raison forte.

## 6. Accesseur d'attaque appelé sur une attaque qui ne le permet pas

**Erreur :** le duel plantait sur un écran bleu « not a recoil move: Queue de Fer ».

**Cause :** l'IA de Red B appelait `GetMoveRecoil` sur toutes les attaques. Cet accesseur contient une assertion et ne vaut que pour `EFFECT_RECOIL`. Dans la simulation, l'assertion passait sans bloquer et l'IA lisait un faux contrecoup.

**Règle :** avant d'appeler `GetMoveRecoil`, `GetMoveAbsorbPercentage` ou un autre accesseur qui vérifie l'effet, on teste l'effet de l'attaque. Une simulation qui compte des assertions non nulles signale un bug, même si les combats finissent.

## 7. Changement de Pokémon choisi pendant un tour de recharge

**Erreur :** Dracaufeu et Florizarre restaient en place et tombaient alors que l'IA avait choisi de les retirer.

**Cause :** après Ultralaser ou Végé-Attak, le Pokémon doit récupérer. Le moteur ignore toute action choisie ce tour-là.

**Règle :** l'IA ne décide rien quand `rechargeTimer` est actif, et sa recherche suppose que le Pokémon qui recharge ne fait rien ce tour.

## 8. IA qui ignore les effets secondaires

**Erreur :** Red B perdait des combats gagnés sur le papier. Son calcul voyait les dégâts mais pas le reste : Blizzard qui ne rate jamais sous la neige, Synthèse qui ne rend qu'un quart des PV sous la neige, Statik du Pikachu adverse, paralysie, brûlure, gel, poison, peur, baisses de Défense, Absorb Eau, Brasier et Torrent sous le tiers des PV.

**Règle :** quand l'IA simule une attaque, elle lit tout ce que le moteur applique : précision réelle (météo, crans, talents), chaque effet secondaire avec sa chance réelle et les immunités de la cible, les talents de contact de la cible, les dégâts de fin de tour et les talents qui changent la puissance. Elle passe par les fonctions du moteur (`GetTotalAccuracy`, `CanSetNonVolatileStatus`, `CalcSecondaryEffectChance`) au lieu de valeurs recopiées à la main.

## 9. IA qui devine les talents, se soigne en boucle et devient passive

**Erreur :** au test réel, Red B a lancé Surf sur un Lokhlass doté d'Absorb Eau, a laissé Florizarre répéter Synthèse face à Pikachu sans jamais le menacer, et a envoyé Pikachu encaisser un Plaquage alors que Lokhlass tenait le coup.

**Cause :** l'IA estimait les talents et objets au lieu de lire ceux du Pokémon en face. Un soin comptait comme un gain même quand l'adversaire reprenait les PV au tour suivant. Une « riposte » pessimiste ajoutée à l'évaluation de chaque option faisait préférer les Pokémon qui encaissent sans frapper : la version testée ne gagnait plus que 6 combats sur 12.

**Règle :** l'IA de Red B lit le vrai talent et le vrai objet de chaque Pokémon. Un soin ne vaut que s'il rend plus de PV que l'adversaire n'en reprend et qu'il reste une menace à jouer après. Un Pokémon qui tient sans pouvoir blesser l'adversaire n'est pas un bon choix de relève. Chaque nouvelle règle de l'IA passe par une ablation en simulation (règle activée contre règle désactivée) avant de rester dans le jeu.

## 10. Deux mouvements de suite sur le même PNJ sans attente

**Erreur :** dans la scène 5, Pikachu restait sur place pendant que Red avançait de trois pas.

**Cause :** le script lançait `applymovement` sur Pikachu (se tourner), puis un second `applymovement` sur lui (marcher) sans attendre la fin du premier. Le moteur ignore un mouvement envoyé à un PNJ qui en exécute déjà un.

**Règle :** entre deux `applymovement` sur le même PNJ, toujours mettre `waitmovement` avec son identifiant. On ne lance en parallèle que des mouvements sur des PNJ différents.

## 11. Croire qu'un déclencheur ne marche pas sans vérifier la position

**Erreur :** j'ai pensé que la case devant la grotte ne déclenchait rien.

**Cause :** Red n'était pas sur la case du déclencheur. Il en était à une case, et le test ne le faisait marcher que d'une case vers le haut.

**Règle :** avant de corriger un déclencheur, vérifier sur une capture où se trouve Red par rapport à la case visée, et le faire marcher assez longtemps pour l'atteindre.

## 12. Confondre la touche Droite et la gâchette R dans l'émulateur

**Erreur :** dans un test, Red refusait d'aller vers la droite.

**Cause :** le script envoyait `r`, qui est la gâchette R. La flèche droite s'écrit `R`, et la flèche gauche `L`.

**Règle :** pour les directions, toujours `U`, `D`, `L`, `R` en majuscules. Les minuscules `r` et `l` sont les gâchettes.

## 13. Une fenêtre de texte qui écrase la carte

**Erreur :** après l'écran titre de la scène 8, des tuiles d'eau et des carrés noirs couvraient la route.

**Cause :** les tuiles de BG0 commencent à 0x8000 et la carte de BG2 à 0xE000. Une fenêtre de 30 x 6 tuiles placée à la tuile 0x280 débordait au-delà de la tuile 0x300 et écrivait dans la carte de BG2.

**Règle :** sur le terrain, une fenêtre ajoutée doit finir avant la tuile 0x300 de BG0. Calculer `baseBlock + largeur x hauteur` avant de compiler.

## 14. Répéter le nom du locuteur sur les pages suivantes

**Erreur :** le bandeau affichait « LUKA », puis la deuxième page commençait encore par « LUKA : ».

**Cause :** le jeu retire le préfixe « NOM : » seulement au début du message. Les pages après `\p` le gardent.

**Règle :** dans un même message, écrire « NOM : » sur la première page seulement.
