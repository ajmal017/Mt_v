import time
import requests
import globals
from bs4 import BeautifulSoup
from requests.packages.urllib3.exceptions import InsecureRequestWarning
requests.packages.urllib3.disable_warnings(InsecureRequestWarning)


def scrape():
    globals.clear()
    r = requests.get("http://mex.co.ir/")
    api_url = 'https://www.markettime.ir/update/exchangeIR/'
    soup = BeautifulSoup(r.content, 'html.parser')
    raw_prices = soup.find_all('span')[0:4]
    prices = [price.text for price in raw_prices]
    arz = {
        'EUR': {'buy': prices[0], 'sell': prices[1]},
        'USD': {'buy': prices[2], 'sell': prices[3]},
    }
    rates = {'exchange_rate': arz}
    r = requests.post(api_url, json=rates,
                      headers=globals.header, verify=False)
    print(r.text)

while 1:
    try:
        scrape()
    except KeyboardInterrupt:
        raise
    time.sleep(1800)
