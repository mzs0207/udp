#!/usr/bin/python
# coding:utf8

from HTMLParser import HTMLParser

class tableParser(HTMLParser):
    def __init__(self):
        self.trStart=False
        self.tdIndex=0
        self.peilvs=[]
        self.peilv={}
        self.trCount=0
        HTMLParser.__init__(self)

    def handle_starttag(self,tag,attrs):
        if tag.strip() == 'tr':
            self.trStart=True
            self.trCount+=1
        if tag.strip() == 'td':
            self.tdIndex+=1

    def handle_data(self,data):
        if self.trStart and self.trCount>2:
            if self.tdIndex == 3 and data.strip():
                self.peilv['sheng']=float(data.strip())
                self.peilv['num']=self.trCount
            if self.tdIndex == 4 and data.strip():
                self.peilv['ping']=float(data.strip())
            if self.tdIndex == 5 and data.strip():
                self.peilv['fu']=float(data.strip())

            if self.tdIndex == 6 and data.strip():
                self.peilv['sgailv']= float(data.strip())
            if self.tdIndex == 7 and data.strip():
                self.peilv['pgailv']= float(data.strip())
            if self.tdIndex == 8 and data.strip() :
                self.peilv['fgailv'] = float(data.strip())


    def handle_endtag(self, tag):
         if tag.strip() == 'tr':
             self.trStart = False
             self.tdIndex=0
             if 'sheng' in self.peilv:
                 self.peilvs.append(self.peilv)
                 self.peilv={}


    def getPeiData(self):
        return self.peilvs

    def clear(self):
        self.peilvs=[]

