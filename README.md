# Shop
This is a simple, CLI shopping application written in Python. The main program file is located in `shop.py`.

## Default User
A default user exists for testing purposes:
Username: `default`
Password: `password`

## Database Introduction
This project makes use of an SQLite database. The actual database is just a file located in `lib/db.sqlite`. To view, insert, or modify data during development, you can use this free program: https://sqlitebrowser.org

For an example of how to access the database through Python, see `sqlite_demo.py`.

## ApplicationClass
The base class, `ApplicationClass`, is one that all program classes should inherit from. It'll just make it easier for us to share functionality between classes in the future, if necessary.

An example of how to use this class is also given within `sqlite_demo.py`.

## User Class
The user class inherits from `ApplicationClass` and provides methods for interacting with the `users` database table.

### Method Return Types
All methods return a tuple: the first element is a boolean `True` or `False`, depending on the success of the action; the second element is a human-readable description of the action's status.

### Example Method Usage
```python
u = User() # Creates an instance of the User class

# User admin methods - - - -

u.create('user', 'pass') # Creates a user
u.delete('pass') # Deletes the current user if the given password is correct

u.login('user', 'pass') # Logs into a user
u.logout() # Logs out of the current user

# User shopping methods - - - -

u.setPaymentInfo('0000000000000000') # Sets the current user's payment information
u.getPaymentInfo() # Returns the current user's payment information

u.setAddress('Address #') # Sets the current user's shipping address
u.getAddress() # Returns the current user's shipping address

```
