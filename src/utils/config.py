import os

from dotenv import load_dotenv

load_dotenv()


def load_config(key):
    configs = {
        'rabbitmq': {
            'user': os.environ.get('RABBIT_MQ_USER'),
            'password': os.environ.get('RABBIT_MQ_PASSWORD'),
            'host': os.environ.get('RABBIT_MQ_HOST'),
            'port': os.environ.get('RABBIT_MQ_PORT'),
            'queue': os.environ.get('RABBITMQ_QUEUE')
        },
        'redis': {
            'host': os.environ.get('REDIS_HOST'),
            'port': os.environ.get('REDIS_PORT'),
        }
    }
    return configs[key]
