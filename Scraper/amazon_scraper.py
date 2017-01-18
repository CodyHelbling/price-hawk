from lxml import html
import requests


def test_scraper():
    page = requests.get("https://www.amazon.com/Dell-210-ADRZ-DELL-UltraSharp-UP2715K/dp/B00R420SU4/ref=sr_1_9?s=pc&ie=UTF8&qid=1484685159&sr=1-9&keywords=monitor&refinements=p_n_feature_three_browse-bin%3A12659079011")
    tree = html.fromstring(page.content)
    print tree.xpath('//span[@id="priceblock_ourprice"]/text()')


def scraper(url):
    print "Scraper URL: ", url
    page = requests.get(url)
    tree = html.fromstring(page.content)
    price = tree.xpath('//span[@id="priceblock_ourprice"]/text()')
    print "Scraper Price: ", price
    
    return price


if __name__ == "__main__":
    test_scraper()
