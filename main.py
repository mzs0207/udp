#!/usr/bin/python
# coding:utf8
from Logic.ObtainData import *
from Logic.MatchTableParser import *
from Logic.PeiLvParser import *
from Logic.select import *
from Logic.Judege import *

import datetime
import time

start = datetime.datetime(2016, 3, 18, 0, 0, 0)
end = datetime.datetime.now()
pr = MatchParser()

biaozhun = 0
totalMatch = 0
rightMatch = 0
while start < end:
    url = 'http://www.okooo.com/livecenter/jingcai/?date=%s' % (start.strftime('%Y-%m-%d'))
    html = obtain_html(url)
    pr.feed(html)
    matches = pr.get_matches()

    print start.strftime("%Y-%m-%d")
    start = start + datetime.timedelta(days=1)
    for item in matches:
        if 'left' in item:

            peilvParser=tableParser()
            peilvHtml = obtain_html("http://www.okooo.com/soccer/match/%s/odds/change/24/" %(item['id']))

            totalMatch += 1
            peilvParser.feed(peilvHtml)
            peilvDatas=peilvParser.getPeiData()

            shengUDP, pingUDP, fuUDP = judge_pre_after(peilvDatas, biaozhun)
            result = max_udp(shengUDP, pingUDP, fuUDP)
            print item['id'], '\t', item['left'], '-', item['right'], '预测:\t', result
            if item['left'] > item['right']:
                match_result = 'sheng'
            elif item['left'] < item['right']:
                match_result = 'ping'
            else:
                match_result = 'fu'
            if match_result in result:
                rightMatch += 1
            print '一共:%s 比赛,命中:%s ,胜率:%s' %(totalMatch,rightMatch,rightMatch*1.0/totalMatch)
            time.sleep(2)



print '一共:%s 比赛,命中:%s ,胜率:%s' %(totalMatch,rightMatch,rightMatch*1.0/totalMatch)

