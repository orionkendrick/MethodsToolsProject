import sqlite3

class ApplicationClass:

    class Table:
        connection = None
        cursor = None

    def __init__(self):
        # Initiate database connection
        self.Table.connection = sqlite3.connect('lib/db.sqlite')
        self.Table.cursor = self.Table.connection.cursor()

    def __del__(self): # Close SQLite connection when an object instance is destroyed
        self.Table.connection.close()

class User(ApplicationClass):
    def __init__(self):
        ApplicationClass.__init__(self)

        self.Table.cursor.execute('SELECT * FROM users')