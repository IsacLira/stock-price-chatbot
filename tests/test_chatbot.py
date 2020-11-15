from unittest import TestCase
from src.chatbot import ChatBot


class TestChatbot(TestCase):

    @classmethod
    def setUp(cls):
        cls.bot = ChatBot()

    def test_invalid_command(self):
        invalid_command = "\\stock!=invalid_code"
        command_status = self.bot.process_message(invalid_command)
        self.assertFalse(command_status)

    def test_invalid_code(self):
        invalid_code = "/stock=invalid_code"
        command_status = self.bot.process_message(invalid_code)
        assert 'Invalid code' in command_status['message']
