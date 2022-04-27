
# Import are classes from the /classes sub-directory
from classes.cart import Cart
from classes.item import Item
from classes.order import Order
from classes.user import User

class Shop:
    def __init__(self):
        self.user = User() # Instantiate a user for the Shop instance
        self.item = Item()

shop = Shop()

# Demo of User methods
shop.user.create('username','password')
print(shop.user.login('username','password'))

# Each user method returns a tuple of the following format:
#   (Boolean True/False, Message)
# The first element will be true if the action was successful and false otherwise.
# Try running this script to see the output from the login example above.

# Demo of Item methods
shop.item.create('A1','Fahrenheit 451','12','5')
print("$" + str(shop.item.getPrice('A1')[0]))

# This shows fetching the price of an item after creating it