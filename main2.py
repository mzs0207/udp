#!/usr/bin/python
# coding:utf8

from tools.LoadData import *
from Logic.Judege import *
from Logic.select import *
biaozhun = 0
quanzhong= 0.2

total_match_count = 0
right_match_count = 0

for matches in loadMatches():
    for matchId in matches:
        left = int( matches[matchId]['left'])
        right = int(matches[matchId]['right'])
        if left > right:
            matchResult= 'sheng'
        elif left < right:
            matchResult = 'fu'
        else:
            matchResult = 'ping'
        if len(matches[matchId]['data']) == 0:
            continue
        sheng_udp, ping_udp, fu_udp =judge_start(matches[matchId]['data'], biaozhun)

        totalUdp=abs(sheng_udp) + abs(ping_udp) + abs(fu_udp)
        if totalUdp == 0:
            continue
        sheng_udp_score = sheng_udp*1.0/ totalUdp * quanzhong
        ping_udp_score = ping_udp * 1.0 / totalUdp * quanzhong
        fu_udp_score = fu_udp * 1.0 / totalUdp * quanzhong

        sheng_gai_lv = matches[matchId]['data'][-1]['sgailv'] /100.0
        ping_gai_lv = matches[matchId]['data'][-1]['pgailv'] / 100.0
        fu_gai_lv = matches[matchId]['data'][-1]['fgailv'] /100.0

        sheng_score =  sheng_gai_lv + sheng_udp_score
        ping_score =  ping_gai_lv + ping_udp_score
        fu_score = fu_gai_lv + fu_udp_score

        yu_ce = max_udp(sheng_score, ping_score, fu_score)
        total_match_count += 1
        if matchResult in yu_ce:
            right_match_count += 1
        print '赔率:胜:',sheng_gai_lv, '\t平:', ping_gai_lv, '负:', fu_gai_lv
        print 'UDP:胜:', sheng_udp, '\t平:', ping_udp, '负:', fu_udp
        print 'UDP Score:胜:', sheng_udp_score, '\t平:', ping_udp_score, '负:', fu_udp_score
        print 'id:', total_match_count, 'matchid:\t', matchId, '\t', left, '--', right, '\t赛果:',matchResult, '\t 预测:',yu_ce, '\t 胜率:', 1.0*right_match_count/total_match_count
        print ' '
        print ' '


