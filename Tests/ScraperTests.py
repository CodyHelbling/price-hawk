# External Imports
from termcolor import cprint
import urllib2


urls = [
    (
        '$1,861.38',
        'https://www.amazon.com/Dell-210-ADRZ-DELL-UltraSharp-UP2715K/dp/B00R420SU4/ref=sr_1_9?s=pc&ie=UTF8&qid=1484685159&sr=1-9&keywords=monitor&refinements=p_n_feature_three_browse-bin%3A12659079011'
    ),
    (
        '$219.99',
        'https://www.amazon.com/Garmin-v%C3%ADvoactive-Smart-Watch-Regular/dp/B01BKUB6BA/ref=sr_1_2?ie=UTF8&qid=1484770697&sr=8-2&keywords=garmin'
    ),

]


def test_urls():
    for url in urls:
        test_price(url[0], url[1])

        
def test_price(expected_price, url):
    response = urllib2.urlopen('http://localhost:8080/price' + "?url=" + url)
    response_str = response.read()
    # print response_str
    if expected_price != response_str:
        print "\n\n----------------------------------------------------------"
        cprint("Url price test failure.\n    Expected " +
               response_str + ".\n", 'red')
        print url
        print "----------------------------------------------------------\n\n"
    else:
        cprint("\nUrl price test success.\n", 'green')


if __name__ == "__main__":
    test_urls()
