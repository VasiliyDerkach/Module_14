import sqlite3
def initiate_db(cursr):

    cursr.execute('''CREATE TABLE IF NOT EXISTS Products (id INTEGER PRIMARY KEY, title TEXT NOT NULL,
    description TEXT, price INTEGER NOT NULL)''')
    cursr.execute('CREATE INDEX IF NOT EXISTS indx ON Products (id)')

def get_all_products(cursr):
    cursr.execute('SELECT * FROM Products')
    return cursr.fetchall()