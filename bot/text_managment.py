from PIL import Image, ImageFont, ImageDraw
from random import randint
import config as cfg


def choose_random_phrase():
    with open(cfg.PHRASES_PATH, "r") as f:
        data = f.readlines()
        return data[randint(0, len(data) - 1)][:-1]


def apply_text(img_name, text, shadows_offset=3):
    with Image.open(img_name) as img:
        draw = ImageDraw.Draw(img)
        font_size = int(img.width * cfg.FONT_FACTOR)
        font = ImageFont.truetype(cfg.FONT_PATH, font_size)

        w, h = draw.textsize(text, font=font)
        x = (img.width - w) // 2
        y = img.height - h - int(img.height * cfg.TEXT_YOFFSET)

        draw.text((x + shadows_offset, y + shadows_offset), text, cfg.BLACK, font=font)
        draw.text((x, y), text, cfg.WHITE, font=font)

        img.save(img_name)

    return font_size

