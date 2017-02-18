import re

import requests

from lxml import etree, html

url = "https://www.walmart.com/"

response = requests.get(url)
print response.status_code
# print response.headers['content-type']
# print response.content
s = (response.content).decode("utf8")
# print "res: ", response

root = html.fromstring(response.content)
tree = etree.ElementTree(root)

# Find all possible prices in an html file.
# Append all possible prices and their xpath
# to list called possible_prices
possible_prices = []
for e in root.iter():
    if e.text:
        m = re.search('\$?[0-9]+\.[0-9][0-9]|\$[0-9]+', e.text)
        if m:
            print "m:    ", m.group(0)
            # print dir(i)
            print tree.getpath(e)
            # print e.text
            possible_prices.append([m.group(0), tree.getpath(e)])


# This is the basics of checking if a price has changed.
print "possible_prices[0]: ", possible_prices[0]
xp = tree.xpath(possible_prices[0][1] + '/text()')
# print "test! ", xp[0], "END:"
m = re.search('\$?[0-9]+\.[0-9][0-9]|\$[0-9]+',
              xp[0])
print "tree.xpath(possible_prices[0]): ", m.group(0)
