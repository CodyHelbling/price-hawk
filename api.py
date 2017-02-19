import json

from flask import Flask, abort, request

from Scraper import Scraper
from User import User

app = Flask(__name__)
user = User('Cody')


@app.route('/')
def hello_world():
    return 'Hello, World!'


@app.route('/prices', methods=['GET'])
def get_prices():
    url = request.args['url']
    print "url: ", url
    scraper = Scraper(url)

    user.update_possible_items(scraper.possible_items)
    items_with_index = {}

    for index in user.possible_items.keys():
        items_with_index[index] = user.possible_items[index].current_price

    return json.dumps(items_with_index)


@app.route('/select', methods=['POST', 'GET'])
def select_price():
    if (not request.json):
        print "ADFADFSFASDFASFASD"
        abort(400)
    item_id = request.json['item_id']
    # Add support for new uncreated user

    # Add item to users items
    user.add_item_from_possible_items_by_id(item_id)
    print user.items[0].current_price
    return "Success"
