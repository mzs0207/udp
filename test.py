#!/usr/bin/python
# coding:utf8
import sys

from tools.LoadData import *
from  Logic.Judege import *

for item in loadMatches():
    for matchid in item:
        print matchid
        for p in item[matchid]['data']:
            #print p
            print  matchid, '\t', p['sheng'], '\t', p['ping'], '\t',  p['fu']
        sheng_udp,ping_udp,fu_udp = judge_start(item[matchid]['data'], 0)
        print sheng_udp, ping_udp, fu_udp
        sys.exit(3)


