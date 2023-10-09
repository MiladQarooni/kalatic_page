import requests
from bs4 import BeautifulSoup
import pandas as pd

url_site = "https://kalatik.com/category/264/huawei"
site = requests.get(url_site)
soup = BeautifulSoup(site.text, 'html.parser')
div1 = soup.find('div' , {'class': 'product-list-cont'})
div2 = div1.find_all('div', {'class': 'item-content'})

names = []
prices = []

kalaticDictionary = {
    'name': names,
    'price': prices}

for item in range(len(div2)):
    name = div2[item].find('a', {'class': 'lnk-title'}).text
    names.append(name)

    price = div2[item].find('div', {'class': 'item-price-value'}).text
    prices.append(price)

df = pd.DataFrame(kalaticDictionary)
df.to_csv('kalaticDictionary.csv')