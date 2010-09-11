#!/usr/bin/env python
import re

def weather_analyze():
    def get_number(x):
        "return the number composed by the first n digits"
        return int(re.findall("\d+", x)[0])

    min_range = 100
    min_day = 1
    # first find a good 

    for x in open("weather.dat"):
        vals = re.split("\s+", x)
        assert(len(vals) >= 3)
        day, max, min = map(get_number, vals[1:4])
        ran = max - min
        if ran < min_range:
            min_range = ran
            min_day = day

    print min_day, min_range

def get_vals(s):
    return re.split("\s+", s)

def football():
    foot = open('football.dat').readlines()
    head = get_vals(foot[0])
    # because we have some shit in the middle
    fo, ag = head.index('F')+1, head.index('A')+2
    min_score = min_team = None
    for line in map(get_vals, foot[1:]):
        diff = int(line[fo]) - int(line[ag])
        if not min_score or (diff < min_score):
            min_score = diff
            min_team = line[2]

    print min_team

football()
