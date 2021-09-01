import re

from config import shop_5ka_url
from parser import parse

soup = parse(shop_5ka_url, 3)

volume = soup.select('.b-offer__description')
# checkDiscountOnBigCan = title.find('0,25')
print(volume)
price = re.sub('\D', '', soup.find('div', class_='b-offer__price-new').text)
price2 = price[-2:]
price1 = price[:-2]
info = "\nПЯТЕРОЧКА: " + price1 + "." + price2 + "р."

#    info = "\nПЯТЕРОЧКА: скидки нет"
