from . import main
from flask import render_template, request, redirect, url_for
from src.repository.user_repository import UserRepo

user_repo = UserRepo()

@main.route('/', methods=['POST'])
def login():
    return render_template('login.html')

@main.route('/chatrooms')
def chatrooms():
    return render_template('session.html')

@main.route('/login', methods=['POST'])
def login_post():
    user = request.form.get('user')
    password = request.form.get('password')
    if user_repo.validate_user(user, password):
        return redirect('chatrooms')
