import sqlite3
def initiate_db(cursr):

    cursr.execute('''CREATE TABLE IF NOT EXISTS Products (id INTEGER PRIMARY KEY, title TEXT NOT NULL,
    description TEXT, price INTEGER NOT NULL)''')
    cursr.execute('CREATE INDEX IF NOT EXISTS indx ON Products (id)')
    cursr.execute('''CREATE TABLE IF NOT EXISTS Users (id INTEGER PRIMARY KEY, username TEXT NOT NULL, 
    email TEXT NOT NULL, age INTEGER NOT NULL, balance INTEGER NOT NULL)''')
    cursr.execute('CREATE INDEX IF NOT EXISTS indx_mail ON Users (email)')
def get_all_products(cursr):
    cursr.execute('SELECT * FROM Products')
    return cursr.fetchall()

def is_included(cursr,username):
    f = cursr.execute(f"SELECT * FROM Users WHERE username=?",(username,))
    if f:
        return True
    else:
        return False
def add_user(connect,cursr,username, email, age):
    if not is_included(cursr,username):
        cursr.execute('INSERT INTO Users (username, email, age, balance) VALUES (?,?,?,?)',(username, email, age,1000))
        connect.commit()
        return True
    else:
        return False
