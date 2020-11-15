from src.utils.logger import logger
from src.repository.user_repository import UserRepo
from werkzeug.security import check_password_hash

def validate_user(user, password):
    user_lis = UserRepo().get_users()
    user_info = [info for info in user_lis if (user == info['user_name'])]
    if len(user_info) == 0:
        logger.info(f'User {user} not found.')
        return False
    status = (user_info[0]['user_name'] == user) & \
        check_password_hash(user_info[0]['password'], password)
    return status