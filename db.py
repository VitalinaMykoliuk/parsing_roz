import sqlite3
from json import dumps, loads


class UserDB:
    def __init__(self, puch):
        self.db = sqlite3.connect(puch)
        self.cur = self.db.cursor()
        self.create_table()

    def create_table(self):
        self.cur.execute('''CREATE TABLE IF NOT EXISTS users(
        id INTEGER PRIMARY KEY,
        name TEXT,
        mail TEXT,
        password INTEGER
         )''')
        self.db.commit()

    def add_user(self, name, mail, password):
        self.cur.execute('INSERT INTO users (name, mail, password) VALUES(?,?,?)', (name, mail, password,))
        self.db.commit()

    def get_user(self, user_id):
        self.cur.execute('SELECT name, mail, password FROM users WHERE id = ?', (user_id,))
        return self.cur.fetchone()

    def del_user(self, user_id):
        self.cur.execute('DELETE FROM users WHERE id = ?', (user_id,))
        self.db.commit()

    def close(self):
        self.db.close()


db = UserDB('database.db')
db.add_user('Vitalina', 'vitalina@gmail.com', 123763)
db.add_user('Vasya', 'vasy@gmail.com', 6578493)
db.add_user('Oleg', 'oleg@gmail.com', 6578439)


user1 = db.get_user(1)
user2 = db.get_user(3)

print(user1)
print(user2)

db.del_user(2)
db.close()







