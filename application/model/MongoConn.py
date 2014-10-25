# coding = utf-8
__author__ = 'CRay'

import pymongo

class MongoConn():
    client = None
    conn = None
    clog_info = None
    cuser_tag = None

    def __init__(self, _type, _log_time=None):
        self.client = pymongo.Connection()
        self.conn = self.client.db_wallpaper
        if _type == 'log':
            col_name = _log_time + '_log'
            self.clog_info = self.conn[col_name]
        elif _type == 'tag':
            self.cuser_tag = self.conn.user_tag