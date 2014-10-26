# coding=utf-8
__author__ = 'CRay'

import sys
sys.path.append('../../')
from datetime import datetime
from application.model.ModelLog import ModelLog
from application.model.ModelUserTag import ModelUserTag
from application.model.RedisConn import RedisConn


# 计算用户的tag使用情况
def count_user_tag_cnt(_time):
    log_conn = ModelLog(_time)
    tag_conn = ModelUserTag()
    redis_conn = RedisConn()
    dict_idfa_pics = log_conn.get_user_pics()

    # 每次循环计算一个idfa的tag使用情况, 然后查询mongodb, 并更新
    for idfa in dict_idfa_pics:
        app = dict_idfa_pics[idfa]['app']
        temp = {}
        list_idfa_view = dict_idfa_pics[idfa]['v']   # save fav 的图片一定在v的集合中
        for v in list_idfa_view:
            pic_tags = redis_conn.cache.lrange(v, 0, -1)
            for t in pic_tags:
                if t in temp:
                    temp[t][0] += 1
                    temp[t][3] += 1
                else:
                    temp[t] = [1, 0, 0, 1]

        list_idfa_view = dict_idfa_pics[idfa]['s']
        for s in list_idfa_view:
            pic_tags = redis_conn.cache.lrange(s, 0, -1)
            for t in pic_tags:
                if t in temp:
                    temp[t][1] += 10
                    temp[t][3] += 10
                else:
                    temp[t] = [0, 10, 0, 10]

        list_idfa_view = dict_idfa_pics[idfa]['f']
        for f in list_idfa_view:
            pic_tags = redis_conn.cache.lrange(f, 0, -1)
            for t in pic_tags:
                if t in temp:
                    temp[t][2] += 10
                    temp[t][3] += 10
                else:
                    temp[t] = [0, 0, 10, 10]

        record = temp
        if len(record)>3:  # 去除仅包含urlLink和view为空的记录
            tag_conn.update(idfa, app, record)


def check_counted(_log_time):
    log_conn = ModelLog(_log_time)
    flag = log_conn.check_is_counted(_log_time)
    return flag


if __name__ == '__main__':
    log_time = '2012-08-06'
    time1 = datetime.now()
    try:
        log_time = sys.argv[1]
        flag = check_counted(log_time)
        if not flag:
            count_user_tag_cnt(log_time)
        else:
            print '该日期已经计算过! 请勿重复计算'
    except Exception as e:
        print e, "输入格式: python CountTag 2014-09-11"
    time2 = datetime.now()
    print 'count tag use time: ', time2-time1
