import telebot
from telebot import types

import parserBristol
import parserLenta
from config import bot_token

bot = telebot.TeleBot(bot_token)


@bot.message_handler(commands=['start', 'help'])
def start_command(message):
    markup = types.InlineKeyboardMarkup()
    btn_my_site = types.InlineKeyboardButton(text='Проект на GitHub',
                                             url='https://github.com/keshe4ka/Telegram_bot_discounts_for_RedBull')
    markup.add(btn_my_site)
    bot.send_message(message.chat.id,
                     "Привет, я показываю скидки на энергетики в твоем городе, по кнопке ниже ты можешь перейти на гитхаб этого проекта и внести свой вклад в развитие бота",
                     reply_markup=markup)


@bot.message_handler(commands=['show'])
def start_command(message):
    bot.send_message(message.chat.id, parserLenta.lenta_info + parserBristol.btistol_info)


if __name__ == '__main__':
    bot.polling(none_stop=True)
