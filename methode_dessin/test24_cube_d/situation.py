"""Écran GBA 240×160 : le Dé en grand (×1, puis le même écran agrandi ×3 pour la lecture)
et l'icône du sac dans une case. Le fond et la case sont des aplats simples."""
from PIL import Image, ImageDraw
de=Image.open('de_64.png'); ic=Image.open('de_icone_24.png')
s=Image.new('RGBA',(240,160),(34,30,44,255)); d=ImageDraw.Draw(s)
s.alpha_composite(de,(88,22))
d.rectangle([4,116,235,155],fill=(236,234,228,255),outline=(30,26,42,255))
d.rectangle([10,124,39,147],fill=(200,198,206,255),outline=(90,88,103,255))
s.alpha_composite(ic,(13,124))
s.save('situation.png'); s.resize((720,480),Image.NEAREST).save('situation_x3.png')
