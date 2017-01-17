"""
This file contains a class for a PriceHawk user.
"""


class User():
    
    first_name = 'Uninitialized'
    urls = []

    def __init__(self, first_name):
        self.first_name = first_name

    def add_url(self, url):
        self.urls.append(url)
        
