import pika

from src.utils.config import load_config


class BaseRabbitMQ:

    def __init__(self, queue=None):
        self.config = load_config('rabbitmq')

        if not queue:
            queue = self.config['queue']
        self.user = self.config['user']
        self.password = self.config['password']
        self.host = self.config['host']
        self.port = self.config['port']
        self.queue_name = queue

    def run(self):
        credentials = pika.credentials.PlainCredentials(
            self.user,
            self.password
        )
        conn_parameters = pika.ConnectionParameters(
            host=self.host,
            port=self.port,
            credentials=credentials,
            virtual_host='/'
        )
        self.connection = pika.BlockingConnection(conn_parameters)
        self.channel = self.connection.channel()
        self.set_queue()

        return self

    def set_queue(self):
        self.queue = self.channel.queue_declare(self.queue_name, durable=True)

    def close(self):
        self.connection.close()
