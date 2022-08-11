import telebot
import requests
from bs4 import BeautifulSoup
import json
import parsjsonTur
from parsjsonTur import *
# import parsing
# from parsing import main


bot = telebot.TeleBot('5382388258:AAGEep0hi5f5p63KNA7vGStHosUDkMtXomc')
url = ("https://www.google.com/finance/quote/TRY-RUB?sa=X&ved=2ahUKEwjc4NzFl6j5AhUGjqQKHf63DIQQmY0JegQIAhAb")


@bot.message_handler(commands=['start'])
def start(message):
    mess = f'Привет {message.from_user.first_name} {message.from_user.last_name} ,просто напишите название игры и бот подскажет вам цену '
    bot.send_message(message.chat.id,mess)

@bot.message_handler()
def get_user_text(message):
    if message.text.lower() == ["", " "] or len(message.text.lower()) == 1:
        msg = message.text.lower()
        print(msg)
        # user_id = message.user_id
        bot.send_message(message.chat.id, '	‼ Бот не распознает стикеры,смайлики и не используется для поиска игры по 1 букве ‼ ')
    elif len(message.text.lower()) <= 3:
        msg = message.text.lower()
        print(msg)
        # user_id = message.user_id
        bot.send_message(message.chat.id, '‼ Используйте для поиска больше 3 символов,иначе бот подберет вам слишком большое количество игр ‼ ')
    elif message.text.lower() == "обновить базу игр":
        msg = message.text.lower()
        print(msg)
        # user_id = message.user_id
        bot.send_message(message.chat.id, 'Начало обновления базы игр')
        parsjsonTur.main()
        # time.sleep(20)
        msg = message.text.lower()
        # user_id = message.user_id
        bot.send_message(message.chat.id, 'Конец обновления базы игр')
    elif message.text.lower() == 'скидка' or message.text.lower() == 'скидки':
        msg = message.text.lower()
        print(msg)
        # user_id = message.user_id
        with open('games_with_sale.json', encoding="utf-8") as file:
            games_with_sale = json.load(file)
        n = 0
        req = requests.get(url)
        src = req.text
        soup = BeautifulSoup(src, 'lxml')
        kurs = soup.find('div', class_='YMlKec fxKbKc').text.split()
        kurs = float(kurs[0])
        for name, price in games_with_sale.items():
            # for i in rep:
            price = price.split(' ', 1)
            smile_skidka = price[1]
            print(smile_skidka)
            price = float(price[0])
            print(price)
            price = price * kurs
            price = round(price)
            print(price)
            message_price = (f"🏷 Название игры: {name}\n 💰;Цена: {price} Руб.  🔥")
            bot.send_message(message.chat.id, message_price)
            n = 1


    elif message.text.lower() != ["", " "]:
        msg = message.text.lower()
        print(msg)
        # user_id = message.user_id
        with open('all_games.json', encoding="utf-8") as file:
            all_games = json.load(file)
        n = 0
        req = requests.get(url)
        src = req.text
        soup = BeautifulSoup(src, 'lxml')
        kurs = soup.find('div', class_='YMlKec fxKbKc').text.split()
        kurs = float(kurs[0])
        for name, price in all_games.items():
            # for i in rep:
            if msg.lower() in name.lower():
                price = price.split(' ', 1)
                if len(price) == 2:
                    smile_skidka = price[1]
                    price = float(price[0])
                    price = price * kurs
                    price = round(price)
                    message_price = (f"🏷 Название игры: {name}\n 💰 Цена: {price} Руб. 🔥🔥")
                    bot.send_message(message.chat.id, message_price)
                    n = 1
                else:
                    price = float(price[0])
                    price = price * kurs
                    price = round(price)

                    message_price = (f"🏷 Название игры: {name}\n 💰 Цена: {price} Руб.")
                    bot.send_message(message.chat.id, message_price)
                    n = 1
        if n == 0:
            message_price = '‼ Такой игры нету,проверьте правильность ввода ‼'
            bot.send_message(message.chat.id, message_price)


bot.polling(none_stop=True)