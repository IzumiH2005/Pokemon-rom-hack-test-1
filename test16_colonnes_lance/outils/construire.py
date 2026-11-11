# Convertit le rendu des Colonnes Lance (couches.py) en jeu de tuiles GBA + carte.
# Usage : python3 construire.py <dossier_rendu> <pokeplatinum> <jeu>
# Écrit les tuiles, palettes et métatuiles dans data/tilesets/{primary,secondary}/colonnes_lance
# et la grille de la carte dans data/layouts/ColonnesLance/.
import sys, os, struct
import numpy as np
from PIL import Image

REND, PLAT, JEU = sys.argv[1:4]
X0, Y0 = 15, 3                    # coin de la découpe dans la grille Platine 64x64
LIM_TUILES = 1024 - 1             # la tuile 0 reste vide (transparente)
NB_PALS = 13

bas = np.array(Image.open(f'{REND}/carte_bas.png').convert('RGB')).astype(int) >> 3
haut = np.array(Image.open(f'{REND}/carte_haut.png').convert('RGBA')).astype(int)
mh = haut[..., 3] > 0
haut = haut[..., :3] >> 3
H, W = bas.shape[:2]
MW, MH = W // 16, H // 16

# --- collisions Platine ---
G = np.zeros((64, 64), int)
for k, (cx, cy) in zip(range(375, 379), [(0, 0), (1, 0), (0, 1), (1, 1)]):
    d = open(f'{PLAT}/res/field/mapmodels/data/map_data_{k}.bin', 'rb').read()
    for i in range(1024):
        G[cy * 32 + i // 32, cx * 32 + i % 32] = struct.unpack_from('<H', d, 16 + 2 * i)[0]

# --- tuiles 8x8 : couleur 15 bits, -1 = transparent ---
def code(rgb, m=None):
    c = (rgb[..., 0] << 10) | (rgb[..., 1] << 5) | rgb[..., 2]
    return np.where(m, c, -1) if m is not None else c
CB, CH = code(bas), code(haut, mh)
def tuile(img, x, y): return img[y:y + 8, x:x + 8]

# palettes : glouton sur les ensembles de couleurs des tuiles
ens = []
for img in (CB, CH):
    for y in range(0, H, 8):
        for x in range(0, W, 8):
            s = frozenset(tuile(img, x, y).ravel()) - {-1}
            if s: ens.append(s)
pals = []
for s in sorted(set(ens), key=len, reverse=True):
    best = None
    for i, p in enumerate(pals):
        u = p | s
        if len(u) <= 15 and (best is None or len(u - p) < best[0]): best = (len(u - p), i)
    if best is None: pals.append(set(s))
    else: pals[best[1]] |= s
assert len(pals) <= NB_PALS, len(pals)
pals = [sorted(p) for p in pals]
def choisir_pal(s):
    return min((len(p), i) for i, p in enumerate(pals) if s <= set(p))[1]

# indexation : chaque tuile -> (palette, tableau 8x8 d'indices 0..15)
def indexer(t):
    s = set(t.ravel()) - {-1}
    if not s: return None
    pi = choisir_pal(s); lut = {c: j + 1 for j, c in enumerate(pals[pi])}; lut[-1] = 0
    return pi, np.vectorize(lut.get)(t).astype(np.uint8)

uniq = {}            # clé -> numéro provisoire
tab = []             # numéro -> tableau d'indices
usage = []
def cle(a): return a.tobytes()
def ajouter(a, pi):
    for hf in (0, 1):
        for vf in (0, 1):
            b = a[:, ::-1] if hf else a
            b = b[::-1] if vf else b
            k = cle(np.concatenate([b, np.full((1, 8), pi, np.uint8)]))
            if k in uniq:
                usage[uniq[k]] += 1
                return uniq[k], hf, vf
    a = np.concatenate([a, np.full((1, 8), pi, np.uint8)])
    uniq[cle(a)] = len(tab); tab.append(a); usage.append(1)
    return len(tab) - 1, 0, 0

refs = {}            # (couche, x, y) -> (num, hf, vf, pal) ou None
for c, img in enumerate((CB, CH)):
    for y in range(0, H, 8):
        for x in range(0, W, 8):
            r = indexer(tuile(img, x, y))
            if r is None: refs[c, x, y] = None; continue
            pi, a = r
            # palette ajoutée dans la clé : deux tuiles de palettes différentes restent distinctes
            n, hf, vf = ajouter(a, pi)
            refs[c, x, y] = (n, hf, vf, pi)

# fusion des tuiles les moins utilisées si on dépasse la limite
remap = list(range(len(tab)))
vivants = set(range(len(tab)))
coul = lambda a, pi: np.array([pals[pi][v - 1] if v else -1 for v in a.ravel()])
def rgb(n):
    a = tab[n][:8]; pi = int(tab[n][8, 0])
    c = coul(a, pi); return np.stack([(c >> 10) & 31, (c >> 5) & 31, c & 31], 1) * (c[:, None] >= 0) - 99 * (c[:, None] < 0)
cache = {}
fusions = 0
while len(vivants) > LIM_TUILES:
    n = min(vivants, key=lambda i: usage[i])
    pi = tab[n][8, 0]
    cand = [m for m in vivants if m != n and tab[m][8, 0] == pi]
    rn = rgb(n)
    best = min(cand, key=lambda m: ((rgb(m) - rn) ** 2).sum())
    remap[n] = best; usage[best] += usage[n]; vivants.discard(n); fusions += 1
def final(n):
    while remap[n] != n: n = remap[n]
    return n
ordre = sorted(vivants)
num = {n: i + 1 for i, n in enumerate(ordre)}     # +1 : tuile 0 vide

# --- métatuiles ---
metas = {}; liste_metas = []; grille = np.zeros((MH, MW), int)
for my in range(MH):
    for mx in range(MW):
        e = []
        for c in (0, 1):
            for dy in (0, 8):
                for dx in (0, 8):
                    r = refs[c, mx * 16 + dx, my * 16 + dy]
                    if r is None: e.append(0); continue
                    n, hf, vf, pi = r
                    e.append(num[final(n)] | hf << 10 | vf << 11 | pi << 12)
        e = tuple(e)
        if e not in metas: metas[e] = len(liste_metas); liste_metas.append(e)
        grille[my, mx] = metas[e]
assert len(liste_metas) <= 1024, len(liste_metas)

# --- écriture ---
def ecrire_tuiles(chemin, plage):
    n = len(plage); lignes = (n + 15) // 16
    im = np.zeros((lignes * 8, 128), np.uint8)
    for i, t in enumerate(plage):
        im[(i // 16) * 8:(i // 16) * 8 + 8, (i % 16) * 8:(i % 16) * 8 + 8] = t
    p = Image.fromarray(im, 'P'); p.putpalette(sum([[v * 17] * 3 for v in range(16)], []) + [0] * 720)
    p.save(chemin)
toutes = [np.zeros((8, 8), np.uint8)] + [tab[n][:8] for n in ordre]
prim, sec = toutes[:640], toutes[640:] or [np.zeros((8, 8), np.uint8)]
def ecrire_pals(dos):
    os.makedirs(dos, exist_ok=True)
    for i in range(NB_PALS):
        p = pals[i] if i < len(pals) else []
        cols = [(0, 0, 0)] + [((c >> 10) * 255 // 31, ((c >> 5) & 31) * 255 // 31, (c & 31) * 255 // 31) for c in p]
        cols += [(0, 0, 0)] * (16 - len(cols))
        open(f'{dos}/{i:02d}.pal', 'w').write('JASC-PAL\r\n0100\r\n16\r\n' + ''.join(f'{r} {g} {b}\r\n' for r, g, b in cols))
for genre, tuiles, mts in (('primary', prim, liste_metas[:640]), ('secondary', sec, liste_metas[640:] or [(0,) * 8])):
    dos = f'{JEU}/data/tilesets/{genre}/colonnes_lance'
    os.makedirs(dos, exist_ok=True)
    ecrire_tuiles(f'{dos}/tiles.png', tuiles)
    ecrire_pals(f'{dos}/palettes')
    open(f'{dos}/metatiles.bin', 'wb').write(b''.join(struct.pack('<8H', *m) for m in mts))
    open(f'{dos}/metatile_attributes.bin', 'wb').write(b''.join(struct.pack('<I', 0) for _ in mts))

# grille : collision Platine (bit 15) ; élévation 3 partout
lay = f'{JEU}/data/layouts/ColonnesLance'
os.makedirs(lay, exist_ok=True)
blk = bytearray()
for my in range(MH):
    for mx in range(MW):
        col = 1 if G[my + Y0, mx + X0] & 0x8000 else 0
        # palier et escalier nord (y Platine <= 13) : ils descendent derrière l'esplanade et
        # restent invisibles en vue GBA, on les ferme
        if my + Y0 <= 13: col = 1
        blk += struct.pack('<H', grille[my, mx] | col << 10 | 3 << 12)
open(f'{lay}/map.bin', 'wb').write(blk)
# bordure : bloc 2x2 pris dans le plateau rose à gauche de l'esplanade
bx, by = 2, 26
open(f'{lay}/border.bin', 'wb').write(b''.join(struct.pack('<H', grille[by + j, bx + i] | 1 << 10 | 3 << 12) for j in (0, 1) for i in (0, 1)))
print(f'carte {MW}x{MH}, palettes {len(pals)}, tuiles {len(toutes)} (fusions {fusions}), métatuiles {len(liste_metas)}')
