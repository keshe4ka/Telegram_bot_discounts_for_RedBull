import telebot
import schedule
from telebot import types

from config import bot_token

import parserBristol
import parserLenta
import parser5ka
import parserMagnit
import parserMetro

bot = telebot.TeleBot(bot_token)

info_from_parsers = parserLenta.info + parserBristol.info + parser5ka.info + parserMagnit.info + parserMetro.info


@bot.message_handler(commands=['start', 'help'])
def start_command(message):
    markup = types.InlineKeyboardMarkup()
    bot.send_message(message.chat.id,
                     "Привет, я показываю скидки на большую баночку редбулла. "
                     "\nМного не пей"
                     "\nТолько Архангельск",
                     reply_markup=markup)


@bot.message_handler(commands=['show'])
def start_command(message):
    bot.send_message(message.chat.id, info_from_parsers)


# schedule.every().day.at("16:04").do(send_info)

if __name__ == '__main__':
    bot.polling(none_stop=True)
