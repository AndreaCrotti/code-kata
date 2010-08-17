#!/usr/bin/env python
# chop(int, array_of_int)  -> int

import unittest
import sys

# the array is sorted already
def chop_rec(n, array):
    if len(array) == 1:
        if array[0] == n:
            return 0
        else:
            return -1
            
    middle = len(array) / 2
    el = array[middle]
    print middle, el
    if n == el:
        return middle
    elif n > el:
        return middle + chop_rec(n, array[:middle])
    else:
        return chop_rec(n, array[middle:])

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

def chop_iterative_double(n, array):
    "Smarter iterative version"
    start, end = 0, (len(array) - 1)
    while True:
        if start > end:
            return -1

        mid = start + ((end - start) / 2)
        el = array[mid]
        if n == el:
            return mid
        # TODO: jump to the middle with the right checks 
        elif n < el:
            end -= 1
        else:
            start += 1
    

# 1 mistake:
# - using the recursive version I'm going in max recurs depth very quickly
# 2 mistake
# - also using the iterative version I come into an infinite loop in the beginning
# - getting wrong the indexing of the middle element

def test_chop(fun):
    assert(fun(2, [1,2,3,4]) == 1)
    assert(fun(4, [1,2,3,4]) == 3)

test_chop(chop_iterative)        
# print fun(2, [1,2,3,4])
