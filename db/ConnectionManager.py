import sqlite3


class DbConnection:
    def __init__(self):
            self.connection=sqlite3.connect("customers.db")

