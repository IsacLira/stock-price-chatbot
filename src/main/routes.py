from . import main
from flask_login import login_user,login_required
from flask import render_template, request, redirect, url_for
from src.repository.user_repository import UserRepo, User

user_repo = UserRepo()

@main.route('/')
def login():
    return render_template('login.html')

@main.route('/chatrooms')
@login_required
def chatrooms():
    return render_template('session.html')

@main.route('/login', methods=['POST'])
def login_post():
    user_name = request.form.get('user')
    password = request.form.get('password')

    if user_repo.validate_user(user_name, password):
        login_user(User(user_name))
        return redirect('chatrooms')
    return redirect('/')
