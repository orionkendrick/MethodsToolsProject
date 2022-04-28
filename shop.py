import os
from enum import IntEnum

# Get colorama for pretty console output
try:
    import colorama
except ImportError:
    print("Trying to Install required module: colorama\n")
    os.system('python3 -m pip install requests')
from colorama import Fore, Back, Style

# Import are classes from the /classes sub-directory
from classes.cart import Cart
from classes.item import Item
from classes.order import Order
from classes.user import User

class Choice(IntEnum):
    
    EXIT = 3

    # Logged out actions
    LOOP = 0
    LOGIN = 1
    CREATE_ACCOUNT = 2

    # Logged in actions
    VIEW_BY_CATEGORY = 4
    ADD_TO_CART = 5
    VIEW_CART = 6
    REMOVE_FROM_CART = 7
    CHECK_OUT = 8
    EDIT_SHIPPING_ADDRESS = 9
    EDIT_PAYMENT_INFORMATION = 10
    VIEW_ORDERS = 11
    DELETE_ACCOUNT = 12
    LOG_OUT = 13


class Shop:
    def __init__(self):
        self.user = User() # Instantiate a user for the Shop instance
        self.item = Item()

        password = input("Password: ")
        success, message = self.user.delete(password)

        if success:
            print(Fore.GREEN, message, Fore.RESET)
        else:
            print(Fore.RED, message, Fore.RESET)

    def editShippingAddressAction(self):
        print(Back.WHITE,Fore.BLACK,"Edit your shipping address.", Style.RESET_ALL)
        success, userAddress = self.user.getAddress()
        if success:
            print(Back.WHITE,Fore.BLACK,f'Your current address: {userAddress}', Style.RESET_ALL)

        newAddress = input("Enter a new address: ")

        success, message = self.user.setAddress(newAddress)
        if success:
            print(Fore.GREEN, message, Fore.RESET)
        else:
            print(Fore.RED, message, Fore.RESET)

    def editPaymentInformationAction(self):
        print(Back.WHITE,Fore.BLACK,"Edit your payment info.", Style.RESET_ALL)

        newCardNum = input("Enter your Card Number: ")

        success, message = self.user.setPaymentInfo(newCardNum)
        if success:
            print(Fore.GREEN, message, Fore.RESET)
        else:
            print(Fore.RED, message, Fore.RESET)

    def loop(self, previousChoice):
        userChoice = previousChoice # Default to looping if a user does not make a selection.

        print(Back.WHITE,Fore.BLACK,f"<SHOP> {'Not logged in' if not self.user.isLoggedIn() else 'Logged in as @' + self.user.username}", Style.RESET_ALL)
        print(Back.GREEN,Fore.BLACK,"Make a choice from the following actions:", Style.RESET_ALL)

        if not self.user.isLoggedIn():
            print(Fore.GREEN,"""
            1. Login
            2. Create Account
            3. Exit Program
            """,Fore.RESET)
        else:
            print(Fore.GREEN,"""
            3. Exit Program
            Browse Items
                4. View by Category
                5. Add to Cart
            Cart Information
                6. View Cart
                7. Remove From Cart
                8. Check Out
            User Information
                9. Edit Shipping Address
                10. Edit Payment Information
                11. View Orders
                12. Delete Account
                13. Log Out
            """,Fore.RESET)
        userChoice = int(input(f'{Back.GREEN + Fore.BLACK}Select a number: {Style.RESET_ALL}'))
        print(userChoice)
        return userChoice
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