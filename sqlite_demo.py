# This file demonstrates how to interact with the SQLite database with Python

# To start, import ApplicationClass
# All program classes should inherit from this
from lib.applicationclass import ApplicationClass

# In this example, I'll create a User class that inherits from ApplicationClass
class User(ApplicationClass):

    # Create the initializer for the User class
    def __init__(self):

        # Call the initializer of the parent, ApplicationClass.
        # Doing this creates a connection to the database.
        ApplicationClass.__init__(self)

        # At this point, SQL can be run on the database using the following syntax:
        # self.Table.cursor.execute('SQL QUERY')

        # To get rows from the database, use .fetchall() on the return of the above function.
        # Here's an example for selecting all rows from the user table:
        users = self.Table.cursor.execute('SELECT * from users').fetchall()
        print(users)

        # When inserting or modifying data, make sure to run self.Table.connection.commit() afterwards.
        # This method saves any changes you've made to the database. For example:

        # - - - - - -
        # self.Table.cursor.execute("INSERT INTO stocks VALUES ('2006-01-05','BUY','RHAT',100,35.14)")
        # self.Table.connection.commit()
        # - - - - - - 

        # More detailed documentation for the Python SQLite module is available here: 
        # https://docs.python.org/3/library/sqlite3.html


# Creating an instance of User for this demo
user = User() 