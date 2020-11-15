from unittest import TestCase
from src.message_broker.rabbitmq_publisher import RabbitMQPublisher
from src.message_broker.rabbitmq_consumer import RabbitMQConsumer

class TestMessageBroker(TestCase):

    @classmethod
    def setUp(cls):
        queue = 'test_queue'
        cls.consumer = RabbitMQConsumer(queue)
        cls.publisher = RabbitMQPublisher(queue)
        cls.publisher.run()
        cls.consumer.run()

    def test_consumer(self):
        message = "/stock=code"
        self.publisher.send(message)
        res = self.consumer.read()
        self.assertEqual(res['body'], message)