import sqlite3
import random
if __name__=='__main__':
    conec = sqlite3.connect('not_telegram.db')
    cursr = conec.cursor()
    cursr.execute('''CREATE TABLE IF NOT EXISTS Users (id INTEGER PRIMARY KEY, username TEXT NOT NULL, 
    email TEXT NOT NULL, age INTEGER, balance INTEGER NOT NULL)''')
    cursr.execute('CREATE INDEX IF NOT EXISTS indx_mail ON Users (email)')
    for i in range(10):
        try:
            cursr.execute('''INSERT INTO Users (username, email, age, balance)
            VALUES (?,?,?,?)''',(f'User{i}',f'example{i}@gmail.com',random.randint(0,100),1000))
        except Exception as E:
            pass
    conec.commit()
    conec.close()