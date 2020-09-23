import time
import requests
from bs4 import BeautifulSoup


def scrape():
    r = requests.get("http://mex.co.ir/")
    soup = BeautifulSoup(r.content, 'html.parser')
    raw_prices = soup.find_all('span')[0:4]
    prices = [price.text for price in raw_prices]
    arz = {
        'EUR': {'buy': prices[0], 'sell': prices[1]},
        'USD': {'buy': prices[2], 'sell': prices[3]},
    }
    rates = {'exchange': arz}
    r = requests.post(self.api_url, json=rates,
                      headers=globals.header, verify=False)
    print(r.text)


scrape()
