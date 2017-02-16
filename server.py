from bottle import route, run, request, response
from bottle import static_file
from Scraper.amazon_scraper import scraper


@route('/add_url')
def add_url():
    url = request.query.url
    name = request.query.name
    price = scraper(url)
    return ("Hello " + name +
            ", is your url: " + str(url) +
            " and price: " + str(price) + "?")


@route('/price')
def get_price():
    url = request.query.url
    price = scraper(url)
    return price
           
           
# Serve Static Files
@route('/static/<filename>')
def server_static(filename):
    print "   Filename: ", filename
    return static_file(filename, root='./Static/JavaScript')


@route('/')
def home():
    response.content_type = 'text/html'
    return static_file('home.html', root='./Static/HTML')


run(host='localhost', port=8080, debug=True)
