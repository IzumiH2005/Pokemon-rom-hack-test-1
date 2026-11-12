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
