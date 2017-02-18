import re
import requests
from lxml import etree, html

from Item import Item


class Scraper():

    def __init__(self, url):
        self.url = url
        self.html_str = self.get_html_str_from_url()
        self.html_root = None
        self.html_tree = None
        self.build_html_tree()
        self.possible_items = self.find_items()

    def build_html_tree(self):
        self.html_root = html.fromstring(self.html_str)
        self.html_tree = etree.ElementTree(self.html_root)

    def find_items(self):
        items = {}
        id = 0
        for node in self.html_root.iter():
            if node.text:
                m = re.search('\$?[0-9]+\.[0-9][0-9]|\$[0-9]+', node.text)
                if m:
                    print "m:    ", m.group(0)
                    # print dir(i)
                    print self.html_tree.getpath(node)
                    # print e.text
                    item = Item(name="todo_name",
                                price=m.group(0),
                                url=self.url,
                                xpath=self.html_tree.getpath(node),
                                )
                    items[id] = item
        return items

    def get_html_str_from_url(self):
        response = requests.get(self.url)
        print response.status_code
        # print response.headers['content-type']
        # print response.content
        return (response.content).decode("utf8")

    def get_price_at_xpath(self, item_xpath):
        # TODO: This isn't completed
        print "possible_prices[0]: ", self.possible_prices[0]
        xp = self.tree.xpath(self.possible_prices[0][1] + '/text()')
        m = re.search('\$?[0-9]+\.[0-9][0-9]|\$[0-9]+', xp[0])
        print "tree.xpath(possible_prices[0]): ", m.group(0)
