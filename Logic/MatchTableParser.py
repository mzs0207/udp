#!/usr/bin/python
# coding:utf8
from HTMLParser import HTMLParser


class MatchParser(HTMLParser):

    def __init__(self):
        self.trStart = False
        self.tdIndex = 0
        self.matches = []
        self.match = {}
        self.bIndex = 0
        HTMLParser.__init__(self)

    def handle_starttag(self, tag, attrs):
        if tag.strip() == 'tr':
            self.trStart = True
        if tag.strip() == 'td':
            self.tdIndex += 1
        if tag.strip() == 'b' and self.tdIndex == 6:
            self.bIndex += 1

        if self.tdIndex == 6:
            for key, value in attrs:
                if key == 'val':
                    self.match['id'] = value

    def handle_data(self, data):
        if self.trStart and self.tdIndex == 6 and data.strip():
            if self.bIndex == 1:
                self.match['left'] = data.strip()
            if self.bIndex == 3:
                self.match['right'] = data.strip()

    def handle_endtag(self, tag):
        if tag.strip() == 'tr':
            self.trStart = False
            self.tdIndex = 0
            self.bIndex = 0
            if 'id' in self.match:
                self.matches.append(self.match)
                self.match = {}

    def clear(self):
        self.matches = []

    def get_matches(self):
        return self.matches
