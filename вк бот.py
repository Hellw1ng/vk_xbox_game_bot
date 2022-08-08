import time
import vk_api
from vk_api.longpoll import VkLongPoll, VkEventType
import requests
from bs4 import BeautifulSoup
import json

import test1
from test1 import *
import parsing
from parsing import main

# vk_session = vk_api.VkApi(token= "vk1.a.TXAsrFqS7uQ_HaCFtdZAvIoX6AQn_9tbNUQboSY0JAfu0NxCVkS9agE_hnHXvVSLU2-j_il-nSUcFJGWZz1oe1LuwWDNxeNcCYonoHXnH_i10mI1yDLGh3P1XJgRroi7VeDt0zOpNGHy3J3B0YFJwdYkRiCtErlDBGwcCqOJWFzkLLGQsqaeSi-i2SZZUa4s")
# session_api = vk_session.get_api()
# longpool = VkLongPoll(vk_session)
url = ("https://www.google.com/finance/quote/TRY-RUB?sa=X&ved=2ahUKEwjc4NzFl6j5AhUGjqQKHf63DIQQmY0JegQIAhAb")
connect = True
def send_some_msg0(user_id,some_txt):
    vk_session.method("messages.send", {
        "user_id": user_id,
        "message": '&#8252;&#65039;Бот не распознает стикеры,смайлики и не используется для поиска игры по 1 букве &#8252;&#65039;',
        "random_id": 0
    })

def send_some_msg1(user_id,some_txt):
    vk_session.method("messages.send", {
        "user_id": user_id,
        "message": '&#128683; Используйте для поиска больше 3 символов,иначе бот подберет вам слишком большое количество игр &#128683;',
        "random_id": 0
    })
def send_some_msg2(user_id,some_txt):
    vk_session.method("messages.send", {
        "user_id": user_id,
        "message": 'Начало обновления базы игр',
        "random_id": 0
    })
def send_some_msg3(user_id,some_txt):
    vk_session.method("messages.send", {
        "user_id": user_id,
        "message": 'Конец обновления базы игр',
        "random_id": 0
    })

def send_some_msg(user_id,some_txt):
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
        if some_txt.lower() in name.lower():
            price = float(price)
            price = price*kurs
            price = round(price)
            message_price = (f"&#128073; Название игры: {name}\n &#128073;Цена: {price} Руб.")
            vk_session.method("messages.send", {
                "user_id": user_id,
                "message": message_price,
                "random_id": 0
            })
            n = 1
    if n == 0:
        message_price = '&#129335; Такой игры нету,проверьте правильность ввода &#129335;'
        vk_session.method("messages.send",{
            "user_id": user_id,
            "message": message_price,
            "random_id":0
        })

def send_skidka_msg (user_id,some_txt):
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
        price = float(price)
        price = price*kurs
        price = round(price)
        message_price = (f"&#128073; Название игры: {name}\n &#128073;Цена: {price} Руб.")
        vk_session.method("messages.send", {
            "user_id": user_id,
            "message": message_price,
            "random_id": 0
        })
        n = 1
while connect:
    connect = False
    vk_session = vk_api.VkApi(
        token="vk1.a.TXAsrFqS7uQ_HaCFtdZAvIoX6AQn_9tbNUQboSY0JAfu0NxCVkS9agE_hnHXvVSLU2-j_il-nSUcFJGWZz1oe1LuwWDNxeNcCYonoHXnH_i10mI1yDLGh3P1XJgRroi7VeDt0zOpNGHy3J3B0YFJwdYkRiCtErlDBGwcCqOJWFzkLLGQsqaeSi-i2SZZUa4s")
    session_api = vk_session.get_api()
    longpool = VkLongPoll(vk_session)
    try:
        for event in longpool.listen():
            if event.type == VkEventType.MESSAGE_NEW and event.to_me and event.text:
                if event.text.lower() == [""," "] or len(event.text.lower()) == 1 :
                    msg = event.text.lower()
                    print(msg)
                    user_id = event.user_id
                    send_some_msg0(user_id, msg)
                elif  len(event.text.lower()) <=3:
                    msg = event.text.lower()
                    print(msg)
                    user_id = event.user_id
                    send_some_msg1(user_id,msg)
                elif event.text.lower() == "обновить базу игр":
                    msg = event.text.lower()
                    print(msg)
                    user_id = event.user_id
                    send_some_msg2(user_id, msg)
                    test1.main()
                    # time.sleep(20)
                    msg = event.text.lower()
                    user_id = event.user_id
                    send_some_msg3(user_id, msg)
                    raise requests.exceptions.ReadTimeout
                elif event.text.lower() == 'скидка' or event.text.lower() == 'скидки':
                    msg = event.text.lower()
                    print(msg)
                    user_id = event.user_id
                    send_skidka_msg(user_id,msg)

                elif event.text.lower() != [""," "]:
                    msg = event.text.lower()
                    print(msg)
                    user_id = event.user_id
                    send_some_msg(user_id,msg)



    except requests.exceptions.ReadTimeout:
        print("\n Переподключение к серверам ВК \n")
        time.sleep(20)
        connect=True
        print("\n Переподключение к серверам ВК прошло успешно \n")
    except :
        connect = True
