"""
PriceHawk User Module
TODO: Document
"""


class User():

    def __init__(self, first_name):
        self.first_name = first_name
        self.possible_items = None
        self.items = []

    def add_item_from_possible_items_by_id(self, id):
        item = self.possible_items[id]
        self.items.append(item)

    def update_possible_items(self, possible_items):
        self.possible_items = possible_items
