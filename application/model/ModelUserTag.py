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
            str_tag = ''
            for tag in _record:
                v = _record[tag][0]
                s = _record[tag][1]
                f = _record[tag][2]
                total = _record[tag][3]
                #TODO: 获得最大的三个值有问题
                if total > a:
                    b = a
                    bb = aa
                    c = b
                    cc = bb
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
                tag_info = str(v)+'=='+str(s)+'=='+str(f)+'=='+str(total)
                str_tag += '&&' + tag + '==' + tag_info
            temp['like'] = [aa, bb, cc]
            temp['tag'] = str_tag
            self.col.insert(temp)

        else:
            a, b, c = 0, 0, 0
            aa, bb, cc = '', '', ''
            temp = {}
            dict_tag = {}
            str_tag = ''
            temp['app'] = _app
            temp['_id'] = _idfa
            list_tag = result['tag'].strip('&&').split('&&')
            for i in range(0, len(list_tag)):
                info = list_tag[i].split('==')
                data_info  = [int(info[1]), int(info[2]), int(info[3]), int(info[4])]
                dict_tag[info[0]] = data_info
            for tag in _record:
                if tag in dict_tag:
                    for i in range(0, 4):
                        dict_tag[tag][0] += _record[tag][0]
                        dict_tag[tag][1] += _record[tag][1]
                        dict_tag[tag][2] += _record[tag][2]
                        dict_tag[tag][3] += _record[tag][3]
                        total = dict_tag[tag][3]
                        if total > a:
                            b = a
                            bb = aa
                            c = b
                            cc = bb
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
                else:
                    dict_tag[tag] = _record[tag]
            for tag in dict_tag:
                v, s, f, total = dict_tag[tag][0], dict_tag[tag][1], dict_tag[tag][2], dict_tag[tag][3]
                tag_info = str(v)+'=='+str(s)+'=='+str(f)+'=='+str(total)
                str_tag += '&&' + tag + '==' +tag_info
            temp['like'] = [aa, bb, cc]
            temp['tag'] = str_tag

            self.col.remove({'_id': _idfa})
            self.col.insert(temp)