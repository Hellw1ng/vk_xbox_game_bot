import telebot
import requests
from bs4 import BeautifulSoup
import json
import parsjsonTur
from parsjsonTur import *
import parsjsonArg
from parsingArg import *
# import parsing
# from parsing import main


bot = telebot.TeleBot('5771576015:AAE4Z0aOJNMH9qWgRo1A7Oq-_P6wE72MKYk')
url_try = ("https://www.google.com/finance/quote/TRY-RUB?sa=X&ved=2ahUKEwjc4NzFl6j5AhUGjqQKHf63DIQQmY0JegQIAhAb")
url_arg = ("https://www.google.com/finance/quote/ARS-RUB?sa=X&ved=2ahUKEwjhiIf8i775AhVmAxAIHfmVChoQmY0JegQIAhAb")


while True:
  try:
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
                parsjsonArg.main()
                # time.sleep(20)
                msg = message.text.lower()
                # user_id = message.user_id
                bot.send_message(message.chat.id, 'Конец обновления базы игр')
            elif message.text.lower() == 'скидка' or message.text.lower() == 'скидки':
                msg = message.text.lower()
                print(msg)
                # user_id = message.user_id
                with open('all_games.json', encoding="utf-8") as file:
                    all_games = json.load(file)
                with open('all_games_arg.json', encoding="utf-8") as file:
                    all_games_arg = json.load(file)
                with open('all_games_id.json', encoding="utf-8") as file:
                    all_games_id = json.load(file)
                with open('all_games_id_tur.json', encoding="utf-8") as file:
                    all_games_id_tur = json.load(file)
                n = 0
                req = requests.get(url_try)
                src = req.text
                soup = BeautifulSoup(src, 'lxml')
                kurs_try = soup.find('div', class_='YMlKec fxKbKc').text.split()
                kurs_try = float(kurs_try[0])
                req = requests.get(url_arg)
                src_arg = req.text
                soup = BeautifulSoup(src_arg, 'lxml')
                kurs_arg = soup.find('div', class_='YMlKec fxKbKc').text.split()
                kurs_arg = float(kurs_arg[0])
                for name_tur, price in all_games.items():
                    #if msg.lower() in name_tur.lower():
                        for name2, id2 in all_games_id_tur.items():
                            if name_tur == name2:
                                id = id2
                                for name1, id1 in all_games_id.items():
                                    if id == id1:
                                        name_arg_a = name1
                                        for name_arg, price_arg in all_games_arg.items():
                                            if name_arg == name_arg_a:
                                                print(name_arg)
                                                print(name_tur)
                                                price = price.split(' ', 1)
                                                price_arg = price_arg.split(' ', 1)
                                                if len(price) == 2 or len(price_arg) == 2:
                                                    smile_skidka = price_arg[1]
                                                    price = float(price[0])
                                                    price = price * kurs_try
                                                    price = round(price)
                                                    price_arg = float(price_arg[0])
                                                    price_arg = price_arg * kurs_arg
                                                    price_arg = round(price_arg)
                                                    if price <= price_arg:
                                                        message_price = (
                                                            f" Название игры: {name_tur}\n Цена: {price} Руб.  ")
                                                        message_price = (
                                                            f"🏷 Название игры: {name_tur}\n 💰 🇹🇷🇹🇷 Цена: {price} Руб. 🔥🔥")
                                                        bot.send_message(message.chat.id, message_price)

                                                    else:
                                                        message_price = (
                                                            f"&#128073; Название игры: {name_arg}\n &#128073; &#127462;&#127479; &#127462;&#127479;Цена: {price_arg} Руб.  {smile_skidka}")
                                                        message_price = (
                                                            f"🏷 Название игры: {name_arg}\n 💰 🇦🇷🇦🇷 Цена: {price_arg} Руб. 🔥🔥")
                                                        bot.send_message(message.chat.id, message_price)

            elif message.text.lower() != ["", " "]:
                msg = message.text.lower()
                print(msg)
                # user_id = message.user_id
                with open('all_games.json', encoding="utf-8") as file:
                    all_games = json.load(file)
                with open('all_games_arg.json', encoding="utf-8") as file:
                    all_games_arg = json.load(file)
                with open('all_games_id.json', encoding="utf-8") as file:
                    all_games_id = json.load(file)
                with open('all_games_id_tur.json', encoding="utf-8") as file:
                    all_games_id_tur = json.load(file)
                n = 0
                req = requests.get(url_try)
                src = req.text
                soup = BeautifulSoup(src, 'lxml')
                kurs_try = soup.find('div', class_='YMlKec fxKbKc').text.split()
                kurs_try = float(kurs_try[0])
                req = requests.get(url_arg)
                src_arg = req.text
                soup = BeautifulSoup(src_arg, 'lxml')
                kurs_arg = soup.find('div', class_='YMlKec fxKbKc').text.split()
                kurs_arg = float(kurs_arg[0])
                for name_tur, price in all_games.items():
                    if msg.lower() in name_tur.lower():
                        for name2, id2 in all_games_id_tur.items():
                            if name_tur == name2:
                                id = id2
                                for name1, id1 in all_games_id.items():
                                    if id == id1:
                                        name_arg_a = name1
                                        for name_arg, price_arg in all_games_arg.items():
                                            if name_arg == name_arg_a:
                                                print(name_arg)
                                                print(name_tur)
                                                price = price.split(' ', 1)
                                                price_arg = price_arg.split(' ', 1)
                                                if len(price) == 2 or len(price_arg) == 2:
                                                    smile_skidka = price_arg[1]
                                                    price = float(price[0])
                                                    price = price * kurs_try
                                                    price = round(price)
                                                    price_arg = float(price_arg[0])
                                                    price_arg = price_arg * kurs_arg
                                                    price_arg = round(price_arg)
                                                    if price <= price_arg:
                                                        message_price = (
                                                            f" Название игры: {name_tur}\n Цена: {price} Руб.  ")
                                                        message_price = ( f"🏷 Название игры: {name_tur}\n 💰 🇹🇷🇹🇷 Цена: {price} Руб. 🔥🔥")
                                                        bot.send_message(message.chat.id, message_price)

                                                    else:
                                                        message_price = (
                                                            f"&#128073; Название игры: {name_arg}\n &#128073; &#127462;&#127479; &#127462;&#127479;Цена: {price_arg} Руб.  {smile_skidka}")
                                                        message_price = (
                                                            f"🏷 Название игры: {name_arg}\n 💰 🇦🇷🇦🇷 Цена: {price_arg} Руб. 🔥🔥")
                                                        bot.send_message(message.chat.id, message_price)

                                                    n = 1
                                                else:
                                                    price = float(price[0])
                                                    price = price * kurs_try
                                                    price = round(price)
                                                    price_arg = float(price_arg[0])
                                                    price_arg = price_arg * kurs_arg
                                                    price_arg = round(price_arg)
                                                    if price <= price_arg:
                                                        message_price = ( f"🏷 Название игры: {name_tur}\n 💰 🇹🇷🇹🇷 Цена: {price} Руб.")
                                                        bot.send_message(message.chat.id, message_price)

                                                    else:
                                                        message_price = (
                                                            f"🏷 Название игры: {name_arg}\n 💰 🇦🇷🇦🇷 Цена: {price_arg} Руб. 🔥🔥")
                                                        bot.send_message(message.chat.id, message_price)

                                                    n = 1
                if n == 0:
                    message_price = '‼ Такой игры нету,проверьте правильность ввода ‼'





        bot.polling(none_stop=True)
  except:
    connect = True