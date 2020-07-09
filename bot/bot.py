import telebot
import config as cfg

from lobster import apply_text
from tempfile import gettempdir

bot = telebot.TeleBot(cfg.TOKEN)

@bot.message_handler(commands=['start'])
def start_handler(message):
    bot.send_message(message.chat.id, "Это старт")


@bot.message_handler(commands=['help'])
def help_handler(message):
    bot.send_message(message.chat.id, "Лобстербот")


@bot.message_handler(func=lambda message: True)
def messages_handler(message):
    bot.send_message(message.chat.id, "Я не понимаю текст")


@bot.message_handler(func=lambda message: True, content_types=['photo'])
def echo_message(message):
    raw = message.photo[-1].file_id
    file_info = bot.get_file(raw)
    
    with open(gettempdir() + "/" + raw + ".jpg", "wb") as tf:
        tf.write(bot.download_file(file_info.file_path))
        apply_text(tf.name, "default") if message.caption is None else apply_text(tf.name, message.caption)

    with open(gettempdir() + "/" + raw + ".jpg", "rb") as tf:
        bot.send_photo(message.chat.id, tf)


bot.polling()
