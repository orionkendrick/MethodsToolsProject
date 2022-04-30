# - - - - - WARNING - - - - -
# Run this script to reset the database.
# - - - - - WARNING - - - - -

import sqlite3

connection = sqlite3.connect('lib/db.sqlite')
cursor = connection.cursor()

# Clear all tables
cursor.execute('DELETE FROM orders')
cursor.execute('DELETE FROM items')
cursor.execute('DELETE FROM users')

# Create default user for testing (default, password)
cursor.execute('INSERT INTO users (username, password) VALUES ("default", "password")')

# Insert test products
cursor.execute('INSERT INTO items (name, description, price, quantity) VALUES ("The Giver", "A 1993 American young adult dystopian novel written by Lois Lowry.", 19.99, 2)')
cursor.execute('INSERT INTO items (name, description, price, quantity) VALUES ("1984", "A dystopian social science fiction novel and cautionary tale written by English writer George Orwell.", 14.99, 1)')
cursor.execute('INSERT INTO items (name, description, price, quantity) VALUES ("Fahrenheit 451", "A 1953 dystopian novel by American writer Ray Bradbury.", 16.99, 2)')

connection.commit()