__author__ = 'ray'

import redis
import ConfigParser


class RedisConn():
    cache = None
    pipe = None

    def __init__(self):
        cf = ConfigParser.ConfigParser()
        cf.read('../../config/redis.conf')
        redis_host = cf.get('redis', 'host')
        redis_port = cf.get('redis', 'port')
        redis_db = cf.get('redis', 'db')
        self.cache = redis.Redis(host=redis_host, port=int(redis_port), db=int(redis_db))
        self.pipe = self.cache.pipeline()