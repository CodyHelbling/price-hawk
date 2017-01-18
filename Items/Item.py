"""
This file contains the class for a PriceHawk item.
"""


class Item():

    name = 'Uninitialized'
    original_price = 'Uninitialized'
    current_price = 'Uninitialized'
    url = 'Uninitialized'
    
    def __init__(self, name, price, url):
        self.name = name
        self.original_price = price
        self.url = url

    # def get_current_price()
        
    # def get_name()

    # def get_original_price()

    # def get_url()

    # def get_users()?

    # def set_current_price()

    # def set_url()
    
    # def set_name()
