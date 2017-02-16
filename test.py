import re

import gumbo
import requests
from gumbo import soup_adapter

from bs4 import BeautifulSoup

#url = ('https://www.amazon.com/s/ref=lp_679307011_ex_n_3?rh=n%3A7141123011%2Cn%3A7147441011%2Cn%3A679255011&bbn=7147441011&sort=date-desc-rank&ie=UTF8&qid=1487221728&lo=fashion')
url = ('https://www.amazon.com/Supra-Henry-stealth-brilliant-fullgrain/dp/B0050NGEAW/ref=sr_1_7?s=apparel&ie=UTF8&qid=1487221744&sr=1-7&nodeID=679255011')
response = requests.get(url)
print response.status_code
# print response.headers['content-type']
# print response.content
s = (response.content).decode("utf8")
# print "res: ", response
soup = gumbo.soup_parse(s)

prices = []
for node in soup.findAll(text=True):
    m = re.search('\$?[0-9]+\.[0-9][0-9]|\$[0-9]+', node)
    if m:
        print "Regex match: ", m.group(0)
        # print node, "\n"
