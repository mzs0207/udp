#!/usr/bin/python
# coding:utf8

import datetime

try:
    import cPickle as pickle
except ImportError:
    import pickle

def loadMatches():
    start = datetime.datetime(2015, 1, 1, 0, 0, 0)
    end = datetime.datetime(2016, 3, 1, 0, 0, 0)
    while start <= end:
        name = "./tools/%s.txt" % (start.strftime("%Y-%m-%d"))
        with open(name,'rb') as f:
            data = pickle.load(f)
        yield data
        start = start + datetime.timedelta(days=1)
