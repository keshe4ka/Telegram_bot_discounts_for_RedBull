import re

from selenium import webdriver
from bs4 import BeautifulSoup
from config import shop_metro_url
from time import sleep

options = webdriver.FirefoxOptions()
options.add_argument('--headless')

browser = webdriver.Firefox(firefox_options=options)
browser.get(shop_metro_url)
sleep(1)  # ожидание прогрузки страницы
browser.find_element_by_xpath(".//a[@class='warning__button']").click()
sleep(1)
generatedHTML = browser.page_source

browser.quit()

soup = BeautifulSoup(generatedHTML, 'html.parser')

price = re.sub('\D', '', soup.find('div', class_='price-card__price').text)
info = "\nМЕТРО: " + price + ".00р."
