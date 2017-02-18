"""
This file contains the class for a PriceHawk item.
"""


class Item():

    def __init__(self, name, price, url, xpath):
        self.name = name
        self.original_price = price
        self.current_price = price
        self.url = url
        self.xpath = xpath

    def get_current_price(self):
        return self.current_price

    # def get_name()

    # def get_original_price()

    # def get_url()

    # def get_users()?

    # def set_current_price()

    # def set_url()

    # def set_name()
