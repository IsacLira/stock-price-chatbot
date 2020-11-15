from unittest import TestCase
from src.repository.user_repository import UserRepo
from src.services.user_signup import UserSignUp
from src.db.database import RedisDB
from werkzeug.security import check_password_hash


class TestUserRepo(TestCase):

    @classmethod
    def setUp(cls):
        cls.user_repo = UserRepo()
        cls.user_sign = UserSignUp()
        cls.db = RedisDB()

    def test_valid_user(self):
        user, password = 'user_test', '12345'
        self.user_sign.signup(user, password)
        user_status = self.user_repo.validate_user(user, password)
        self.assertTrue(user_status)

    def test_invalid_user(self):
        user, password = 'invalid_user', '12345'
        user_status = self.user_repo.validate_user(user, password)
        self.assertFalse(user_status)

    def test_insert_user(self):
        user, password = 'user_test', '12345'
        self.user_repo.set_user(user, password)
        all_users = self.db.lrange('user', 0, -1)
        with self.subTest('Assert saved user'):
            status_lis = [u['user_name'] == user for u in all_users]
            self.assertTrue(any(status_lis))

        with self.subTest('Assert user and password'):
            user_info = [u for u in all_users if u['user_name'] == user][0]
            self.assertTrue(check_password_hash(
                user_info['password'], password))

        with self.subTest('Assert user on db'):
            self.assertFalse(self.user_repo.set_user(user, password))

