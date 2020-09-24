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


class Crawler:

    driver = webdriver.Chrome("chromedriver.exe", options=globals.options)
    currency_list = [
     'EUR/USD', 'GBP/USD', 'AUD/USD', 'USD/CAD', 'USD/JPY',
     'WTI/USD', 'Brent/USD', 'NatGas/USD', 'Gasoline/USD',
     'Gold/USD', 'Silver/USD', 'Copper/USD', 'Palladium/USD',
     'Platinum/USD',
    ]
    rows = 1
    cookie_name = "forexfactory.pk1"
    url = "https://www.forexfactory.com/market"
    api_url = "https://www.markettime.ir/update/ForexExchange/"


    def add_row(self):
        """ Each row containt 8 price (instrument). To have them all we
            need to add a row. Each row added increase [self.rows] by 1.
            A good choice would be to check if the row exists first.
        """
        row = f"#content > section.content.market_v3 > div.pagearrange__layout.pagearrange__layout--arrangeable.pagearrange__layout--zippable.full > div:nth-child({self.rows+1}) > div > div > div > div > div.market__scanner > div.slidetable > div > div.slidetable__overflow > table > tr > td.market__scanner-blocks.market__scanner-blocks--8 > table > tr:nth-child(2)"
        try:
            self.driver.find_element_by_css_selector(row)
        except NoSuchElementException:
            add_row = "#mds_sidebar > div > ul > li:nth-child(1) > a"
            self.driver.find_element_by_css_selector(add_row).click()
            self.rows += 1
        self.driver.implicitly_wait(2)
        return


    def live_check(self):
        """ Live check box Allows us to get live feed
            To check both checkboxes and pass the test
            We need to have row_2 added, so we check it beforehand
        """
        checkbox = "#mds-live-toggle-11"
        checkbox_element = self.driver.find_element_by_css_selector(checkbox)
        live = checkbox_element.is_selected()
        if not live:
            checkbox_element.click()
        if self.rows == 2:
            checkbox_2 = "#mds-live-toggle-29"
            checkbox2_element = self.driver.find_element_by_css_selector(checkbox_2)
            live2 = checkbox2_element.is_selected()
            if not live2:
                checkbox2_element.click()
        self.driver.implicitly_wait(1)
        return


    def load_cookies(self):
        try:
            cookies = pickle.load(open(self.cookie_name, 'rb'))
            for cookie in cookies:
                self.driver.add_cookie(cookie)
            self.driver.refresh()
        except Exception as e:
            traceback.print_exc()
            print("Something happened during cookie loading...")
        return


    def manual(self):
        """ Instruments of ForexFactory are harder to automate (TODO)
            So lets ask the admin if he wants to manually set it
            What ever he/she wants
            Once you do it manually it will be saved inside a cookie
            so you can skip manual changes next time
        """
        # Load cookies first
        self.load_cookies()
        try:
            prompt = "Do you want to manually change instruments? (Y \ N):\n"
            manual = inputimeout(prompt=prompt, timeout=5)
        except TimeoutOccurred:
            manual = "n"
            print("Timeout...\nUsing pre-existing instruments")

        if manual.lower() == "y":
            input("Press enter when you are done...\n")
            # Refresh to get the cookies updated
            self.driver.refresh()
            # Store cookies in file to use them later
            cookies = self.driver.get_cookies()
            pickle.dump(cookies, open(self.cookie_name, 'wb'))
            return
        return


    def start(self):
        globals.clear()
        self.driver.get(self.url)
        print("opening site...")

        # Check if there are 2 rows
        # self.add_row()
        # Check if live checkbox is selected
        self.live_check()
        # Prompt for manual change
        self.manual()
        params = {}
        k_list = {
            # low
            2: 'l',
            # change
            3: 'c',
            4: 'cprc',
        }
        # Wait for everything to load correctly
        self.driver.implicitly_wait(5)
        while 1:
            # Row
            start = timer()
            globals.clear()
            for i in range (1, 3):
                # Column
                for j in range(1,9):
                    # We don't want to scrape more than what is inside >
                    # > Our currency list. So we check if everytime.
                    row_neg = i - 1
                    cur_element = (row_neg*8)+j
                    if (cur_element) > len(self.currency_list):
                        break
                    name_text = self.currency_list[cur_element-1]
                    params[name_text] = {}
                    for k in k_list.keys():
                        selector =  f"#content > section.content.market_v3 > div.pagearrange__layout.pagearrange__layout--arrangeable.pagearrange__layout--zippable.full > div:nth-child({i}) > div > div > div > div > div.market__scanner > div.slidetable > div > div.slidetable__overflow > table > tr > td.market__scanner-blocks.market__scanner-blocks--8 > table > tr:nth-child({k}) > td:nth-child({j})"
                        price = self.driver.find_element_by_css_selector(selector)
                        price_text = price.text
                        # if k == 5:
                        #     low = price_text.split("|")
                        #     price_text = low[0]
                        #     low = low[1]
                        #     params[name_text]["low"] = low
                        params[name_text][k_list[k]] = price_text
            end = timer()
            rates = {'forex_rates' : params}
            r = requests.post(self.api_url, json=rates,
                              headers=globals.header, verify=False)
            print(r.text)
            print(f"Iteration ended on {end-start}")
            time.sleep(1)



crawler = Crawler()
while True:
    try:
        crawler.start()
    except KeyboardInterrupt:
        crawler.driver.close()
        crawler.driver.quit()
        raise
    except Exception as e:
        traceback.print_exc()
        print("\a\a\a\a\a\a\a")
        time.sleep(10)
        crawler.start()
