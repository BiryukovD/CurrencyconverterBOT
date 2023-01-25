import telebot
from extensions import *
from config import TOKEN

bot = telebot.TeleBot(TOKEN)

@bot.message_handler(commands=['start', 'help'])
def answer(message):
    text = 'Конвертер валют\nБыстрый и удобный перевод валют в соответствии с актуальными курсами' \
           '\nДоступные валюты: евро(EUR), доллар(USD), канадский доллар(CAD), рубль(RUB), японская йена(JPY)' \
           '\nЧтобы начать работу с ботом введите команду в следующем формате:' \
           '\n<тикер валюты> <тикер валюты в которую нужно перевести> <количество переводимой валюты>'
    bot.send_message(message.chat.id, text)

@bot.message_handler(content_types=['text'])
def convert(message):
    try:
        values = message.text.split()
        if len(values) != 3:
            raise ConvertionException('Количество параметров не соответсвует требованиям')
        base, quote, amount = values
        result = CurrencyConverter.convert(base, quote, amount, values)
    except ConvertionException as e:
        bot.reply_to(message, f'Ошибка пользователя.\n{e}')
    except Exception as e:
        bot.reply_to(message, f'Не удалось обработать команду\n{e}')
    else:
        text = f'{amount} {base} составляет {round(result, 2)} {quote}'
        bot.send_message(message.chat.id, text)

bot.infinity_polling()

