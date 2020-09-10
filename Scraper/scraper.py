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
    globals.clear()
    driver.get(url)
    print("Opening page")
    last_price = None
    err_count = 0
    while 1:
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
