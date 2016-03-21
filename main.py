#!/usr/bin/python
# coding:utf8
from Logic.ObtainData import *
from Logic.MatchTableParser import *
from Logic.select import *

import datetime
import time

start = datetime.datetime(2016, 1, 1, 0, 0, 0)
end = datetime.datetime.now()
pr = MatchParser()
while start < end:
    url = 'http://www.okooo.com/livecenter/jingcai/?date=%s' % (start.strftime('%Y-%m-%d'))
    html = obtain_html(url)
    pr.feed(html)
    matches = pr.get_matches()
    print start.strftime("%Y-%m-%d")
    start = start + datetime.timedelta(days=1)
    for item in matches:
        if 'left' in item:
            print item['id'], '\t', item['left'], '-', item['right']

    time.sleep(3)

