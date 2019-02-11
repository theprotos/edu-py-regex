import unittest

from chapter1.common import *


class TestChapter2(unittest.TestCase):

    # TODO: 6 cases
    def test_task2_1(self):
        regex_pattern = r'^[123][012][xs0][30Aa][xsu][\.,]$'
        my_string1 = '1203x.'
        my_string2 = '123.456.abc.def1'
        self.assertTrue(bool(run_search(regex_pattern, my_string1)))

    # TODO: 6 cases
    def test_task2_2(self):
        regex_pattern = r'^\D[^aeiou][^bcDF]\S[^AEIOU][^\.,]$'
        my_string1 = 'think?'
        my_string2 = '123.456.abc.def1'
        self.assertTrue(bool(run_search(regex_pattern, my_string1)))

    # TODO: 6 cases
    def test_task2_3(self):
        regex_pattern = r'^[a-z][1-9][^a-z][^A-Z][A-Z]'
        my_string1 = 'h4CkR'
        my_string2 = '123.456.abc.def1'
        self.assertTrue(bool(run_search(regex_pattern, my_string1)))


