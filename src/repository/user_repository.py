import json
from src.db.database import RedisDB
from werkzeug.security import generate_password_hash, check_password_hash


class UserRepo(RedisDB):
    def __init__(self):
        super().__init__()

    def set_user(self, user, password):
        password = generate_password_hash(password, method='sha256')
        user_info = {'user_name': user, 'password':password}
        self.rpush('user', user_info)

    def validate_user(self, user, password):
        user_lis = self.lrange('user', 0, -1)
        user_info = [info for info in user_lis if (user == info['user_name'])]
        if len(user_info) == 0:
            print('user not found')
            return False
        print(user_info[0]['user_name'] == user)
        condition = (user_info[0]['user_name'] == user) & \
            check_password_hash(user_info[0]['password'], password)
        return condition


if __name__ == '__main__':
    user_repo = UserRepo()
    user_repo.set_user('admin4', '123')
    print(user_repo.validate_user('admin4', '123'))
