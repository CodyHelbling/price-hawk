""""
This file contains tests for the PriceHawk User class.
"""

# External Library Imports
from termcolor import cprint

# Internal Imports
from Users.User import User

successful_test = True

# Test User __init__()
test_user = User('Test_Name')
if test_user.first_name != 'Test_Name':
    cprint("Failed User __init__() unit test.", 'red')
    successful_test = False

if successful_test:
    cprint("Passed all tests!", 'green')
