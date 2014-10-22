# coding=utf-8
__author__ = 'ray'

from MongoConn import MongoConn


class ModelUserTag():
    db = None
    col = None

    def __init__(self):
        self.db = MongoConn('tag')
        self.col = self.db.cuser_tag

    def update(self, _idfa, _app, _record):
        result = self.col.find({'_id': _idfa})
        if not result:
            # 插入一条新的记录, 记录排行前三的tag名称
            temp = {}
            temp['_id'] = _idfa
            temp['app'] = _app
            a, b, c = 0, 0, 0
            aa, bb, cc = '', '', ''
            for tag in _record:
                v = _record[tag][0]
                s = _record[tag][1]
                f = _record[tag][2]
                total = _record[tag][3]
                if total > a:
                    a = total
                    aa = tag
                elif total > b:
                    b = total
                    bb = tag
                elif total > c:
                    c = total
                    cc = tag
                tag_info = str(v)+'-'+str(s)+'-'+str(f)+'-'+str(total)
                temp[tag] = tag_info
            temp['like'] = [aa, bb, cc]
            self.col.insert(temp)

        else:
            a, b, c = 0, 0, 0
            aa, bb, cc = '', '', ''

