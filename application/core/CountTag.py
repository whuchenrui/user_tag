# coding: utf-8
__author__ = 'CRay'


from application.model.ModelLog import ModelLog
from application.model.ModelUserTag import ModelUserTag
from application.model.RedisConn import RedisConn


def count_user_tag_cnt(_time):
    log_conn = ModelLog(_time)
    tag_conn = ModelUserTag()
    redis_conn = RedisConn()
    dict_idfa_pics = log_conn.get_user_pics()

    # 每次循环计算一个idfa的tag使用情况, 然后查询mongodb, 并更新
    for idfa in dict_idfa_pics:
        app = dict_idfa_pics['app']
        temp = {}
        list_idfa_view = dict_idfa_pics[idfa]['v']   # save fav 的图片一定在v的集合中
        for v in list_idfa_view:
            pic_tags = redis_conn.cache.lrange(v, 0, -1)
            for t in pic_tags:
                if t in temp:
                    temp[t][0] += 1
                else:
                    temp[t] = [1, 0, 0, 0]

        list_idfa_view = dict_idfa_pics[idfa]['s']
        for s in list_idfa_view:
            pic_tags = redis_conn.cache.lrange(s, 0, -1)
            for t in pic_tags:
                if t in temp:
                    temp[t][1] += 10
                else:
                    temp[t] = [0, 10, 0, 0]

        list_idfa_view = dict_idfa_pics[idfa]['f']
        for f in list_idfa_view:
            pic_tags = redis_conn.cache.lrange(f, 0, -1)
            for t in pic_tags:
                if t in temp:
                    temp[t][2] += 10
                else:
                    temp[t] = [0, 0, 10, 0]

        record = temp
        tag_conn.update(idfa, app, record)
        #TODO: 把字典重新制空是否有必要, 减少内存还是增加查询时间消耗, 需要验证
        dict_idfa_pics[idfa] = ''


if __name__ == '__main__':
    count_user_tag_cnt('2014-07-09')