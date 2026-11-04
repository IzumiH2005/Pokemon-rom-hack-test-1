# Test 19 : portrait 128×128 à partir d'une illustration

Une illustration fournie par l'utilisateur sert de guide. Elle n'est **pas** dans le dépôt, et sa conversion brute non plus.

## Ce qui n'a pas marché
Une réduction directe vers la palette (`convertir.py`, puis `zones.py` et `nettoyer.py`) donne un résultat boueux :
- le voile lumineux fait passer les cheveux pour de la peau ;
- la peau dans l'ombre est lue comme des cheveux.

Ces scripts ne servent qu'à repérer les grandes masses.

## Méthode retenue : repeindre en calques, à la main
Chaque calque est un petit fichier de formes placées à la main. Après chaque calque, je compare avec la référence agrandie, avec une grille.

1. `f01` : silhouettes (cheveux, visage, cou, kimono).
2. `f02` : plans de lumière sur la peau. La lumière vient d'en haut à droite : arête du nez, pommette, menton et bande du cou.
3. `f03` : frange et mèches qui coupent le visage.
4. `f04`, `c30`, `f025`, `c31` : nez, yeux mi-clos à iris rouge, sourcils fins, bouche en grimace sur 4 rangées.
5. `f05` : volume des cheveux, liseré du contre-jour et lignes de mèches.
6. `f06` : cou élargi, ombre portée de la mâchoire, col en V.
7. `f07` : sang et sueur.
   - Coulures de 1 px, sombres en haut, avec une goutte claire au bout.
   - Pas de grosses taches.
8. `f08` : contour sélectif.
   - Noir côté ombre.
   - Côté lumière, un liseré clair qui s'éteint vers le bas.

`python3 construire.py` reconstruit tout. `etapes.png` montre chaque calque.

## Corrections faites en comparant
- Les yeux faisaient des « lunettes noires » : je les ai affinés et passés sous les mèches.
- La bouche était trop épaisse et doublée : je l'ai redessinée rangée par rangée.
- La peau de base était trop sombre (h) et se confondait avec les cheveux : je l'ai remontée d'un cran (i).
- Le sang sur le torse faisait une tache trop vive : remplacé par des traînées sombres.
- Une ligne noire sous le menton ressemblait à une deuxième bouche : supprimée.
