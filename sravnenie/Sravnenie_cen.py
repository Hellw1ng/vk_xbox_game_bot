import json
import requests
from bs4 import BeautifulSoup

url_try = ("https://www.google.com/finance/quote/TRY-RUB?sa=X&ved=2ahUKEwjc4NzFl6j5AhUGjqQKHf63DIQQmY0JegQIAhAb")
url_arg = ("https://www.google.com/finance/quote/ARS-RUB?sa=X&ved=2ahUKEwjhiIf8i775AhVmAxAIHfmVChoQmY0JegQIAhAb")

some_txt = input()
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
    if some_txt.lower() in name_tur.lower():
        for name2, id2 in all_games_id_tur.items():
            if name_tur == name2:
                id = id2
                for name1, id1 in all_games_id.items():
                    if id == id1:
                        name_arg_a = name1
                        for name_arg, price_arg in all_games_arg.items():
                            if name_arg == name_arg_a:

                    # for name1, id1 in all_games_id.items():
                    #     for name2, id2 in all_games_id_tur.items():
                    #         if some_txt.lower() in name_arg.lower() and name_arg ==name1 and id1 == id2:
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
                                            f"&#128073; Название игры: {name_tur}\n &#128073; &#127481;&#127479; &#127481;&#127479;Цена: {price} Руб.  {smile_skidka}")
                                        print(message_price)

                                    else:
                                        message_price = (
                                            f"&#128073; Название игры: {name_arg}\n &#128073; &#127462;&#127479; &#127462;&#127479;Цена: {price_arg} Руб.  {smile_skidka}")
                                        print(message_price)

                                    n = 1
                                else:
                                    price = float(price[0])
                                    price = price * kurs_try
                                    price = round(price)
                                    price_arg = float(price_arg[0])
                                    price_arg = price_arg * kurs_arg
                                    price_arg = round(price_arg)
                                    if price <= price_arg:
                                        message_price = (
                                            f"&#128073; Название игры: {name_tur}\n &#128073; &#127481;&#127479; &#127481;&#127479;Цена: {price} Руб.")
                                        print(message_price)

                                    else:
                                        message_price = (
                                            f"&#128073; Название игры: {name_arg}\n &#128073; &#127462;&#127479; &#127462;&#127479;Цена: {price_arg} Руб. ")
                                        print(message_price)

                                    n = 1
if n == 0:
    message_price = '&#129335; Такой игры нету,проверьте правильность ввода &#129335;'
    print(message_price)



