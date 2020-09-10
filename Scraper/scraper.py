import sys
import requests
import time
import globals
from selenium import webdriver
from colorama import Fore, Style, init
init()


def start():
    # Expected Arguments:
    # URL to scrape , API URL to send data, Selector
    # Selector is either "default" or custom
    if len(sys.argv) < 2:
        return f"Expected 2 arguments. got {sys.argv}"
    print(sys.argv)
    url = sys.argv[1]
    api_url = sys.argv[2]
    driver = webdriver.Chrome("chromedriver.exe", options=globals.options)
<<<<<<< HEAD
    globals.clear()
    driver.get(url)
    print("Opening page")
    last_price = None
    err_count = 0
    while 1:
=======
    API_url = [
    "https://195.114.8.222/update/EURtoUSD/",
    ]
    scrape_url = [
    "https://www.tradingview.com/symbols/EURUSD/",
    "https://www.tradingview.com/symbols/GBPUSD/?exchange=OANDA",
    "https://www.tradingview.com/symbols/AUDUSD/?exchange=FX",
    "https://www.tradingview.com/symbols/USDCAD/?exchange=OANDA",
    "https://www.tradingview.com/symbols/USDJPY/?exchange=OANDA",
    "https://www.tradingview.com/symbols/USDINR/?exchange=FX_IDC",
    "https://www.tradingview.com/symbols/USDTRY/?exchange=OANDA",
    "https://www.tradingview.com/symbols/USDCNY/?exchange=FX_IDC",
    "https://www.tradingview.com/symbols/USDAED/?exchange=FX_IDC",
    "https://www.tradingview.com/symbols/USDRUB/?exchange=FOREXCOM"
    ]
    
    API_url = {    
    "https://www.tradingview.com/symbols/EURUSD/":"https://localhost/update/EURtoUSD/",
    "https://www.tradingview.com/symbols/GBPUSD/?exchange=OANDA":"https://localhost/update/GBPtoUSD/",
    "https://www.tradingview.com/symbols/AUDUSD/?exchange=FX":"https://localhost/update/AUDtoUSD/",
    "https://www.tradingview.com/symbols/USDCAD/?exchange=OANDA":"https://localhost/update/USDtoCAD/",
    "https://www.tradingview.com/symbols/USDJPY/?exchange=OANDA":"https://localhost/update/USDtoJPY/",
    "https://www.tradingview.com/symbols/USDINR/?exchange=FX_IDC":"https://localhost/update/USDtoINR/",
    "https://www.tradingview.com/symbols/USDTRY/?exchange=OANDA":"https://localhost/update/USDtoTRY/",
    "https://www.tradingview.com/symbols/USDCNY/?exchange=FX_IDC":"https://localhost/update/USDtoCNY/",
    "https://www.tradingview.com/symbols/USDRUB/?exchange=FOREXCOM":"https://localhost/update/USDtoRUB/",
    "https://www.tradingview.com/symbols/USDAED/?exchange=FX_IDC":"https://localhost/update/USDtoAED/"
    }
    

    
    def crawl(self):
        clear()
        last_prices = {}
        print(f"""
                ============================================================
                Please be patient. The crawler is going to open {len(self.scrape_url)} tabs.
                This is a very CPU intensive proccess. 
                For the crawler to perform better in tab opening stage,
                Close all cpu intensive proccess if possible.
                ============================================================
        """)
>>>>>>> 31d6886599118d06896c8755ff7cad31c6f05a39
        try:
            globals.clear()
            price = driver.find_element_by_css_selector(globals.selector)
            price_text = price.text
            if price_text == last_price:
                continue
            params = {'rate': price.text}
            r = requests.post(api_url, data=params,
                              headers=globals.header,
                              verify=False)
            print(f"{Fore.GREEN}{price.text}{Style.RESET_ALL}")
            print(r.text)
            last_price = price_text
            time.sleep(1)
        except Exception as e:
            print(f"Exception {e} occured.")
            if err_count > 5:
                return -1
            err_count += 1


start()
