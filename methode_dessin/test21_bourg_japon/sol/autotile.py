"""Assemble une case 16x16 par quarts 8x8 depuis le bloc 3x3 (48x48) et la planche interieure (32x32).
quart(dx,dy) : h = voisin horizontal dans la region, v = vertical, d = diagonal."""
def quart_src(qx, qy, h, v, d):
    if h and v and not d:                      # coin interieur : herbe au coin exterieur du quart
        return 'I', (16 if qx == 0 else 8), (8 if qy == 1 else 16)
    col = 1 if h else (0 if qx == 0 else 2)
    row = 1 if v else (0 if qy == 0 else 2)
    return 'B', col * 16 + qx * 8, row * 16 + qy * 8

def case(B, I, reg, cx, cy):
    out = [['.'] * 16 for _ in range(16)]
    for qy in (0, 1):
        for qx in (0, 1):
            dx, dy = qx * 2 - 1, qy * 2 - 1
            k, sx, sy = quart_src(qx, qy, (cx + dx, cy) in reg, (cx, cy + dy) in reg, (cx + dx, cy + dy) in reg)
            S = B if k == 'B' else I
            for y in range(8):
                out[qy * 8 + y][qx * 8:qx * 8 + 8] = list(S[sy + y][sx:sx + 8])
    return out

def apercu(B, I, reg, W, H):
    G = [['.'] * (W * 16) for _ in range(H * 16)]
    for (cx, cy) in reg:
        c = case(B, I, reg, cx, cy)
        for y in range(16): G[cy * 16 + y][cx * 16:cx * 16 + 16] = c[y]
    return G

if __name__ == '__main__':
    import sys
    lire = lambda p: [l.rstrip('\n') for l in open(p) if l.strip()]
    B, I = lire(sys.argv[1]), lire(sys.argv[2])
    reg = {(x, y) for x in range(1, 7) for y in (2, 3)} | {(x, y) for x in (3, 4) for y in range(3, 8)} | {(6, 1)} \
        | {(x, y) for x in range(4, 7) for y in (6, 7)}
    G = apercu(B, I, reg, 8, 9)
    open(sys.argv[3], 'w').write('\n'.join(''.join(r) for r in G) + '\n')
