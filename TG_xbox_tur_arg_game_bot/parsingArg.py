import codecs
import sys
import time
import requests
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService, Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.common.proxy import *
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import timeit
import asyncio

def get_data_with_selenium(url):

    PROXY = "103.109.239.142:8081"  # IP:PORT or HOST:PORT
    # PROXY = "45.187.76.2:3629"
    options = Options()
    options.add_argument('--proxy-server=http://%s' % PROXY)
    # options.add_argument('window-size=1920x1080')
    # options.add_argument('headless')
    options.add_argument('--incognito')
    options.add_experimental_option("excludeSwitches", ["enable-automation"])
    options.add_experimental_option("useAutomationExtension", False)
    options.add_argument("--disable-blink-features=AutomationControlled")

    service = Service(executable_path=ChromeDriverManager().install())

    options.add_argument("user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/103.0.0.0 Safari/537.36")
    # driver = webdriver.Chrome(service=service,options= options)
    # wait = WebDriverWait(driver, 500)

    connect_to_page = True
    while connect_to_page == True:
        try:
            connect_to_page = False
            driver = webdriver.Chrome(service=service, options=options)
            driver.get(url=url)
            i = 1
            # if timeit.timeit("""wait.until(EC.visibility_of_element_located((By.XPATH, "//span[contains(.,'Sonraki')]")))""") > 10:
            #     raise Exception
            # wait.until(EC.visibility_of_element_located((By.XPATH, "//span[contains(.,'Sonraki')]")))
            time.sleep(100)
            if driver.find_element(By.XPATH, "//span[contains(.,'Siguiente')]").is_displayed() == False:
                raise ex
            # driver.find_element(By.XPATH, "//span[contains(.,'Sonraki')]").is_displayed()
            elements = driver.find_elements(By.CLASS_NAME, 'paginatenum')
            pages = len(elements)
            print(elements)
            print(len(elements))
            while i<=pages:
                # wait.until(EC.visibility_of_element_located((By.XPATH ,"//span[contains(.,'Далее')]")))
                # i = i + 1
                with open(f"index_selenium_arg_{i}.html", "w", encoding="utf-8") as file:
                    file.write(driver.page_source)
                if driver.find_element(By.XPATH, "//span[contains(.,'Siguiente')]").is_displayed() == True:
                    element = driver.find_element(By.XPATH, "//span[contains(.,'Siguiente')]")
                    element.click()
                # else:
                #     raise ex
                print(f'Итерация {i} прошла успешно')
                i = i + 1
            # i=i+1
            # with open(f"index_selenium{i}.html", "w", encoding="utf-8") as file:
            #     file.write(driver.page_source)
            time.sleep(10)
            return pages

        except Exception as ex:
            print(ex)
            connect_to_page = True
            # driver.close()
            # driver.quit()
        except:
            connect_to_page = True
            # driver.close()
            # driver.quit()
        finally:
            driver.close()
            driver.quit()

        # with open("index_selenium.html") as file:
        #     src = file.read()

def main():

    get_data_with_selenium("https://www.xbox.com/es-AR/games/all-games?xr=shellnav")



if __name__ == '__main__':
    main()