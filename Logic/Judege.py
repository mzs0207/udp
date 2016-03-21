#!/usr/bin/python
# coding:utf8
# udp判断方法
# 用开盘赔率进行对比


def judge_start(dataes, biaozhun):
    length = len(dataes)
    sheng_pei = dataes[length]['sheng']
    ping_pei = dataes[length]['ping']
    fu_pei = dataes[length]['fu']

    sheng_up = 0
    sheng_down = 0

    ping_up = 0
    ping_down = 0

    fu_up = 0
    fu_down = 0

    while length > 0:
        if sheng_pei - dataes[length -1]['sheng']>biaozhun:
            sheng_up += 1
        else:
            sheng_down += 1

        if ping_pei - dataes[length - 1]['ping']> biaozhun:
            ping_up += 1
        else:
            ping_down += 1

        if fu_pei - dataes[length -1 ]['fu'] > biaozhun:
            fu_up += 1
        else:
            fu_down += 1

        sheng_udp=sheng_up - sheng_down
        ping_udp=ping_up - ping_down
        fu_udp=fu_up - fu_down

        return sheng_udp, ping_udp, fu_udp


# 使用平均赔率
def judge_avg(dataes,biaozhun):
    length=len(dataes)

    totalSheng = 0
    totalPing = 0
    totalFu = 0

    for item in dataes:
        totalSheng += item['sheng']
        totalPing += item['ping']
        totalFu += item['fu']

    avgSheng = totalSheng / length
    avgPing = totalPing / length
    avgFu = totalFu / length

    shengUp = 0
    shengDown =0
    shengUDP = 0

    pingUp = 0
    pingDown = 0
    pingUDP = 0

    fuUp = 0
    fuDown = 0
    fuUDP = 0

    for item in dataes:
        if avgSheng - item['sheng'] > biaozhun:
            shengUp += 1
        else:
            shengDown += 1

        if avgPing - item['ping'] > biaozhun :
            pingUp += 1
        else:
            pingDown += 1

        if avgFu - item['fu'] > biaozhun:
            fuUp += 1
        else:
            fuDown += 1

    shengUDP = shengUp - shengDown
    pingUDP = pingUp - pingDown
    fuUDP = fuUp - fuDown

    return shengUDP, pingUDP, fuUDP


# 前一个与后一个进行比较
def judge_pre_after(dataes,biaozhun):
    shengUp = 0
    shengDown = 0
    shengUDP = 0

    pingUp = 0
    pingDown = 0
    pingUDP = 0

    fuUp = 0
    fuDown = 0
    fuUDP = 0

    length = len(dataes)
    while length > 0:
        if dataes[length]['sheng'] - dataes[length - 1] > biaozhun:
            shengUp += 1
        else:
            shengDown += 1

        if dataes[length]['ping'] - dataes[length - 1]['ping'] > biaozhun:
            pingUp += 1
        else:
            pingDown += 1
        if dataes[length]['fu'] - dataes[length - 1]['fu'] > biaozhun :
            fuUp += 1
        else:
            fuDown += 1

        length -= 1

    shengUDP = shengUp - shengDown
    pingUDP = pingUp - pingDown
    fuUDP = fuUp - fuDown

    return shengUDP, pingUDP, fuUDP








