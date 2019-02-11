import re


def run_match(re_pattern, str_in):
    match = re.findall(re_pattern, str_in)
    return match


def run_search(re_pattern, str_in):
    search = re.search(re_pattern, str_in)
    return search
