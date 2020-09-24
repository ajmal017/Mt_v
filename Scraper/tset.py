import os
import requests
import globals
import time
from selenium import webdriver
from bs4 import BeautifulSoup
from selenium.common.exceptions import NoSuchElementException, StaleElementReferenceException
from timeit import default_timer as timer
from requests.packages.urllib3.exceptions import InsecureRequestWarning
requests.packages.urllib3.disable_warnings(InsecureRequestWarning)



class Crawler():
    driver = webdriver.Chrome("chromedriver.exe", options=globals.options)

    url = 'http://www.tsetmc.com/'
    api_url = 'https://www.markettime.ir/update/saham/'

    def real_time(self):
        self.driver.get(self.url)
        params = {}
        rows = [1, 3]
        columns = [3, 4, 5]
        while 1:
            for row in rows:
                for col in columns:
                    selector_list = [f"div > div.box1.silver.tbl.z3_4.h210 > div.content > table > tbody > tr:nth-child({row}) > td:nth-child({col})",
                                     f"#GlobalTab0Elm > div:nth-child(2) > div.box1.silver.tbl.z3_4.h210 > div.content > table > tbody > tr:nth-child({row}) > td:nth-child({col})"]
                    for selector in selector_list:
                        print(selector)
                        try:
                            price = self.driver.find_element_by_css_selector(selector)
                            print(price.text)
                            break
                        except (NoSuchElementException, StaleElementReferenceException):
                            print("Selector failed...")
            time.sleep(1)


    def scrape(self):
        headers = {
            'Access-Control-Allow-Origin': '*',
            'Access-Control-Allow-Methods': 'GET',
            'Access-Control-Allow-Headers': 'Content-Type',
            'Access-Control-Max-Age': '3600',
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.102 Safari/537.36 Edge/18.19582'
        }
        while 1:
            page = requests.get(self.url, headers)
            soup = BeautifulSoup(page.content, 'html.parser')
            try:
                t = soup.select('div.pn')[15]
                print(t.text)
            except KeyboardInterrupt:
                raise
            except:
                pass
            time.sleep(1)





crawler = Crawler()
crawler.scrape()
