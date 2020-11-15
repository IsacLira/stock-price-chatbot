from unittest import TestCase
from src.repository.user_repository import UserRepo
from src.repository.user_signup import UserSignUp


class TestUserRepo(TestCase):

    @classmethod
    def setUp(cls):
        cls.user_repo = UserRepo()
        cls.user_sign = UserSignUp()

    def test_valid_user(self):
        user, password = 'test_user', '12345'
        self.user_sign.signup(user, password)
        user_status = self.user_repo.validate_user(user, password)
        self.assertTrue(user_status)

    def test_invalid_user(self):
        user, password = 'invalid', '12345'
        user_status = self.user_repo.validate_user(user, password)
        self.assertFalse(user_status)
