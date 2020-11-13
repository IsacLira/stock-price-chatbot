from .. import socketio
from src.message_handler import MessageHandler

message_handler = MessageHandler()

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