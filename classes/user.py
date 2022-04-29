from lib.applicationclass import ApplicationClass
from classes.cart import Cart

# In this example, I'll create a User class that inherits from ApplicationClass
class User(ApplicationClass):

    def __init__(self):
        ApplicationClass.__init__(self)

        self.userID = None
        self.username = None
        self.password = None
        self.shippingAddress = None
        self.paymentInfo = None

        self.cart = None

    # User management functions - - - -
    def create(self, username, password):
        try:
            self.Table.cursor.execute('INSERT INTO users (username, password) VALUES (?, ?)',(username, password))
            self.Table.connection.commit()
        except Exception: # Catch any exceptions and return False to signal failure
            return False, 'User already exists!'
        return True, 'User created.'

    def delete(self, password):
        if not self.username: return False, 'No user is logged in.'

        user_info = self.Table.cursor.execute('SELECT * FROM users WHERE username = ? AND password = ?', (self.username, password)).fetchone()
        
        # If no user matches the passed username and password, return a failure
        if not user_info: return False, 'Incorrect authentication information provided.'

        # Remove user from database and log out instance
        self.Table.cursor.execute('DELETE FROM users WHERE username = ? AND password = ?', (self.username, password))
        self.Table.connection.commit()

        self.logout()
        return True, 'User deleted.'
    
    def login(self,username, password):
        if self.username: self.logout() # If a user is already logged in, log out first.

        try:
            user_info = self.Table.cursor.execute('SELECT * FROM users WHERE username = ? AND password = ?', (username, password)).fetchone()
        except Exception: # Catch any exceptions and return False to signal failure
            return False, 'Error attempting to login.'
        
        # If no user matches the passed username and password, return a failure
        if not user_info: return False, 'Incorrect authentication information provided.'

        # Set local attributes to returned database values
        self.userID, self.username, self.password, self.shippingAddress, self.paymentInfo = user_info
        self.cart = Cart(self)
        
        return True, f'Logged in as {username}.'

    def logout(self):
        if not self.username: return False, 'No user is logged in.'
        self.username, self.password, self.shippingAddress, self.paymentInfo = (None, None, None, None)
        return True, 'Logged out.'

    def isLoggedIn(self):
        return self.username

    # User shopping functions - - - -
    def getPaymentInfo(self):
        if not self.username: return False, 'No user is logged in.'
        if not self.paymentInfo: return False, f'No payment information is stored for {self.username}.'

        return True, self.paymentInfo
    
    def setPaymentInfo(self, cardNum):
        if not self.username: return False, 'No user is logged in.'

        # Make sure card number is valid
        cardNum = str(cardNum)
        if not cardNum.isnumeric() or len(cardNum) != 16: return False, 'Please provide a valid credit card number with no spaces or dashes.'

        # Update database
        self.Table.cursor.execute('UPDATE users SET payment = ? WHERE username = ?',(cardNum, self.username))
        self.Table.connection.commit()

        # Update local attributes
        self.paymentInfo = cardNum
        return True, f'Payment information updated for {self.username}.'

    def getAddress(self):
        if not self.username: return False, 'No user is logged in.'
        if not self.shippingAddress: return False, f'No shipping address is stored for {self.username}.'
        
        return True, self.shippingAddress

    def setAddress(self, newAddress):
        if not self.username: return False, 'No user is logged in.'

        # Update database
        self.Table.cursor.execute('UPDATE users SET address = ? WHERE username = ?',(newAddress, self.username))
        self.Table.connection.commit()

        # Update local attributes
        self.shippingAddress = newAddress
        return True, f'Shipping information updated for {self.username}.'

