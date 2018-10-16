import unittest
import shunting_yard as sy

class OperatorBracketTest(unittest.TestCase):
    def test_is_operator(self):
        self.assertTrue(sy.isOperator('*'))
    def test_not_operator(self):
        self.assertFalse(sy.isOperator('('))
    def test_is_left_bracket(self):
        self.assertTrue(sy.isLeftBracket('('))
    def test_is_not_left_bracket(self):
        self.assertFalse(sy.isLeftBracket(')'))
    def test_is_right_bracket(self):
        self.assertTrue(sy.isRightBracket(')'))
    def test_is_not_right_bracket(self):
        self.assertFalse(sy.isRightBracket('('))
