import re
from requests_html import HTMLSession
from bs4 import BeautifulSoup
from config import shop_bristol_url

session = HTMLSession()
response = session.get(shop_bristol_url)
soup = BeautifulSoup(response.content, 'html.parser')

title = re.sub(" +", " ", soup.find('h1').string)
#price1 = re.sub('\D', '', soup.find('span', class_='new').string)
#price2 = re.sub('\D', '', soup.find('small', class_='kopeck').string)

#btistol_info = "\nБРИСТОЛЬ:" + title + "Цена: " + price1.replace(' ', '') + "." + price2.replace(' ', '') + "р."
btistol_info = "\nБРИСТОЛЬ:\n" + title