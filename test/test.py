# encoding: utf-8
__author__ = 'ray'

import pymongo


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
    a ,b = 1, 2
    c = str(a) + '-'
    print c


if __name__ == '__main__':
    test()