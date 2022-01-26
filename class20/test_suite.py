import unittest
from unittest.mock import Mock
import datetime

from unit_tests import addition, one_more_function

print(datetime.datetime.today())

class TestAddition(unittest.TestCase):
    """Methods name should start with test"""
    def setUp(self) -> None:
        pass

    def test_adition(self):
        expected_value = 10
        with self.assertRaises(TypeError) as func:
            addition(5,5)

    def test_addition_one_more(self):
        expected_value = "hi welcome kuna"
        self.assertEqual(expected_value, addition("hi ", "welcome "))


    def test_datetime(self):
        datetime = Mock()
        datetime.datetime.today.return_value = "tuesday"
        print(datetime.datetime.today())



if __name__=="__main__":
    unittest.main()