from src.message_broker.rabbitmq_base import BaseRabbitMQ


class RabbitMQConsumer(BaseRabbitMQ):
    def __init__(self):
        super().__init__()

    def read(self):
        method_frame, _, body = self.channel.basic_get(self.queue_name)
        if method_frame:
            return {
                'body': body.decode("utf-8")
            }
        return None

    def consume(self, callback):
        self.run()
        self.channel.basic_consume(self.queue_name, callback)
        self.channel.start_consuming()
