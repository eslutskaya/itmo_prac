import telebot
import requests
from bs4 import BeautifulSoup as BS

r = requests.get('https://sinoptik.ua/%D0%BF%D0%BE%D0%B3%D0%BE%D0%B4%D0%B0-%D1%81%D0%B0%D0%BD%D0%BA%D1%82-%D0%BF%D0%B5%D1%82%D0%B5%D1%80%D0%B1%D1%83%D1%80%D0%B3')
bot = telebot.TeleBot('850481393:AAETR5yudioMXUMuW-21Nn7S_rfATSgANP8')
html = BS(r.content, 'html.parser')

for el in html.select('#content'):
    t_min = el.select('.temperature .min')[0].text
    t_max = el.select('.temperature .max')[0].text
    text = el.select('.wDescription .description')[0].text

@bot.message_handler(content_types=['text'])
def send_text(message):
    if message.text== 'Погода':
        bot.send_message(message.chat.id, "Привет, погода на сегодня:\n" +
                         t_min + ', ' + t_max + '\n' + text)
    elif message.text=='Привет!':
        bot.send_message(message.chat.id, 'Привет, набери "Погода, если хочешь узгать погоду на сегодня"')


bot.polling()