import os

TOKEN = os.environ['TOKEN']

PHRASES_PATH = "data/sentences.txt"

FONT_PATH = "data/lobster.ttf"
FONT_FACTOR = 0.04
MIN_FONT_BORDER = 7

TEXT_YOFFSET = 0.03

BLACK = (0, 0, 0)
WHITE = (255, 255, 255)


START_MESSAGE = """🦞 Отправь мне картинку и я верну тебе лобстер-картинку.\n
✉️ Можешь добавить свою надпись, и я нанесу ее на твою картинку.\n
👥Так же меня можно добавлять в групповые чаты."""

HELP_MESSAGE = START_MESSAGE

TEXT_MESSAGE = """📌 К сожалению, пока что я не воспринимаю текст.
Лучше отправь мне картинку!"""
