import sqlite3
from db import db


class UserModel(db.Model):
    __tablename__ = 'users'
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80))
    password = db.Column(db.String(80))

    def __init__(self, _id, username, password):
        self.id = _id
        self.username = username
        self.password = password

    # def find_by_username(self, username):
    #     connection = sqlite3.connect('data.db')
    #     cursor = connection.cursor()

    #     query = "SELECT * FROM users WHERE username=?"
    #     # the parameters, even though it's single, need to be in tuple by making param with brackets and comma (param,)
    #     result = cursor.execute(query, (username,))
    #     row = result.fetchone()
    #     if row:
    #         user = User(row[0], row[1], row[2])
    #     else:
    #         user = None

    #     connection.close()
    #     return user

    # change to
    @classmethod
    def find_by_username(cls, username):
        connection = sqlite3.connect('data.db')
        cursor = connection.cursor()

        query = "SELECT * FROM users WHERE username=?"
        # the parameters, even though it's single, need to be in tuple by making param with brackets and comma (param,)
        result = cursor.execute(query, (username,))
        row = result.fetchone()
        if row:
            user = cls(*row)
        else:
            user = None

        connection.close()
        return user

    @classmethod
    def find_by_id(cls, _id):
        connection = sqlite3.connect('data.db')
        cursor = connection.cursor()

        query = "SELECT * FROM users WHERE id=?"
        result = cursor.execute(query, (_id,))
        row = result.fetchone()
        if row:
            user = cls(*row)
        else:
            user = None

        connection.close()
        return user
