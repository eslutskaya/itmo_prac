import telebot
import requests
from bs4 import BeautifulSoup as BS
bot = telebot.TeleBot('TOKEN')

r = requests.get('https://sinoptik.ua/погода-санкт-петербург')
html = BS(r.content, 'html.parser')
for el in html.select('#content'):
    t_min = el.select('.temperature .min')[0].text
    t_max = el.select('.temperature .max')[0].text
    text = el.select('.wDescription .description')[0].text

#for examle
# def exchange_command(message):
#     keyboard = telebot.types.InlineKeyboardMarkup()
#     keyboard.row(
#         telebot.types.InlineKeyboardButton('USD', callback_data='get-USD')
#     )
#     keyboard.row(
#         telebot.types.InlineKeyboardButton('EUR', callback_data='get-EUR')
#     )
#     bot.send_message(
#         message.chat.id,
#         'Click on the currency of choice:',
#         reply_markup=keyboard
#     )


@bot.message_handler(content_types=['text'])
def send_text(message):
    if message.text.lower() == 'Погода':
        bot.send_message(message.chat.id, "Привет, погода на сегодня:\n" +
                         t_min + ', ' + t_max + '\n' + text)
    elif message.text.lower() == 'Привет!':
        bot.send_message(message.chat.id, 'Привет, наберите "Погода", если хотите узгать погоду на сегодня')

#for examle
# @bot.message_handler(content_types=["text"])
# def text(message):
#     if message.text == 'photo':
#         file = open('photo.png', 'rb')
#         bot.send_photo(message.chat.id, file)
#
# @bot.message_handler(content_types=["text"])
# def text(message):
#     if message.text == 'document':
#         file = open('file.txt', 'rb')
#         bot.send_document(message.chat.id, file)

bot.polling()