from src.message_broker.rabbitmq_base import BaseRabbitMQ


class RabbitMQPublisher(BaseRabbitMQ):
    def __init__(self):
        super().__init__()

    def send(self, msg):
        return self.channel.basic_publish('', self.queue.method.queue, msg)
