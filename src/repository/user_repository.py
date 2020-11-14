import json
from flask_login import UserMixin
from src.db.database import RedisDB
from werkzeug.security import generate_password_hash, check_password_hash


class UserRepo(RedisDB):
    def __init__(self):
        super().__init__()

    def set_user(self, user, password):
        password = generate_password_hash(password, method='sha256')
        user_info = {'user_name': user, 'password':password}
        self.rpush('user', user_info)

    def instantiate_users(self):
        users = {user['user_name'].encode("utf-8"): User(user['user_name'])
                 for user in self.user_lis}
        return users

    def get_instances(self, user_id):
        res = self.user_instance[user_id]
        return res

    def get_users(self):
        self.user_lis = self.lrange('user', 0, -1)
        return self.user_lis

    def validate_user(self, user, password):
        user_lis = self.get_users()
        user_info = [info for info in user_lis if (user == info['user_name'])]
        if len(user_info) == 0:
            print('user not found')
            return False
        status = (user_info[0]['user_name'] == user) & \
            check_password_hash(user_info[0]['password'], password)
        return status


class User(UserMixin):
    def __init__(self, user):
        super().__init__()
        self.user = user

    def get_id(self):
        return self.user.encode("utf-8")
