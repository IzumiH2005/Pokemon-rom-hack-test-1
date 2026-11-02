# Test 9 — Illustration convertie en sprite de combat

But : partir d'une illustration officielle (pas du pixel art) pour faire le sprite de combat d'Aventurine.

## Méthode
1. `conv.py` fait la conversion :
   - il retire le fond blanc (remplissage depuis les bords) ;
   - il cadre le sujet dans un carré, posé en bas ;
   - il réduit l'image en 64x64 (moyenne par zone) ;
   - il renforce la saturation et le contraste, puis applique un contour noir ;
   - il réduit à 15 couleurs + 1 transparente.
2. Le choix des couleurs se fait de deux façons :
   - automatique (k-means) : les cheveux blonds deviennent blancs et le rouge du fauteuil prend trop de couleurs ;
   - palette choisie à la main (`pal_main.txt`) : blond, peau, turquoise, rouge, or… C'est bien plus lisible.
3. Le visage (8 px de large) est retouché à la main dans le studio du test 8 : yeux, frange, menton.

```
python3 conv.py illustration.jpg sortie.png sat=1.6 con=1.2 pal=pal_main.txt
```

L'illustration source n'est pas incluse dans le dépôt.

## Résultat
- `1_comparaison.png` : illustration / auto / palette choisie / version finale
- `4_en_combat.png` : capture dans le jeu
- `aventurine_combat.png` + `.pal` : à copier dans `graphics/trainers/front_pics/aventurine.png` et `graphics/trainers/palettes/aventurine.pal`
