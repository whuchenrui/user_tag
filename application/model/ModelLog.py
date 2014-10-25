__author__ = 'ray'

from MongoConn import MongoConn


class ModelLog():
    db = None
    col = None
    status = None

    def __init__(self, _log_time):
        self.db = MongoConn('log', _log_time)
        self.col = self.db.clog_info


    def check_is_counted(self, _log_time):
        self.status = self.db.cstatue
        result = self.status.find_one({'type': 'tag'})
        if result:
            list_time = result['time']
            if _log_time in list_time:
                return True
            else:
                list_time.append(_log_time)
                self.status.update({'type': 'tag'}, {'$set': {'time': list_time}})
                return False
        else:
            temp = {}
            temp['type'] = 'tag'
            temp['time'] = [_log_time]
            self.status.insert(temp)
            return False


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