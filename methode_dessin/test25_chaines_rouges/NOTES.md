# Chaînes Rouges (VFX prologue, Colonnes Lances)

Planche 64×384, 6 images de 64×64, dessinées pixel par pixel (grilles f0 à f5).

- f0 : étincelles, la chaîne s'annonce.
- f1 : chaîne fantôme, rouge sombre.
- f2 : chaîne pleine, en diagonale sur le poitrail.
- f3 à f5 : un reflet blanc court le long des maillons.

Pièces : A (anneau) et B (barre qui traverse l'anneau). `Am`, `Bm` sont les miroirs.
Palette : pal.json (O contour, r/R corps, h reflet, w éclat).
Construction de la planche indexée : `python3 ../outils/indexe.py pal.json chaine.png f*.txt`.
