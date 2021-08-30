import re

from config import shop_lenta_url
from parser import parse

soup = parse(shop_lenta_url, 0)

prices = soup.find('div',
                   class_='price-label price-label--primary sku-price sku-price--primary sku-prices-block__price')
price1 = re.sub('\D', '', prices.find('span', class_='price-label__integer').string)
price2 = re.sub('\D', '', prices.find('small', class_='price-label__fraction').string)
info = "ЛЕНТА: " + price1.replace(' ', '') + "." + price2.replace(' ', '') + "р."
