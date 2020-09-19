import os
import time
import requests
from timeit import default_timer as timer
import globals
from datetime import datetime
from selenium import webdriver
from requests.packages.urllib3.exceptions import InsecureRequestWarning
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
from colorama import Fore, Style, init
init()
requests.packages.urllib3.disable_warnings(InsecureRequestWarning)
clear = lambda: os.system('cls' if os.name == 'nt' else 'clear')


class Crawler():

    driver = webdriver.Chrome("chromedriver.exe", options=globals.options)
    req_url= "https://www.markettime.ir/update/CurrencyExchange/"

    scrape_url = {
        "https://www.tradingview.com/symbols/EURUSD/": "EURUSD",
        "https://www.tradingview.com/symbols/GBPUSD/?exchange=OANDA": "GBPUSD",
        "https://www.tradingview.com/symbols/AUDUSD/?exchange=FX": "AUDUSD",
        "https://www.tradingview.com/symbols/USDCAD/?exchange=OANDA": "USDCAD",
        "https://www.tradingview.com/symbols/USDJPY/?exchange=OANDA": "USDJPY",
        "https://www.tradingview.com/symbols/USDINR/?exchange=FX_IDC": "USDINR",
        "https://www.tradingview.com/symbols/USDTRY/?exchange=OANDA": "USDTRY",
        "https://www.tradingview.com/symbols/USDCNY/?exchange=FX_IDC": "USDCNY",
        "https://www.tradingview.com/symbols/USDAED/?exchange=FX_IDC": "USDAED",
        "https://www.tradingview.com/symbols/USDRUB/?exchange=FOREXCOM": "USDRUB",
    }

    API_url = {
        "https://www.tradingview.com/symbols/EURUSD/": "http://localhost/update/EURtoUSD/",
        "https://www.tradingview.com/symbols/GBPUSD/?exchange=OANDA": "http://localhost/update/GBPtoUSD/",
        "https://www.tradingview.com/symbols/AUDUSD/?exchange=FX": "http://localhost/update/AUDtoUSD/",
        "https://www.tradingview.com/symbols/USDCAD/?exchange=OANDA": "http://localhost/update/USDtoCAD/",
        "https://www.tradingview.com/symbols/USDJPY/?exchange=OANDA": "http://localhost/update/USDtoJPY/",
        "https://www.tradingview.com/symbols/USDINR/?exchange=FX_IDC": "http://localhost/update/USDtoINR/",
        "https://www.tradingview.com/symbols/USDTRY/?exchange=OANDA": "http://localhost/update/USDtoTRY/",
        "https://www.tradingview.com/symbols/USDCNY/?exchange=FX_IDC": "http://localhost/update/USDtoCNY/",
        "https://www.tradingview.com/symbols/USDRUB/?exchange=FOREXCOM": "http://localhost/update/USDtoRUB/",
        "https://www.tradingview.com/symbols/USDAED/?exchange=FX_IDC": "http://localhost/update/USDtoAED/"
    }

    # Windows dictionary contains handles and url names
    # handle : url_name
    windows = {}

    def identify(self):
        # Identify each page handle and store them
        print("Identifying pages...")
        for window in self.driver.window_handles:
            self.driver.switch_to.window(window)
            url_name = self.scrape_url[self.driver.current_url]
            self.windows[window] = url_name


    def send_data(self, payload):
        pass


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
        try:
            # After opening the driver, we don't want a dangling tab
            # So open the first url manually
            self.driver.get("https://www.tradingview.com/symbols/EURUSD/")
            print("Opening pages...")

            # We get the handle of each page opened
            # Store their handle and assign a value (short name of url)
            # Then collect data and pack it in a json according to name
            for url in list(self.scrape_url.keys())[1:]:
                self.driver.execute_script(f'''window.open("{url}","_blank");''')

            self.identify()
            print(self.windows)
            while 1:
                # clear()
                print("Visiting pages...")
                i = 1
                t = timer()
                params = {}
                for window in self.windows.keys():
                    try:
                        self.driver.switch_to.window(window)
                        price = self.driver.find_element_by_css_selector(globals.selector)
                        price_text = price.text
                        print(self.windows[window])
                        params[self.windows[window]] = price_text
                        print(f"Page {i} Visited, status -> {Fore.GREEN}{price.text}{Style.RESET_ALL}")
                    except KeyboardInterrupt:
                        raise
                    except Exception as e:
                        print(f"Page {i} Visited, status -> {Fore.RED}{e}{Style.RESET_ALL}")
                    i += 1
                print(params)
                r = requests.post(self.req_url, data=params, headers=globals.header, verify=False)
                print(r.text)
                t1 = timer()
                print(f"Batch ended after {t1-t} secs.")
                time.sleep(1)
        except KeyboardInterrupt:
            raise
        except Exception as e:
            print(e)
            self.driver.close()




crawler = Crawler()
crawler.crawl()
