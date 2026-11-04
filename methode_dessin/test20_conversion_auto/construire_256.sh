#!/bin/sh
# Version 256x256. Usage : sh construire_256.sh carre.png
set -e
T=$(mktemp -d)
python3 conv.py "$1" "$T" 14 256
cp "$T/palette.json" palette_256.json
python3 ../outils/formes.py "$T/auto.txt" "$T/r1.txt" r1_yeux_256.txt
python3 lisser.py "$T/r1.txt" portrait_256.txt 80 188 184 256
python3 ../outils/px.py portrait_256.txt 2 palette_256.json
