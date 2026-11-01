from PIL import Image
import sys
src=Image.open('orig_message_box.png')
pal=src.getpalette()[:48]
P=[tuple(pal[i:i+3]) for i in range(0,48,3)]
# Japanese palette: vermilion lacquer, gold kanagu, washi interior
P[1]=(248,240,220)   # washi (text background)
P[2]=(80,72,64)      # text, warm dark
P[3]=(216,204,180)   # text shadow, warm
P[10]=(248,224,136)  # gold highlight
P[11]=(200,152,56)   # gold
P[12]=(248,240,220)  # interior fill = washi
P[13]=(48,24,24)     # outline, black lacquer
P[14]=(208,64,40)    # vermilion
P[15]=(144,32,32)    # dark vermilion
K={'.':0,'d':13,'e':14,'f':15,'g':11,'h':10,'c':12}
def T(rows): return [[K[ch] for ch in r] for r in rows]
bar=["........","dddddddd","eeeeeeee","eeeeeeee","ffffffff","dddddddd","gggggggg","cccccccc"]
# top-left kanagu (gold corner fitting) spanning tile1 + left part of tile3
t1=T([".ddddddd",
      "dhhhhhhh",
      "dhggggggg"[:8],
      "dhgdhggg",
      "dhghhggg",
      "dhgggggg",
      "dhggggdd",
      "dhgggdgc"])
t3=T(["dd......",
      "hhdddddd",
      "ggdeeeee",
      "ggdeeeee",
      "ggdfffff",
      "dddddddd",
      "gggggggg",
      "cccccccc"])
t4=T(bar)
side=["..dddddd"]
t7=T([".deefdgc"]*8)
def hflip(t): return [r[::-1] for r in t]
t5=hflip(t3); t6=hflip(t1); t10=hflip(t7)
t9=T(["cccccccc"]*8)
tiles={1:t1,3:t3,4:t4,5:t5,6:t6,7:t7,9:t9,10:t10}
im=Image.new('P',(56,16),0)
flat=[]
for c in P: flat+=list(c)
im.putpalette(flat)
for n,t in tiles.items():
    ox,oy=(n%7)*8,(n//7)*8
    for y in range(8):
        for x in range(8): im.putpixel((ox+x,oy+y),t[y][x])
im.save(sys.argv[1] if len(sys.argv)>1 else 'message_box.png')
# preview: assemble a 240x48 box like WindowFunc_DrawDialogueFrame
def tile(n):
    ox,oy=(n%7)*8,(n//7)*8; return im.crop((ox,oy,ox+8,oy+8))
B=Image.new('P',(240,48),0); B.putpalette(im.getpalette())
row=[1,3]+[4]*26+[5,6]
for i,n in enumerate(row):
    B.paste(tile(n),(i*8,0)); B.paste(tile(n).transpose(Image.FLIP_TOP_BOTTOM),(i*8,40))
for r in range(1,5):
    B.paste(tile(7),(0,r*8)); B.paste(tile(10),(29*8,r*8))
    for i in range(1,29): B.paste(tile(9),(i*8,r*8))
bg=Image.new('RGB',(240,48),(120,180,120)); m=Image.new('L',(240,48),0)
m.putdata([255 if v else 0 for v in B.getdata()])
bg.paste(B.convert('RGB'),(0,0),m); bg.resize((960,192),Image.NEAREST).save('preview.png')
