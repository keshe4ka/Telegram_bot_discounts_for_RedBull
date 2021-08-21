import re

from selenium import webdriver
from bs4 import BeautifulSoup
from config import shop_5ka_url
from time import sleep

options = webdriver.FirefoxOptions()
options.add_argument('--headless')

browser = webdriver.Firefox(firefox_options=options)
browser.get(shop_5ka_url)
sleep(3)  # ожидание прогрузки страницы
generatedHTML = browser.page_source

browser.quit()

soup = BeautifulSoup(generatedHTML, 'html.parser')

title = soup.find('div', class_='b-offer__description')

checkDiscountOnBigCan = title.find('0,473')
print(checkDiscountOnBigCan)
checkDiscountInfo = ""
if checkDiscountOnBigCan == -1:
    checkDiscountInfo = "Скидок на большую банку нет "
    checkDiscountOnMiddleCan = title.find('0,355')
    if checkDiscountOnMiddleCan != -1:
        checkDiscountInfo = "Банка 0,355 "

price = re.sub('\D', '', soup.find('div', class_='b-offer__price-new').text)
price2 = price[-2:]
price1 = price[:-2]

info = "\n ПЯТЕРОЧКА: " + checkDiscountInfo + price1 + "." + price2 + "р."
print(info)
