import unittest
import shunting_yard as sy

class AppendToOutputTest(unittest.TestCase):
    def test_append_to_output(self):
        outString = '1 2'
        token = '+'
        self.assertEqual(sy.appendToOutput(outString, token), '1 2 +')
