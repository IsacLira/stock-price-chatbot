import re
import time
import json
from io import BytesIO

import pandas as pd
import requests

from src.db.database import RedisDB
from src.message_broker.rabbitmq_consumer import RabbitMQConsumer
from src.message_handler import MessageHandler
from src.utils.utils import get_current_time
from src.utils.logger import logger



class ChatBot:
    def __init__(self):
        self.consumer = RabbitMQConsumer()
        self.db = RedisDB()

    def process_stock_code(self, stock_code):
        url = f'https://stooq.com/q/l/?s={stock_code}&f=sd2t2ohlcv&h&e=csv'
        invalid_message = {'message': f"Invalid code {stock_code.upper()}"}

        try:
            response = requests.get(url)
            df_stock = pd.read_csv(BytesIO(response.content))
        except:
            logger.error('Unable to get stock info from api.')
            return invalid_message

        if df_stock.empty:
            return invalid_message

        price = df_stock['Close'].at[0]
        if price == 'N/D':
            return invalid_message
        valid_message = stock_code.upper() + f" is ${price} per share."
        return {'message': valid_message}

    def process_message(self, msg):
        if re.search(r"/stock=", msg):
            code = msg.split('=')[1]
            logger.info('Processing stock command.')
            response = self.process_stock_code(code)
            return response
        return False

    def callback(self, ch, method, properties, body):
        response = json.loads(body)
        bot_response = self.process_message(response['message'])
        if bot_response:
            response.update(bot_response)
            current_time = get_current_time()
            response.update({
                'user_name': 'Bot',
                'time': current_time,
            })
            self.db.rpush('chat', response)
        ch.basic_ack(method.delivery_tag)

    def run(self):
        self.consumer.consume(self.callback)


if __name__ == "__main__":
    bot = ChatBot()
    bot.run()
