# External Imports
from termcolor import cprint
import urllib2

from Scraper import Scraper


# TODO: Start development server hosting html with known prices.

url = "https://www.walmart.com/"


def scraper_test_1():
    """
    [Y] Will a scraper object populate its possible_items attribute?
    """
    scraper = Scraper(url)
    possible_items = scraper.possible_items
    print "Items:"
    for item in possible_items:
        print "   url          : ", item.url
        print "   current_price: ", item.current_price
        print ""

    if possible_items:
        cprint("Success: Scraper Test 1", 'green')

if __name__ == "__main__":
    scraper_test_1()
