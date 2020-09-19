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


class Crawler(object):

    driver = webdriver.Chrome("chromedriver.exe", options=globals.options)
    indexes = [3, 9, 10, 29, 30, 32]
    #cross_rates_container > table > tbody > tr:nth-child(29) > td.pid-178-last
    index_to_name = {
        3: "nasdaq",
        9: "DAX",
        10: "FTSE100",
        29: "Nikkei225",
        30: "S&P/ASX200",
        32: "Shanghai",

    }

    url = "https://www.investing.com/commodities/real-time-futures"
    api_url = ""
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
        globals.clear()
        self.driver.get(self.url)
        print("opening site...")

        params = {}
        # selector_list = ["td.pid-8830-last", "td.pid-8830-high",
        #                  "td.pid-8830-low", "td.bold",
        #                  "td.bold"]
        selector_list = [4, 5, 6, 7, 8]
        self.cookie_loaded = self.load_cookies()
        if not self.cookie_loaded:
            print("Cookies are not loaded...\a")
            print("Setup the site for first time use.")
            self.manual()
            self.cookie_loaded = True
        self.driver.execute_script('videos = document.querySelectorAll("video"); for(video of videos) {video.pause()}')

        # Wait for everything to load correctly
        self.driver.implicitly_wait(5)
        while 1:
            start = timer()
            globals.clear()
            for index in self.indexes:
                for j in selector_list:
                    selector = f'//*[@id="cross_rate_1"]/tbody/tr[{index}]/td[{j}]'
                    # selector = f"#cross_rate_1 > tbody > tr:nth-child({index}) > {j}"
                    t = self.driver.find_element_by_xpath(selector)
                    print(f'{self.index_to_name[index]}: {t.text}')
            end = timer()
            print(f"Iteration ended on {end-start}")
            time.sleep(5)


crawler = Crawler()
while True:
    try:
        crawler.start()
    except KeyboardInterrupt:
        raise
    except:
        traceback.print_exc()
        time.sleep(10)
        pass
