# coding = utf-8
__author__ = 'CRay'

import pymongo

class Mongo():
    client = None
    conn = None

    def __init__(self):
        self.client = pymongo.Connection()
        self.conn = self.client.db_wallpaper

    def insert(self, _collection, _list_insert):
        if _collection == 'user_tag':
            try:
                self.conn[_collection].insert(_list_insert)
            except:
                print 'error'

    @property
    def get_user_tag(self):
        """
        :return:
        """
        dict_idfa = {}
        user_tag = self.conn.user_tag
        results = user_tag.find({}, {'_id': 0})
        for result in results:
            idfa_name = result['idfa']
            dict_idfa[idfa_name] = {}
            dict_idfa[idfa_name]['app'] = result['app']
            dict_idfa[idfa_name]['app_v'] = result['app_v']
            for item in result['tag']:
                tag_name = item.encode('utf8')
                dict_idfa[idfa_name][tag_name] = result['tag'][item]
        user_tag.drop()
        return dict_idfa


    def get_user_pics(self, _log_time):
        dict_idfa = {}
        collection_name = _log_time + '_log'
        user_pics = self.conn[collection_name]
        results = user_pics.find({}, {'_id': 0, 'time': 0})

        for result in results:
            if result['idfa'] in dict_idfa:
                temp = dict_idfa[result['idfa']]
                for v in result['v']:
                    temp['v'].append(v)
                for s in result['s']:
                    temp['s'].append(s)
                for f in result['f']:
                    temp['f'].append(f)
                dict_idfa[result['idfa']] = temp
            else:
                dict_idfa[result['idfa']] = {}
                dict_idfa[result['idfa']]['app'] = result['app']
                dict_idfa[result['idfa']]['app_v'] = result['app_v']
                dict_idfa[result['idfa']]['v'] = result['v']
                dict_idfa[result['idfa']]['s'] = result['s']
                dict_idfa[result['idfa']]['f'] = result['f']
        return dict_idfa

    def drop_coll(self):
        self.conn.user_tag.drop()
