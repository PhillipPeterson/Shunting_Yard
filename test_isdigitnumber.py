import unittest
import shunting_yard as sy

class IsDigitTest(unittest.TestCase):
    def test_is_digit(self):
        self.assertTrue(sy.isDigit('2'))
    def test_is_not_digit(self):
        self.assertFalse(sy.isDigit('a'))
    def test_is_number(self):
        self.assertTrue(sy.isNumber('135'))    
