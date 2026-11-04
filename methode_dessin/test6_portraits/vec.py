# Petit moteur « croquis vectoriel → pixels » : on construit en courbes (comme un croquis),
# on rasterise à la taille voulue, puis on ombre et on nettoie à la main.
import numpy as np
from PIL import Image

def bez(p0, p1, p2, p3, n=40):
    t = np.linspace(0, 1, n)[:, None]
    P = [np.array(p, float) for p in (p0, p1, p2, p3)]
    return (1-t)**3*P[0] + 3*(1-t)**2*t*P[1] + 3*(1-t)*t**2*P[2] + t**3*P[3]

def chemin(*segs):
    """segs : liste de points ; un tuple de 3 points = courbe de Bézier depuis le point courant."""
    pts = [np.array(segs[0], float)[None]]
    cur = segs[0]
    for s in segs[1:]:
        if len(s) == 3 and isinstance(s[0], (tuple, list)):
            pts.append(bez(cur, *s)[1:]); cur = s[2]
        else:
            pts.append(np.array(s, float)[None]); cur = s
    return np.concatenate(pts)

def masque(poly, S, u=100):
    """Remplit un polygone (coordonnées en unités 0..u) : test au centre de chaque pixel."""
    k = S / u
    P = poly * k
    ys, xs = np.mgrid[0:S, 0:S] + .5
    inside = np.zeros((S, S), bool)
    x0, y0 = P[:, 0], P[:, 1]; x1, y1 = np.roll(x0, -1), np.roll(y0, -1)
    for a, b, c, d in zip(x0, y0, x1, y1):
        if b == d: continue
        cond = (ys >= min(b, d)) & (ys < max(b, d))
        xi = a + (ys - b) * (c - a) / (d - b)
        inside ^= cond & (xs < xi)
    return inside

def meche(p0, p1, p2, p3, w0, S, u=100, forme=.8, n=60):
    """Mèche = ruban le long d'une courbe, large à la racine, pointue au bout.
    Renvoie le masque, et pour chaque pixel t (0 racine → 1 pointe) et s (-1 bord gauche → 1 droit)."""
    C = bez(p0, p1, p2, p3, n)
    T = np.gradient(C, axis=0); T /= np.linalg.norm(T, axis=1)[:, None] + 1e-9
    N = np.stack([-T[:, 1], T[:, 0]], 1)
    t = np.linspace(0, 1, n)
    w = w0 * (1 - t) ** forme * (1 + .25 * np.sin(np.pi * t)) / 2
    poly = np.concatenate([C + N * w[:, None], (C - N * w[:, None])[::-1]])
    M = masque(poly, S, u)
    k = S / u
    ys, xs = np.nonzero(M)
    pts = np.stack([(xs + .5) / k, (ys + .5) / k], 1)
    d = ((pts[:, None, :] - C[None]) ** 2).sum(2)
    j = d.argmin(1)
    v = pts - C[j]
    side = (v * N[j]).sum(1) / (w[j] + 1e-6)
    Tm = np.zeros((S, S)); Sm = np.zeros((S, S))
    Tm[ys, xs] = t[j]; Sm[ys, xs] = np.clip(side, -1, 1)
    return M, Tm, Sm

def png(G, pal, nom, k=1, fond=None):
    S = len(G)
    im = Image.new('RGBA', (S, S), (0, 0, 0, 0))
    for y, r in enumerate(G):
        for x, c in enumerate(r):
            if c != '.': im.putpixel((x, y), pal[c] + (255,))
            elif fond: im.putpixel((x, y), fond + (255,))
    if k > 1: im = im.resize((S * k, S * k), Image.NEAREST)
    if nom: im.save(nom)
    return im
