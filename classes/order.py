from lib.applicationclass import ApplicationClass

# In this example, I'll create a User class that inherits from ApplicationClass
class Order(ApplicationClass):
    def __init__(self, user):
        ApplicationClass.__init__(self)
        
        self.user = user
        
        self.__updateOrders()
    
   
