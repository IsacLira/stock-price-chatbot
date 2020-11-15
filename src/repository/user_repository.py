import json
from flask_login import UserMixin
from src.db.database import RedisDB
from werkzeug.security import generate_password_hash
from src.utils.logger import logger


class UserRepo(RedisDB):
    def __init__(self):
        super().__init__()

    def set_user(self, user, password):
        users = self.get_users()
        saved_user_bool = any([user == info['user_name']
                               for info in users])
        if saved_user_bool:
            logger.info('User already in the database')
            return False

        password = generate_password_hash(password, method='sha256')
        user_info = {'user_name': user, 'password': password}
        self.rpush('user', user_info)
        logger.info('User saved successfully.')
        return True

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


class User(UserMixin):
    def __init__(self, user):
        super().__init__()
        self.user = user

    def get_id(self):
        return self.user.encode("utf-8")
