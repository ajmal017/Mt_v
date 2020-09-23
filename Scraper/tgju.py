import os
import traceback
import time
import globals
import pickle
import requests
from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.support.ui import WebDriverWait
from inputimeout import inputimeout, TimeoutOccurred
from timeit import default_timer as timer
from requests.packages.urllib3.exceptions import InsecureRequestWarning
requests.packages.urllib3.disable_warnings(InsecureRequestWarning)


class Crawler(object):

    driver = webdriver.Chrome("chromedriver.exe", options=globals.options)
    #main > div:nth-child(5) > div:nth-child(3) > div:nth-child(2) > table > tbody > tr:nth-child(1) > td:nth-child(2)
    #main > div:nth-child(5) > div:nth-child(3) > div:nth-child(2) > table > tbody > tr:nth-child(1) > td:nth-child(3)

    #coin-table > tbody > tr:nth-child(2) > td:nth-child(2)
    #coin-table > tbody > tr:nth-child(3) > td:nth-child(2)


    url = "https://www.tgju.org/"
    api_url = "https://www.markettime.ir/update/stock/latest/"
    cookie_name = "investing.pk1"


    def tala(self):
        tala_row = [1, 2]
        tala_col = [2, 3]
        tala_names = {
            1: 'gold_18',
            2: 'gold_24',
        }
        tala_col_name = {
            # last
            2: 'l',
            # change
            3: 'c',
            # change percent
            4: 'cprc'
        }
        data = {}
        for row in tala_row:
            data[tala_names[row]] = {}
            for col in tala_col:
                selector = f'#main > div:nth-child(5) > div:nth-child(3) > div:nth-child(2) > table > tbody > tr:nth-child({row}) > td:nth-child({col})'
                price = self.driver.find_element_by_css_selector(selector)
                text = price.text
                col_name = tala_col_name[col]
                if col == 3:
                    # Column 3 is for price change which is composed like >
                    # xxxx (xx.xx) so we split it into two
                    change = text.split(" ")
                    text = change[1]
                    change_perc = change[0].replace("(", "").replace(")", "")
                    sign = selector + " > span"
                    sign = self.driver.find_element_by_css_selector(sign)
                    # Get sign of the change
                    # High is +
                    # low is -
                    if sign.get_attribute('class') == 'high':
                        change_perc = f'+{change_perc}'
                    else :
                        change_perc = f'-{change_perc}'
                    data[tala_names[row]][tala_col_name[4]] = change_perc
                # We want our json to be like this:
                # product : {'l': xx, 'c': xx, 'cprc': xx}
                data[tala_names[row]][col_name] = text
        return data


    def seke(self):
        #coin-table > tbody > tr:nth-child(2) > td:nth-child(2)
        tala_row = [2, 3, 4]
        tala_col = [2, 3]
        tala_names = {
            2: 'tamam',
            3: 'nim',
            4: 'rob',
        }
        tala_col_name = {
            2: 'l',
            3: 'c',
            4: 'cprc'
        }
        data = {}
        for row in tala_row:
            data[tala_names[row]] = {}
            for col in tala_col:
                selector = f'#coin-table > tbody > tr:nth-child({row}) > td:nth-child({col})'
                price = self.driver.find_element_by_css_selector(selector)
                text = price.text
                col_name = tala_col_name[col]
                if col == 3:
                    change = text.split(" ")
                    text = change[1]
                    change_perc = change[0].replace("(", "").replace(")", "")
                    sign = selector + " > span"
                    sign = self.driver.find_element_by_css_selector(sign)
                    # Get sign of the change
                    # High is +
                    # low is -
                    if sign.get_attribute('class') == 'high':
                        change_perc = f'+{change_perc}'
                    else :
                        change_perc = f'-{change_perc}'
                    data[tala_names[row]][tala_col_name[4]] = change_perc
                data[tala_names[row]][col_name] = text
        return data


    def start(self):
        globals.clear()
        self.driver.get(self.url)
        print("opening site...")


        params = {}
        while 1:
            start = timer()
            globals.clear()
            tala = self.tala()
            seke = self.seke()

            rates = {"gold": {**tala, **seke}}
            print(rates)
            # r = requests.post(self.api_url, json=rates,
            #                   headers=globals.header, verify=False)
            # print(r.text)
            end = timer()
            print(f"Iteration ended on {end-start}")
            time.sleep(2)


crawler = Crawler()
while True:
    try:
        crawler.start()
    except KeyboardInterrupt:
        crawler.driver.close()
        raise
    except:
        traceback.print_exc()
        time.sleep(10)
        pass
