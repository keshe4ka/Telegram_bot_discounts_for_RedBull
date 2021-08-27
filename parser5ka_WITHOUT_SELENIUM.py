import re

from requests_html import HTMLSession
from selenium import webdriver
from bs4 import BeautifulSoup
from config import shop_5ka_url
from time import sleep

session = HTMLSession()
response = session.get(shop_5ka_url)
sleep(3)  # ожидание прогрузки страницы

soup = BeautifulSoup(response.content, 'html.parser')

title = soup.find('div', class_='b-offer__description')

checkDiscountOnBigCan = title.find('0,473')
print(checkDiscountOnBigCan)
if checkDiscountOnBigCan:
    checkDiscountInfo = ""
else:
    # checkDiscountInfo = "Скидок на большую банку нет "
    checkDiscountOnMiddleCan = title.find('0,355')
    if checkDiscountOnMiddleCan:
        checkDiscountInfo = "Банка 0,355 "
    else:
        checkDiscountInfo = "скидок на большую/среднюю банку нет"
price = re.sub('\D', '', soup.find('div', class_='b-offer__price-new').text)
price2 = price[-2:]
price1 = price[:-2]

info = "\nПЯТЕРОЧКА: " + checkDiscountInfo + price1 + "." + price2 + "р."
print(info)
