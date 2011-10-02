#!/usr/bin/env python
# chop(int, array_of_int)  -> int

import unittest
import sys

# the array is sorted already
def chop_rec(n, array):
    def chop_rec_inter(n, array, start, end):
        if end < start:
            return -1
        mid = start + ((end - start) / 2)
        val = array[mid]
        if val > n:
            return chop_rec_inter(n, array, start, end-1)
        elif val < n:
            return chop_rec_inter(n, array, start+1, end)
        else:
            return mid

    return chop_rec_inter(n, array, 0, len(array) - 1)

def chop_iterative(n, array):
    "simple version with increments"
    start, end = 0, (len(array) - 1)
    while True:
        if start > end:
            return -1

        mid = start + ((end - start) / 2)
        el = array[mid]
        if n == el:
            return mid
        elif n < el:
            end -= 1
        else:
            start += 1
# 1 mistake:
# - using the recursive version I'm going in max recurs depth very quickly
# 2 mistake
# - also using the iterative version I come into an infinite loop in the beginning
# - getting wrong the indexing of the middle element
# 3 mistake
# - in the recursive version, calling chop_rec_inter in the other way around

def test_chop(fun):
    assert(fun(2, [1,2,3,4]) == 1)
    assert(fun(4, [1,2,3,4]) == 3)

test_chop(chop_iterative)        
# print fun(2, [1,2,3,4])
