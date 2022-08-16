import json
import re
import time
import requests
from bs4 import BeautifulSoup
from parsingArg import get_data_with_selenium
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager


def pars_json (lens):
    z=1
    n=0
    all_games = {}
    all_games_id = {}
    games_with_sale = {}
    while z<=lens:
        with open(f"index_selenium_arg_{z}.html",encoding="utf-8") as file:
            src = file.read()
        soup = BeautifulSoup(src, "lxml")
        quotes = soup.find_all('div', class_ ='m-product-placement-item f-size-medium context-game gameDiv qlButtonFunc')
        # print(soup.find_all('span',class_ = 'x-screen-reader').next_element)

        for l,i in enumerate(quotes, start=0):
            if i.find('span',class_='textpricenew x-hidden-focus') is not None:
                itemName = i.find('h3', class_='c-subheading-4 x1GameName').text.strip()
                itemPrice = i.find('span',class_='textpricenew x-hidden-focus').text.strip()
                itemId = i["data-bigid"]
                # print(itemId)
                n=n+1
                if i.find('span',class_ = 'x-screen-reader') is not None:
                    itemPreviousPrice = i.find('span',class_ = 'x-screen-reader').next_element.next_element
                    print(f'{n}: Было {itemPreviousPrice} стало {itemPrice} за {itemName}',)
                    itemPrice = itemPrice.replace(".", "")
                    itemPrice = itemPrice.replace("₺","")
                    itemPrice = itemPrice.replace(",", ".")
                    itemPrice = itemPrice.replace(" ", "")
                    itemPrice = itemPrice.replace("$", "")
                    # itemPrice = float(itemPrice)
                    itemPrice = itemPrice + " &#128293; "
                    print(itemPrice)
                    all_games_id [itemName] = itemId
                    all_games[itemName] = itemPrice
                    games_with_sale [itemName] = itemPrice

                else:
                    print(f'{n}:  {itemPrice} за {itemName}')
                    itemPrice = itemPrice.replace(".", "")
                    itemPrice = itemPrice.replace("₺","")
                    itemPrice = itemPrice.replace(",", ".")
                    itemPrice = itemPrice.replace("$", "")
                    itemPrice = itemPrice.replace(" ", "")
                    all_games_id[itemName] = itemId
                    # itemPrice = float(itemPrice)
                    all_games[itemName] = itemPrice

        z = z + 1
    # all_games = all_games.replace('\xa0', ' ')
    with open ('all_games_arg.json',"w",encoding="utf-8") as file:
        json.dump(all_games,file,indent=4,ensure_ascii=False)
    with open ('games_with_sale_arg.json',"w",encoding="utf-8") as file:
        json.dump(games_with_sale,file,indent=4,ensure_ascii=False)
    with open ('all_games_id.json',"w",encoding="utf-8") as file:
        json.dump(all_games_id,file,indent=4,ensure_ascii=False)

def main():
    # get_data_with_selenium("https://www.xbox.com/tr-tr/games/all-games?xr=shellnav")
    lens = get_data_with_selenium("https://www.xbox.com/es-AR/games/all-games?xr=shellnav")
    pars_json(lens)
    # pars_json(58)

if __name__ == '__main__':
    main()