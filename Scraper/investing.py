import os
import traceback
import time
import globals
import pickle
import requests
import json
from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from inputimeout import inputimeout, TimeoutOccurred
from timeit import default_timer as timer
from requests.packages.urllib3.exceptions import InsecureRequestWarning
requests.packages.urllib3.disable_warnings(InsecureRequestWarning)

class Crawler(object):

    driver = webdriver.Chrome("chromedriver.exe", options=globals.options)
    indexes = [20, 22, 23, 26, 30, 13, 14]
    index_to_name = {
        13: "gas_oil",
        14: "aluminum",
        20: "us_wheat",
        22: "us_corn",
        23: "us_soybeans",
        26: "us_cotton",
        30: "us_sugar",

    }

    url = "https://www.investing.com/commodities/real-time-futures"
    api_url = "https://www.markettime.ir/update/product/"
    cookie_name = "investing.pk1"
    cookie_loaded = False


    def load_cookies(self):
        try:
            cookies = pickle.load(open(self.cookie_name, 'rb'))
            for cookie in cookies:
                self.driver.add_cookie(cookie)
            self.driver.refresh()
        except Exception as e:
            traceback.print_exc()
            print("Something happened during cookie loading...")
            return False
        return True


    def manual(self):
        input("Press enter when you are done...\n")
        # Refresh to get the cookies updated
        self.driver.refresh()
        # Store cookies in file to use them later
        cookies = self.driver.get_cookies()
        pickle.dump(cookies, open(self.cookie_name, 'wb'))


    def start(self):
        # globals.clear()
        self.driver.get(self.url)
        print("opening site...")

        params = {}
        # selector_list = ["td.pid-8830-last", "td.pid-8830-high",
        #                  "td.pid-8830-low", "td.bold",
        #                  "td.bold"]
        selector_list = [4, 5, 6, 7, 8]
        selector_names = {
            4:"last",
            5:"high",
            6:"low",
            7:"change_num",
            8:"change_perc"
            }
        self.cookie_loaded = self.load_cookies()
        if not self.cookie_loaded:
            print("Cookies are not loaded...\a")
            print("Setup the site for first time use.")
            self.manual()
            self.cookie_loaded = True
        self.driver.execute_script('videos = document.querySelectorAll("video"); for(video of videos) {video.pause()}')

        # Wait for everything to load correctly
        self.driver.implicitly_wait(5)
        params = {}
        while 1:
            start = timer()
            # globals.clear()
            for index in self.indexes:
                params[self.index_to_name[index]] = {}
                for j in selector_list:
                    selector = f'//*[@id="cross_rate_1"]/tbody/tr[{index}]/td[{j}]'
                    # selector = f"#cross_rate_1 > tbody > tr:nth-child({index}) > {j}"
                    t = self.driver.find_element_by_xpath(selector)
                    t_text = t.text
                    name = selector_names[j]
                    params[self.index_to_name[index]][name] = t_text
            rates = {"products": params}
            r = requests.post(self.api_url, json=rates,
                              headers=globals.header, verify=False)
            print(r.text)
            end = timer()
            print(f"Iteration ended on {end-start}")
            time.sleep(5)


crawler = Crawler()
while True:
    try:
        crawler.start()
    except KeyboardInterrupt:
        crawler.driver.close()
        raise
    except:
        traceback.print_exc()
