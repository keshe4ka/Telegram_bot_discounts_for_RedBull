import re

from config import shop_magnit_url
from parser import parse

soup = parse(shop_magnit_url, 3)

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
