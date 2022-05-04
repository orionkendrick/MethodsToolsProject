from lib.applicationclass import ApplicationClass

# In this example, I'll create a Order class that inherits from ApplicationClass
class Order(ApplicationClass):
    def __init__(self):
        pass
    
    # lists all orders associated with the user
    def viewOrders(self, userID):
        return self.execute('SELECT item_id, item_quantity FROM orders WHERE user_id = ? AND status = 1', (userID,), fetchOne=False)

    # cancels the oder (NOT IMPLEMENTED YET -- not a part of requirements)
    def cancel(self):
        orderToCancel = input('Enter orderID of order you would like to cancel:')
        return True, f"You chose to cancel order: {orderToCancel}"
