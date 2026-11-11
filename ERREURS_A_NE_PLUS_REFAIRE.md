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
