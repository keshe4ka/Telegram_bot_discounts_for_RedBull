import re
from requests_html import HTMLSession
from bs4 import BeautifulSoup
from config import shop_bristol_url

session = HTMLSession()
response = session.get(shop_bristol_url)
soup = BeautifulSoup(response.content, 'html.parser')

# title = re.sub(" +", " ", soup.find('h1').string)

price = re.sub('\D', '', soup.find('span', class_='new').text)
price2 = price[-2:]
price1 = price[:-2]

btistol_info = "\nБРИСТОЛЬ: " + price1 + "." + price2 + "р."
