import json
import os
import pickle

import redis

from src.utils.config import load_config


class RedisDB:
    def __init__(self):
        config = load_config('redis')
        self.conn = redis.Redis(
            host=config['host'],
            port=config['port'],
            decode_responses=False
        )

    def get_value(self, key):
        return self.conn.get(key)

    def set_value(self, key, value):
        self.conn.set(key, value)

    def rpush(self, key, value):
        self.conn.rpush(key, json.dumps(value))

    def lrange(self, key, start, stop):
        messages = self.conn.lrange(key, start, stop)
        messages = [json.loads(m) for m in messages]
        return messages

    def get_keys(self, key):
        return self.conn.keys(key)

    def hget(self, key, field):
        return self.conn.hget(key, field)

    def hset(self, key, field, value):
        self.conn.hset(key, field, value)

if __name__ == "__main__":
    import json
    db = RedisDB()

    key = 'contatos'
    db.rpush(key, msg)
    messages = db.lrange(key, 0, -1)
    print(messages)