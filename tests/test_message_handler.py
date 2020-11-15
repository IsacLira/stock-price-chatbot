from unittest import TestCase
from src.services.message_handler import MessageHandler

MESSAGES = [{'message': 'Hey, how are you doing?',
             'id': 'bbcd9',
             'user_name': 'John',
             'time': '22:20:11'},
            {'message': 'Hi',
             'id': 'bbcd9',
             'user_name': 'David',
             'time': '22:18:11'},
            {'message': "Good, and you?",
             'id': 'bbcd9',
             'user_name': 'David',
             'time': '22:22:11'},
            ]


class TestMessageHandler(TestCase):

    @classmethod
    def setUp(cls):
        cls.message_handler = MessageHandler()

    def test_sort_messages(self):
        sorted_messages = self.message_handler.sort_messages(MESSAGES)
        sorted_time = [m['time'] for m in sorted_messages]
        time_reference_ = sorted([m['time'] for m in MESSAGES])
        # Assert the order of sorted dates
        assert sorted_time == time_reference_

    def test_messate_filter(self):
        # Repeat messages
        input_ = MESSAGES*20
        messages = self.message_handler.sort_messages(input_)

        # Assert the number of filtered messages
        self.assertEqual(len(messages), self.message_handler.max_msg)
