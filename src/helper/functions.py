__author__ = 'CRay'
# encoding: utf-8

import redis
import ConfigParser
from datetime import datetime, timedelta


def get_time_list(_time_a, _time_b):
    """
    :param _time_a:  start from time_a
    :param _time_b:  start from time_b
    :return:        time list in string between time_a and time_b
    """
    time_a = datetime.strptime(_time_a, '%Y-%m-%d')
    time_b = datetime.strptime(_time_b, '%Y-%m-%d')
    time3 = time_a
    time_len = (time_b - time_a).days + 1
    num = 0
    list_time = list()
    while num < time_len:
        t3 = time3.strftime('%Y-%m-%d')
        time3 += timedelta(days=1)
        list_time.append(t3)
        num += 1
    return list_time


def redis_pic_tag():
    cf = ConfigParser.ConfigParser()
    cf.read('../../config/redis.conf')
    redis_host = cf.get('redis', 'host')
    redis_port = cf.get('redis', 'port')
    cache = redis.Redis(host=redis_host, port=int(redis_port), db=2)
    pipe = cache.pipeline()

    now = datetime.now()
    fin = open(r'../../data/pictures.csv', 'r')

    count = 0
    while True:
        line = fin.readline()
        if not line:
            break
        try:
            (pic_id, tags, create_time) = line.split('\t')
            list_tags = tags.split(',')
            for t in list_tags:
                t = t.decode('utf-8')
                pipe.rpush(pic_id, t)
                count += 1
            if count > 50000:
                pipe.execute()
                count = 0
        except:
            print line
            continue
    pipe.execute()
    fin.close()

    now1 = datetime.now()
    print 'use time:', now1 - now


def test_get():
    cf = ConfigParser.ConfigParser()
    cf.read('../../config/redis.conf')
    redis_host = cf.get('redis', 'host')
    redis_port = cf.get('redis', 'port')
    cache = redis.Redis(host=redis_host, port=int(redis_port), db=1)
    results = cache.lrange(72321025, 0, -1)
    for r in results:
        print r


if __name__ == '__main__':
    redis_pic_tag()
