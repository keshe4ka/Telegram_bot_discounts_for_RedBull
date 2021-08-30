from requests_html import HTMLSession
from bs4 import BeautifulSoup
from time import sleep


def parse(url, time=0):
    session = HTMLSession()
    response = session.get(url)
    sleep(time)
    return BeautifulSoup(response.content, 'html.parser')
