import sqlite3
import random
if __name__=='__main__':
    conec = sqlite3.connect('not_telegram.db')
    cursr = conec.cursor()
    # cursr.execute('''CREATE TABLE IF NOT EXISTS Users (id INTEGER PRIMARY KEY, username TEXT NOT NULL,
    # email TEXT NOT NULL, age INTEGER, balance INTEGER NOT NULL)''')
    # cursr.execute('CREATE INDEX IF NOT EXISTS indx_mail ON Users (email)')
    # for i in range(10):
    #     cursr.execute(f"SELECT * FROM Users WHERE email='example{i}@gmail.com'")
    #     usr = cursr.fetchall()
    #     if not usr:
    #         cursr.execute('''INSERT INTO Users (username, email, age, balance)
    #         VALUES (?,?,?,?)''',(f'User{i}',f'example{i}@gmail.com',random.randint(0,100),1000))
    #
    # for i in range(10):
    #     if i%2!=0:
    #         cursr.execute('UPDATE Users SET balance =500 WHERE username=?',(f'User{i}',))
    # for i in range(10):
    #     if (i+2)%3==0:
    cursr.execute('DELETE FROM Users WHERE id=?',(6,))
    conec.commit()
    cursr.execute('SELECT count(*) FROM Users')
    cuser = cursr.fetchone()[0]
    cursr.execute('SELECT sum(balance) FROM Users')
    buser = cursr.fetchone()[0]
    print(buser/cuser)

    # cursr.execute('SELECT username,email,age,balance FROM Users WHERE not age=60')
    # user60 = cursr.fetchall()
    # for us in user60:
    #     print(f'Имя: {us[0]}| Почта: {us[1]} | Возраст: {us[2]} | Баланс: {us[3]}')
    conec.close()