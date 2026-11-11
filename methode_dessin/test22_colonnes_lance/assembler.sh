# Écrit le fichier de commandes d'une colonne : assembler.sh nom type hauteur "joints"
# type = pointe (sommet 24 rangées, fût dès y22) ou brise (sommet 26 rangées, fût dès y26)
nom=$1; type=$2; H=$3; joints=$4
f=colonnes/c_$nom.txt
s=$((H-14))
{
echo "# colonne $nom : $type, hauteur $H, joints à $joints"
echo "stamp pieces/socle.txt 0 $s"
if [ $type = pointe ]; then d=22; else d=26; fi
for y in $(seq $d $((s+2))); do echo "stamp pieces/fut.txt 5 $y"; done
echo "stamp pieces/pied.txt 5 $((s+3))"
echo "stamp pieces/$type.txt 5 0"
for j in $joints; do echo "stamp pieces/joint.txt 5 $j"; done
echo "# ombre portée du fût sur le dessus du socle (côté droit, loin de la lumière)"
echo "hline d 20 22 $((s+5))"
echo "hline d 23 24 $((s+4))"
echo "hline d 23 24 $((s+5))"
[ -f colonnes/d_$nom.txt ] && cat colonnes/d_$nom.txt
} > $f
python3 ../outils/trace.py NEW:30x$H colonnes/$nom.txt $f
python3 ../outils/px.py colonnes/$nom.txt 4 palette.json
