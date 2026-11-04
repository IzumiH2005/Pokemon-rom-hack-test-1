"""Image en situation : écran GBA 240×160, décor neutre assombri (pause), inventaire au centre."""
from PIL import Image
inv = Image.open('etape90_assemblage.png').convert('RGBA')
fond = Image.new('RGBA', (240, 160), (58, 96, 62, 255))
for y in range(0, 160, 16):          # tuiles d'herbe 16×16 en damier de deux verts
    for x in range(0, 240, 16):
        if (x // 16 + y // 16) % 2:
            fond.paste((66, 108, 68, 255), (x, y, x + 16, y + 16))
for y in range(64, 96):              # chemin de terre
    for x in range(240):
        fond.putpixel((x, y), (150, 120, 82, 255))
voile = Image.new('RGBA', (240, 160), (20, 16, 30, 140))   # pause : décor assombri
fond.alpha_composite(voile)
fond.alpha_composite(inv, (56, 16))
fond.save('situation.png')
fond.resize((720, 480), Image.NEAREST).save('situation_x3.png')
