from seasons import check_valid, return_diff
import pytest


def test1():
    assert check_valid("2004-04-01") == True


def test2():
    assert check_valid("2004-200-01") == False


def test5():
    assert return_diff("2022-03-09") == "five hundred and twenty-five thousand, six hundred minutes"