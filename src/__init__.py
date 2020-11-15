from flask_login import LoginManager, UserMixin
from flask import Flask, Blueprint
from flask_socketio import SocketIO
from src.repository.user_repository import UserRepo, User

socketio = SocketIO()
login_manager = LoginManager()

def create_app(debug=False):
    app = Flask(__name__)

    app.debug = debug
    app.config['SECRET_KEY'] = 'gjr39dkjn344_!67#'

    from .main import main as main_blueprint
    app.register_blueprint(main_blueprint)

    user_repo = UserRepo()

    login_manager.login_view = '/'
    login_manager.init_app(app)

    @login_manager.user_loader
    def load_user(user_id):
        return User(user_id)

    socketio.init_app(app,  manage_session=True)
    return app
