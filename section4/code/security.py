from user import User

users = [
    User(1, 'bob', 'asdf')
]

username_mapping = { u.username: u for u in users}
userid_mapping = {u.id: u for u in users}

# /auth sends with pw and id, activates authenticate function, returns user(identity) and JWT
def authenticate(username, password):
    user = username_mapping.get(username, None)
    if user and user.password == password:
        return user

# JWT sent with requests calls identity function and get(returns) user id that token represents
def identity(payload):
    user_id = payload['identity']
    return userid_mapping.get(user_id, None)