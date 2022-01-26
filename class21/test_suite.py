import unittest
from unittest.mock import Mock, patch
import datetime

from unit_tests import addition, one_more_function, additionmultiple

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

    @patch("unit_tests.one_more_function")
    def test_addition_one_more_patch(self, func1):
        expected_value = "hi welcome ravi"
        func1.return_value = "ravi"
        self.assertEqual(expected_value, addition("hi ", "welcome "))

    @patch("unit_tests.one_more_function")
    def test_addition_one_more_patch_multiple_functions(self, func1):
        expected_value = "hi welcome kunaravihappy"
        func1.side_effect = ["kuna","ravi","happy"]
        self.assertEqual(expected_value, additionmultiple("hi ", "welcome "))



if __name__=="__main__":
    unittest.main()