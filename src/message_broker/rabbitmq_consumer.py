from src.message_broker.rabbitmq_base import BaseRabbitMQ


class RabbitMQConsumer(BaseRabbitMQ):
    def __init__(self, queue=None):
        super().__init__(queue)

    def read(self):
        method_frame, _, body = self.channel.basic_get(self.queue_name)
        if method_frame:
            return {
                'body': body.decode("utf-8")
            }
        return None

    def consume(self, callback):
        self.run()
        self.channel.basic_consume(callback, self.queue_name)
        self.channel.start_consuming()
