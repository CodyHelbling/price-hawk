import json

from flask import Flask, abort, request


import Scraper
import User

app = Flask(__name__)


@app.route('/')
def hello_world():
    return 'Hello, World!'


@app.route('/prices', methods=['GET'])
def get_prices():
    url = request.args['url']
    print "url: ", url
    # scraper = Scraper(url)
    # user = User('Cody')
    # user.possible_items = scraper.possible_items
    # return json.dump(user.possible_items)
    return url

@app.route('/select/price', methods=['POST'])
def select_price():
    if (not request.json) or ('price' not in request.json):
        abort(400)
    item_id = request.json['item_id']
    # Add support for new uncreated user

    # Add item to users items
    user = User('Cody')
    user.add_item_from_possible_items_by_id(item_id)
