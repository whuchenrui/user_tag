# coding: utf-8
__author__ = 'ray'

import pymongo
import chardet

def classify():
    client = pymongo.Connection()
    conn = client.db_wallpaper
    user_coll = conn['2013-07-07_log']
    dict_app = {}

    results = user_coll.find({}, {'_id': 0, 'time': 0})
    for result in results:
        if result['app'] in dict_app:
            pass
        else:
            dict_app[result['app']] = {}
        dict_app[result['app']][result['idfa']] = {}
        dict_app[result['app']][result['idfa']]['app'] = result['app']
        dict_app[result['app']][result['idfa']]['app_v'] = result['app_v']
        for item in result['tag']:
            dict_app[result['app']][result['idfa']][item['name']] = item['cnt']
    client.close()


def test():
    t = {'a': 5, 'b': 7, 'c': 6, 'd': 2, 'e': 9, 'f': 10, 'g': 0, 'h': 1}
    a, b, c = 0, 0, 0
    aa, bb, cc = '', '', ''
    for tag in t:
        total = t[tag]
        if total > a:
            c = b
            cc = bb
            b = a
            bb = aa
            a = total
            aa = tag
        elif total > b:
            c = b
            cc = bb
            b = total
            bb = tag
        elif total > c:
            c = total
            cc = tag
    print a, b, c
    print aa, bb, cc

def encode():
    x = '天气'
    print chardet.detect(x), type(x), x
    y = x.decode('GB2312').encode('utf-8')
    # y = xx.decode('').encode('utf-8')
    # z = x.encode(encoding='utf-8')
    print chardet.detect(y), type(y), y
    # print chardet.detect(z), type(z), z

def mongo():
    client = pymongo.Connection()
    conn = client.db_wallpaper
    col = conn.user_tag
    results = col.find()
    count = 0
    for result in results:
        a = result['like'][0].encode('utf-8')
        b = result['like'][1].encode('utf-8')
        c = result['like'][2].encode('utf-8')
        count += 1
        print a, b, c, chardet.detect(b)
        if a == b:
            print result['_id'], result['like']
        if b == c:
            print 'aaa'
    print count

if __name__ == '__main__':
    mongo()