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
from classes.item import Item
# from classes.order import Order
from classes.user import User
# from classes.cart import Cart

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

        self.currentChoice = Choice.LOOP
        while self.currentChoice != Choice.EXIT:
            if self.currentChoice == Choice.LOGIN:
                self.loginAction()
            elif self.currentChoice == Choice.CREATE_ACCOUNT:
                self.createAccountAction()
            if self.user.isLoggedIn():
                if self.currentChoice == Choice.VIEW_BY_CATEGORY:
                    self.viewItemsAction()
                elif self.currentChoice == Choice.ADD_TO_CART:
                    self.addToCartAction()
                elif self.currentChoice == Choice.VIEW_CART:
                    self.viewCartAction()
                elif self.currentChoice == Choice.REMOVE_FROM_CART:
                    self.removeFromCartAction()
                elif self.currentChoice == Choice.CHECK_OUT:
                    self.checkOutAction()
                elif self.currentChoice == Choice.EDIT_SHIPPING_ADDRESS:
                    self.editShippingAddressAction()
                elif self.currentChoice == Choice.EDIT_PAYMENT_INFORMATION:
                    self.editPaymentInformationAction()
                elif self.currentChoice == Choice.VIEW_ORDERS:
                    self.viewOrdersAction()
                elif self.currentChoice == Choice.DELETE_ACCOUNT:
                    self.deleteAccountAction()
                elif self.currentChoice == Choice.LOG_OUT:
                    self.logOutAction()
        
            print("\n- - - - - - - - - -\n")
            self.currentChoice = self.loop(self.currentChoice)

    def loginAction(self):
        print(Back.WHITE,Fore.BLACK,"Enter your Login Information:", Style.RESET_ALL)
        username = input("Username: ")
        password = input("Password: ")

        success, message = self.user.login(username,password)
        if success:
            print(Fore.GREEN, message, Fore.RESET)
        else:
            print(Fore.RED, message, Fore.RESET)

    def createAccountAction(self):
        print(Back.WHITE,Fore.BLACK,"To create your account, provide the following information:", Style.RESET_ALL)
        
        username = input("Username: ")
        password = input("Password: ")

        success, message = self.user.create(username,password)
        
        if success:
            print(Fore.GREEN, message, Fore.RESET)
        else:
            print(Fore.RED, message, Fore.RESET)

    def deleteAccountAction(self):
        print(Back.WHITE,Fore.BLACK,"To remove your account, please provide your password:", Style.RESET_ALL)

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

    def viewOrdersAction(self):
        userID = self.user.userID
        orders = self.user.cart.viewOrders(userID)

        print("Previous Orders:")

        for order in orders:
            print(Fore.BLUE,f"""
            Book: {Item(order[0]).getName()[1]}
            Quantity: {order[1]}
            """,Fore.RESET)

    def viewItemsAction(self):
        print(Back.WHITE,Fore.BLACK,"Here's what we currently have in stock:", Style.RESET_ALL)

        items = Item().getAllItems()
        
        for item in items:
            print(Fore.BLUE,f"""
            Name: {item[1]}
            Price: ${item[3]}
            Description:
                {item[2]}
            """,Fore.RESET)

    def addToCartAction(self):
        print(Back.WHITE,Fore.BLACK,"Here's what we currently have in stock:", Style.RESET_ALL)

        items = Item().getAllItems()
        
        for item in items:
            print(Fore.BLUE,f'{item[0]}: {item[1]} (${item[3]})',Fore.RESET)

        item_id = input("What would you like to add to your cart? Please enter the item number listed above: ")
        success, message = self.user.cart.addItem(item_id)

        if success:
            print(Fore.GREEN, message, Fore.RESET)
        else:
            print(Fore.RED, message, Fore.RESET)

    def viewCartAction(self):
        print(Back.WHITE,Fore.BLACK,"Here's what is currently in your cart:", Style.RESET_ALL)
        
        cart = self.user.cart.get()
        
        for item in cart:
            item_obj = Item(item[1])
            item_obj.getName()
            print(Fore.BLUE,f'{item[1]}: {item_obj.getName()[1]} (${item_obj.getPrice()[1]})',Fore.RESET)
        
    def removeFromCartAction(self):
        print(Back.WHITE,Fore.BLACK,"Here's what is currently in your cart:", Style.RESET_ALL)
        
        cart = self.user.cart.get()
        
        for item in cart:
            item_obj = Item(item[1])
            item_obj.getName()
            print(Fore.BLUE,f'{item[1]}: {item_obj.getName()[1]} (${item_obj.getPrice()[1]})',Fore.RESET)
            
        item_id = input("What would you like to remove from your cart? Please enter the item number listed above: ")
        success, message = self.user.cart.removeItem(item_id)
        
        if success:
            print(Fore.GREEN, message, Fore.RESET)
        else:
            print(Fore.RED, message, Fore.RESET)
        
    def checkOutAction(self):
        print(Back.WHITE,Fore.BLACK,"Checking out...", Style.RESET_ALL)
        
        success, message = self.user.cart.placeOrder()
        
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
                4. View Items
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
# shop.user.create('username','password')
# print(shop.user.login('username','password'))

# Each user method returns a tuple of the following format:
#   (Boolean True/False, Message)
# The first element will be true if the action was successful and false otherwise.
# Try running this script to see the output from the login example above.

# Demo of Item methods
# shop.item.create('The Giver','A book.', 19.99, 12)
# shop.item.load(7)
# print(shop.item.setName('New Product Name'))
# print(shop.item.setPrice(22.32))
# print(shop.item.getPrice())
# print(shop.item.setDescription('New description!'))
# print(shop.item.setQuantity(12309))
# This shows fetching the price of an item after creating it
