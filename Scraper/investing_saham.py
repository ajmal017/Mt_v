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
    indexes = [3, 9, 10, 29, 30, 32]
    index_to_name = {
        3: "nasdaq",
        9: "DAX",
        10: "FTSE100",
        29: "Nikkei225",
        30: "S&P/ASX200",
        32: "Shanghai",

    }

    url = "https://www.investing.com/indices/major-indices"
    api_url = "https://www.markettime.ir/update/stock/"
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
        selector_list = [3, 6, 7]
        selector_names = {
            3:"last",
            # change
            6:"c",
            # change percent
            7:"cprc"
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
            globals.clear()
            for index in self.indexes:
                params[self.index_to_name[index]] = {}
                for j in selector_list:
                    selector = f'//*[@id="cross_rates_container"]/table/tbody/tr[{index}]/td[{j}]'
                    # selector = f"#cross_rate_1 > tbody > tr:nth-child({index}) > {j}"
                    t = self.driver.find_element_by_xpath(selector)
                    t_text = t.text
                    name = selector_names[j]
                    params[self.index_to_name[index]][name] = t_text
            rates = {"stock": params}
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
        time.sleep(10)
        pass
