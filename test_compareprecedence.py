import unittest
import shunting_yard as sy


class ComparePrecedenceTest(unittest.TestCase):
    def test_operator_left_and_right(self):
        self.assertEqual(sy.comparePrecedence('+', '-'), 0 )
    def test_operator_left_not_right(self): 
        self.assertEqual(sy.comparePrecedence('+', '/'), -1 )
    def test_operator_not_left_right(self):
        self.assertEqual(sy.comparePrecedence('*', '+'), 1 )
    def test_operator_not_left_not_right(self):
        self.assertEqual(sy.comparePrecedence('*', '/'), 0 )
