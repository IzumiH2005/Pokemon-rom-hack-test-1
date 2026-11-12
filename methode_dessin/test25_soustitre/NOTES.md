# Test 25 : sous-titre « I.C / CONVERGENCE IDENTITAIRE »

## Intention
Le logo « Pokémon Version Rouge Feu » ne change pas. Le sous-titre s'ajoute dans la bande noire
sous les flammes, à gauche de Dracaufeu. Il reprend les couleurs du feu de l'écran titre :
crème en haut, jaune, orange, rouge en bas.

## Construction
- Toile de 128 × 24 px, soit 16 × 3 tuiles du BG2 (tuiles 64 à 111, palette 14).
- Emblème « I.C » : 18 px de haut, fûts de 4 px, relief de 2 px vers le bas à droite.
- Filet vertical de 1 px entre l'emblème et le texte.
- Texte sur deux lignes de 11 lettres : « CONVERGENCE » et « IDENTITAIRE ». Les lettres font 6 × 7 px
  (le I fait 4 px) avec un relief de 1 px. Les deux lignes partagent le même centre (x = 76,5).

## Étapes
1. `c01_relief.txt` : copies décalées des pièces peintes en `r`, puis les faces par-dessus.
2. `contour.py ... X r` : le trait ne touche que les faces de l'emblème. Le texte n'en reçoit pas,
   car un trait intérieur réduirait ses fûts de 2 px à 0 px de face.
3. `c03_couleurs.txt` : bandes horizontales du clair au foncé.

## Choix
- Sur fond noir, un trait presque noir disparaît et assombrit l'emblème. Le trait prend donc
  le rouge `#c81c14` (comparaison de trois variantes à l'écran).
- La palette 14 garde les couleurs 0, 6 et 11, que le cadre du BG3 utilise.
- « Appuyez sur Start » descend d'une rangée de tuiles pour laisser la place.

## Version 2 (retenue) : sous le logo
Le sous-titre quitte la bande noire et se place sous « VERSION ROUGE FEU », centré sur lui
(BG2, colonnes 5 à 15, rangées 11 à 13). Il reprend le style du logo : faces blanches qui
grisent vers le bas, trait sombre `#181818` posé sur les 8 voisins, profondeur `#293131`.
Les lettres suivent l'arc de « ROUGE FEU » : celles du bord descendent de 2 px, les suivantes de 1 px.
Les flammes (sprites de priorité 3) passent derrière. « Appuyez sur Start » reprend sa place d'origine.
Fichiers : `c11_logo.txt`, `c12_couleurs.txt`, `palette_v2.json`, `build_v2.sh`, `planche_v2.png`.
