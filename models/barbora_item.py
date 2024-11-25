from models.db import DB
from page_objects.barbora_item_page import BarboraItemPage


class BarboraItem():

    def __init__(self, driver):
        self.driver = driver

    def save(self):
        self.db = DB()
        query = "INSERT INTO `items`(`title`, `price`, `unit`, `quantity`, `property`, `category`, `shop`) VALUES (%s, %s, %s, %s, %s, %s,%s)"
        self.db.conn.cursor().execute(query, (self.title, self.price, self.unit, self.quantity, self.property, self.category, "Barbora",))
        self.db.conn.commit()
        self.db.close()

    def fill(self):
        bpo = BarboraItemPage(self.driver)
        self.title = bpo.get_title()
        self.quantity = bpo.get_quantity()
        self.property = bpo.get_property()
        self.price = bpo.get_price()
        self.unit = bpo.get_unit()
        self.category = bpo.get_category()
