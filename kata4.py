#!/usr/bin/env python
import re

def get_number(x):
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
