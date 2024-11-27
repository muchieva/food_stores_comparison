import re

from bs4 import BeautifulSoup
from selenium.webdriver.common.by import By


class RimiItemPage():
    def __init__(self, driver):
        self.driver = driver

    def get_title(self):
        return self.driver.find_element(By.XPATH, '//*[@id="details"]/div/div/div[1]/div[1]/ul/li[2]/div/p').text

    def get_quantity(self):
        # html_content = self.driver.find_element(By.XPATH, '/html/body/div[2]/div/div[3]/div/div[3]/div/dl[2]')
        # soup = BeautifulSoup(html_content.get_attribute("outerHTML"), 'html.parser')
        # target_fields = ['Prekės ženklas:']
        # extracted_value = ""
        # for dt in soup.find_all('dt'):
        #     if dt.get_text(strip=True) in target_fields:
        #         dd = dt.find_next('dd')
        #         if dd:
        #             extracted_value = (dd.get_text(strip=True))
        #             break
        # return extracted_value
        # element = self.driver.find_element(By.XPATH, '//*[@id="details"]/div/div/div[1]/div[1]/ul/li[3]/div/p').text
        # print(element)
        # if element == :
        #     return self.driver.find_element(By.XPATH, '//*[@id="details"]/div/div/div[1]/div[1]/ul/li[4]/div/p').text
        # number_match = re.sub("kg", "", element)
        li_element = self.driver.find_element(By.XPATH,'//*[@id="details"]/div/div/div[1]/div[1]/ul/li[3]/span')
        print(li_element)
        if li_element == None:
            return self.driver.find_element(By.XPATH, '//*[@id="details"]/div/div/div[1]/div[1]/ul/li[4]/span')
        p_tag = li_element.find_element(By.TAG_NAME, 'p').text
        weight = float(re.sub(' kg', '', p_tag))
        return weight

    def get_price(self):
        eur = self.driver.find_element(By.XPATH, '//*[@id="main"]/section/div[1]/div/div[2]/section/div/div/div[2]/div[1]/div[1]/span').text
        cents = self.driver.find_element(By.XPATH, '//*[@id="main"]/section/div[1]/div/div[2]/section/div/div/div[2]/div[1]/div[1]/div/sup').text
        price = int(eur) + (int(cents) / 100)
        return round(price, 2)

    def get_unit(self):
        full_text = self.driver.find_element(By.XPATH,'//*[@id="main"]/section/div[1]/div/div[2]/section/div/div/div[2]/h1' ).text
        unit = str(full_text)[-1]
        return unit

    def get_property(self):
        pass
        # element = self.driver.find_element(By.XPATH,
        #                                    '/html/body/div[2]/div/div[3]/div/div[3]/div/div[2]/div[1]/div/div[2]/h1')
        # product_title = element.text
        # properties = r'Ekologiški|ekologiški|skrudinti|neskrudinti|skrudintos|neskrudintos|lukštenti'
        # property_match = re.search(properties, product_title)
        # if property_match:
        #     return property_match.group()
        # else:
        #     return None

    def get_category(self):
        return self.driver.find_element(By.XPATH, '//*[@id="main"]/section/div[1]/div/div[2]/div[1]/div/p/a[3]').text
