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
    
   
