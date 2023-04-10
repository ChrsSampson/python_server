from bcrypt import hashpw, gensalt, checkpw
import sqlite3

class User():
    def __init__(self, id, name, email, password):
        self.id = id
        self.name = name
        self.email = email
        # hash password 
        self.password = hashpw(password.encode('utf-8'), gensalt())
        # init table if not exists
        self.init_table()
    
    def init_table(self):
        # connect to db
        db = sqlite3.connect('db/data.db')
        # create cursor
        cursor = db.cursor()
        # create table if not exists
        cursor.execute("CREATE TABLE IF NOT EXISTS users (id SERIAL PRIMARY KEY, name TEXT, email TEXT, password TEXT)")
        # commit changes
        db.commit()
        # close db connection
        db.close()

    # tgus us mostly for debugging and logging
    def __repr__(self):
        return f"User: {self.name}, {self.email}, {self.password}"
    
    # takes plain text password and compares it to the hashed password
    def check_password(self, password):
        return checkpw(password.encode('utf-8'), self.password)
    
    # save user to db
    def save(self):
        # connect to db
        db = sqlite3.connect('db/data.db')
        # create cursor
        cursor = db.cursor()
        # insert user into db
        cursor.execute("INSERT INTO users VALUES (?, ?, ?, ?)", (self.id, self.name, self.email, self.password))
        # commit changes
        db.commit()
        # close db connection
        db.close()
