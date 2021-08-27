import re

from requests_html import HTMLSession
from bs4 import BeautifulSoup
from config import shop_magnit_url
from time import sleep

session = HTMLSession()
response = session.get(shop_magnit_url)
sleep(3)  # ожидание прогрузки страницы

soup = BeautifulSoup(response.content, 'html.parser')

try:
    title = soup.find('div', class_='b-offer__description')
    checkDiscountOnBigCan = title.find('0,473')
    print(checkDiscountOnBigCan)
    price = re.sub('\D', '', soup.find('div', class_='b-offer__price-new').text)
    price2 = price[-2:]
    price1 = price[:-2]
    info = "\nМАГНИТ: " + price1 + "." + price2 + "р."
except:
    info = "\nМАГНИТ: скидки нет"
