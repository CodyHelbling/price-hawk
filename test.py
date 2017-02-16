import BeautifulSoup
import gumbo
import requests
from gumbo import soup_adapter

url = ('https://docs.python.org/2/tutorial/errors.html')
response = requests.get(url)
print response.status_code
# print response.headers['content-type']
# print response.content
s = (response.content).decode("utf8")
# print "res: ", response
soup = gumbo.soup_parse(s)

for node in soup.findAll(text=True):
    """
    \$?[0-9]+\.[0-9]+|\$?[0-9]+
    """
    print node, "\n\n"
