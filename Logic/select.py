#!/usr/bin/python
# choose result


def reverse_cmp(m, n):
    if m['udp'] < n['udp']:
        return -1
    if m['udp'] > n['udp']:
        return 1
    return 0


def max_udp(sheng, ping, fu):
    dataes=[{'result': 'sheng', 'udp': sheng}, {'result': 'ping', 'udp': ping}, {'result': 'fu', 'udp':fu}]
    sort_datas=sorted(dataes, reverse_cmp)

    if sort_datas[0]['udp'] == sort_datas[1]['udp']:
        return sort_datas[0]['result'] + ','+sort_datas[1]['result']

    else:
        return sort_datas[0]['result']

