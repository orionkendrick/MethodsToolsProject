from lib.applicationclass import ApplicationClass

# In this example, I'll create a Item class that inherits from ApplicationClass
class Item(ApplicationClass):
    def __init__(self):
        items = self.Table.cursor.execute('SELECT * FROM items').fetchall()

        self.itemID = None
        self.itemName = None
        self.price = None
        self.quantity = None

    #Item management functions
    def create(self, itemID, itemName, price, quantity):
        try:
            self.Table.cursor.execute('INSERT INTO items (itemID, itemName, price, quantity) VALUES (?, ?, ?, ?)',(itemID, itemName, price, quantity))
            self.Table.connection.commit()
        except Exception: # Catch any exceptions and return False to signal failure
            return False, 'Item already exists!'
        return True, 'Item created.'

    def decrement(self, itemID, num):
        try:
            decrementedQuantity = self.quantity - num
            self.Table.cursor.execute('UPDATE items SET quantity = ? WHERE itemID = ?'),(decrementedQuantity, itemID)
        except:
            return False, 'Error decrementing item quantity'
    
    def getName(self, itemID):
        return self.itemName
    
    def getPrice(self, itemID):
        return self.price
    
    def getQuantity(self, itemID):
        return self.quantity
    