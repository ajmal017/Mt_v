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



    url = "https://www.tgju.org/"
    api_url = "https://www.markettime.ir/update/gold/"
    cookie_name = "investing.pk1"


    def tala_row_xpath(self, row, col):
        selector = f'//*[@id="main"]/div[4]/div[3]/div[2]/table/tbody/tr[{row}]/td[{col}]'
        price = self.driver.find_element_by_xpath(selector)
        text = price.text
        # col_name = tala_col_name[col]
        if col == 2:
            # Column 3 is for price change which is composed like xx (xx.xx)
            change = text.split(" ")
            text = change[1]
            change_perc = change[0].replace("(", "").replace(")", "")
            # Get sign of the change. High class is for + low is for -
            if price.get_attribute('class') == 'high':
                change_perc = f'+{change_perc}'
            else :
                change_perc = f'-{change_perc}'
            # data[tala_names[row]][tala_col_name[4]] = change_perc
            print(change_perc)
        print(text)
        return text


    def tala_row_old_css(self, row, col):
        selector = f'#main > div:nth-child(5) > div:nth-child(3) > div:nth-child(2) > table > tbody > tr:nth-child({row}) > td:nth-child({col})'
        price = self.driver.find_element_by_xpath(selector)
        text = price.text
        # col_name = tala_col_name[col]
        if col == 3:
            # Column 3 is for price change which is composed like xx (xx.xx)
            change = text.split(" ")
            text = change[1]
            change_perc = change[0].replace("(", "").replace(")", "")
            sign = selector + " > span"
            sign = self.driver.find_element_by_css_selector(sign)
            # Get sign of the change. High class is for + low is for -
            if price.get_attribute('class') == 'high':
                change_perc = f'+{change_perc}'
            else :
                change_perc = f'-{change_perc}'
            # data[tala_names[row]][tala_col_name[4]] = change_perc
            print(change_perc)
        print(text)
        return text


    def tala(self):
        tala_row = [1, 2]
        tala_col = [1, 2]
        tala_names = {
            1: 'gold-18',
            2: 'gold-24',
        }
        tala_col_name = {
            # last
            2: 'l',
            # change
            3: 'c',
            # change percent
            4: 'cprc'
        }
        col_class = {
            "high": "+",
            "low": "-",
            "nf": ""
        }
        data = {}
        for row in tala_row:
            data[tala_names[row]] = {}
            price_selector = f'#main > div:nth-child(5) > div:nth-child(3) > div:nth-child(2) > table > tbody > tr:nth-child({row}) > td.nf'
            price = self.driver.find_element_by_css_selector(price_selector)
            sign = ""
            for cls in ['high', 'low', 'nf']:
                try:
                    change_selector = f'#main > div:nth-child(5) > div:nth-child(3) > div:nth-child(2) > table > tbody > tr:nth-child({row}) > td.{cls}'
                    change = self.driver.find_element_by_css_selector(change_selector)
                    sign = col_class[cls]
                    break
                except NoSuchElementException:
                    pass
            change = self.driver.find_element_by_css_selector(change_selector)
            change_text = change.text.split(" ")
            c = change_text[1]
            change_perc = change_text[0].replace("(", "").replace(")", "")
            cprc = f"{sign}{change_perc}"
            data[tala_names[row]]['l'] = price.text
            data[tala_names[row]]['c'] = c
            data[tala_names[row]]['cprc'] = cprc
        return data


    def seke_row_old(self, row, col):
        selector = f'#coin-table > tbody > tr:nth-child({row}) > td:nth-child({col})'
        #main > div:nth-child(5) > div:nth-child(7) > div:nth-child(18) > table > tbody > tr:nth-child(2) > td.nf
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
                #main > div:nth-child(5) > div:nth-child(7) > div:nth-child(18) > table > tbody > tr:nth-child(2) > td.nf
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
            r = requests.post(self.api_url, json=rates,
                              headers=globals.header, verify=False)
            print(r.text)
            end = timer()
            print(f"Iteration ended on {end-start}")
            time.sleep(2)


crawler = Crawler()
while True:
    try:
        crawler.start()
    except KeyboardInterrupt:
        crawler.driver.close()
        crawler.driver.quit()
        raise
    except:
        traceback.print_exc()
        time.sleep(10)
        pass
