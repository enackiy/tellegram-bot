import telebot

from config import token
from extensions import *

bot = telebot.TeleBot(token)

kyes = {
    'евро': 'EUR',
    'доллар': 'USD',
    'рубль': 'RUB',
}


@bot.message_handler(commands=['start', 'help'])
def send_help(message: telebot.types.Message):
    text = 'Доброе время суток\n\nВведи /start или /help для того что бы увидеть эту инструкцию\n\nВвед /values что бы увидеть информацию о всех доступных валютах\n\nДля того что бы узнать курс напишите :\nИмя валюты, цену на которую надо узнать\nИмя валюты, цену в которой надо узнать\nКоличество переводимой валюты'
    bot.reply_to(message, text)

@bot.message_handler(commands='values')
def send_values(message: telebot.types.Message):
	text = 'Валюты:\nRUB\nUSD\nEUR'
	bot.reply_to(message, text)

@bot.message_handler(func=lambda message: True)
def ne_komanda(message):
	try:
		otpravka=message.text.split()
		if otpravka[1]!="RUB":
			if otpravka[1]!="USD":
				if otpravka[1]!="EUR":
					raise APIException
		if otpravka[0]!="RUB":
			if otpravka[0]!="USD":
				if otpravka[0]!="EUR":
					raise APIException
		try:
			proverka= float(otpravka[2])
			otprvaka2= get_price(otpravka[0], otpravka[1], otpravka[2])
			bot.reply_to(message, f"Имя валюты, цену на которую надо узнать\n{otpravka[0]}\n\nИмя валюты, цену в которой надо узнать\n{otpravka[1]}\n\nКоличество переводимой валюты\n{otpravka[2]}\n\nРезультат\n{otprvaka2}")
		except:
			bot.reply_to(message, "Нужно ввести число при указаниях количества")
	except APIException:
		bot.reply_to(message, "Вы ввели не правильно название валюты")

print("Запустилось")
bot.infinity_polling()