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
    # client = pymongo.Connection()
    # conn = client.db_wallpaper
    # coll = conn.test
    # test =  'd:\job\iphone5\2013\10月\10-12\magi'
    # print chardet.detect(test)
    # t1 = test.encode('utf-8')
    # print t1, chardet.detect(t1)
    # coll.insert({'name' : test})
    # client.close()
    # now1 = datetime.now()
    # redis_connection = redis_conn()
    # view = [ "189968129" , "191622145" , "183247873" , "184413441" , "188012033" , "171123713" , "172254721" , "171123713" , "172254721" , "182952449" , "190119681" , "192478209" , "192762881" , "192478209" , "192762881" , "177644289" , "183673089" , "189960193" , "169473281" , "169503233" , "169504513" , "169504769" , "178140417" , "181532417" , "188852737" , "193250305" , "169467905" , "187052033" , "187052289" , "187052545" , "180055809" , "184393729" , "184811265" , "184811521" , "184811777" , "184812033" , "184812545" , "184812801" , "184813057" , "184630785" , "193317377" , "184630785" , "193317377" , "193422081" , "193446401" , "175051265" , "184648961" , "193433601" , "193546241" , "178877697" , "178877697" , "182296065" , "193434881" , "193484289" , "193482753" , "180057089" , "192702977" , "193434113" , "196693505" , "193534721" , "169350913" , "185681409" , "191451137" , "185681409" ,  "68976129" , "201654273" , "195980801" , "61210625" , "200729601" , "183056385" , "183057665" , "183059713" , "183060737" , "183061761" , "183060737" , "183061761" , "183053057" , "183064321" , "183064577" , "178599681" , "178599937" , "178599425" , "178600705" , "178600193" , "178600705" , "178600193" , "178600449" , "178601473" , "178600961" , "178601217" , "178624001" , "178625281" , "178624513" , "178624769" , "178624513" , "178624769" , "178625025" , "178625793" , "178625537" , "178624257" , "178626049" , "178846465" , "178848769" , "178850305" , "178852097" , "178854913" , "178855169" , "178856193" , "178856449" , "178856961" , "179280897" , "179279873" , "179279873" , "179280129" , "179279105" , "179279361" , "179279617" , "179280641" , "179280385" , "179281153" , "190937345" , "190937601" , "190937857" , "190939393" , "190938369" , "190938625" , "190938369"]
    # a = {}
    # for v in view:
    #     a[v] = redis_connection.cache.lrange(v, 0, -1)
    #
    # # for v in view:
    # #     redis_connection.pipe.lrange(v, 0, -1)
    # # temp = redis_connection.pipe.execute()
    # # a = {}
    # # count = 0
    # # for item in temp:
    # #     a[view[count]] = item
    # #     count += 1
    #
    # now2 = datetime.now()
    # print 'use: ', now2 - now1
    # print a

    fin = open('/home/ray/backup/picture-2014-08-01.log', 'r')
    fout = open('/home/ray/backup/picture-2014-08-01_output.log', 'w')
    count = 0
    while True:
        line = fin.readline()
        count += 1
        if count%90000 == 0:
            print line
            count = 0
        if 'sort' in line:
            fout.write(line)
            print line

    fout.close()
    fin.close()

if __name__ == '__main__':
    test()