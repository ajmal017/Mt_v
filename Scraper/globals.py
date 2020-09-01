from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains

# Webdriver options
options = webdriver.ChromeOptions()
prefs = {"profile.managed_default_content_settings.images": 2}
options.add_argument("--log-level=3")
options.add_argument("--headless")
options.add_experimental_option("prefs", prefs)

# Exchange rate price selector
selector = "#anchor-page-1 > div > div.tv-category-header__price-line.tv-category-header__price-line--allow-wrap-on-tablet.js-header-symbol-quotes.quote-ticker-inited > div.tv-category-header__main-price.js-scroll-container > div > div > div > div.tv-symbol-price-quote__row.js-last-price-block-value-row > div.tv-symbol-price-quote__value.js-symbol-last"

# Header for Token authorization
header = {
    'authorization': 'Token f09d8beedcee6d0ca21e9a4ec52ffa79d61f8b53',
}

# API endpoint URLs

