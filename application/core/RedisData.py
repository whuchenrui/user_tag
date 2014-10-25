# coding=utf-8
__author__ = 'ray'

import codecs
from application.model.RedisConn import RedisConn

def make_data():
    fin = codecs.open('../../data/pictures.csv', 'r', encoding='UTF-8')
    redis_conn = RedisConn()
    while True:
        line = fin.readline()
        if not line:
            break
        list_line = line.split('\t')
        pid = list_line[0]
        list_tag = list_line[1].split(',')
        for i in range(0, len(list_tag)):
            redis_conn.cache.lpush(pid, list_tag[i])
    fin.close()

if __name__ == '__main__':
    make_data()
