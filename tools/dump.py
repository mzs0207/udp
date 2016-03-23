#!/usr/bin/python
# coding:utf8
# 保存采集好的数据

import datetime
import  sys
import time
from Logic.ObtainData import *
from Logic.PeiLvParser import *
from Logic.MatchTableParser import *

try:
    import cPickle as pickle
except ImportError:
    import pickle

datas={}
pr = MatchParser()

start = datetime.datetime(2015, 1, 11, 0, 0, 0)
end = datetime.datetime(2016, 3, 2, 0, 0, 0)
while start < end:
    day = start.strftime("%Y-%m-%d")
    print day
    url = 'http://www.okooo.com/livecenter/jingcai/?date=%s' % (start.strftime('%Y-%m-%d'))
    start = start + datetime.timedelta(days=1)
    try:
        matchHtml = obtain_html(url)
        pr.feed(matchHtml)
        matches = pr.get_matches()
        pr.clear()
        for item in matches:
            if 'left' in item:
                print item['id']
                peilvParser=tableParser()
                peilvHtml = obtain_html("http://www.okooo.com/soccer/match/%s/odds/change/24/" %(item['id']))
                peilvParser.feed(peilvHtml)
                peilvDatas=peilvParser.getPeiData()
                datas[item['id']] = {'left':item['left'],'right':item['right'],'data':peilvDatas}
                # time.sleep(5)
        f = open(day+'.txt','wb')
        pickle.dump(datas, f)
        f.close()
        datas.clear()
    except Exception, e:
        print e
        f = open(day+'.txt', 'wb')
        pickle.dump(datas, f)
        f.close()