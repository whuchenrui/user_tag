__author__ = 'ray'
# encoding: utf-8

import pymongo


def classify():
    client = pymongo.MongoClient('localhost', 10001)
    conn = client.bzDB
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




if __name__ == '__main__':
    classify()