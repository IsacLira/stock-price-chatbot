
from flask import Flask, render_template
from flask_socketio import SocketIO
from src.message_handler import MessageHandler

app = Flask(__name__)

socketio = SocketIO(app)
message_handler = MessageHandler()


@app.route('/')
def sessions():
    return render_template('session.html')

@socketio.on('read messages')
def read_messages(methods=['GET', 'POST']):
    content = message_handler.build_messages()
    socketio.emit('response event', content)

@socketio.on('user connection')
def user_connected(json, methods=['GET', 'POST']):
    pass

@socketio.on('message event')
def handle_messages(json, methods=['GET', 'POST']):
    message_handler.process_payload(json)

if __name__ == '__main__':
    socketio.run(app, debug=True, port=5007)
