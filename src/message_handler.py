import re
import time
import json
from src.db.database import RedisDB
from src.message_broker.rabbitmq_publisher import RabbitMQPublisher
from src.utils.utils import get_current_time

db = RedisDB()


class MessageHandler:
    def __init__(self):
        self.max_msg = 50
        self.publisher = RabbitMQPublisher()
        self.stock_commands = []

    def sort_messages(self, messages):
        tuples = [(m['time'], m) for m in messages]
        sorted_messages = sorted(tuples, key=lambda tup: tup[0])
        _, sorted_messages = zip(*sorted_messages)
        sorted_messages = list(sorted_messages)
        return sorted_messages[-self.max_msg:]

    def build_messages(self):
        html_content = ''
        messages = db.lrange('chat', -self.max_msg, -1)
        all_messages = messages + self.stock_commands

        if len(all_messages) == 0:
            return {'content': html_content}

        sorted_messages = self.sort_messages(all_messages)
        for message in sorted_messages:
            if 'user_name' in message.keys():
                user = message['user_name']
                msg = message['message']
                time = message['time']
                html_content += f'<div>{time} - <b style="color: #000"> {user}</b> said: {msg} </div>'
        return {'content': html_content}

    def process_payload(self, payload=None):
        current_time = get_current_time()
        if payload is not None:
            payload.update({'time': current_time})
            if re.search(r"/stock=", payload['message']):
                self.publisher.run()
                self.publisher.send(json.dumps(payload))

                # The stock commands won't be saved into db
                self.stock_commands.append(payload)
            elif payload['message'] != '':
                db.rpush('chat', payload)
