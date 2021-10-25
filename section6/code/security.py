from resources.user import UserModel


# /auth sends with pw and id, activates authenticate function, returns user(identity) and JWT
def authenticate(username, password):
    user = UserModel.find_by_username(username)
    if user and user.password == password:
        return user

# JWT sent with requests calls identity function and get(returns) user id that token represents


def identity(payload):
    user_id = payload['identity']
    return UserModel.find_by_id(user_id)
