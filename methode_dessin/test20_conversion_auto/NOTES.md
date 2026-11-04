# Test 20 : conversion automatique soignée, puis retouche

Ce test reprend l'illustration du test 19 (elle n'est pas dans le dépôt). Le test 19 dessinait tout à la main, forme par forme : les proportions et le trait de l'original s'y perdaient. Ici, l'ordinateur produit la base et je ne retouche qu'à la main.

## Conversion (`conv.py`)
1. **Retirer le voile lumineux.** Sans cette étape, les cheveux contre-jour passent pour de la peau.
2. **Lisser la texture, puis accentuer les bords.** Un filtre médian enlève le grain, ce qui supprime le bruit à 128 px.
3. **Réduire par couleur dominante.** Chaque case de ~8×8 px prend la couleur de son groupe majoritaire, pas la moyenne. La moyenne donne de la boue.
4. **Traiter les traits noirs à part.** Ce sont les pixels nettement plus sombres que leur voisinage. Ils sont réduits séparément, puis reposés en noir par-dessus. Sans ça, les mèches et la mâchoire disparaissent. Avec un seuil trop haut, ils sortent en pointillés.
5. **Calculer la palette de 14 couleurs.** Chaque couleur pèse selon la racine de son nombre de pixels :
   - pondérer au nombre de pixels donne 3 noirs presque identiques, à cause de la masse des cheveux ;
   - ne pas pondérer du tout donne des cheveux en aplat noir et une peau rouge.
   Deux rouges sont fixés à la main : le sang et la lueur de l'iris.
6. **Nettoyer les pixels isolés.**

## Retouches à la main
- `r1_yeux.txt` : paupières, blanc grisé, iris rouge. La conversion les avait perdus.
- `lisser.py`, appliqué sur le cou et le torse seulement : enlève les points noirs épars.
- `r3_meches.txt` : quelques mèches brunes dans la masse sombre du bas, et l'oreille.

`sh construire.sh carre.png` refait tout.
