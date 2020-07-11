import os
import time
import telebot
from tempfile import gettempdir

import bot.config as cfg
import bot.text_managment as tm

bot = telebot.TeleBot(cfg.TOKEN)

@bot.message_handler(commands=['start'])
def start_handler(message):
    bot.send_message(message.chat.id, cfg.START_MESSAGE)


@bot.message_handler(commands=['help'])
def help_handler(message):
    bot.send_message(message.chat.id, cfg.HELP_MESSAGE)


@bot.message_handler(func=lambda message: True)
def messages_handler(message):
    if message.json['chat']['type'] != 'group':
        bot.send_message(message.chat.id, cfg.TEXT_MESSAGE)


@bot.message_handler(func=lambda message: True, content_types=['photo'])
def echo_message(message):
    bot.send_chat_action(message.chat.id, 'upload_photo')

    raw = message.photo[-1].file_id
    file_info = bot.get_file(raw)
    
    with open(gettempdir() + "/" + raw + ".jpg", "wb+") as tf:
        tf.write(bot.download_file(file_info.file_path))
        tf.flush()

        font_size = tm.apply_text(tf.name, tm.choose_random_phrase()) if message.caption is None \
            else tm.apply_text(tf.name, message.caption)

        tf.seek(0)
        bot.send_photo(message.chat.id, tf)

    if font_size < cfg.MIN_FONT_BORDER:
        bot.send_message(message.chat.id,  "❗️Картинка слишком маленькая. Попробуй отправить картинку с расширением побольше!")

    os.remove(gettempdir() + "/" + raw + ".jpg")
    

if __name__ == "__main__":
    while True:
        try:
            bot.polling(none_stop=True)
        except Exception:
            time.sleep(25)
