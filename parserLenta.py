import re
from requests_html import HTMLSession
from bs4 import BeautifulSoup
from config import shop_lenta_url

session = HTMLSession()
response = session.get(shop_lenta_url)
soup = BeautifulSoup(response.content, 'html.parser')

# title = re.sub(" +", " ", soup.find('h1', class_='sku-page__title').string)
prices = soup.find('div',
                   class_='price-label price-label--primary sku-price sku-price--primary sku-prices-block__price')
price1 = re.sub('\D', '', prices.find('span', class_='price-label__integer').string)
price2 = re.sub('\D', '', prices.find('small', class_='price-label__fraction').string)
info = "ЛЕНТА: " + price1.replace(' ', '') + "." + price2.replace(' ', '') + "р."
