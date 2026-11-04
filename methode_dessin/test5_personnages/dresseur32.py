# Lina en 32x32 (≈ 2,5 têtes, tête ≈ 45 %). Yeux 2x3 (le 2x2 avec reflet en bas faisait
# « blanc d'œil » et regard endormi) : haut sombre, reflet en haut côté lumière, iris en bas. Nez = 1 px d'ombre, bouche 2 px, mains en bloc 2x2.
from base import *

def L(*parts, w=32):
    """Assemble une rangée : (n points) ou chaîne ; complète à droite par des points."""
    s = ''.join('.' * p if isinstance(p, int) else p for p in parts)
    assert len(s) <= w, (s, len(s)); return s + '.' * (w - len(s))

G = [
L(32),
L(11, 'O' * 10),
L(9, 'OO', 'aaaabbbbbb', 'OO'),
L(8, 'O', 'aaaaabbbbbbbbc', 'O'),
L(7, 'O', 'aaaabbbbbbbbbbbc', 'O'),
L(7, 'O', 'Y' * 16, 'O'),
L(7, 'O', 'aabaabbbabbbbbbc', 'O'),
L(6, 'O', 'bbbbbcbbbbbcbbbbcc', 'O'),
L(6, 'O', 'abb', 'c1bbc11bbc1b', 'bcc', 'O'),
L(6, 'O', 'bcb', '1111111b1112', 'bcc', 'O'),
L(6, 'O', 'bcb', '11EE1111EE12', 'ccc', 'O'),
L(6, 'O', 'bcb', '11WE1111WE22', 'ccc', 'O'),
L(6, 'O', 'bcb', '11bE1111bE22', 'ccc', 'O'),
L(6, 'O', 'bcb', '111111211122', 'ccc', 'O'),
L(6, 'O', 'bcb', '11111p311222', 'ccc', 'O'),
L(6, 'O', 'bcc', 'O2222222233O', 'ccc', 'O'),
L(7, 'OOOO', 'OO', '333333', 'OO', 'OOOO'),
L(8, 'Or', 'rrqqWWWWqqqp', 'pO'),
L(7, 'O', 'rq', 'prqqqWWqqqqp', 'qp', 'O'),
L(7, 'O', 'rq', 'prqqqqqqqqqp', 'qp', 'O'),
L(7, 'O', 'rq', 'prqqqqqqqqpp', 'qp', 'O'),
L(7, 'O', 'qq', 'pqqqqqqqqqpp', 'pp', 'O'),
L(7, 'O', '12', 'mnnnnYYnnnnm', '23', 'O'),
L(7, 'O', '22', 'nnnnnnnnnnnm', '33', 'O'),
L(7, 'OOO', 'nnnnnnnnnnnm', 'OOO'),
L(9, 'O', 'nnnnnmOnnnnm', 'O'),
L(10, 'O1122O', 'O2233O'),
L(10, 'O1222O', 'O2233O'),
L(10, 'OWWWWO', 'OWWWWO'),
L(9, 'OrqqqpO', 'OrqqqpO'),
L(9, 'OOOOOOO', 'OOOOOOO'),
L(32),
]
