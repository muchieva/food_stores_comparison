import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from models.barbora_item import BarboraItem
from scrapers.barbora_scraper import BarboraScraper
from scrapers.rimi_scraper import RimiScraper


def init_gathering():
    driver = webdriver.Chrome()
    driver.maximize_window()
    driver.implicitly_wait(5)
    wait = WebDriverWait(driver, 10)
    return driver, wait


def execute_data_gathering():
    driver,wait = init_gathering()
    barbora = BarboraScraper(driver, 'https://www.barbora.lt/darzoves-ir-vaisiai/darzoves-ir-grybai')
    # rimi = RimiScraper(driver, 'https://www.barbora.lt/bakaleja/kruopos')
    barbora.collect_data()
    # rimi.collect_data()

execute_data_gathering()

