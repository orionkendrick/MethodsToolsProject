import sqlite3

class ApplicationClass:

    class Table:
        connection = None
        cursor = None

    def execute(self, sql, params=[], fetchOne=False):
        print("EXECUTING")
        self.Table.connection = sqlite3.connect('lib/db.sqlite')
        self.Table.cursor = self.Table.connection.cursor()

        if sql.startswith('SELECT'):
            results = self.Table.cursor.execute(sql,params)
            if fetchOne == False:
                results = results.fetchall()
            else:
                results = results.fetchone()
        else:
            results = self.Table.cursor.execute(sql,params)
            self.Table.connection.commit()

        self.Table.connection.close()
        return results

    def __init__(self):
        # Initiate database connection
        self.Table.connection = sqlite3.connect('lib/db.sqlite')
        self.Table.cursor = self.Table.connection.cursor()

    def __del__(self): # Close SQLite connection when an object instance is destroyed
        self.Table.connection.close()

class User(ApplicationClass):
    def __init__(self):
        ApplicationClass.__init__(self)

        self.execute('SELECT * FROM users')