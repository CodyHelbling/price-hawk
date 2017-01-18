"""
This file contains the class for a PriceHawk item.
"""


class Item():

    name = 'Uninitialized'
    price = 'Uninitialized'
    
    def __init__(self, name, price):
        self.name = name
        self.price = price
