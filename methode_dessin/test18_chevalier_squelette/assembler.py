# Empile les calques (du fond vers le devant) sur un fond transparent ('.').
# Ne décide aucune forme : '.' d'un calque laisse voir ce qui est dessous.
import sys
ORDRE = """calque28_cape calque14_jambes calque27_jambiere calque12_bassin calque26_ceinture
calque11_tronc calque23_plastron calque13_bras calque29_epee calque25_gantelet calque29c_pommeau
calque24_epauliere calque22_gorgerin calque10_crane calque21_panache calque20_heaume
calque30_flamme calque31_volutes""".split()
if __name__ == '__main__':
    G = [['.'] * 128 for _ in range(128)]
    for nom in ORDRE:
        for y, l in enumerate(x.rstrip('\n') for x in open(nom + '.txt') if x.strip()):
            for x, c in enumerate(l):
                if c != '.': G[y][x] = c
    open(sys.argv[1] if len(sys.argv) > 1 else 'assemble.txt', 'w').write('\n'.join(''.join(r) for r in G) + '\n')
