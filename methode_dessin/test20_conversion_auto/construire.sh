#!/bin/sh
# Usage : sh construire.sh carre.png   (l'illustration source n'est pas dans le dépôt)
set -e
T=$(mktemp -d)
python3 conv.py "$1" "$T" 14
python3 ../outils/formes.py "$T/auto.txt" "$T/r1.txt" r1_yeux.txt
python3 lisser.py "$T/r1.txt" "$T/r2.txt" 40 94 92 128
python3 ../outils/formes.py "$T/r2.txt" portrait.txt r3_meches.txt
python3 ../outils/px.py portrait.txt 4 palette.json
