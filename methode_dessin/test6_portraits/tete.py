# Tête Loomis simplifiée en 3D, proportions anime (méthode C12).
# Repère tête : sphère du crâne de rayon 1 centrée en 0 ; x vers la droite du perso vu de face,
# y vers le bas, z vers nous. On tourne la tête (lacet, tangage, roulis), on projette à plat
# (pas de perspective : à cette taille elle ne se voit pas) et on en tire, toujours à partir de
# la forme : le contour du visage, la ligne de mâchoire, le plan de côté et la place des traits.
import numpy as np

# Hauteurs (rayon = 1, haut du crâne = -1). Anime fille :
SOURCILS, YEUX, NEZ, BOUCHE, MENTON = .02, .30, .84, 1.06, 1.48
#  - ligne des yeux un peu sous le milieu de la tête (milieu = .24) ;
#  - nez à mi-chemin des yeux au menton ; bouche au tiers entre nez et menton.
# Points de la mâchoire, côté droit (x > 0) ; le côté gauche est le miroir.
POMMETTE = (.80, .50, .55)   # le « coin » de Loomis : saillie sous l'œil, se voit côté lointain
GONION = (.62, .98, .00)     # angle de la mâchoire, sous l'oreille, en arrière
JOUE_BAS = (.40, 1.24, .40)  # milieu de la ligne de mâchoire
MENTON_C = (.11, 1.45, .52)  # coin du menton : menton étroit et pointu (V)
PROFIL = {'sourcils': (0, SOURCILS, 1.0), 'yeux': (0, YEUX, .95), 'nez': (0, NEZ, .93),
          'bouche': (0, BOUCHE, .80), 'menton': (0, MENTON, .55)}
OREILLE = (.86, .45, -.12)   # centre ; l'oreille va de la ligne des yeux à celle du nez

def rot(lacet, tangage, roulis):
    a, b, c = np.radians([lacet, tangage, roulis])
    Ry = np.array([[np.cos(a), 0, -np.sin(a)], [0, 1, 0], [np.sin(a), 0, np.cos(a)]])
    Rx = np.array([[1, 0, 0], [0, np.cos(b), np.sin(b)], [0, -np.sin(b), np.cos(b)]])
    Rz = np.array([[np.cos(c), -np.sin(c), 0], [np.sin(c), np.cos(c), 0], [0, 0, 1]])
    return Rz @ Rx @ Ry

def enveloppe(P):
    """Enveloppe convexe (chaîne monotone)."""
    P = sorted(map(tuple, P))
    def cote(seq):
        h = []
        for p in seq:
            while len(h) >= 2 and (h[-1][0] - h[-2][0]) * (p[1] - h[-2][1]) - (h[-1][1] - h[-2][1]) * (p[0] - h[-2][0]) <= 0:
                h.pop()
            h.append(p)
        return h
    return cote(P)[:-1] + cote(P[::-1])[:-1]

def miroir(p): return (-p[0], p[1], p[2])

class Tete:
    def __init__(self, cx, cy, R, lacet=28, tangage=5, roulis=-5):
        self.cx, self.cy, self.R = cx, cy, R
        self.M = rot(lacet, tangage, roulis)
    def tourne(self, p): return self.M @ np.asarray(p, float)
    def proj(self, p):
        q = self.tourne(p)
        return np.array([self.cx + self.R * q[0], self.cy + self.R * q[1], q[2]])
    def p2(self, p): return tuple(self.proj(p)[:2])
    def machoire(self):
        cote = [POMMETTE, GONION, JOUE_BAS, MENTON_C]
        return cote + [miroir(p) for p in cote] + [PROFIL['menton']]
    def contour(self):
        """Contour du visage = enveloppe du cercle du crâne et des points de mâchoire."""
        a = np.linspace(0, 2 * np.pi, 96, endpoint=False)
        cercle = [(self.cx + self.R * np.cos(t), self.cy + self.R * np.sin(t)) for t in a]
        return enveloppe(cercle + [self.p2(p) for p in self.machoire()])
    def oreille(self, s=1):
        c = np.array(OREILLE) * (s, 1, 1)
        a = np.linspace(0, 2 * np.pi, 24, endpoint=False)
        return [self.p2(c + (0, .27 * np.sin(t), .17 * np.cos(t) + .04 * np.sin(t))) for t in a]
    def cou(self, bas):
        """Cou : cylindre étroit planté sous le crâne, un peu en arrière du menton."""
        h = (bas - self.cy) / self.R
        a = np.linspace(0, 2 * np.pi, 32)
        pts = [self.p2((.26 * np.sin(t), y, -.20 + .26 * np.cos(t))) for t in a for y in (.70, h)]
        return enveloppe(pts)
    def plan_cote(self, s=1):
        """Plan de côté de Loomis (tempe → pommette → angle de mâchoire → arrière) :
        c'est lui qui passe à l'ombre quand la lumière vient de l'autre côté."""
        pts = [(.74, -.05, .67), (.82, .32, .52), POMMETTE, GONION, (.55, 1.1, -.4), (1.1, .4, -.5), (1.1, -.4, -.3)]
        return [self.p2(np.array(p) * (s, 1, 1)) for p in pts]
    def regard(self, s):
        """Centre de l'œil (sur la sphère), et facteur de raccourci horizontal."""
        x = .52 * s; p = np.array([x, YEUX, np.sqrt(1 - x * x - YEUX ** 2)])
        n = self.tourne(p)
        return self.p2(p), float(max(.45, n[2]))
    def point(self, nom, dx=0):
        x, y, z = PROFIL[nom]
        return self.p2((x + dx, y, z))
    def guides(self):
        """Lignes de construction projetées, et visibles (z > 0)."""
        g = {}
        def arc(f, ts):
            out = []
            for t in ts:
                q = self.proj(f(t)); out.append((q[0], q[1], q[2]))
            return out
        T = np.linspace(-np.pi / 2, np.pi / 2, 50)
        g['cercle'] = [(self.cx + self.R * np.cos(t), self.cy + self.R * np.sin(t), 1) for t in np.linspace(0, 2 * np.pi, 80)]
        haut = arc(lambda t: (0, -np.cos(t), np.sin(t)), np.linspace(0, np.pi / 2 + np.arcsin(YEUX), 30))
        g['axe'] = haut + [tuple(self.proj(PROFIL[k])) for k in ('nez', 'bouche', 'menton')]
        for nom, y in (('sourcils', SOURCILS), ('yeux', YEUX)):
            r = np.sqrt(1 - y * y)
            g[nom] = arc(lambda t: (r * np.sin(t), y, r * np.cos(t)), T)
        for nom in ('nez', 'bouche'):
            y = PROFIL[nom][1]; w = .62 if nom == 'nez' else .48
            g[nom] = [tuple(self.proj((x, y, PROFIL[nom][2] - .5 * x * x))) for x in np.linspace(-w, w, 9)]
        for s in (-1, 1):
            r = np.sqrt(1 - .7 ** 2)
            g['cote%+d' % s] = arc(lambda t: (s * .7, r * np.sin(t), r * np.cos(t)), np.linspace(0, 2 * np.pi, 60))
            g['mach%+d' % s] = [tuple(self.proj(np.array(p) * (s, 1, 1))) for p in (OREILLE, GONION, JOUE_BAS, MENTON_C)] + [tuple(self.proj(PROFIL['menton']))]
        return g
