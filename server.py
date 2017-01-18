from bottle import route, run, request, response
from lxml_scraper.amazon_scraper import scraper


@route('/add_url')
def add_url():
    url = request.query.url
    name = request.query.name
    price = scraper(url)
    return "Hello " + name + ", is your url: " + str(url) + " and price: " + str(price) + "?"


run(host='localhost', port=8080, debug=True)
