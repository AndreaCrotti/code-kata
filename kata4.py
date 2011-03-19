#!/usr/bin/env python

import re

class Matcher(object):
    def __init__(self, regexp, fname):
        self.regexp = re.compile(regexp)
        self.fname = fname

    def compute(self, func):
        res = {}
        for line in open(self.fname):
            m = self.regexp.match(line)
            if m:
                res[m.group(1)] = int(m.group(2)) - int(m.group(3))

        return func(res, key=lambda x: res[x])



def footbal():
    line_re = re.compile(r'\s+\d+\. (?P<team>\w+).*?(?P<for>\d+)\s+-\s+(?P<ag>\d+).*')
    res = {}
    for line in open('football.dat'):
        m = line_re.match(line)
        res[m.group('team')] = int(m.group('for')) - int(m.group('ag'))

    return min(res, key=lambda x: res[x])

print Matcher('^\s+(?P<day>\d+)\s+(?P<max>\d+)\s+(?P<min>\d+).*', 'weather.dat').compute(max)
print Matcher('\s+\d+\. (?P<team>\w+).*?(?P<for>\d+)\s+-\s+(?P<ag>\d+).*', 'football.dat').compute(min)
              
