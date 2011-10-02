#!/usr/bin/env python2

import re

FOOTBAL_RE = re.compile(r'\s+\d+\. (?P<team>\w+).*?(?P<for>\d+)\s+-\s+(?P<ag>\d+).*')
WEATHER_RE = re.compile(r'^\s+(?P<day>\d+)\s+(?P<max>\d+)\s+(?P<min>\d+).*')

class Matcher(object):

    def __init__(self, regexp, fname):
        self.regexp = regexp
        self.fname = fname

    def compute(self, func):
        """Compute takes in input the function to apply to the result, as a callable
        """
        res = {}
        for line in open(self.fname):
            m = self.regexp.match(line)
            if m:
                res[m.group(1)] = int(m.group(2)) - int(m.group(3))

        return func(res, key=lambda x: res[x])



def footbal():
    res = {}
    for line in open('football.dat'):
        m = FOOTBAL_RE.match(line)
        res[m.group('team')] = int(m.group('for')) - int(m.group('ag'))

    return min(res, key=lambda x: res[x])


assert Matcher(WEATHER_RE, 'weather.dat').compute(max) == '9'
assert Matcher(FOOTBAL_RE, 'football.dat').compute(min) == 'Leicester'
              
