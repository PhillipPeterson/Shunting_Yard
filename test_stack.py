import unittest
import shunting_yard as sy

class StackTest(unittest.TestCase):
    
    def test_stack_is_empty(self):
        stack = []
        self.assertTrue(sy.stackIsEmpty(stack))

    def test_peek_at_stack(self):
        stack = [1, 2, 3]
        self.assertEqual(sy.peekAtStack(stack), 1)
    def test_pop_from_stack(self):
        stack = [1, 2, 3]
        self.assertEqual(sy.popFromStack(stack), 1)
    def test_push_to_stack(self):
        stack = [1, 2, 3]
        sy.pushToStack(stack, 0)
        self.assertEqual(sy.peekAtStack(stack), 0)
