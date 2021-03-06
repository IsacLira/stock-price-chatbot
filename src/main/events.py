from .. import socketio
from src.services.message_handler import MessageHandler
from flask_socketio import join_room, leave_room
from flask import session


message_handler = MessageHandler()

@socketio.on('read messages')
def read_messages(methods=['GET', 'POST']):
    content = message_handler.build_messages()
    socketio.emit('response event', content)

@socketio.on('user connection')
def user_connected(json, methods=['GET', 'POST']):
    join_room('chat')
    # Avoid replacing the last user info by the current one.
    try:
        current_user = session[json['id']]
    except:
        session[json['id']] = json['user']

@socketio.on('user disconnected')
def user_disconnected( methods=['GET', 'POST']):
    leave_room('chat')

@socketio.on('message event')
def handle_messages(json, methods=['GET', 'POST']):
    json['user_name'] = session[json['id']]
    message_handler.process_payload(json)