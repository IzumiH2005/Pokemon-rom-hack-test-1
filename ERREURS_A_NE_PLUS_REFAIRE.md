# Erreurs à ne plus refaire

## 1. Orientation du joueur à l'arrivée sur une carte

**Erreur :** au début du jeu, Red arrivait aux Colonnes Lances tourné vers le bas, dos à l'escalier et à l'autel où il doit aller.

**Cause :** un warp sans porte (`WARP_ID_NONE`) pose le joueur dans la direction par défaut, c'est-à-dire vers le bas. Personne n'avait choisi l'orientation.

**Règle :** à chaque arrivée scriptée (nouvelle partie, téléportation, warp de cinématique), on fixe l'orientation du joueur vers ce qu'il vient voir ou vers là où il doit aller. On le fait dans `MAP_SCRIPT_ON_WARP_INTO_MAP_TABLE` avec `turnobject OBJ_EVENT_ID_PLAYER, DIR_...`, avant le fondu. Sinon, le joueur se retourne à l'écran.

**Vérification :** sur la première capture après l'arrivée, le joueur regarde dans la bonne direction.
