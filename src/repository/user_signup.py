import argparse
from src.repository.user_repository import UserRepo


class UserSignUp:
    def __init__(self):
        self.user_repo = UserRepo()

    def signup(self, user, password):
        self.user_repo.set_user(user, password)


if __name__ == "__main__":
    sgn_ = UserSignUp()
    params = {}
    parser = argparse.ArgumentParser(description="User signup")
    parser.add_argument('--user', type=str)
    parser.add_argument('--password', type=str)
    params.update(vars(parser.parse_args()))
    sgn_.signup(params['user'], params['password'])
