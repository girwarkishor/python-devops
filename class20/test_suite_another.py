import unittest

from unit_tests import addition


def addition_test():
    expected_value = 10
    assert expected_value == addition(10,5)



if __name__=="__main__":
    addition_test()