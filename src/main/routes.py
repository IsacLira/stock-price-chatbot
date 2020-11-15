from . import main
from flask_login import login_user, login_required, logout_user, current_user
from flask import session, render_template, request, redirect, url_for
from src.repository.user_repository import User
from src.services.user_validation import validate_user
from src.utils.logger import logger
from .. import login_manager


@main.route('/chatrooms', methods=['GET', 'POST'])
@login_required
def chatrooms():
    return render_template('session.html',
           name=session['user_name'])

@main.route('/logout', methods=['POST'])
@login_required
def logout():
    logger.info('User logged out')
    logout_user()
    return redirect('/')

@main.route('/', methods=['POST', 'GET'])
def index():
    user_name = request.form.get('user')
    password = request.form.get('password')
    if validate_user(user_name, password):
        session['user_name'] = user_name
        login_user(User(session.get('user_name')))
        logger.info('User logged in successfully.')
        return redirect('chatrooms')
    return render_template('login.html')

@login_manager.unauthorized_handler
def unauthorized_callback():
    return redirect('/')

