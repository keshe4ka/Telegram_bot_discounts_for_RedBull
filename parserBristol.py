import re

from config import shop_bristol_url
from parser import parse

soup = parse(shop_bristol_url)

price = re.sub('\D', '', soup.find('span', class_='new').text)
price2 = price[-2:]
price1 = price[:-2]

info = "\nБРИСТОЛЬ: " + price1 + "." + price2 + "р."
