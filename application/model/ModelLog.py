__author__ = 'ray'

from MongoConn import MongoConn


class ModelLog():
    db = None
    col = None

    def __init__(self, _log_time):
        self.db = MongoConn('log', _log_time)
        self.col = self.db.clog_info

    def get_user_pics(self):
        dict_idfa = {}
        results = self.col.find({}, {'_id': 0, 'time': 0})

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
                dict_idfa[result['idfa']]['v'] = result['v']
                dict_idfa[result['idfa']]['s'] = result['s']
                dict_idfa[result['idfa']]['f'] = result['f']
        return dict_idfa