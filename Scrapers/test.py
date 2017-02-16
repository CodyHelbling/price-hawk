from lxml import html
from lxml import etree
import requests

url = "http://lxml.de/xpathxslt.html#xpath"

doc1 = requests.get(url)
print doc1
doc = html.parse(url)

regexpNs = 'http://exslt.org/regular-expressions'
find = etree.XPath("//*[re:test(., '^abc$', 'i')]",
                   namespaces={'re': regexpNs})
#  root = etree.XML("<root><a>aB</a><b>aBc</b></root>")
root = etree.HTML(doc)
print (find(root)[0].text)
