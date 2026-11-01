# Test 6 : création d'un nouveau personnage (Aventurine)

Sprite overworld 16x32 complet (9 frames : face, dos, profil, 2 pas de marche par direction). Il reprend la structure du sprite de Brendan : gabarit de tête, placement du visage et des yeux, bras écartés, jambes et décalage de marche.

## Ce qui a été repris des références
- Cheveux blond cendré, mèche balayée sur le front, mèches sur la nuque.
- Yeux violets.
- Col en fourrure blanche.
- Chemise turquoise avec as de pique doré.
- Gilet noir à liseré doré.
- Manches noires avec revers turquoise et gants noirs.
- Pans dorés sur les côtés.
- Basques turquoise et bleues avec pompons (visibles de dos et de profil).
- Pantalon blanc et chaussures noires et turquoise.

## Ajout dans le moteur (pokeemerald-expansion)
- `OBJ_EVENT_GFX_AVENTURINE` et une palette dédiée `OBJ_EVENT_PAL_TAG_AVENTURINE` (0x1170).
- Pic, palette, table d'images, GraphicsInfo, pointeur, entrée dans `sObjectEventSpritePalettes`.
- PNJ placé à Bourg-en-Vol (8,10). Il se promène et a son propre dialogue.

## Fichiers
- `aventurine.png` et `aventurine.pal` : la planche finale et sa palette.
- `avk.py`, `av4.py` (poses fixes), `av5.py` (marche) : le dessin pixel par pixel.
- `install_av.py` : installe la planche et enregistre le PNJ dans le moteur.

## Retouche : coiffure (v2)

La coupe a été redessinée pixel par pixel, à partir d'un zoom sur la tête et des images de référence :
- **Face** : raie sur la gauche, frange en mèches pointues qui balaie vers la droite et couvre en partie l'œil gauche, petites pointes vers l'extérieur au niveau des oreilles, mèches latérales jusqu'à la mâchoire.
- **Profil** : frange qui tombe sur le front, nuque en pointes.
- **Dos** : mèches en couches et nuque dentelée au lieu d'un arrondi lisse.
- Le haut du crâne est plus plat, pour casser l'effet « casque ».

Les animations de marche suivent automatiquement, car elles ne modifient que le corps.

Fichiers :
- `4_cheveux_avant_apres.png` : comparaison avant/après ; `5_cheveux_en_jeu.png` : résultat dans l'émulateur.
- `av4b.py` : nouvelles poses fixes ; `av6.py` : animations de marche.
- Installation : `python3 install_av.py av6` puis `make`.
