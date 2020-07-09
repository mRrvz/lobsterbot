#import os
from tempfile import gettempdir, NamedTemporaryFile
from PIL import Image, ImageFont, ImageDraw
import config as cfg


def apply_text(img_name, text):
    with Image.open(img_name) as img:
        draw = ImageDraw.Draw(img)
        font = ImageFont.truetype("lobster.ttf", int(img.height * 0.04) * 2)
        w, h = draw.textsize(text, font=font)
        draw.text(((img.width - w) // 2, (img.height - h) -  1 * int(img.height * 0.06) * 0.5), text, cfg.WHITE, font=font)
        img.save(img_name)

