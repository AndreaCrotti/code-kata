#!/usr/bin/env python

# compute
import sys
from itertools import permutations
import timeit

WORDS_FILE = "/usr/share/dict/words"

# most suited is of course the set
words_set = set(s.lower().strip() for s in open(WORDS_FILE).readlines())


def anagrams(word, container):
    print "total memory used %d" % sys.getsizeof(container)
    for w in permutations(word.lower()):
        s = ''.join(w)
        if s in container:
            print s

# measure the memory consumption
