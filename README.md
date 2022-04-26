## Database Introduction
This project makes use of an SQLite database. The actual database is just a file located in `lib/db.sqlite`. To view, insert, or modify data during development, you can use this free program: https://sqlitebrowser.org

For an example of how to access the database through Python, see `sqlite_demo.py`.

## ApplicationClass
The base class, `ApplicationClass`, is one that all program classes should inherit from. It'll just make it easier for us to share functionality between classes in the future, if necessary.

An example of how to use this class is also given within `sqlite_demo.py`.