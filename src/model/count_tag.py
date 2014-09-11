# encoding: utf-8

__author__ = 'CRay'

import sys
sys.path.append('../')
import ConfigParser
from helper import conn_db
import redis
import datetime

def count_user_tag_cnt(_time):
    now1 = datetime.datetime.now()
    print now1
    mongo_conn = conn_db.Mongo()
    cf = ConfigParser.ConfigParser()
    cf.read('../../config/redis.conf')
    redis_host = cf.get('redis', 'host')
    redis_port = cf.get('redis', 'port')
    redis_db = cf.get('redis', 'db')
    cache = redis.Redis(host=redis_host, port=int(redis_port), db=int(redis_db))

    dict_idfa_tag = mongo_conn.get_user_tag
    now2 = datetime.datetime.now()
    print 'finish tag collection read', now2 - now1
    dict_idfa_pics = mongo_conn.get_user_pics(_time)
    now2 = datetime.datetime.now()
    print 'finish pic collection read', now2 - now1

    for idfa in dict_idfa_pics:
        nowin1 = datetime.datetime.now()
        if idfa in dict_idfa_tag:
            pass
        else:
            dict_idfa_tag[idfa] = {}
            dict_idfa_tag[idfa]['app'] = dict_idfa_pics[idfa]['app']
            dict_idfa_tag[idfa]['app_v'] = dict_idfa_pics[idfa]['app_v']

        for v in dict_idfa_pics[idfa]['v']:

            list_tags = cache.lrange(v, 0, -1)
            for t in list_tags:
                if t in dict_idfa_tag[idfa]:
                    pass
                else:
                    dict_idfa_tag[idfa][t] = [0, 0, 0, 0]
                try:
                    dict_idfa_tag[idfa][t][0] += 1
                except Exception as e:
                    print dict_idfa_tag[idfa][t], t, 'view'

        for s in dict_idfa_pics[idfa]['s']:
            list_tags = cache.lrange(s, 0, -1)

            for t in list_tags:
                if t in dict_idfa_tag[idfa]:
                    pass
                else:
                    dict_idfa_tag[idfa][t] = [0, 0, 0, 0]
                try:
                    dict_idfa_tag[idfa][t][1] += 10
                except Exception as e:
                    print dict_idfa_tag[idfa][t] , t, 'save'

        for f in dict_idfa_pics[idfa]['f']:
            list_tags = cache.lrange(f, 0, -1)
            for t in list_tags:
                if t in dict_idfa_tag[idfa]:
                    pass
                else:
                    dict_idfa_tag[idfa][t] = [0, 0, 0, 0]
                try:
                    dict_idfa_tag[idfa][t][2] += 10
                except Exception as e:
                    print dict_idfa_tag[idfa][t] , t, 'fav'
        nowfor2 = datetime.datetime.now()

    # input into db
    list_new_user_tag_insert = []
    for idfa in dict_idfa_tag.keys():
        row = {'idfa': idfa, 'tag': {}}
        temp_list_tag = []
        for item in dict_idfa_tag[idfa]:
            if item == 'app':
                row['app'] = dict_idfa_tag[idfa][item]
            elif item == 'app_v':
                row['app_v'] = dict_idfa_tag[idfa][item]
            else:
                if '.' in item:
                    print item
                else:
                    dict_idfa_tag[idfa][item][3] = dict_idfa_tag[idfa][item][0] + dict_idfa_tag[idfa][item][1] +\
                                               dict_idfa_tag[idfa][item][2]
                    row['tag'][item] = dict_idfa_tag[idfa][item]
        list_new_user_tag_insert.append(row)
        dict_idfa_tag.pop(idfa)    # delete those useless info to reduce size of dict
        if len(list_new_user_tag_insert) > 1000:
            print list_new_user_tag_insert[999]
            mongo_conn.insert('user_tag', list_new_user_tag_insert)
            list_new_user_tag_insert = []
        # end input

    if 0 < len(list_new_user_tag_insert) < 1000:
        mongo_conn.insert('user_tag', list_new_user_tag_insert)

    now2 = datetime.datetime.now()
    print 'finish all', now2 - now1


def test():
    mongo_conn = conn_db.Mongo()
    mongo_conn.drop_coll()


if __name__ == '__main__':
    count_user_tag_cnt('2014-08-23')
