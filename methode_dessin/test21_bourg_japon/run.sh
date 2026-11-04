#!/bin/sh
# usage: run.sh dossier cXX in(NEW:WxH|etape.txt) etapeXX_nom
O=/home/user/Pokemon-rom-hack-test-1/methode_dessin/outils
cd "$1" && python3 $O/trace.py "$3" "$4.txt" "$2.txt" && python3 $O/px.py "$4.txt" 8 palette.json
