from lib.applicationclass import ApplicationClass
from classes.item import Item

# In the example, I'll create an Cart class that inherits from ApplicationClass

class Cart(ApplicationClass):
    def __init__(self, user):                         # shoudld work?
        ApplicationClass.__init__(self)

        # Store a reference to the user who owns this cart
        self.user = user

        self.__updateOrders()

    def __updateOrders(self):
        # Load all items in user's cart
        # If an order's status is 0, it is considered an unplaced order (or cart)
        # If an order's status is 1, it is considered to be placed
        self.orders = self.execute('SELECT id, item_id, item_quantity FROM orders WHERE user_id = ? AND status = 0',(self.user.userID,),fetchOne=False)
    
    def __isItemInCart(self, item_id):
        for i in range(0,len(self.orders)):
            if self.orders[i][1] == item_id: return i
        return -1

    def addItem(self, item_id):
        matching_items = self.execute('SELECT quantity FROM items WHERE id = ?',(item_id,),fetchOne=False)
        if len(matching_items) != 1:
            return False, 'No items found with this item number.'
        
        item_quantity = matching_items[0][0]

        if item_quantity < 1:
            return False, 'This item is not currently in stock.'
        
        
        self.execute('INSERT INTO orders (user_id, item_id, item_quantity, status) VALUES (?, ?, ?, ?)' , (self.user.userID, item_id, 1, 0))

        # Update the local cart with what's stored in the database
        self.__updateOrders()

        # Decrement the item in inventory
        item = Item(item_id)
        print(item.decrement())

        return True, f'"{item.getName()[1]}" was added to the cart.'    

        # status = 'In Cart'
        # quantity = 1
        # # get the orderID associated with the username where status == "In Cart"
        # ordID = self.execute('SELECT id FROM orders WHERE username = ? AND status = ?', (username, status)).fetchone()

        # # if there is no current cart for the user
        # if ordID == None:
        #     # gets the largest order id number from the table
        #     oID = self.execute('SELECT MAX(id) FROM orders').fetchone()

        #     # if there is no orders in the table - orderID == 1
        #     if oID == None:
        #         self.orderID = 1
        #         self.execute('INSERT INTO orders (id, username, itemID, quantity, status) VALUES (?, ?, ?, ?, ?)' , (self.orderID, username, itemid, quantity, status))
        #      
        #     # if there are orders in the table - orderId == largest orderID + 1
        #     else:
        #         self.orderID = oID + 1
        #         self.execute('INSERT INTO orders (id, username, itemID, quantity, status) VALUES (?, ?, ?, ?, ?)' , (self.orderID, username, itemid, quantity, status))
        #      
        # # if there is a current open cart for the the user - uses the open carts id
        # else:
        #     self.execute('INSERT INTO orders (id, username, itemID, quantity, status) VALUES (?, ?, ?, ?, ?)' , (ordID, username, itemid, quantity, status))
        #  
        
        # # add the itemid to the items list
        # self.items.append(itemid)

    # def editQuantity(self, item_id, quantity):
    #     if type(quantity) != int or quantity < 0: return False, 'Please provide a valid positive integer.'

    #     item_loc = self.__isItemInCart(item_id)
    #     if item_loc == -1:
    #         return False, 'This item is not in the cart.'
        
    #     order_id = self.orders[item_loc][0]
    #     try:
    #         # Make sure that the number of this item in active carts does not exceed available stock
    #         quantities = self.execute('SELECT item_quantity FROM orders WHERE item_id = ? AND status = 0', (item_id,))
            
    #         total_quantity_in_carts = 0
    #         for q in quantities: total_quantity_in_carts += q[0]

    #         available_stock = self.execute('SELECT item_quantity FROM orders WHERE item_id = ? AND status = 0', (item_id,))

    #         if 

    #         self.execute('UPDATE orders SET item_quantity = ? WHERE id = ?',(quantity, order_id))
    #      
    #     except Exception:
    #         return False, 'No matching order in database. Cannot update item quantity.'
        
    #     self.__updateOrders()

    #     return True, 'Item quantity set.'

    #     itemid1 = self.item_ob.getId(itemName)
    #     status = 'In Cart'
    
    def removeItem(self, item_id):

        matching_items = self.execute('SELECT id, quantity FROM items WHERE id = ?',(item_id,),fetchOne=False)
        if len(matching_items) != 1:
            return False, 'No items found with this item number.'

        try:
            self.execute('DELETE FROM orders WHERE user_id = ? AND item_id = ? AND status = 0', (self.user.userID, item_id,))
        except:
            return False, 'Item is not in shopping cart.'

        self.__updateOrders()

        # Decrement the item in inventory
        item = Item(item_id)
        item.increment()   
        
        return True, 'Item was removed.'

    def get(self):
        return self.orders

    def clear(self):                    # should work?
        self.execute('DELETE FROM orders WHERE user_id = ? AND status = 0', (self.user.userID,))
        
        self.__updateOrders()

        return True, 'Cart was cleared.'

    def placeOrder(self):         # should work?
        try:
            for order in self.orders:
                self.execute('UPDATE orders SET status = 1 WHERE  id = ?', (order[0],))
    
        except Exception:
            return False, 'Error attempting to place order'

        self.__updateOrders()

        return True, "Order was placed."

    def viewOrders(self, userID):   # might work
        return self.execute('SELECT item_id, item_quantity FROM orders WHERE user_id = ? AND status = 1', (userID,), fetchOne=False)