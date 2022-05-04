from lib.applicationclass import ApplicationClass

# In this example, I'll create a Order class that inherits from ApplicationClass
class Order(ApplicationClass):
    def __init__(self):
      
        self.userID = None
        self.username = None
        self.itemID = None
        self.quantity = None
        self.status = None

        self.cart = None
    
   from lib.applicationclass import ApplicationClass

# In this example, I'll create a Order class that inherits from ApplicationClass
class Order(ApplicationClass):
    def __init__(self):
      
        self.orderID = 0
        self.items[]

    
#initializer method    
    def Order(self, orderID):
    
#lists all orders associated with the user
    def viewOrders(self, items):
      for item in orderID.items:
        print(f'Items are: {orderID.items}')

#cancels the oder
    def cancel(self):
      orderToCancel= input('Enter orderID of order you would like to cancel:')
      return void f"You chose to cancel order: {orderToCancel}"
