import unittest

from chapter1.common import *


class TestChapter3(unittest.TestCase):

    # TODO: 6 cases
    def test_task3_1(self):
        regex_pattern = r'^[a-zA-z24680]{40}[13579\s]{5}$'
        my_string1 = '2222222222aaaaaaaaaa2222222222aaaaaaaaaa13 57'
        my_string2 = '123.456.abc.def1'
        self.assertTrue(bool(run_search(regex_pattern, my_string1)))

    # TODO: 6 cases
    def test_task3_2(self):
        regex_pattern = r'^\d{1,2}[a-zA-z]{3,}\.{0,3}$'
        my_string1 = '3threeormorealphabets.'
        my_string2 = '123.456.abc.def1'
        self.assertTrue(bool(run_search(regex_pattern, my_string1)))

    # TODO: 6 cases
    def test_task3_3(self):
        regex_pattern = r'^\d{2,}[a-z]*[A-Z]*$'
        my_string1 = '14'
        my_string2 = '123.456.abc.def1'
        self.assertTrue(bool(run_search(regex_pattern, my_string1)))

    # TODO: 6 cases
    def test_task3_4(self):
        regex_pattern = r'^\d+[A-Z]+[a-z]+$'
        my_string1 = '1Qa'
        my_string2 = '123.456.abc.def1'
        self.assertTrue(bool(run_search(regex_pattern, my_string1)))

    # TODO: 6 cases
    def test_task3_5(self):
        regex_pattern = r'^[a-zA-Z]*s$'
        my_string1 = 'Kites'
        my_string2 = '123.456.abc.def1'
        self.assertTrue(bool(run_search(regex_pattern, my_string1)))

