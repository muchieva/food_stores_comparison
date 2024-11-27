from models.db import DB
from page_objects.rimi_item_page import RimiItemPage


class RimiItem():

    def __init__(self, driver):
        self.driver = driver

    def save(self):
        self.db = DB()
        query = "INSERT INTO `items`(`title`, `price`, `unit`, `quantity`, `property`, `category`, `shop`) VALUES (%s, %s, %s, %s, %s, %s,%s)"
        self.db.conn.cursor().execute(query, (self.title, self.price, self.unit, self.quantity, "" , self.category, "Rimi",))
        self.db.conn.commit()
        self.db.close()

    def fill(self):
        rip = RimiItemPage(self.driver)
        self.title = rip.get_title()
        self.quantity = rip.get_quantity()
        # self.property = rip.get_property()
        self.price = rip.get_price()
        self.unit = rip.get_unit()
        self.category = rip.get_category()
