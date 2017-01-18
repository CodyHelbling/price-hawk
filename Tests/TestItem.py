""""
This file contains tests for the PriceHawk Item class.
"""

# External Library Imports
from termcolor import cprint

# Internal Imports
from Items.Item import Item

successful_test = True

# Test Item __init__()
test_item = Item('Test_Name', 123)

if test_item.name != 'Test_Name':
    cprint("Failed User __init__() unit test.", 'red')
    successful_test = False

if test_item.price != 123:
    cprint("Failed User __init__() unit test.", 'red')
    successful_test = False

    
if successful_test:
    cprint("Passed all tests!", 'green')
