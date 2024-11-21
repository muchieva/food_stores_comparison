import unittest
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium import webdriver

from models.barbora_item import BarboraItem


class BarboraSelenium(unittest.TestCase):

    def acceptCookies(self):
        self.driver.get("https://elenta.lt")
        self.driver.find_element(By.CLASS_NAME, 'fc-cta-consent').click()

    def test_first(self):
        item = BarboraItem("" , "")

    def setUp(self):
        self.driver = webdriver.Chrome()
        self.driver.maximize_window()
        self.driver.implicitly_wait(5)
        self.wait = WebDriverWait(self.driver, 10)
        self.acceptCookies()

