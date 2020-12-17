import time
from selenium import webdriver
import scrapy

# =============================================================================
# ENVIRONMENTAL SETTINGS
# Chrome Driver used here. Please change the driver path with yours.
# =============================================================================
chrome_options = webdriver.ChromeOptions()
chrome_options.add_argument('--no-sandbox')
chrome_options.add_argument('--disable-dev-shm-usage')
chrome_options.add_argument("--window-size=1920,1080")
driver = webdriver.Chrome('C:\\Users\\Bugra\\Documents\\GitHub\\Web-Scraper-For-Sciencedirect-With-Selenium-Scrapy\\chromedriver.exe',options = chrome_options)


