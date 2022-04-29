from lib.applicationclass import ApplicationClass

# In this example, I'll create a Item class that inherits from ApplicationClass
class Item(ApplicationClass):
    def __init__(self, id=None):

        # Default values
        self.id = id
        self.name = None
        self.description = None
        self.price = None
        self.quantity = None

        # If an item ID is provided, load pre-existing data from table
        if id:
            item = self.Table.cursor.execute('SELECT name, description, price, quantity FROM items WHERE id = ?',(id,)).fetchall()
            self.name, self.description, self.price, self.quantity = item[0]

    #Item management functions
    def load(self, id):
        try:
            item = self.Table.cursor.execute('SELECT name, description, price, quantity FROM items WHERE id = ?',(id,)).fetchall()
            self.name, self.description, self.price, self.quantity = item[0]
        except Exception:
            return False, 'No matching item in database.'
        
        self.id = id
        return True, 'Item successfully loaded into instance.'

    def create(self, name, description, price, quantity=0):
        try:
            self.Table.cursor.execute('INSERT INTO items (name, description, price, quantity) VALUES (?, ?, ?, ?)',(name, description, price, quantity))
            self.Table.connection.commit()

            self.id = self.Table.cursor.execute('SELECT id FROM items WHERE name = ?', (name,)).fetchall()[0][0]

        except Exception: # Catch any exceptions and return False to signal failure
            return False, 'Item already exists!'


        self.name = name
        self.description = description
        self.price = price
        self.quantity = quantity

        return True, 'Item created.'




    def setQuantity(self, quantity):
        if type(quantity) != int or quantity < 0: return False, 'Please provide a valid positive integer.'
        try:
            self.Table.cursor.execute('UPDATE items SET quantity = ? WHERE id = ?',(quantity, self.id))
            self.Table.connection.commit()
        except Exception:
            return False, 'No matching item in database.'
        
        self.quantity = quantity
        return True, 'Item quantity set.'

    def getQuantity(self):
        quantity = self.Table.cursor.execute('SELECT quantity FROM items WHERE id = ?',(self.id,))
        quantity = self.Table.cursor.fetchall()
        return True, quantity[0]

    def decrement(self, byNum=1):
        if type(byNum) != int or byNum < 0: return False, 'Please provide a valid positive integer.'
        try:
            self.Table.cursor.execute('UPDATE items SET quantity = ? WHERE id = ?',(max(self.quantity - byNum,0), self.id))
            self.Table.connection.commit()
        except:
            return False, 'Error decrementing item quantity'
        
        return True, 'Item quantity decremented.'
    
    def setName(self, name):
        try:
            self.Table.cursor.execute('UPDATE items SET name = ? WHERE id = ?',(name, self.id))
            self.Table.connection.commit()
        except Exception:
            return False, 'No matching item in database.'
        
        self.name = name
        return True, 'Item name set.'

    def getName(self):
        name = self.Table.cursor.execute('SELECT name FROM items WHERE id = ?',(self.id,))
        name = self.Table.cursor.fetchall()
        return True, name[0]

    def setPrice(self, price):
        if type(price) != float or price < 0: return False, 'Please provide a valid float to represent the price.'
        try:
            self.Table.cursor.execute('UPDATE items SET price = ? WHERE id = ?',(price, self.id))
            self.Table.connection.commit()
        except Exception:
            return False, 'No matching item in database.'
        
        self.price = price
        return True, 'Item price set.'
    
    def getPrice(self):
        price = self.Table.cursor.execute('SELECT price FROM items WHERE id = ?', (self.id,))
        price = self.Table.cursor.fetchall()

        return True, price[0]

    def setDescription(self, description):
        try:
            self.Table.cursor.execute('UPDATE items SET description = ? WHERE id = ?', (description, self.id))
            self.Table.connection.commit()
        except Exception:
            return False, 'No matching item in database.'
        
        self.description = description
        return True, 'Item description set.'
    
    def getDescription(self):
        description = self.Table.cursor.execute('SELECT description FROM items WHERE id = ?', (self.id,))
        description = self.Table.cursor.fetchall()
        return True, description[0]

    