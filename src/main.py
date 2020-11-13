from flask import Blueprint,render_template

main = Blueprint('main', __name__)


@main.route('/')
def login():
    return render_template('login.html')


@app.route('/chatrooms')
def sessions():
    return render_template('session.html')