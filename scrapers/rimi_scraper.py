import time

from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from models.rimi_item import RimiItem


class RimiScraper():
    def __init__(self, driver, url):
        self.driver = driver
        self.url = url
        self.hrefs = []

    def collect_data(self):
        self.accept_cookies()
        self.additional_banner()
        self.get_urls()
        self.collect_each()

    def get_urls(self):
        for i in range(1, 10):
            self.driver.get(f"{self.url}?currentPage={i}")
            try:
                close_button = WebDriverWait(self.driver, 5).until(
                    EC.element_to_be_clickable((By.XPATH, "//button[@class='modal__close']"))
                )
                close_button.click()
            except Exception as e:
                print(f"Close button not found or not clickable on page {i}, skipping...")
            # self.driver.find_element(By.XPATH, "//button[@class='modal__close']").click()
            ul = self.driver.find_element(By.XPATH, '//*[@id="main"]/section/div[1]/div/div[2]/div[1]/div/div[2]/ul')
            lis = ul.find_elements(By.TAG_NAME, 'li')
            print(len(lis))
            if len(lis) == 0:
                break
            for a in lis:
                href = a.find_element(By.TAG_NAME, 'a').get_attribute('href')
                self.hrefs.append(href)

    def collect_each(self):
        for link in self.hrefs:
            self.driver.get(link)
            item = RimiItem(self.driver)
            item.fill()
            item.save()

    def accept_cookies(self):
        self.driver.get(self.url)
        self.driver.find_element(By.XPATH, '//*[@id="CybotCookiebotDialogBodyLevelButtonLevelOptinAllowAll"]').click()

    def additional_banner(self):
        self.driver.get(self.url)
        self.driver.find_element(By.XPATH, "//button[@class='modal__close']").click()