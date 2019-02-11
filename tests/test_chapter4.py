import unittest

from chapter1.common import *


class TestChapter4(unittest.TestCase):

    # TODO: 6 cases
    def test_task3_1(self):
        regex_pattern = r'^[a-zA-z24680]{40}[13579\s]{5}$'
        my_string1 = '2222222222aaaaaaaaaa2222222222aaaaaaaaaa13 57'
        my_string2 = '123.456.abc.def1'
        self.assertTrue(bool(run_search(regex_pattern, my_string1)))
