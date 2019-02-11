import unittest

from chapter1.common import *


class TestChapter1(unittest.TestCase):
    def test_task1_1(self):
        regex_pattern = r'hackerrank'
        my_string1 = 'The hackerrank team is on a mission to flatten the world by restructuring the DNA of every ' \
                     'company on the planet. We rank programmers based on their coding skills, helping companies ' \
                     'source great programmers and reduce the time to hire. As a result, we are revolutionizing the ' \
                     'way companies discover and evaluate talented engineers. The hackerrank platform is the ' \
                     'destination for the best engineers to hone their skills and companies to find top engineers. '
        self.assertAlmostEqual(len(run_match(regex_pattern, my_string1)), 2)

    # TODO: 16 cases
    def test_task1_2(self):
        regex_pattern = r'^...\....\....\....$'
        my_string1 = '123.456.abc.def'
        my_string2 = '123.456.abc.def1'
        self.assertAlmostEqual(len(run_match(regex_pattern, my_string1)), 1)
        self.assertAlmostEqual(len(run_match(regex_pattern, my_string2)), 0)

    # TODO: 5 cases
    def test_task1_3(self):
        regex_pattern = r'\d\d\D\d\d\D\d\d\d\d'
        my_string1 = '06-11-2015'
        my_string2 = '123.456.abc.def1'
        self.assertTrue(bool(run_search(regex_pattern, my_string1)))

    # TODO: 5 cases
    def test_task1_4(self):
        regex_pattern = r'\S\S\s\S\S\s\S\S'
        my_string1 = '12 11 15'
        my_string2 = '123.456.abc.def1'
        self.assertTrue(bool(run_search(regex_pattern, my_string1)))

    # TODO: 5 cases
    def test_task1_5(self):
        regex_pattern = r'\w{3}\W\w{10}\W\w{3}'
        my_string1 = 'www.hackerrank.com'
        my_string2 = '123.456.abc.def1'
        self.assertTrue(bool(run_search(regex_pattern, my_string1)))

    # TODO: 5 cases
    def test_task1_6(self):
        regex_pattern = r'^\d\w{4}\.$'
        my_string1 = '0qwer.'
        my_string2 = '123.456.abc.def1'
        self.assertTrue(bool(run_search(regex_pattern, my_string1)))
