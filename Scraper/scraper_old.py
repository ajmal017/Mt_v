import os
import time
import requests
from timeit import default_timer as timer
import globals
from datetime import datetime
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
from colorama import Fore, Style, init
init()

clear = lambda: os.system('cls' if os.name == 'nt' else 'clear')


class Crawler():

    driver = webdriver.Chrome("chromedriver.exe", options=globals.options)
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

    windows = {}

    def identify(self):
        for window in self.driver.window_handles:
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
            self.driver.get("https://www.tradingview.com/symbols/EURUSD/")
            print("Opening pages...")
            # Maybe I can get handles while opening pages
            # and identify them on the go
            # If not possible, We use identify() to give name to each handle
            for url in self.scrape_url[1:]:
                self.driver.execute_script(f'''window.open("{url}","_blank");''')
            while 1:
                clear()
                print("Visiting pages...")
                i = 1
                for window in self.driver.window_handles:
                    try:
                        self.driver.switch_to.window(window)
                        price = self.driver.find_element_by_css_selector(globals.selector)
                        params = {}
                        params['rate'] = price.text
                        current_url = self.driver.current_url
                        req_url = self.API_url[current_url]
                        if current_url in last_prices:
                            if price.text != last_prices[current_url]:
                                r = requests.post(req_url, data=params, headers=globals.header)
                                print(f"Page {i} Visited, status -> {Fore.GREEN}{price.text}{Style.RESET_ALL}")
                                print(r.text)
                            else:
                                print(f"Page {i} --Unchanged--")
                        last_prices[current_url] = price.text

                    except KeyboardInterrupt:
                        raise
                    except Exception as e:
                        print(f"Page {i} Visited, status -> {Fore.RED}{e}{Style.RESET_ALL}")
                    i += 1

                # time.sleep(3)
        except KeyboardInterrupt:
            raise
        except Exception as e:
            print(e)
            self.driver.close()




crawler = Crawler()
crawler.crawl()
