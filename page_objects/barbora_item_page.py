import re
from selenium.webdriver.common.by import By
from bs4 import BeautifulSoup

class BarboraItemPage():

    def __init__(self, driver):
        self.driver = driver

    def get_title(self):
        title = self.driver.find_element(By.XPATH, '/html/body/div[2]/div/div[3]/div/div[3]/div/div[2]/div[1]/div/div[2]/h1').text
        product = title.split(',')
        props = self.get_maker()
        if len(product) >= 2:
            good_title = re.sub(props , '' , product[0], flags=re.IGNORECASE)
            return good_title

    def get_maker(self):
        html_content = self.driver.find_element(By.XPATH, '/html/body/div[2]/div/div[3]/div/div[3]/div/dl[2]')
        soup = BeautifulSoup(html_content.get_attribute("outerHTML"), 'html.parser')
        target_fields = ['Prekės ženklas:']
        extracted_value = ""
        for dt in soup.find_all('dt'):
            if dt.get_text(strip=True) in target_fields:
                dd = dt.find_next('dd')
                if dd:
                    extracted_value = (dd.get_text(strip=True))
                    break
        return extracted_value

    def get_quantity(self):
        product_title  = self.driver.find_element(By.XPATH, '/html/body/div[2]/div/div[3]/div/div[3]/div/div[2]/div[1]/div/div[2]/h1').text
        number_pattern =  r',\s*(\d+)(?=\s*g(?!.*\d))'
        number_match = re.search(number_pattern, product_title)
        product_number = number_match.group(1) if number_match else None
        return product_number

    def get_price(self):
        price_element = self.driver.find_element(By.XPATH, '//*[@id="b-product-info--price-placeholder"]')
        price_html = price_element.get_attribute('outerHTML')
        soup = BeautifulSoup(price_html, 'html.parser')
        price_meta = soup.find('meta', {'itemprop': 'price'})
        price = price_meta['content'] if price_meta else None
        return price

    def get_unit(self):
        full_text =  self.driver.find_element(By.XPATH, '/html/body/div[2]/div/div[3]/div/div[3]/div/div[2]/div[1]/div/div[2]/h1').text
        unit = str(full_text)[-1]
        return unit

    def get_property(self):
        element = self.driver.find_element(By.XPATH, '/html/body/div[2]/div/div[3]/div/div[3]/div/div[2]/div[1]/div/div[2]/h1')
        product_title = element.text
        properties = r'Ekologiški|ekologiški|skrudinti|neskrudinti|skrudintos|neskrudintos|lukštenti|rudieji|rudi|plikyti|ilgagrūdžiai|basmati'
        property_match = re.findall(properties, product_title)
        if property_match:
            return ', '.join(property_match)
        else:
            return None

    def get_category(self):
        return self.driver.find_element(By.XPATH, '/html/body/div[2]/div/div[3]/div/ol/li[4]/a/span').text
