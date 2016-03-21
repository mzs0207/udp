#!/usr/bin/python
# coding:utf8
from tools.Network import *


def obtain_html(url):
    nt = network()
    br = nt.getBrowser()
    try:
        response = br.open(url)
        html = response.read()
        br.close()
        return html.decode('gbk')
    except Exception, e:
        br.close()
        print e
