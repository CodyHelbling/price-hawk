""""
This file contains tests for the PriceHawk Item class.
"""

# External Library Imports
from termcolor import cprint

# Internal Imports
from Items.Item import Item

successful_test = True

# Test Item __init__()
test_item = Item('Test_Name', 123, 'http://test/url.html')

if test_item.name != 'Test_Name':
    cprint("Failed Item __init__() unit test.", 'red')
    successful_test = False

if test_item.original_price != 123:
    cprint("Failed Item __init__() unit test.", 'red')
    successful_test = False

if test_item.current_price != 123:
    cprint("Failed Item __init__() unit test.", 'red')
    successful_test = False

if test_item.url != 'http://test/url.html':
    cprint("Failed Item __init__() unit test.", 'red')
    successful_test = False


# Test Item.get_current_price()
if test_item.get_current_price() != 123:
    cprint("Failed Item.get_current_price unit test.", 'red')
    successful_test = False

    
# If all tests passed, communicate success via std. out.
if successful_test:
    cprint("Passed all tests!", 'green')
