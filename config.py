from dotenv import load_dotenv
import os
from os.path import join, dirname

dotenv_path = join(dirname(__file__), '.env')
load_dotenv(dotenv_path)

bot_token = os.environ.get("BOT_TOKEN")
shop_lenta_url = 'https://lenta.com/product/napitok-bezalkogolnyjj-red-bull-big-can-bolshaya-banka-toniz-energet-gaz-zhb-shvejjcariya-0473l-148381/'
shop_bristol_url = 'https://bristol.ru/catalog/produkty/red_bull_0_473l/'
shop_5ka_url = 'https://edadeal.ru/arhangelsk/retailers/5ka?brand=edde830c-9b8f-5bea-a477-adc00c912bc5'
shop_magnit_url = 'https://edadeal.ru/arhangelsk/retailers/magnit-univer?brand=edde830c-9b8f-5bea-a477-adc00c912bc5'
shop_metro_url = 'https://arh.metro-cc.ru/category/bezalkogolnye-napitki/energetiki/red-bull-0473-l'
