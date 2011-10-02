#!/usr/bin/env python2

import unittest
import timeit

from kata5 import NaiveChecker, BloomChecker
# TODO: see how we can include testing which involve memory usage and
# timing, to avoid performances regressions


VALID_WORD = 'Andres'
NOT_VALID_WORD = 'dsflkl'

class TestNaiveChecker(unittest.TestCase):

    def setUp(self):
        self.n = NaiveChecker()
        self.n.populate()

    def test_simple_word_is_in(self):
        self.assertTrue(self.n.check(VALID_WORD))


if __name__ == '__main__':
    unittest.main()
