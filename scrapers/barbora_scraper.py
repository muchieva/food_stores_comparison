import time

from selenium.webdriver.common.by import By

from models.barbora_item import BarboraItem


class BarboraScraper():
    def __init__(self, driver, url):
        self.driver = driver
        self.url = url
        self.hrefs = []

    def collect_data(self):
        self.accept_cookies()
        self.age_consent()
        self.get_urls()
        self.collect_each()

    def get_urls(self):
        for i in range(1, 10):
            self.driver.get(f"{self.url}?page={i}")
            ul = self.driver.find_element(By.XPATH, '//*[@id="category-page-results-placeholder"]/div/ul')
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
            item = BarboraItem(self.driver)
            item.fill()
            item.save()

    def accept_cookies(self):
        self.driver.get("https://barbora.lt")
        self.driver.find_element(By.XPATH, '//*[@id="CybotCookiebotDialogBodyLevelButtonLevelOptinDeclineAll"]').click()

    def age_consent(self):
        self.driver.get(self.url)
        is_20 = len(self.driver.find_elements(By.ID, 'fti-modal-option-1')) != 0
        if is_20:
            self.driver.find_element(By.ID, 'fti-modal-option-1').click()
