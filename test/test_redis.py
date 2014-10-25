# coding:utf-8
from multiprocessing import Process
import os
from application.model.RedisConn import RedisConn
import chardet

def info(title):
    print title
    print 'model name:', __name__
    if hasattr(os, 'getppid'):  # only available on Unix
        print 'parent process:', os.getppid()
    print 'process id:', os.getpid()

def f(name):
    info('function f')
    print 'hello', name

def get_data():
    redis_conn = RedisConn()
    a = redis_conn.cache.lrange('10000129', 0 ,-1)
    print chardet.detect(a[4]), a


if __name__ == '__main__':
    info('main line')
    p = Process(target=f, args=('bob',))
    p.start()
    p.join()