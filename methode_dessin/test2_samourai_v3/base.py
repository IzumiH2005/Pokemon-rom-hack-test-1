"""Outils communs : canevas 128x192, agrandissement, guides."""
import os
from PIL import Image, ImageDraw
OUT = os.path.dirname(os.path.abspath(__file__))
W, H = 128, 192
S = 4
BG = (236, 232, 222, 255)

def up(img, s=S):
    return img.resize((img.width * s, img.height * s), Image.NEAREST)

def on_bg(img):
    bg = Image.new("RGBA", img.size, BG)
    bg.alpha_composite(img)
    return bg

def guide():
    """Calque guide agrandi (on dessine les lignes de construction en coordonnées pixel)."""
    g = Image.new("RGBA", (W * S, H * S), (0, 0, 0, 0))
    return g, ImageDraw.Draw(g)

def P(x, y):
    return (x * S + S // 2, y * S + S // 2)
