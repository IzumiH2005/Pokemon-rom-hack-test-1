# Outils communs du test 4 : rendu, vues agrandies, contrôle des contours.
from PIL import Image, ImageDraw
from commun import rendre, vue

def grille_vide(w, h):
    return [['.'] * w for _ in range(h)]

def chaine(g):
    return [''.join(r) for r in g]

def angles_L(grille, contour):
    """Liste les pixels de contour qui forment un angle en L (pixel doublé)."""
    h = len(grille); w = len(grille[0]); res = []
    est = lambda x, y: 0 <= x < w and 0 <= y < h and grille[y][x] in contour
    for y in range(h):
        for x in range(w):
            if not est(x, y): continue
            for dx, dy in ((1, 1), (1, -1), (-1, 1), (-1, -1)):
                if est(x + dx, y) and est(x, y + dy) and not est(x - dx, y) and not est(x, y - dy):
                    res.append((x, y))
    return res

def orphelins(grille):
    """Pixels sans voisin (8 directions) de la même couleur."""
    h = len(grille); w = len(grille[0]); res = []
    for y in range(h):
        for x in range(w):
            c = grille[y][x]
            if c == '.': continue
            if not any(0 <= x+dx < w and 0 <= y+dy < h and grille[y+dy][x+dx] == c
                       for dx in (-1, 0, 1) for dy in (-1, 0, 1) if dx or dy):
                res.append((x, y, c))
    return res

def gris(im):
    return im.convert('LA').convert('RGBA')
