from PIL import Image
from PIL import ImageFont
from PIL import ImageDraw 
import os


img = Image.open("test.jpg")
print(img, dir(img))
print(img.height, img.width)
draw = ImageDraw.Draw(img)
# font = ImageFont.truetype(<font-file>, <font-size>)
print(img.height * 0.04)
font = ImageFont.truetype("lobster.ttf", int(img.height * 0.04) * 2)
# draw.text((x, y),"Sample Text",(r,g,b))
msg = input("вводи: ")
w, h = draw.textsize(msg, font=font)
print(w, h, "ayo", img.height - int(img.height * 0.06))
draw.text(((img.width - w) // 2, (img.height - h) -  1 * int(img.height * 0.06) * 0.5),msg,(255,255,255),font=font)
img.save('sample-out.jpg')
print(img.height - h - int(img.height * 0.06))
